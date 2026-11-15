#!/usr/bin/env python3
"""
Deterministic, Sandbox-Native CV PDF & Markdown Renderer for Sherpa.
Calibrated to the exact page geometry, typography (Times New Roman 14pt/12pt/11pt),
line spacing (12.67pt), rules, and bullet hierarchy of `Minesh Wadhwa CV - Product.pdf`.
"""

import argparse
import json
import re
import struct
import sys
from pathlib import Path

import pypdf

TTF_PATHS = {
    "R": "/System/Library/Fonts/Supplemental/Times New Roman.ttf",
    "B": "/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf",
    "I": "/System/Library/Fonts/Supplemental/Times New Roman Italic.ttf",
    "BI": "/System/Library/Fonts/Supplemental/Times New Roman Bold Italic.ttf",
}

PDF_BASE_FONTS = {
    "R": "/Times-Roman",
    "B": "/Times-Bold",
    "I": "/Times-Italic",
    "BI": "/Times-BoldItalic",
}

LOCKED_COMPANIES = [
    ("Lowe’s India", "Bangalore, Karnataka", [("Senior Product Manager", "Sep 2024 – Present")]),
    ("Hype Marketing & Product Services", "Bangalore, Karnataka", [("Founder", "Oct 2023 – Nov 2024")]),
    ("HealthQ Rehab", "Bangalore, Karnataka", [("Head of Marketing", "May 2023 – Dec 2023")]),
    (
        "Byju’s - Product Development",
        "Bangalore, Karnataka",
        [
            ("Senior Product Manager", "July 2020 – April 2023"),
            ("Multiple Roles", "Jun 2015 – June 2020"),
        ],
    ),
]


class TrueTypeMetrics:
    """Reads exact glyph advance widths from a macOS system TrueType font file."""

    def __init__(self, ttf_path: str):
        data = Path(ttf_path).read_bytes()
        num_tables = struct.unpack(">H", data[4:6])[0]
        tables = {}
        for i in range(num_tables):
            off = 12 + i * 16
            tag = data[off : off + 4].decode("latin1")
            t_off, t_len = struct.unpack(">II", data[off + 8 : off + 16])
            tables[tag] = (t_off, t_len)

        head_off, _ = tables["head"]
        self.units_per_em = struct.unpack(">H", data[head_off + 18 : head_off + 20])[0]

        hhea_off, _ = tables["hhea"]
        num_hmetrics = struct.unpack(">H", data[hhea_off + 34 : hhea_off + 36])[0]

        maxp_off, _ = tables["maxp"]
        num_glyphs = struct.unpack(">H", data[maxp_off + 4 : maxp_off + 6])[0]

        hmtx_off, _ = tables["hmtx"]
        advances = []
        for i in range(num_hmetrics):
            adv, _ = struct.unpack(">Hh", data[hmtx_off + i * 4 : hmtx_off + (i + 1) * 4])
            advances.append(adv)
        last_adv = advances[-1] if advances else 1000
        while len(advances) < num_glyphs:
            advances.append(last_adv)
        self.advances = advances

        cmap_off, _ = tables["cmap"]
        num_sub = struct.unpack(">H", data[cmap_off + 2 : cmap_off + 4])[0]
        self.cmap = {}
        for i in range(num_sub):
            soff = cmap_off + 4 + i * 8
            plat, enc, sub_rel = struct.unpack(">HHI", data[soff : soff + 8])
            if (plat == 3 and enc == 1) or plat == 0:
                sub_off = cmap_off + sub_rel
                fmt = struct.unpack(">H", data[sub_off : sub_off + 2])[0]
                if fmt == 4:
                    seg_count = struct.unpack(">H", data[sub_off + 6 : sub_off + 8])[0] // 2
                    end_codes = struct.unpack(f">{seg_count}H", data[sub_off + 14 : sub_off + 14 + 2 * seg_count])
                    start_off = sub_off + 16 + 2 * seg_count
                    start_codes = struct.unpack(f">{seg_count}H", data[start_off : start_off + 2 * seg_count])
                    delta_off = start_off + 2 * seg_count
                    id_deltas = struct.unpack(f">{seg_count}h", data[delta_off : delta_off + 2 * seg_count])
                    range_off = delta_off + 2 * seg_count
                    id_range_offsets = struct.unpack(f">{seg_count}H", data[range_off : range_off + 2 * seg_count])
                    for s_idx in range(seg_count):
                        sc, ec, delta, ro = (
                            start_codes[s_idx],
                            end_codes[s_idx],
                            id_deltas[s_idx],
                            id_range_offsets[s_idx],
                        )
                        if sc == 0xFFFF:
                            break
                        for code in range(sc, ec + 1):
                            if ro == 0:
                                gid = (code + delta) & 0xFFFF
                            else:
                                idx_off = range_off + 2 * s_idx + ro + 2 * (code - sc)
                                gid = struct.unpack(">H", data[idx_off : idx_off + 2])[0]
                                if gid != 0:
                                    gid = (gid + delta) & 0xFFFF
                            self.cmap[code] = gid
                    break

    def char_width_pt(self, ch: str, font_size: float) -> float:
        gid = self.cmap.get(ord(ch), 0)
        adv = self.advances[gid] if gid < len(self.advances) else self.advances[0]
        return (adv / self.units_per_em) * font_size

    def text_width_pt(self, text: str, font_size: float) -> float:
        return sum(self.char_width_pt(c, font_size) for c in text)


METRICS = {k: TrueTypeMetrics(v) for k, v in TTF_PATHS.items()}


def pdf_escape_winansi(text: str) -> str:
    """Encode string to WinAnsi (cp1252) and escape PDF literal string delimiters."""
    raw = text.encode("cp1252", errors="replace")
    out = []
    for b in raw:
        if b == 0x28:  # (
            out.append("\\(")
        elif b == 0x29:  # )
            out.append("\\)")
        elif b == 0x5C:  # \
            out.append("\\\\")
        elif 32 <= b <= 126:
            out.append(chr(b))
        else:
            out.append(f"\\{b:03o}")
    return "".join(out)


def parse_styled_Runs(text: str, default_style: str = "R") -> list[tuple[str, str]]:
    """
    Parse inline *italic* and **bold** markers into (style, text) tokens.
    """
    tokens = []
    pattern = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*)")
    pos = 0
    for m in pattern.finditer(text):
        if m.start() > pos:
            tokens.append((default_style, text[pos : m.start()]))
        chunk = m.group(0)
        if chunk.startswith("**"):
            tokens.append(("B", chunk[2:-2]))
        else:
            tokens.append(("I", chunk[1:-1]))
        pos = m.end()
    if pos < len(text):
        tokens.append((default_style, text[pos:]))
    return tokens


def wrap_styled_words(runs: list[tuple[str, str]], font_size: float, max_width: float) -> list[list[tuple[str, str]]]:
    """
    Split styled runs into words and wrap them into lines that fit within max_width points.
    """
    words: list[tuple[str, str]] = []
    for style, segment in runs:
        parts = re.split(r"(\s+)", segment)
        for p in parts:
            if not p:
                continue
            words.append((style, p))

    lines: list[list[tuple[str, str]]] = []
    curr_line: list[tuple[str, str]] = []
    curr_w = 0.0

    for style, token in words:
        if token.isspace():
            if not curr_line:
                continue
            w = METRICS[style].text_width_pt(" ", font_size)
            curr_line.append((style, " "))
            curr_w += w
        else:
            w = METRICS[style].text_width_pt(token, font_size)
            if curr_line and curr_w + w > max_width:
                # Trim trailing space on current line
                while curr_line and curr_line[-1][1].isspace():
                    curr_line.pop()
                lines.append(curr_line)
                curr_line = [(style, token)]
                curr_w = w
            else:
                curr_line.append((style, token))
                curr_w += w

    if curr_line:
        while curr_line and curr_line[-1][1].isspace():
            curr_line.pop()
        lines.append(curr_line)
    return lines or [[(runs[0][0] if runs else "R", "")]]


class PDFCanvas:
    """Lightweight, deterministic PDF 1.4 multi-page canvas."""

    PAGE_W = 612.0
    PAGE_H = 792.0
    LEFT_X = 30.6
    RIGHT_X = 581.4
    BOTTOM_MARGIN = 44.0
    TOP_Y = 738.0

    def __init__(self):
        self.pages: list[list[str]] = [[]]
        self.y = 721.3

    @property
    def stream(self) -> list[str]:
        return self.pages[-1]

    def new_page(self):
        self.pages.append([])
        self.y = self.TOP_Y

    def ensure_space(self, needed_pt: float):
        if self.y - needed_pt < self.BOTTOM_MARGIN:
            self.new_page()

    def draw_text(self, x: float, y: float, text: str, style: str = "R", size: float = 11.0, color: tuple = (0, 0, 0)):
        r, g, b = color
        esc = pdf_escape_winansi(text)
        self.stream.append(
            f"q {r:.3f} {g:.3f} {b:.3f} rg BT /F{style} {size:.2f} Tf 1 0 0 1 {x:.2f} {y:.2f} Tm ({esc}) Tj ET Q"
        )

    def draw_runs_line(self, x: float, y: float, line_tokens: list[tuple[str, str]], size: float = 11.0):
        cur_x = x
        # Merge adjacent tokens of the same style for cleaner PDF operators
        merged: list[tuple[str, str]] = []
        for st, txt in line_tokens:
            if merged and merged[-1][0] == st:
                merged[-1] = (st, merged[-1][1] + txt)
            else:
                merged.append((st, txt))
        for st, txt in merged:
            self.draw_text(cur_x, y, txt, style=st, size=size)
            cur_x += METRICS[st].text_width_pt(txt, size)

    def draw_hline(self, x1: float, x2: float, y: float, width: float = 0.75, gray: float = 0.4):
        self.stream.append(f"q {gray:.2f} G {width:.2f} w {x1:.2f} {y:.2f} m {x2:.2f} {y:.2f} l S Q")

    def draw_color_hline(self, x1: float, x2: float, y: float, width: float = 0.75, color: tuple = (0, 0, 0)):
        r, g, b = color
        self.stream.append(f"q {r:.3f} {g:.3f} {b:.3f} RG {width:.2f} w {x1:.2f} {y:.2f} m {x2:.2f} {y:.2f} l S Q")

    def draw_bullet_disc(self, cx: float, cy: float, r: float = 2.2):
        k = 0.5522847498 * r
        self.stream.append(
            f"q 0 0 0 rg {cx+r:.2f} {cy:.2f} m "
            f"{cx+r:.2f} {cy+k:.2f} {cx+k:.2f} {cy+r:.2f} {cx:.2f} {cy+r:.2f} c "
            f"{cx-k:.2f} {cy+r:.2f} {cx-r:.2f} {cy+k:.2f} {cx-r:.2f} {cy:.2f} c "
            f"{cx-r:.2f} {cy-k:.2f} {cx-k:.2f} {cy-r:.2f} {cx:.2f} {cy-r:.2f} c "
            f"{cx+k:.2f} {cy-r:.2f} {cx+r:.2f} {cy-k:.2f} {cx+r:.2f} {cy:.2f} c f Q"
        )

    def draw_bullet_circle(self, cx: float, cy: float, r: float = 2.2):
        k = 0.5522847498 * r
        self.stream.append(
            f"q 0 0 0 RG 0.75 w {cx+r:.2f} {cy:.2f} m "
            f"{cx+r:.2f} {cy+k:.2f} {cx+k:.2f} {cy+r:.2f} {cx:.2f} {cy+r:.2f} c "
            f"{cx-k:.2f} {cy+r:.2f} {cx-r:.2f} {cy+k:.2f} {cx-r:.2f} {cy:.2f} c "
            f"{cx-r:.2f} {cy-k:.2f} {cx-k:.2f} {cy-r:.2f} {cx:.2f} {cy-r:.2f} c "
            f"{cx+k:.2f} {cy-r:.2f} {cx+r:.2f} {cy-k:.2f} {cx+r:.2f} {cy:.2f} c S Q"
        )

    def save(self, out_path: Path):
        objects: list[bytes] = []

        def add_obj(content: bytes) -> int:
            objects.append(content)
            return len(objects)

        # 1-4: Font objects
        font_ids = {}
        for key, base_font in PDF_BASE_FONTS.items():
            fid = add_obj(
                f"<< /Type /Font /Subtype /Type1 /BaseFont {base_font} /Encoding /WinAnsiEncoding >>".encode("ascii")
            )
            font_ids[key] = fid

        font_res_str = " ".join(f"/F{k} {fid} 0 R" for k, fid in font_ids.items())

        # Reserve Pages object ID
        pages_obj_id = add_obj(b"")
        page_ids = []

        for page_cmds in self.pages:
            stream_bytes = "\n".join(page_cmds).encode("latin1")
            c_id = add_obj(
                f"<< /Length {len(stream_bytes)} >>\nstream\n".encode("ascii")
                + stream_bytes
                + b"\nendstream"
            )
            p_id = add_obj(
                f"<< /Type /Page /Parent {pages_obj_id} 0 R /MediaBox [0 0 612 792] "
                f"/Resources << /Font << {font_res_str} >> >> /Contents {c_id} 0 R >>".encode("ascii")
            )
            page_ids.append(p_id)

        kids_str = " ".join(f"{pid} 0 R" for pid in page_ids)
        objects[pages_obj_id - 1] = f"<< /Type /Pages /Kids [{kids_str}] /Count {len(page_ids)} >>".encode("ascii")

        catalog_id = add_obj(f"<< /Type /Catalog /Pages {pages_obj_id} 0 R >>".encode("ascii"))
        info_id = add_obj(b"<< /Title (Minesh Wadhwa CV - Product) /Producer (Sherpa PDF Renderer) >>")

        out = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
        offsets = []
        for idx, obj_bytes in enumerate(objects, start=1):
            offsets.append(len(out))
            out.extend(f"{idx} 0 obj\n".encode("ascii"))
            out.extend(obj_bytes)
            out.extend(b"\nendobj\n")

        xref_pos = len(out)
        out.extend(f"xref\n0 {len(objects) + 1}\n".encode("ascii"))
        out.extend(b"0000000000 65535 f \n")
        for off in offsets:
            out.extend(f"{off:010d} 00000 n \n".encode("ascii"))
        out.extend(
            f"trailer\n<< /Size {len(objects) + 1} /Root {catalog_id} 0 R /Info {info_id} 0 R >>\n"
            f"startxref\n{xref_pos}\n%%EOF\n".encode("ascii")
        )
        out_path.write_bytes(bytes(out))


def render_cv_to_pdf(data: dict, out_path: Path):
    c = PDFCanvas()
    LH = 12.67

    # 1. Header
    name = data["header"]["name"]
    name_w = METRICS["B"].text_width_pt(name, 14.0)
    c.draw_text((612.0 - name_w) / 2.0, c.y, name, style="B", size=14.0)
    c.draw_hline(c.LEFT_X, c.RIGHT_X, c.y - 3.2, width=1.0, gray=0.15)

    c.y -= 14.8
    p1 = "Bangalore \u2022 "
    p2 = data["header"].get("email", "w.minesh@gmail.com")
    p3 = " \u2022 +91 9035 199 024"
    w1 = METRICS["R"].text_width_pt(p1, 11.0)
    w2 = METRICS["R"].text_width_pt(p2, 11.0)
    w3 = METRICS["R"].text_width_pt(p3, 11.0)
    start_x = (612.0 - (w1 + w2 + w3)) / 2.0
    c.draw_text(start_x, c.y, p1, style="R", size=11.0)
    c.draw_text(start_x + w1, c.y, p2, style="R", size=11.0, color=(0.067, 0.333, 0.800))
    c.draw_color_hline(start_x + w1, start_x + w1 + w2, c.y - 1.5, width=0.6, color=(0.067, 0.333, 0.800))
    c.draw_text(start_x + w1 + w2, c.y, p3, style="R", size=11.0)

    def draw_section_header(title: str, top_gap: float = 26.2):
        c.ensure_space(42.0)
        c.y -= top_gap
        c.draw_text(c.LEFT_X, c.y, title, style="B", size=12.0)
        c.draw_hline(c.LEFT_X, c.RIGHT_X, c.y - 7.5, width=0.75, gray=0.45)
        c.y -= 25.5

    # 2. Profile Summary
    draw_section_header("Profile Summary", top_gap=31.3)
    sum_runs = parse_styled_Runs(data["profile_summary"], "R")
    sum_lines = wrap_styled_words(sum_runs, 11.0, c.RIGHT_X - c.LEFT_X)
    for idx, line in enumerate(sum_lines):
        if idx > 0:
            c.ensure_space(LH)
            c.y -= LH
        c.draw_runs_line(c.LEFT_X, c.y, line, size=11.0)

    # 3. Professional Experience
    draw_section_header("Professional Experience", top_gap=26.2)
    first_comp = True
    for comp in data["professional_experience"]:
        if not first_comp:
            c.ensure_space(36.0)
            c.y -= 24.5
        first_comp = False

        c_name = comp["company"]
        c_loc = comp.get("location", "")
        c_runs = [("B", c_name)] + ([("R", f", {c_loc}")] if c_loc else [])
        c.draw_runs_line(c.LEFT_X, c.y, c_runs, size=11.0)

        for r_idx, role in enumerate(comp.get("roles", [])):
            c.ensure_space(28.0)
            c.y -= 18.6 if r_idx == 0 else 18.6
            c.draw_text(44.8, c.y, role["title"], style="B", size=11.0)
            dates_str = role["dates"]
            dates_w = METRICS["R"].text_width_pt(dates_str, 11.0)
            c.draw_text(551.0 - dates_w, c.y, dates_str, style="R", size=11.0)

            if role.get("products_line"):
                c.ensure_space(LH + 6)
                c.y -= 18.6
                p_runs = [("R", "Products: "), ("I", role["products_line"])]
                p_lines = wrap_styled_words(p_runs, 11.0, c.RIGHT_X - 44.1)
                for pl_idx, pl in enumerate(p_lines):
                    if pl_idx > 0:
                        c.y -= LH
                    c.draw_runs_line(44.1, c.y, pl, size=11.0)

            for b_idx, bullet in enumerate(role.get("bullets", [])):
                gap = 12.7 if (b_idx > 0 or role.get("products_line")) else 18.6
                b_runs = parse_styled_Runs(bullet, "R")
                b_lines = wrap_styled_words(b_runs, 11.0, c.RIGHT_X - 66.6)
                c.ensure_space(len(b_lines) * LH + 4)
                c.y -= gap
                c.draw_bullet_disc(51.5, c.y + 3.2)
                for l_idx, bl in enumerate(b_lines):
                    if l_idx > 0:
                        c.y -= LH
                    c.draw_runs_line(66.6, c.y, bl, size=11.0)

            for g_idx, grp in enumerate(role.get("groups", [])):
                gap = 18.6 if (g_idx == 0 and not role.get("bullets")) else 12.7
                g_runs = parse_styled_Runs(grp["group_title"], "R")
                g_lines = wrap_styled_words(g_runs, 11.0, c.RIGHT_X - 66.6)
                c.ensure_space(len(g_lines) * LH + 4)
                c.y -= gap
                c.draw_bullet_disc(51.5, c.y + 3.2)
                for l_idx, gl in enumerate(g_lines):
                    if l_idx > 0:
                        c.y -= LH
                    c.draw_runs_line(66.6, c.y, gl, size=11.0)

                for sb in grp.get("sub_bullets", []):
                    sb_runs = parse_styled_Runs(sb, "R")
                    sb_lines = wrap_styled_words(sb_runs, 11.0, c.RIGHT_X - 84.6)
                    c.ensure_space(len(sb_lines) * LH + 4)
                    c.y -= LH
                    c.draw_bullet_circle(69.5, c.y + 3.2)
                    for l_idx, sbl in enumerate(sb_lines):
                        if l_idx > 0:
                            c.y -= LH
                        c.draw_runs_line(84.6, c.y, sbl, size=11.0)

    # 4. Certifications
    draw_section_header("Certifications", top_gap=26.2)
    for cert in data.get("certifications", []):
        c.draw_text(c.LEFT_X, c.y, cert["institution"], style="BI", size=12.0)
        cd_w = METRICS["R"].text_width_pt(cert["dates"], 11.0)
        c.draw_text(572.5 - cd_w, c.y, cert["dates"], style="R", size=11.0)
        for b in cert.get("bullets", []):
            b_runs = parse_styled_Runs(b, "R")
            b_lines = wrap_styled_words(b_runs, 11.0, c.RIGHT_X - 66.6)
            c.ensure_space(len(b_lines) * LH + 4)
            c.y -= LH
            c.draw_bullet_disc(51.5, c.y + 3.2)
            for l_idx, bl in enumerate(b_lines):
                if l_idx > 0:
                    c.y -= LH
                c.draw_runs_line(66.6, c.y, bl, size=11.0)

    # 5. Social Entrepreneurship
    draw_section_header("Social Entrepreneurship", top_gap=26.2)
    for s_idx, item in enumerate(data.get("social_entrepreneurship", [])):
        if s_idx > 0:
            c.y -= LH
        s_runs = parse_styled_Runs(item, "R")
        s_lines = wrap_styled_words(s_runs, 11.0, c.RIGHT_X - 80.1)
        c.ensure_space(len(s_lines) * LH + 4)
        c.draw_bullet_disc(65.0, c.y + 3.2)
        for l_idx, sl in enumerate(s_lines):
            if l_idx > 0:
                c.y -= LH
            c.draw_runs_line(80.1, c.y, sl, size=11.0)

    # 6. Education
    draw_section_header("Education", top_gap=26.2)
    c.y -= 6.0
    for e_idx, edu in enumerate(data.get("education", [])):
        if e_idx > 0:
            c.y -= 23.9
        c.ensure_space(28.0)
        e_runs = [("B", edu["institution"])]
        if edu.get("location"):
            e_runs.append(("R", f", {edu['location']}"))
        c.draw_runs_line(35.8, c.y, e_runs, size=11.0)
        c.draw_text(434.8, c.y - 6.3, edu["dates"], style="R", size=11.0)
        c.y -= LH
        c.draw_text(35.8, c.y, edu["degree"], style="R", size=11.0)

    c.save(out_path)


def validate_locked_fields(data: dict) -> list[str]:
    errors = []
    meta = data.get("metadata", {})
    if meta.get("profile_version") != "1.1.0":
        errors.append(
            f"Gate 3 Error: metadata.profile_version is '{meta.get('profile_version')}', expected '1.1.0'."
        )

    header = data.get("header", {})
    if header.get("name") != "Minesh Wadhwa":
        errors.append("Gate 6 Error: header.name must be 'Minesh Wadhwa'.")

    exp = data.get("professional_experience", [])
    if len(exp) != len(LOCKED_COMPANIES):
        errors.append(
            f"Gate 6 Error: Expected {len(LOCKED_COMPANIES)} companies in professional_experience, found {len(exp)}."
        )
    else:
        for idx, (comp_name, comp_loc, expected_roles) in enumerate(LOCKED_COMPANIES):
            actual_comp = exp[idx]
            if actual_comp.get("company") != comp_name:
                errors.append(
                    f"Gate 6 Error: Company #{idx+1} is '{actual_comp.get('company')}', expected '{comp_name}'."
                )
            roles = actual_comp.get("roles", [])
            if len(roles) != len(expected_roles):
                errors.append(
                    f"Gate 6 Error: Company '{comp_name}' has {len(roles)} roles, expected {len(expected_roles)}."
                )
            else:
                for r_idx, (r_title, r_dates) in enumerate(expected_roles):
                    if roles[r_idx].get("title") != r_title or roles[r_idx].get("dates") != r_dates:
                        errors.append(
                            f"Gate 6 Error: Role in '{comp_name}' is ({roles[r_idx].get('title')}, {roles[r_idx].get('dates')}), "
                            f"expected ({r_title}, {r_dates})."
                        )
    return errors


def build_markdown(data: dict) -> str:
    lines = [
        f"# {data['header']['name']}",
        f"{data['header']['contact_line']}",
        "",
        "## Profile Summary",
        data["profile_summary"],
        "",
        "## Professional Experience",
    ]
    for comp in data["professional_experience"]:
        lines.append(f"\n### {comp['company']}, {comp.get('location', '')}")
        for role in comp.get("roles", []):
            lines.append(f"**{role['title']}** | {role['dates']}")
            if role.get("products_line"):
                lines.append(f"*Products: {role['products_line']}*")
            for b in role.get("bullets", []):
                lines.append(f"- {b}")
            for grp in role.get("groups", []):
                lines.append(f"- {grp['group_title']}")
                for sb in grp.get("sub_bullets", []):
                    lines.append(f"  - {sb}")
    lines.append("\n## Certifications")
    for cert in data.get("certifications", []):
        lines.append(f"***{cert['institution']}*** | {cert['dates']}")
        for b in cert.get("bullets", []):
            lines.append(f"- {b}")
    lines.append("\n## Social Entrepreneurship")
    for s in data.get("social_entrepreneurship", []):
        lines.append(f"- {s}")
    lines.append("\n## Education")
    for edu in data.get("education", []):
        loc = f", {edu['location']}" if edu.get("location") else ""
        lines.append(f"- **{edu['institution']}**{loc} — {edu['degree']} ({edu['dates']})")
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description="Render CV JSON to PDF and Markdown.")
    parser.add_argument("--input", required=True, help="Path to input CV JSON file.")
    parser.add_argument("--output", required=True, help="Path to output PDF file.")
    parser.add_argument("--markdown", required=False, help="Optional path to output Markdown CV.")
    args = parser.parse_args()

    input_path = Path(args.input).resolve()
    output_pdf = Path(args.output).resolve()
    output_pdf.parent.mkdir(parents=True, exist_ok=True)

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    errors = validate_locked_fields(data)
    if errors:
        for e in errors:
            print(e, file=sys.stderr)
        sys.exit(1)

    if args.markdown:
        md_path = Path(args.markdown).resolve()
        md_path.parent.mkdir(parents=True, exist_ok=True)
        md_path.write_text(build_markdown(data), encoding="utf-8")

    render_cv_to_pdf(data, output_pdf)

    reader = pypdf.PdfReader(str(output_pdf))
    num_pages = len(reader.pages)
    print(f"Rendered PDF: {output_pdf} ({num_pages} pages)")
    if num_pages > 2:
        print(
            f"WARNING: Generated PDF is {num_pages} pages (exceeds 2-page target).",
            file=sys.stderr,
        )
        sys.exit(2)


if __name__ == "__main__":
    main()
