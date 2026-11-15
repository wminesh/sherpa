#!/usr/bin/env python3
"""
Automated Review Gate Validator (Gates 1-8 & 10) for Sherpa Opportunity Records.
"""

import json
import sys
from pathlib import Path


REQUIRED_DOSSIER_SECTIONS = [
    "## 1. Opportunity Metadata",
    "## 2. JD Review",
    "## 3. Requirement-to-Evidence Matrix",
    "## 4. Fit Assessment",
    "## 5. Application Recommendation",
    "## 6. Tailored Materials",
    "## 7. Mandatory Review Gate Status",
    "## 8. Tracking & User Approval",
]


def validate_opportunity_dir(opp_dir: Path) -> list[str]:
    errors = []
    if not opp_dir.exists() or not opp_dir.is_dir():
        return [f"Opportunity directory does not exist: {opp_dir}"]

    # Gate 1 & 2: jd_full.md
    jd_path = opp_dir / "jd_full.md"
    if not jd_path.exists():
        errors.append("Gate 1/2 FAIL: Missing jd_full.md")
    else:
        jd_text = jd_path.read_text(encoding="utf-8")
        if "LinkedIn URL:" not in jd_text and "http" not in jd_text:
            errors.append("Gate 1 FAIL: jd_full.md missing LinkedIn URL")
        if "Retrieval Status:" not in jd_text:
            errors.append("Gate 2 FAIL: jd_full.md missing Retrieval Status")

    # Dossier check (Gates 3, 4, 5, 8)
    dossier_path = opp_dir / "dossier.md"
    if not dossier_path.exists():
        errors.append("Dossier FAIL: Missing dossier.md")
    else:
        d_text = dossier_path.read_text(encoding="utf-8")
        for sec in REQUIRED_DOSSIER_SECTIONS:
            if sec not in d_text:
                errors.append(f"Dossier FAIL: Missing section '{sec}' in dossier.md")
        if "v1.1.0" not in d_text:
            errors.append("Gate 3 FAIL: dossier.md does not verify canonical profile version v1.1.0")

    # Check if tailored materials exist (required if recommended to Apply)
    cv_json = opp_dir / "cv_tailored.json"
    if cv_json.exists():
        # Must also have changelog, fact_check_report, ats_editorial_report, and PDF
        for req_file in ["cv_changelog.md", "fact_check_report.md", "ats_editorial_report.md"]:
            p = opp_dir / req_file
            if not p.exists():
                errors.append(f"Gate 6/7/8 FAIL: Missing {req_file} for tailored CV")
            else:
                txt = p.read_text(encoding="utf-8")
                if req_file in ("fact_check_report.md", "ats_editorial_report.md") and "PASS" not in txt:
                    errors.append(f"Gate Audit FAIL: {req_file} does not contain 'PASS' verdict")
        pdfs = list(opp_dir.glob("*.pdf"))
        if not pdfs:
            errors.append("PDF FAIL: No rendered tailored PDF CV found in opportunity folder")

    return errors


def main():
    if len(sys.argv) < 2:
        print("Usage: validate_opportunity_record.py <opportunity-dir>", file=sys.stderr)
        sys.exit(1)

    opp_dir = Path(sys.argv[1]).resolve()
    errors = validate_opportunity_dir(opp_dir)
    if errors:
        print(f"VALIDATION FAILED for {opp_dir.name}:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    print(f"VALIDATION PASSED (Gates 1-8 verified) for {opp_dir.name}")


if __name__ == "__main__":
    main()
