#!/usr/bin/env python3
"""
Builds the organized Job Application Hub for /Users/mineshwadhwa/Documents/Sherpa/:
  - dashboard/
      - index.html                               (Interactive UI Dashboard)
      - 00_Jobs_Listed_and_Application_Status.md (Master status & index)
  - tailored_cvs/
      - 01_<Company>_<Role>_CV.pdf ..            (Finished PDF CVs)
      - md/                                      (Markdown CV copies)
  - jds/
      - 01_<Company>_<Role>_JD.md ..             (All full Job Descriptions)
"""

import json
import shutil
from pathlib import Path

BASE_DIR = Path("/Users/mineshwadhwa/Documents/Sherpa")
TRACKER_JSON = BASE_DIR / "tracker" / "application_tracker.json"
DASHBOARD_DIR = BASE_DIR / "dashboard"
TAILORED_CVS_DIR = BASE_DIR / "tailored_cvs"
TAILORED_CVS_MD_DIR = TAILORED_CVS_DIR / "md"
JDS_DIR = BASE_DIR / "jds"

SLUG_MAP = {
    "4479117229-nutanix-spm-ai": ("01", "Nutanix_SPM_AI"),
    "4485584664-motive-spm-growth": ("02", "Motive_SPM_Growth"),
    "4488864307-elsa-pm-b2c": ("03", "ELSA_PM_B2C"),
    "4489943092-target-pm-cdp": ("04", "Target_PM_CDP"),
    "4480353427-sage-spm": ("05", "Sage_SPM"),
    "4470165775-duck-creek-spm-agentic": ("06", "Duck_Creek_SPM_Agentic"),
    "4488679433-rippling-lead-pm": ("07", "Rippling_Lead_PM"),
    "4489495690-razorpay-spm": ("08", "Razorpay_SPM_Hold"),
    "4488663182-intuit-staff-pm": ("09", "Intuit_Staff_PM_DoNotApply"),
    "4480375215-microsoft-spm": ("10", "Microsoft_SPM_DoNotApply"),
}


def read_text_safe(path_str: str) -> str:
    if not path_str:
        return ""
    p = Path(path_str)
    if p.exists():
        return p.read_text(encoding="utf-8")
    return ""


def read_json_safe(path_str: str) -> dict:
    if not path_str:
        return {}
    p = Path(path_str)
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    return {}


HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Sherpa — Job Application Dashboard</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    __FALLBACK_VARS__
    .custom-scroll::-webkit-scrollbar { width: 6px; height: 6px; }
    .custom-scroll::-webkit-scrollbar-track { background: transparent; }
    .custom-scroll::-webkit-scrollbar-thumb { background: rgba(148, 163, 184, 0.35); border-radius: 3px; }
    .markdown-body h1 { font-size: 1.25rem; font-weight: 700; margin-top: 0.75rem; margin-bottom: 0.5rem; }
    .markdown-body h2 { font-size: 1.05rem; font-weight: 600; margin-top: 1rem; margin-bottom: 0.4rem; padding-bottom: 0.25rem; border-bottom: 1px solid var(--border); }
    .markdown-body h3 { font-size: 0.95rem; font-weight: 600; margin-top: 0.75rem; margin-bottom: 0.25rem; }
    .markdown-body p { margin-bottom: 0.5rem; line-height: 1.55; }
    .markdown-body ul { list-style-type: disc; padding-left: 1.25rem; margin-bottom: 0.6rem; }
    .markdown-body li { margin-bottom: 0.25rem; line-height: 1.5; }
    .markdown-body code { font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 0.8rem; padding: 0.1rem 0.3rem; border-radius: 0.25rem; border: 1px solid var(--border); }
  </style>
</head>
<body class="bg-[var(--background)] text-[var(--foreground)] antialiased p-4 md:p-6">
  <div class="max-w-7xl mx-auto space-y-5">

    <!-- Top Header Card -->
    <div class="bg-[var(--card)] border border-[var(--border)] rounded-xl p-5 shadow-sm">
      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
        <div>
          <div class="flex items-center gap-2.5 flex-wrap">
            <span class="px-2.5 py-0.5 text-xs font-semibold rounded-full bg-emerald-500/15 text-emerald-500 border border-emerald-500/30">
              Gates 1–8 &amp; 10 PASS
            </span>
            <span class="px-2.5 py-0.5 text-xs font-medium rounded-full border border-[var(--border)] text-[var(--muted-foreground)]">
              Canonical Profile v<span id="hdr-profile-ver">1.1.0</span>
            </span>
            <span class="px-2.5 py-0.5 text-xs font-medium rounded-full border border-[var(--border)] text-[var(--muted-foreground)]" id="hdr-scan-window">
              Nov 5 – Nov 12, 2026
            </span>
          </div>
          <h1 class="text-xl md:text-2xl font-bold mt-2 text-[var(--foreground)]">
            Sherpa — Job Application Progress, JDs &amp; Tailored CVs
          </h1>
          <p class="text-sm text-[var(--muted-foreground)] mt-1">
            Dashboard: <code class="text-xs px-1.5 py-0.5 rounded border border-[var(--border)] select-all">/Users/mineshwadhwa/Documents/Sherpa/dashboard/</code>
            · PDF CVs: <code class="text-xs px-1.5 py-0.5 rounded border border-[var(--border)] select-all">/Users/mineshwadhwa/Documents/Sherpa/tailored_cvs/</code>
            · JDs: <code class="text-xs px-1.5 py-0.5 rounded border border-[var(--border)] select-all">/Users/mineshwadhwa/Documents/Sherpa/jds/</code>
          </p>
        </div>

        <div class="flex flex-wrap items-center gap-2">
          <button onclick="exportStatusSnapshot()" class="px-3.5 py-1.5 text-xs font-semibold rounded-lg bg-[var(--primary)] text-[var(--primary-foreground)] hover:opacity-90 transition">
            Export Status Snapshot (.json)
          </button>
        </div>
      </div>

      <!-- Funnel KPI Strip -->
      <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3 mt-5">
        <div class="p-3 rounded-lg border border-[var(--border)] bg-[var(--background)]">
          <div class="text-xs text-[var(--muted-foreground)]">Listed Jobs Discovered</div>
          <div class="text-2xl font-bold mt-0.5" id="kpi-total-jobs">49</div>
          <div class="text-xs text-[var(--muted-foreground)] mt-0.5">From 16 Gmail alerts</div>
        </div>
        <div class="p-3 rounded-lg border border-[var(--border)] bg-[var(--background)]">
          <div class="text-xs text-[var(--muted-foreground)]">Gate 1 Pass (BLR/India)</div>
          <div class="text-2xl font-bold mt-0.5 text-sky-500" id="kpi-gate1-pass">41</div>
          <div class="text-xs text-[var(--muted-foreground)] mt-0.5">8 excluded · 1 applied</div>
        </div>
        <div class="p-3 rounded-lg border border-[var(--border)] bg-[var(--background)]">
          <div class="text-xs text-[var(--muted-foreground)]">Full JDs Evaluated</div>
          <div class="text-2xl font-bold mt-0.5 text-indigo-500" id="kpi-evaluated">10</div>
          <div class="text-xs text-[var(--muted-foreground)] mt-0.5">Batch 1 (10 JDs in folder)</div>
        </div>
        <div class="p-3 rounded-lg border border-[var(--border)] bg-[var(--background)]">
          <div class="text-xs text-[var(--muted-foreground)]">Tailored PDF CVs</div>
          <div class="text-2xl font-bold mt-0.5 text-emerald-500" id="kpi-cvs">7</div>
          <div class="text-xs text-[var(--muted-foreground)] mt-0.5">4 High Priority · 3 Consider</div>
        </div>
        <div class="p-3 rounded-lg border border-[var(--border)] bg-[var(--background)]">
          <div class="text-xs text-[var(--muted-foreground)]">Approved / Applied</div>
          <div class="text-2xl font-bold mt-0.5 text-amber-500" id="kpi-approved-applied">1</div>
          <div class="text-xs text-[var(--muted-foreground)] mt-0.5" id="kpi-pending-sub">7 pending Gate 9 approval</div>
        </div>
        <div class="p-3 rounded-lg border border-[var(--border)] bg-[var(--background)]">
          <div class="text-xs text-[var(--muted-foreground)]">Batch 2 Queue</div>
          <div class="text-2xl font-bold mt-0.5" id="kpi-batch2">35</div>
          <div class="text-xs text-[var(--muted-foreground)] mt-0.5">Awaiting JD deep-dive</div>
        </div>
      </div>

      <!-- Workflow Progress Bar -->
      <div class="mt-4 pt-4 border-t border-[var(--border)]">
        <div class="flex items-center justify-between text-xs mb-1.5">
          <span class="font-medium text-[var(--foreground)]">Batch 1 End-to-End Gate Pipeline (Gates 1–8 Complete · Gate 9 User Approval Ready)</span>
          <span class="text-[var(--muted-foreground)]" id="pipeline-pct-label">90% Complete (9 / 10 Gates Passed)</span>
        </div>
        <div class="w-full h-2.5 rounded-full bg-[var(--background)] border border-[var(--border)] overflow-hidden flex">
          <div class="bg-emerald-500 h-full" style="width: 80%" title="Gates 1–8 Passed"></div>
          <div class="bg-amber-500 h-full" style="width: 10%" title="Gate 9 Pending User Approval"></div>
          <div class="bg-emerald-500 h-full" style="width: 10%" title="Gate 10 Tracker Synced"></div>
        </div>
        <div class="grid grid-cols-2 sm:grid-cols-5 lg:grid-cols-10 gap-1.5 mt-2.5 text-xs">
          <div class="px-2 py-1 rounded border border-emerald-500/30 bg-emerald-500/10 text-emerald-500 font-medium truncate" title="Gate 1: Opportunity Validation">G1: Validated ✓</div>
          <div class="px-2 py-1 rounded border border-emerald-500/30 bg-emerald-500/10 text-emerald-500 font-medium truncate" title="Gate 2: Full JD Confirmation">G2: Full JDs ✓</div>
          <div class="px-2 py-1 rounded border border-emerald-500/30 bg-emerald-500/10 text-emerald-500 font-medium truncate" title="Gate 3: Canonical Profile Lock">G3: Profile v1.1 ✓</div>
          <div class="px-2 py-1 rounded border border-emerald-500/30 bg-emerald-500/10 text-emerald-500 font-medium truncate" title="Gate 4: Evidence Classification">G4: D/A/G Map ✓</div>
          <div class="px-2 py-1 rounded border border-emerald-500/30 bg-emerald-500/10 text-emerald-500 font-medium truncate" title="Gate 5: Role Fit & Prioritisation">G5: Fit Scored ✓</div>
          <div class="px-2 py-1 rounded border border-emerald-500/30 bg-emerald-500/10 text-emerald-500 font-medium truncate" title="Gate 6: Fact-Check Review">G6: Fact-Check ✓</div>
          <div class="px-2 py-1 rounded border border-emerald-500/30 bg-emerald-500/10 text-emerald-500 font-medium truncate" title="Gate 7: Confidentiality Review">G7: Safe Disclosure ✓</div>
          <div class="px-2 py-1 rounded border border-emerald-500/30 bg-emerald-500/10 text-emerald-500 font-medium truncate" title="Gate 8: ATS & Editorial Review">G8: ATS Audit ✓</div>
          <div class="px-2 py-1 rounded border border-amber-500/40 bg-amber-500/10 text-amber-500 font-medium truncate" title="Gate 9: User Approval">G9: User Review</div>
          <div class="px-2 py-1 rounded border border-emerald-500/30 bg-emerald-500/10 text-emerald-500 font-medium truncate" title="Gate 10: Tracker Updated">G10: Tracked ✓</div>
        </div>
      </div>
    </div>

    <!-- ==================== UNIFIED WORKSPACE (ALL JOBS MASTER-DETAIL) ==================== -->
    <div id="view-workspace" class="space-y-4">
      <!-- Unified Filter & Search Bar -->
      <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-3 bg-[var(--card)] border border-[var(--border)] rounded-xl p-3.5">
        <div class="flex flex-wrap gap-1.5" id="unified-filter-pills"></div>
        <div class="relative w-full lg:w-72 shrink-0">
          <input id="unified-search" type="text" oninput="renderUnifiedList()" placeholder="Search by company, role, location, job ID..." class="w-full px-3 py-1.5 text-xs rounded-lg bg-[var(--background)] border border-[var(--border)] text-[var(--foreground)] placeholder-[var(--muted-foreground)] focus:outline-none" />
        </div>
      </div>

      <!-- Master-Detail Grid -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-4 items-start">
        <!-- Left Column: Unified Job Cards -->
        <div id="unified-list-container" class="lg:col-span-5 space-y-2.5 max-h-[780px] overflow-y-auto custom-scroll pr-1"></div>

        <!-- Right Column: Selected Job Inspector -->
        <div id="unified-detail-container" class="lg:col-span-7 bg-[var(--card)] border border-[var(--border)] rounded-xl p-5 shadow-sm"></div>
      </div>
    </div>

  </div>

  <script>
    const DASHBOARD_DATA = __DASHBOARD_JSON_PAYLOAD__;
    const STORAGE_KEY = "sherpa_application_statuses_v1";

    let currentUnifiedFilter = "ALL";
    let selectedJobKey = DASHBOARD_DATA.evaluated_batch_1[0]?.opportunity_id || null;
    let currentDetailSubTab = "jd"; // 'jd' | 'cv' | 'fit' | 'matrix' | 'audits'
    let currentCvSubMode = "formatted"; // 'formatted' | 'changelog' | 'pdf'

    function loadSavedStatuses() {
      try {
        const raw = localStorage.getItem(STORAGE_KEY);
        return raw ? JSON.parse(raw) : {};
      } catch (e) {
        return {};
      }
    }

    function saveStatus(key, val) {
      try {
        const map = loadSavedStatuses();
        map[key] = val;
        localStorage.setItem(STORAGE_KEY, JSON.stringify(map));
      } catch (e) {}
      updateTopKpis();
      renderUnifiedList();
      renderUnifiedDetail();
    }

    function getJobStatus(key, defaultStatus) {
      const map = loadSavedStatuses();
      return map[key] || defaultStatus;
    }

    function exportStatusSnapshot() {
      const statuses = {};
      getUnifiedJobs().forEach(job => {
        if (job.kind === "BATCH1") {
          const item = job.batch1Item;
          statuses[job.key] = {
            job_id: job.job_id,
            stage: job.stage,
            company: item.company,
            role_title: item.role_title,
            fit_score: item.overall_fit_score,
            recommendation: item.recommendation,
            jd_file: item.dashboard_jd_file,
            cv_pdf_file: item.dashboard_cv_pdf_file,
            cv_md_file: item.dashboard_cv_md_file,
            status: getJobStatus(job.key, job.defaultStatus)
          };
        } else {
          statuses[job.key] = {
            job_id: job.job_id,
            stage: job.stage,
            company: job.company,
            role_title: job.role_title,
            location: job.location,
            status: getJobStatus(job.key, job.defaultStatus)
          };
        }
      });
      const blob = new Blob([JSON.stringify(statuses, null, 2)], { type: "application/json" });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = "sherpa_application_status_snapshot.json";
      a.click();
      URL.revokeObjectURL(url);
    }

    function escapeHtml(str) {
      if (str === null || str === undefined) return "";
      return String(str)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;");
    }

    function cleanMarkdownForView(md, kind) {
      if (!md) return "";
      const lines = md.split("\n");
      if (kind === "jd") {
        const provIdx = lines.findIndex(l => l.startsWith("## Source Email Provenance"));
        const jdIdx = lines.findIndex(l => l.startsWith("## Full Verbatim Job Description"));
        const startIdx = provIdx !== -1 ? provIdx : (jdIdx !== -1 ? jdIdx : 0);
        return lines.slice(startIdx).join("\n").trim();
      }
      if (kind === "audit" || kind === "dossier") {
        const redundantKeys = [
          "Opportunity ID:", "Target Company:", "Company:", "Target Role:", "Job Title:",
          "Role Title:", "Location:", "Location & Work Mode:", "LinkedIn URL:",
          "Canonical Master Profile Version:", "Canonical Source:", "Canonical Baseline:",
          "Guardrails Reference:"
        ];
        const out = [];
        let inHeaderBlock = true;
        for (let i = 0; i < lines.length; i++) {
          const line = lines[i];
          if (i === 0 && line.startsWith("# ")) continue;
          if (inHeaderBlock) {
            if (/^##\s+(Audit Metadata|1\. Opportunity Metadata)\s*$/.test(line.trim())) continue;
            if (/^##\s+/.test(line.trim())) {
              inHeaderBlock = false;
              out.push(line);
              continue;
            }
            if (line.trim().startsWith("- **") && redundantKeys.some(k => line.includes(k))) continue;
            if (line.trim() === "---" && out.every(x => x.trim() === "")) continue;
          }
          out.push(line);
        }
        return out.join("\n").trim();
      }
      return md;
    }

    function renderSimpleMarkdown(md) {
      if (!md) return "<p class='text-xs text-[var(--muted-foreground)]'>No content available.</p>";
      const lines = md.split("\n");
      let html = "";
      let inList = false;
      for (let rawLine of lines) {
        const line = rawLine.trimEnd();
        if (line.startsWith("# ")) {
          if (inList) { html += "</ul>"; inList = false; }
          html += `<h1>${formatInline(line.slice(2))}</h1>`;
        } else if (line.startsWith("## ")) {
          if (inList) { html += "</ul>"; inList = false; }
          html += `<h2>${formatInline(line.slice(3))}</h2>`;
        } else if (line.startsWith("### ")) {
          if (inList) { html += "</ul>"; inList = false; }
          html += `<h3>${formatInline(line.slice(4))}</h3>`;
        } else if (line.startsWith("- ") || line.startsWith("  - ") || line.startsWith("    - ")) {
          if (!inList) { html += "<ul>"; inList = true; }
          const indent = line.startsWith("    - ") ? "ml-6" : (line.startsWith("  - ") ? "ml-3" : "");
          html += `<li class="${indent}">${formatInline(line.replace(/^\s*-\s+/, ""))}</li>`;
        } else if (line.trim() === "---") {
          if (inList) { html += "</ul>"; inList = false; }
          html += `<hr class="my-3 border-[var(--border)]" />`;
        } else if (line.trim() === "") {
          if (inList) { html += "</ul>"; inList = false; }
        } else {
          if (inList) { html += "</ul>"; inList = false; }
          html += `<p>${formatInline(line)}</p>`;
        }
      }
      if (inList) html += "</ul>";
      return `<div class="markdown-body text-xs md:text-sm">${html}</div>`;
    }

    function formatInline(text) {
      let s = escapeHtml(text);
      s = s.replace(/\*\*\*(.+?)\*\*\*/g, "<strong><em>$1</em></strong>");
      s = s.replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");
      s = s.replace(/\*(.+?)\*/g, "<em>$1</em>");
      s = s.replace(/`([^`]+)`/g, "<code>$1</code>");
      return s;
    }

    function getScoreBadgeClasses(score) {
      if (score >= 83) return "bg-emerald-500/15 text-emerald-500 border-emerald-500/30";
      if (score >= 75) return "bg-sky-500/15 text-sky-500 border-sky-500/30";
      if (score >= 65) return "bg-amber-500/15 text-amber-500 border-amber-500/30";
      return "bg-rose-500/15 text-rose-500 border-rose-500/30";
    }

    function getDecisionBadgeClasses(decision) {
      if (decision === "Apply") return "bg-emerald-500/15 text-emerald-500 border-emerald-500/30";
      if (decision === "Hold") return "bg-amber-500/15 text-amber-500 border-amber-500/30";
      return "bg-rose-500/15 text-rose-500 border-rose-500/30";
    }

    function updateTopKpis() {
      const s = DASHBOARD_DATA.summary || {};
      document.getElementById("kpi-total-jobs").textContent = s.unique_linkedin_jobs_discovered || 49;
      document.getElementById("kpi-gate1-pass").textContent = s.gate_1_pass_count || 41;
      document.getElementById("kpi-evaluated").textContent = s.batch_1_evaluated_count || 10;
      document.getElementById("kpi-cvs").textContent = s.tailored_pdf_cvs_generated || 7;
      document.getElementById("kpi-batch2").textContent = (DASHBOARD_DATA.secondary_queue_batch_2 || []).length;

      let approvedOrApplied = (DASHBOARD_DATA.already_applied || []).length;
      let pendingApproval = 0;
      DASHBOARD_DATA.evaluated_batch_1.forEach(item => {
        const st = getJobStatus(item.opportunity_id, item.application_status);
        if (st.includes("Approved") || st === "Applied") approvedOrApplied++;
        else if (st.includes("Pending") && item.recommendation === "Apply") pendingApproval++;
      });
      document.getElementById("kpi-approved-applied").textContent = approvedOrApplied;
      document.getElementById("kpi-pending-sub").textContent = `${pendingApproval} Apply roles pending Gate 9`;
    }

    function getUnifiedJobs() {
      const rows = [];
      (DASHBOARD_DATA.evaluated_batch_1 || []).forEach(item => {
        rows.push({
          key: item.opportunity_id,
          kind: "BATCH1",
          stage: "Evaluated Batch 1",
          job_id: item.job_id,
          company: item.company,
          role_title: item.role_title,
          location: `${item.location} (${item.workplace_mode})`,
          linkedin_url: item.linkedin_url || "",
          defaultStatus: item.application_status,
          searchText: `${item.job_id} ${item.company} ${item.role_title} ${item.location} ${item.priority_band} ${item.recommendation} Evaluated Batch 1`.toLowerCase(),
          batch1Item: item
        });
      });

      (DASHBOARD_DATA.secondary_queue_batch_2 || []).forEach(sq => {
        const key = `sq-${sq.job_id}`;
        const defaultStatus = sq.queue_status || "Secondary Queue (Batch 2)";
        rows.push({
          key,
          kind: "BATCH2",
          stage: "Batch 2 Queue",
          job_id: sq.job_id,
          company: sq.company,
          role_title: sq.role_title,
          location: sq.location || "",
          linkedin_url: sq.linkedin_url || "",
          defaultStatus,
          searchText: `${sq.job_id} ${sq.company} ${sq.role_title} ${sq.location} Batch 2 Queue ${defaultStatus}`.toLowerCase(),
          meta: sq
        });
      });

      (DASHBOARD_DATA.already_applied || []).forEach(app => {
        const key = `app-${app.job_id}`;
        const defaultStatus = `Already Applied (${app.applied_date || ""})`;
        rows.push({
          key,
          kind: "APPLIED",
          stage: "Already Applied",
          job_id: app.job_id,
          company: app.company,
          role_title: app.role_title,
          location: app.location || "",
          linkedin_url: app.linkedin_url || "",
          defaultStatus,
          searchText: `${app.job_id} ${app.company} ${app.role_title} ${app.location} Already Applied ${app.notes || ""}`.toLowerCase(),
          meta: app
        });
      });

      (DASHBOARD_DATA.gate_1_exclusions || []).forEach(exc => {
        const key = `exc-${exc.job_id}`;
        const defaultStatus = exc.gate_1_status || "Gate 1 Excluded";
        rows.push({
          key,
          kind: "EXCLUDED",
          stage: `Gate 1 Excluded (${defaultStatus})`,
          job_id: exc.job_id,
          company: exc.company || "",
          role_title: exc.role_title || "",
          location: exc.location || "",
          linkedin_url: exc.linkedin_url || "",
          defaultStatus,
          searchText: `${exc.job_id} ${exc.company} ${exc.role_title} ${exc.location} Gate 1 Excluded ${defaultStatus} ${exc.reason || ""}`.toLowerCase(),
          meta: exc
        });
      });

      return rows;
    }

    function renderUnifiedFilterPills() {
      const jobs = getUnifiedJobs();
      const b1 = jobs.filter(j => j.kind === "BATCH1");
      const counts = {
        ALL: jobs.length,
        BATCH1: b1.length,
        HAS_CV: b1.filter(j => !!j.batch1Item.dashboard_cv_pdf_file).length,
        HIGH: b1.filter(j => j.batch1Item.priority_band === "High Priority").length,
        CONSIDER: b1.filter(j => j.batch1Item.priority_band === "Consider").length,
        DNA: b1.filter(j => j.batch1Item.recommendation === "Do Not Apply").length,
        BATCH2: jobs.filter(j => j.kind === "BATCH2").length,
        APPLIED: jobs.filter(j => j.kind === "APPLIED").length,
        EXCLUDED: jobs.filter(j => j.kind === "EXCLUDED").length
      };

      const defs = [
        ["ALL", `All Jobs (${counts.ALL})`],
        ["BATCH1", `Evaluated (${counts.BATCH1})`],
        ["HAS_CV", `With Tailored CV (${counts.HAS_CV})`],
        ["HIGH", `High Priority (${counts.HIGH})`],
        ["CONSIDER", `Consider (${counts.CONSIDER})`],
        ["DNA", `Do Not Apply (${counts.DNA})`],
        ["BATCH2", `Batch 2 Queue (${counts.BATCH2})`],
        ["APPLIED", `Already Applied (${counts.APPLIED})`],
        ["EXCLUDED", `Gate 1 Excluded (${counts.EXCLUDED})`]
      ];

      const container = document.getElementById("unified-filter-pills");
      container.innerHTML = defs.map(([id, label]) => {
        const active = currentUnifiedFilter === id;
        return `<button onclick="setUnifiedFilter('${id}')" class="px-3 py-1 text-xs rounded-lg transition ${active ? 'font-semibold bg-[var(--primary)] text-[var(--primary-foreground)]' : 'font-medium border border-[var(--border)] text-[var(--muted-foreground)] hover:text-[var(--foreground)]'}">${escapeHtml(label)}</button>`;
      }).join("");
    }

    function setUnifiedFilter(filter) {
      currentUnifiedFilter = filter;
      renderUnifiedFilterPills();
      renderUnifiedList();
    }

    function renderUnifiedList() {
      const container = document.getElementById("unified-list-container");
      const query = (document.getElementById("unified-search")?.value || "").toLowerCase().trim();

      const filtered = getUnifiedJobs().filter(job => {
        if (currentUnifiedFilter === "BATCH1" && job.kind !== "BATCH1") return false;
        if (currentUnifiedFilter === "HAS_CV" && !(job.kind === "BATCH1" && job.batch1Item.dashboard_cv_pdf_file)) return false;
        if (currentUnifiedFilter === "HIGH" && !(job.kind === "BATCH1" && job.batch1Item.priority_band === "High Priority")) return false;
        if (currentUnifiedFilter === "CONSIDER" && !(job.kind === "BATCH1" && job.batch1Item.priority_band === "Consider")) return false;
        if (currentUnifiedFilter === "DNA" && !(job.kind === "BATCH1" && job.batch1Item.recommendation === "Do Not Apply")) return false;
        if (currentUnifiedFilter === "BATCH2" && job.kind !== "BATCH2") return false;
        if (currentUnifiedFilter === "APPLIED" && job.kind !== "APPLIED") return false;
        if (currentUnifiedFilter === "EXCLUDED" && job.kind !== "EXCLUDED") return false;
        if (query) {
          const curStatus = getJobStatus(job.key, job.defaultStatus).toLowerCase();
          if (!job.searchText.includes(query) && !curStatus.includes(query)) return false;
        }
        return true;
      });

      if (filtered.length === 0) {
        container.innerHTML = `<div class="p-6 text-center text-xs text-[var(--muted-foreground)] border border-[var(--border)] rounded-xl bg-[var(--card)]">No jobs match the current filter.</div>`;
        return;
      }

      if (!filtered.some(x => x.key === selectedJobKey)) {
        selectedJobKey = filtered[0].key;
        renderUnifiedDetail();
      }

      const batch1StatusOptions = [
        "Evaluated — Pending User Approval (Gate 9)",
        "Approved — Ready to Apply",
        "Applied",
        "On Hold",
        "Do Not Apply / Archived"
      ];

      container.innerHTML = filtered.map(job => {
        const isSelected = job.key === selectedJobKey;
        const curStatus = getJobStatus(job.key, job.defaultStatus);

        if (job.kind === "BATCH1") {
          const item = job.batch1Item;
          const ev = item.evidence_counts || { direct: 0, adjacent: 0, gap: 0 };
          return `
            <div onclick="selectUnifiedJob('${job.key}')" class="cursor-pointer rounded-xl p-3.5 border transition ${isSelected ? 'border-[var(--primary)] bg-[var(--card)] ring-1 ring-[var(--primary)] shadow-sm' : 'border-[var(--border)] bg-[var(--card)] hover:border-[var(--muted-foreground)]'}">
              <div class="flex items-start justify-between gap-2">
                <div class="min-w-0">
                  <div class="flex items-center gap-1.5 flex-wrap">
                    <span class="text-xs font-bold px-1.5 py-0.5 rounded bg-[var(--background)] border border-[var(--border)]">#${item.rank}</span>
                    <span class="text-sm font-bold text-[var(--foreground)] truncate">${escapeHtml(item.company)}</span>
                    <span class="text-xs px-2 py-0.5 rounded-full border font-semibold ${getDecisionBadgeClasses(item.recommendation)}">${escapeHtml(item.recommendation)}</span>
                  </div>
                  <div class="text-xs font-medium text-[var(--foreground)] mt-1 leading-snug">${escapeHtml(item.role_title)}</div>
                  <div class="text-xs text-[var(--muted-foreground)] mt-0.5">${escapeHtml(item.location)} · ${escapeHtml(item.workplace_mode)}</div>
                </div>
                <div class="text-right shrink-0">
                  <span class="inline-block text-xs font-bold px-2.5 py-1 rounded-lg border ${getScoreBadgeClasses(item.overall_fit_score)}">
                    ${item.overall_fit_score} / 100
                  </span>
                  <div class="text-xs text-[var(--muted-foreground)] mt-1">${escapeHtml(item.priority_band)}</div>
                </div>
              </div>

              <!-- Compact Evidence & CV Status Pills -->
              <div class="flex flex-wrap items-center gap-1.5 mt-2.5 pt-2.5 border-t border-[var(--border)] text-xs">
                <span class="px-2 py-0.5 rounded bg-[var(--background)] border border-[var(--border)] text-[var(--muted-foreground)]" title="Direct / Adjacent / Gap Evidence">
                  Evidence: <strong class="text-emerald-500">${ev.direct}D</strong> / <strong class="text-amber-500">${ev.adjacent}A</strong> / <strong class="text-rose-500">${ev.gap}G</strong>
                </span>
                ${item.dashboard_cv_pdf_file ? `
                  <span class="px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-500 border border-emerald-500/30 font-medium">
                    Tailored CV Ready
                  </span>
                ` : `
                  <span class="px-2 py-0.5 rounded border border-[var(--border)] text-[var(--muted-foreground)]">
                    No CV (${escapeHtml(item.recommendation)})
                  </span>
                `}
              </div>

              <!-- Status Selector -->
              <div class="mt-2.5 flex items-center justify-between gap-2" onclick="event.stopPropagation()">
                <span class="text-xs text-[var(--muted-foreground)] font-medium">Status:</span>
                <select onchange="saveStatus('${item.opportunity_id}', this.value)" class="flex-1 text-xs px-2 py-1 rounded-lg bg-[var(--background)] border border-[var(--border)] text-[var(--foreground)] focus:outline-none">
                  ${batch1StatusOptions.map(opt => `<option value="${escapeHtml(opt)}" ${curStatus === opt ? 'selected' : ''}>${escapeHtml(opt)}</option>`).join("")}
                </select>
              </div>
            </div>
          `;
        }

        const stageBadgeClass = job.kind === "BATCH2"
          ? "bg-sky-500/15 text-sky-500 border-sky-500/30"
          : (job.kind === "APPLIED"
            ? "bg-emerald-500/15 text-emerald-500 border-emerald-500/30"
            : "bg-rose-500/15 text-rose-500 border-rose-500/30");

        return `
          <div onclick="selectUnifiedJob('${job.key}')" class="cursor-pointer rounded-xl p-3.5 border transition ${isSelected ? 'border-[var(--primary)] bg-[var(--card)] ring-1 ring-[var(--primary)] shadow-sm' : 'border-[var(--border)] bg-[var(--card)] hover:border-[var(--muted-foreground)]'}">
            <div class="flex items-start justify-between gap-2">
              <div class="min-w-0">
                <div class="flex items-center gap-1.5 flex-wrap">
                  <span class="text-xs px-2 py-0.5 rounded-full border font-semibold ${stageBadgeClass}">${escapeHtml(job.stage)}</span>
                  <span class="text-sm font-bold text-[var(--foreground)] truncate">${escapeHtml(job.company)}</span>
                </div>
                <div class="text-xs font-medium text-[var(--foreground)] mt-1 leading-snug">${escapeHtml(job.role_title)}</div>
                <div class="text-xs text-[var(--muted-foreground)] mt-0.5">${escapeHtml(job.location)} · ID: <code>${escapeHtml(job.job_id)}</code></div>
              </div>
              ${job.linkedin_url ? `
                <a href="${escapeHtml(job.linkedin_url)}" target="_blank" rel="noopener noreferrer" onclick="event.stopPropagation()" class="shrink-0 px-2 py-1 text-xs rounded border border-[var(--border)] text-[var(--muted-foreground)] hover:text-[var(--foreground)]">
                  LinkedIn ↗
                </a>
              ` : ""}
            </div>
            <div class="mt-2 pt-2 border-t border-[var(--border)] text-xs text-[var(--muted-foreground)] flex items-center justify-between gap-2">
              <span>Status: <strong class="text-[var(--foreground)]">${escapeHtml(curStatus)}</strong></span>
            </div>
          </div>
        `;
      }).join("");
    }

    function selectUnifiedJob(jobKey) {
      selectedJobKey = jobKey;
      renderUnifiedList();
      renderUnifiedDetail();
    }

    function setDetailSubTab(tab) {
      currentDetailSubTab = tab;
      renderUnifiedDetail();
    }

    function setCvSubMode(mode) {
      currentCvSubMode = mode;
      renderUnifiedDetail();
    }

    function renderUnifiedDetail() {
      const container = document.getElementById("unified-detail-container");
      const job = getUnifiedJobs().find(x => x.key === selectedJobKey);
      if (!job) {
        container.innerHTML = `<div class="text-xs text-[var(--muted-foreground)]">Select a job on the left to inspect its details, JD, CV, and status.</div>`;
        return;
      }

      if (job.kind !== "BATCH1") {
        const curStatus = getJobStatus(job.key, job.defaultStatus);
        const meta = job.meta || {};
        const extraRows = [];
        if (meta.applied_date) extraRows.push(`<div><span class="text-[var(--muted-foreground)]">Applied Date:</span> <strong>${escapeHtml(meta.applied_date)}</strong></div>`);
        if (meta.notes) extraRows.push(`<div><span class="text-[var(--muted-foreground)]">Notes:</span> ${escapeHtml(meta.notes)}</div>`);
        if (meta.queue_status) extraRows.push(`<div><span class="text-[var(--muted-foreground)]">Queue Status:</span> <strong>${escapeHtml(meta.queue_status)}</strong></div>`);
        if (meta.gate_1_status) extraRows.push(`<div><span class="text-[var(--muted-foreground)]">Gate 1 Status:</span> <strong>${escapeHtml(meta.gate_1_status)}</strong></div>`);
        if (meta.reason) extraRows.push(`<div><span class="text-[var(--muted-foreground)]">Disposition Reason:</span> ${escapeHtml(meta.reason)}</div>`);

        container.innerHTML = `
          <div class="space-y-4">
            <div class="flex flex-col sm:flex-row sm:items-start justify-between gap-3 pb-3.5 border-b border-[var(--border)]">
              <div>
                <div class="flex items-center gap-2 flex-wrap">
                  <span class="text-xs font-bold px-2 py-0.5 rounded bg-[var(--background)] border border-[var(--border)]">${escapeHtml(job.stage)}</span>
                  <h2 class="text-lg font-bold text-[var(--foreground)]">${escapeHtml(job.company)} — ${escapeHtml(job.role_title)}</h2>
                </div>
                <p class="text-xs text-[var(--muted-foreground)] mt-1">
                  ${escapeHtml(job.location)} · Job ID: <code>${escapeHtml(job.job_id)}</code> · Status: <strong>${escapeHtml(curStatus)}</strong>
                </p>
              </div>
              <div class="flex items-center gap-2 shrink-0">
                ${job.linkedin_url ? `<a href="${escapeHtml(job.linkedin_url)}" target="_blank" rel="noopener noreferrer" class="px-3 py-1.5 text-xs rounded-lg bg-[var(--primary)] text-[var(--primary-foreground)] font-semibold">View on LinkedIn ↗</a>` : ""}
              </div>
            </div>
            <div class="p-4 rounded-xl bg-[var(--background)] border border-[var(--border)] text-xs space-y-2 leading-relaxed">
              ${extraRows.join("") || `<div class="text-[var(--muted-foreground)]">No additional pipeline notes recorded yet.</div>`}
            </div>
          </div>
        `;
        return;
      }

      const item = job.batch1Item;
      const fit = item.fit_assessment_detail || {};
      const reqMatrix = item.requirement_matrix_detail || {};

      // Sub-tab Content
      let subContentHtml = "";
      if (currentDetailSubTab === "jd") {
        subContentHtml = `
          <div class="space-y-3">
            <div class="flex flex-wrap items-center justify-between gap-2 p-3 rounded-lg bg-[var(--background)] border border-[var(--border)] text-xs">
              <div>
                <span class="font-semibold">JD File:</span>
                <code class="ml-1 select-all">/Users/mineshwadhwa/Documents/Sherpa/jds/${escapeHtml(item.dashboard_jd_file)}</code>
              </div>
              <a href="../jds/${escapeHtml(item.dashboard_jd_file)}" target="_blank" class="px-2.5 py-1 rounded bg-[var(--card)] border border-[var(--border)] hover:text-[var(--foreground)] font-medium">Open Raw JD ↗</a>
            </div>
            <div class="p-4 rounded-xl bg-[var(--background)] border border-[var(--border)] max-h-[540px] overflow-y-auto custom-scroll">
              ${renderSimpleMarkdown(cleanMarkdownForView(item.jd_markdown, "jd"))}
            </div>
          </div>
        `;
      } else if (currentDetailSubTab === "cv") {
        if (!item.dashboard_cv_pdf_file) {
          subContentHtml = `
            <div class="p-5 rounded-xl bg-[var(--background)] border border-[var(--border)] space-y-2">
              <div class="text-sm font-bold text-amber-500">No Tailored CV Created (${escapeHtml(item.recommendation)} — Fit Score ${item.overall_fit_score}/100)</div>
              <p class="text-xs text-[var(--muted-foreground)] leading-relaxed">
                Per Gate 5 &amp; Gate 6 rules, tailored CVs were generated only for the 7 roles recommended for application (<strong>Apply</strong>). This role was dispositioned as <strong>${escapeHtml(item.recommendation)}</strong> due to domain/technical requirements not evidenced in <code>canonical_master_profile.md</code>:
              </p>
              <ul class="list-disc pl-5 text-xs space-y-1 mt-2">
                ${(fit.red_flags_and_gaps || []).map(g => `<li>${escapeHtml(g)}</li>`).join("")}
              </ul>
            </div>
          `;
        } else {
          let cvInner = "";
          if (currentCvSubMode === "formatted") {
            cvInner = `
              <div class="p-4 rounded-xl bg-[var(--background)] border border-[var(--border)] max-h-[520px] overflow-y-auto custom-scroll">
                ${renderSimpleMarkdown(item.cv_markdown)}
              </div>
            `;
          } else if (currentCvSubMode === "changelog") {
            cvInner = `
              <div class="p-4 rounded-xl bg-[var(--background)] border border-[var(--border)] max-h-[520px] overflow-y-auto custom-scroll">
                ${renderSimpleMarkdown(item.cv_changelog_markdown)}
              </div>
            `;
          } else if (currentCvSubMode === "pdf") {
            cvInner = `
              <div class="rounded-xl overflow-hidden border border-[var(--border)] bg-[var(--background)]">
                <iframe src="../tailored_cvs/${escapeHtml(item.dashboard_cv_pdf_file)}" class="w-full h-[520px]" title="Tailored PDF CV"></iframe>
              </div>
            `;
          }

          subContentHtml = `
            <div class="space-y-3">
              <div class="flex flex-wrap items-center justify-between gap-2 p-3 rounded-lg bg-[var(--background)] border border-[var(--border)] text-xs">
                <div class="space-y-1">
                  <div>
                    <span class="font-semibold text-emerald-500">Tailored PDF CV:</span>
                    <code class="ml-1 select-all">/Users/mineshwadhwa/Documents/Sherpa/tailored_cvs/${escapeHtml(item.dashboard_cv_pdf_file)}</code>
                  </div>
                  ${item.dashboard_cv_md_file ? `
                    <div>
                      <span class="font-semibold text-[var(--muted-foreground)]">Markdown CV:</span>
                      <code class="ml-1 select-all">/Users/mineshwadhwa/Documents/Sherpa/tailored_cvs/md/${escapeHtml(item.dashboard_cv_md_file)}</code>
                    </div>
                  ` : ""}
                </div>
                <div class="flex flex-wrap items-center gap-1.5">
                  <button onclick="setCvSubMode('formatted')" class="px-2.5 py-1 rounded font-medium ${currentCvSubMode === 'formatted' ? 'bg-[var(--primary)] text-[var(--primary-foreground)]' : 'bg-[var(--card)] border border-[var(--border)]'}">CV Text</button>
                  <button onclick="setCvSubMode('changelog')" class="px-2.5 py-1 rounded font-medium ${currentCvSubMode === 'changelog' ? 'bg-[var(--primary)] text-[var(--primary-foreground)]' : 'bg-[var(--card)] border border-[var(--border)]'}">Changelog</button>
                  <button onclick="setCvSubMode('pdf')" class="px-2.5 py-1 rounded font-medium ${currentCvSubMode === 'pdf' ? 'bg-[var(--primary)] text-[var(--primary-foreground)]' : 'bg-[var(--card)] border border-[var(--border)]'}">PDF Preview</button>
                  <a href="../tailored_cvs/${escapeHtml(item.dashboard_cv_pdf_file)}" target="_blank" class="px-2.5 py-1 rounded bg-emerald-500/15 text-emerald-500 border border-emerald-500/30 font-semibold">Open PDF ↗</a>
                  ${item.dashboard_cv_md_file ? `<a href="../tailored_cvs/md/${escapeHtml(item.dashboard_cv_md_file)}" target="_blank" class="px-2.5 py-1 rounded bg-[var(--card)] border border-[var(--border)] hover:text-[var(--foreground)] font-medium">Open MD ↗</a>` : ""}
                </div>
              </div>
              ${cvInner}
            </div>
          `;
        }
      } else if (currentDetailSubTab === "fit") {
        const dims = fit.dimension_scores || {};
        const dimRows = Object.entries(dims).map(([k, v]) => {
          const label = k.replace(/_/g, " ").replace(/\b\w/g, c => c.toUpperCase());
          return `
            <div class="p-3 rounded-lg bg-[var(--background)] border border-[var(--border)] space-y-1">
              <div class="flex items-center justify-between text-xs">
                <span class="font-semibold">${escapeHtml(label)} <span class="text-[var(--muted-foreground)] font-normal">(Weight ${Math.round((v.weight || 0)*100)}%)</span></span>
                <span class="font-bold">${v.score} / 100 <span class="text-[var(--muted-foreground)] font-normal">(${v.weighted_score} pts)</span></span>
              </div>
              <div class="w-full h-1.5 rounded-full bg-[var(--card)] overflow-hidden">
                <div class="bg-emerald-500 h-full" style="width: ${v.score}%"></div>
              </div>
              <p class="text-xs text-[var(--muted-foreground)] leading-relaxed">${escapeHtml(v.rationale)}</p>
            </div>
          `;
        }).join("");

        subContentHtml = `
          <div class="space-y-4 max-h-[540px] overflow-y-auto custom-scroll pr-1">
            ${fit.positioning_angle ? `
              <div class="p-3.5 rounded-xl bg-emerald-500/10 border border-emerald-500/30 text-xs space-y-1">
                <div class="font-bold text-emerald-500">Recommended Positioning Angle</div>
                <p class="leading-relaxed">${escapeHtml(fit.positioning_angle)}</p>
              </div>
            ` : ""}

            <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
              <div class="p-3.5 rounded-xl bg-[var(--background)] border border-[var(--border)] text-xs space-y-1.5">
                <div class="font-bold text-emerald-500">Key Strengths (Direct Evidence)</div>
                <ul class="list-disc pl-4 space-y-1 text-[var(--muted-foreground)]">
                  ${(fit.key_strengths || []).map(s => `<li>${escapeHtml(s)}</li>`).join("")}
                </ul>
              </div>
              <div class="p-3.5 rounded-xl bg-[var(--background)] border border-[var(--border)] text-xs space-y-1.5">
                <div class="font-bold text-amber-500">Adjacent Bridges &amp; Gaps</div>
                <ul class="list-disc pl-4 space-y-1 text-[var(--muted-foreground)]">
                  ${(fit.red_flags_and_gaps || []).map(g => `<li>${escapeHtml(g)}</li>`).join("")}
                </ul>
              </div>
            </div>

            <div class="space-y-2">
              <div class="text-xs font-bold uppercase tracking-wider text-[var(--muted-foreground)]">7-Dimension Weighted Fit Breakdown</div>
              ${dimRows}
            </div>
          </div>
        `;
      } else if (currentDetailSubTab === "matrix") {
        const allReqs = [
          ...(reqMatrix.must_have || []),
          ...(reqMatrix.preferred || []),
          ...(reqMatrix.implicit || []),
          ...(reqMatrix.domain || [])
        ];
        subContentHtml = `
          <div class="space-y-2.5 max-h-[540px] overflow-y-auto custom-scroll pr-1">
            ${allReqs.map(r => {
              const clsColor = r.classification === "Direct"
                ? "bg-emerald-500/15 text-emerald-500 border-emerald-500/30"
                : (r.classification.includes("Adjacent") ? "bg-amber-500/15 text-amber-500 border-amber-500/30" : "bg-rose-500/15 text-rose-500 border-rose-500/30");
              return `
                <div class="p-3 rounded-xl bg-[var(--background)] border border-[var(--border)] text-xs space-y-1.5">
                  <div class="flex items-center justify-between gap-2 flex-wrap">
                    <div class="flex items-center gap-2">
                      <span class="font-mono font-bold px-1.5 py-0.5 rounded bg-[var(--card)] border border-[var(--border)]">${escapeHtml(r.id)}</span>
                      <span class="uppercase text-[var(--muted-foreground)] font-semibold">${escapeHtml(r.category)}</span>
                    </div>
                    <div class="flex items-center gap-2">
                      <code class="text-[var(--muted-foreground)]">${escapeHtml(r.canonical_line_refs)}</code>
                      <span class="px-2 py-0.5 rounded-full border font-semibold ${clsColor}">${escapeHtml(r.classification)}</span>
                    </div>
                  </div>
                  <div class="font-semibold text-[var(--foreground)]">${escapeHtml(r.requirement)}</div>
                  <div class="text-[var(--muted-foreground)]"><strong class="text-[var(--foreground)]">Canonical Evidence:</strong> ${escapeHtml(r.evidence_summary)}</div>
                  <div class="text-[var(--muted-foreground)]"><strong class="text-[var(--foreground)]">Positioning Bridge:</strong> ${escapeHtml(r.positioning_bridge)}</div>
                </div>
              `;
            }).join("")}
          </div>
        `;
      } else if (currentDetailSubTab === "audits") {
        subContentHtml = `
          <div class="space-y-4 max-h-[540px] overflow-y-auto custom-scroll pr-1">
            ${item.fact_check_markdown ? `
              <div class="p-4 rounded-xl bg-[var(--background)] border border-[var(--border)]">
                <div class="text-xs font-bold text-emerald-500 uppercase mb-2">Independent Fact-Check &amp; Confidentiality Audit (Gates 6 &amp; 7)</div>
                ${renderSimpleMarkdown(cleanMarkdownForView(item.fact_check_markdown, "audit"))}
              </div>
            ` : ""}
            ${item.ats_report_markdown ? `
              <div class="p-4 rounded-xl bg-[var(--background)] border border-[var(--border)]">
                <div class="text-xs font-bold text-sky-500 uppercase mb-2">ATS &amp; Editorial Audit Report (Gate 8)</div>
                ${renderSimpleMarkdown(cleanMarkdownForView(item.ats_report_markdown, "audit"))}
              </div>
            ` : ""}
            <div class="p-4 rounded-xl bg-[var(--background)] border border-[var(--border)]">
              <div class="text-xs font-bold text-[var(--muted-foreground)] uppercase mb-2">Consolidated Opportunity Dossier</div>
              ${renderSimpleMarkdown(cleanMarkdownForView(item.dossier_markdown, "dossier"))}
            </div>
          </div>
        `;
      }

      container.innerHTML = `
        <div class="space-y-4">
          <!-- Selected Job Header -->
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-3 border-b border-[var(--border)]">
            <div class="min-w-0">
              <h2 class="text-base md:text-lg font-bold text-[var(--foreground)] truncate">${escapeHtml(item.company)} — ${escapeHtml(item.role_title)}</h2>
              <p class="text-xs text-[var(--muted-foreground)] mt-0.5">
                Job ID: <code>${escapeHtml(item.job_id)}</code>
              </p>
            </div>
            ${item.linkedin_url ? `<a href="${escapeHtml(item.linkedin_url)}" target="_blank" rel="noopener noreferrer" class="shrink-0 px-3 py-1 rounded-lg border border-[var(--border)] text-xs font-medium hover:text-[var(--foreground)]">LinkedIn ↗</a>` : ""}
          </div>

          <!-- Inspector Sub-Tabs -->
          <div class="flex flex-wrap gap-1.5">
            <button onclick="setDetailSubTab('jd')" class="px-3 py-1.5 text-xs font-semibold rounded-lg transition ${currentDetailSubTab === 'jd' ? 'bg-[var(--primary)] text-[var(--primary-foreground)]' : 'bg-[var(--background)] border border-[var(--border)] text-[var(--muted-foreground)] hover:text-[var(--foreground)]'}">
              Full JD
            </button>
            <button onclick="setDetailSubTab('cv')" class="px-3 py-1.5 text-xs font-semibold rounded-lg transition ${currentDetailSubTab === 'cv' ? 'bg-[var(--primary)] text-[var(--primary-foreground)]' : 'bg-[var(--background)] border border-[var(--border)] text-[var(--muted-foreground)] hover:text-[var(--foreground)]'}">
              ${item.dashboard_cv_pdf_file ? 'Tailored CV' : 'Tailored CV (None)'}
            </button>
            <button onclick="setDetailSubTab('fit')" class="px-3 py-1.5 text-xs font-semibold rounded-lg transition ${currentDetailSubTab === 'fit' ? 'bg-[var(--primary)] text-[var(--primary-foreground)]' : 'bg-[var(--background)] border border-[var(--border)] text-[var(--muted-foreground)] hover:text-[var(--foreground)]'}">
              Role Fit
            </button>
            <button onclick="setDetailSubTab('matrix')" class="px-3 py-1.5 text-xs font-semibold rounded-lg transition ${currentDetailSubTab === 'matrix' ? 'bg-[var(--primary)] text-[var(--primary-foreground)]' : 'bg-[var(--background)] border border-[var(--border)] text-[var(--muted-foreground)] hover:text-[var(--foreground)]'}">
              Evidence Matrix
            </button>
            <button onclick="setDetailSubTab('audits')" class="px-3 py-1.5 text-xs font-semibold rounded-lg transition ${currentDetailSubTab === 'audits' ? 'bg-[var(--primary)] text-[var(--primary-foreground)]' : 'bg-[var(--background)] border border-[var(--border)] text-[var(--muted-foreground)] hover:text-[var(--foreground)]'}">
              Audits &amp; Dossier
            </button>
          </div>

          <!-- Inspector Body -->
          <div>${subContentHtml}</div>
        </div>
      `;
    }

    // Initialize UI
    updateTopKpis();
    renderUnifiedFilterPills();
    renderUnifiedList();
    renderUnifiedDetail();
  </script>
</body>
</html>
"""


def main():
    DASHBOARD_DIR.mkdir(parents=True, exist_ok=True)
    TAILORED_CVS_DIR.mkdir(parents=True, exist_ok=True)
    TAILORED_CVS_MD_DIR.mkdir(parents=True, exist_ok=True)
    JDS_DIR.mkdir(parents=True, exist_ok=True)

    # Keep dashboard/ clean: remove any stale JD/CV files from earlier flat layout
    for pattern in ("*_JD.md", "*_CV.pdf", "*_CV.md"):
        for stale in DASHBOARD_DIR.glob(pattern):
            stale.unlink()

    tracker = json.loads(TRACKER_JSON.read_text(encoding="utf-8"))

    enriched_batch_1 = []
    folder_files_manifest = []

    for idx, item in enumerate(tracker.get("evaluated_batch_1", []), start=1):
        opp_id = item["opportunity_id"]
        rank_prefix, short_name = SLUG_MAP.get(opp_id, (f"{idx:02d}", opp_id))
        app_dir = BASE_DIR / "applications" / opp_id
        artifacts = item.get("artifacts", {})

        # Copy JD to jds/
        jd_src = Path(artifacts.get("jd_full", app_dir / "jd_full.md"))
        jd_dest_name = f"{rank_prefix}_{short_name}_JD.md"
        jd_dest = JDS_DIR / jd_dest_name
        if jd_src.exists():
            shutil.copy2(jd_src, jd_dest)

        # Copy CV PDF to tailored_cvs/ and CV Markdown to tailored_cvs/md/ if present
        cv_pdf_dest_name = None
        cv_md_dest_name = None
        cv_pdf_src_str = artifacts.get("tailored_cv_pdf")
        if cv_pdf_src_str and Path(cv_pdf_src_str).exists():
            cv_pdf_dest_name = f"{rank_prefix}_{short_name}_CV.pdf"
            shutil.copy2(cv_pdf_src_str, TAILORED_CVS_DIR / cv_pdf_dest_name)

        cv_md_src = app_dir / "cv_tailored.md"
        if cv_md_src.exists():
            cv_md_dest_name = f"{rank_prefix}_{short_name}_CV.md"
            shutil.copy2(cv_md_src, TAILORED_CVS_MD_DIR / cv_md_dest_name)

        jd_text = read_text_safe(str(jd_src))
        cv_md_text = read_text_safe(str(cv_md_src))
        cv_changelog_text = read_text_safe(artifacts.get("cv_changelog", ""))
        dossier_text = read_text_safe(artifacts.get("dossier", ""))
        fact_check_text = read_text_safe(artifacts.get("fact_check_report", ""))
        ats_report_text = read_text_safe(artifacts.get("ats_editorial_report", ""))
        fit_data = read_json_safe(artifacts.get("fit_assessment", ""))
        req_matrix = read_json_safe(artifacts.get("requirement_matrix", ""))

        enriched_item = {
            **item,
            "rank": idx,
            "rank_prefix": rank_prefix,
            "short_name": short_name,
            "dashboard_jd_file": jd_dest_name,
            "dashboard_jd_path": str(jd_dest),
            "dashboard_cv_pdf_file": cv_pdf_dest_name,
            "dashboard_cv_pdf_path": str(TAILORED_CVS_DIR / cv_pdf_dest_name) if cv_pdf_dest_name else None,
            "dashboard_cv_md_file": cv_md_dest_name,
            "dashboard_cv_md_path": str(TAILORED_CVS_MD_DIR / cv_md_dest_name) if cv_md_dest_name else None,
            "jd_markdown": jd_text,
            "cv_markdown": cv_md_text,
            "cv_changelog_markdown": cv_changelog_text,
            "dossier_markdown": dossier_text,
            "fact_check_markdown": fact_check_text,
            "ats_report_markdown": ats_report_text,
            "fit_assessment_detail": fit_data,
            "requirement_matrix_detail": req_matrix,
        }
        enriched_batch_1.append(enriched_item)

        folder_files_manifest.append({
            "rank": idx,
            "company": item["company"],
            "role_title": item["role_title"],
            "fit_score": item["overall_fit_score"],
            "priority_band": item["priority_band"],
            "recommendation": item["recommendation"],
            "status": item["application_status"],
            "jd_file": jd_dest_name,
            "cv_pdf_file": cv_pdf_dest_name or "— (Not tailored: " + item["recommendation"] + ")",
            "cv_md_file": cv_md_dest_name or "—",
        })

    # Write 00_Jobs_Listed_and_Application_Status.md in dashboard/
    status_md_lines = [
        "# Sherpa — Job Application Status, JDs & CVs",
        "",
        f"- **Dashboard Folder:** `/Users/mineshwadhwa/Documents/Sherpa/dashboard/`",
        f"- **Tailored PDF CVs:** `/Users/mineshwadhwa/Documents/Sherpa/tailored_cvs/` (Markdown copies in `tailored_cvs/md/`)",
        f"- **Full Job Descriptions:** `/Users/mineshwadhwa/Documents/Sherpa/jds/`",
        f"- **Interactive UI:** [index.html](file:///Users/mineshwadhwa/Documents/Sherpa/dashboard/index.html)",
        f"- **Canonical Master Profile Version:** `{tracker.get('canonical_profile_version', '1.1.0')}`",
        f"- **Last Updated:** `{tracker.get('last_updated', '')}`",
        f"- **Discovery Scan Window:** `{tracker.get('scan_window', '')}`",
        "",
        "## Progress Summary",
        f"- **Emails Scanned:** `{tracker['summary']['total_emails_scanned']}`",
        f"- **Unique LinkedIn Jobs Listed:** `{tracker['summary']['unique_linkedin_jobs_discovered']}`",
        f"- **Gate 1 Pass (Bengaluru / India Remote PM Roles):** `{tracker['summary']['gate_1_pass_count']}`",
        f"- **Batch 1 Full JDs Evaluated (Gates 1–8 PASS):** `{tracker['summary']['batch_1_evaluated_count']}`",
        f"- **Tailored 2-Page PDF CVs Created:** `{tracker['summary']['tailored_pdf_cvs_generated']}` (`4 High Priority` + `3 Consider`)",
        f"- **Secondary Queue (Batch 2):** `{len(tracker.get('secondary_queue_batch_2', []))}`",
        "",
        "---",
        "",
        "## 1. Evaluated Jobs (Batch 1) — JDs, Tailored CVs & Application Status",
        "",
        "| Rank | Company | Role Title | Fit Score | Priority | Recommendation | JD (`jds/`) | Tailored CV PDF (`tailored_cvs/`) | Tailored CV MD (`tailored_cvs/md/`) | Application Status |",
        "| :---: | :--- | :--- | :---: | :--- | :---: | :--- | :--- | :--- | :--- |",
    ]

    for row in enriched_batch_1:
        jd_link = f"[{row['dashboard_jd_file']}](file:///Users/mineshwadhwa/Documents/Sherpa/jds/{row['dashboard_jd_file']})"
        if row["dashboard_cv_pdf_file"]:
            cv_pdf_link = f"[{row['dashboard_cv_pdf_file']}](file:///Users/mineshwadhwa/Documents/Sherpa/tailored_cvs/{row['dashboard_cv_pdf_file']})"
            cv_md_link = f"[{row['dashboard_cv_md_file']}](file:///Users/mineshwadhwa/Documents/Sherpa/tailored_cvs/md/{row['dashboard_cv_md_file']})"
        else:
            cv_pdf_link = f"— (`{row['recommendation']}`)"
            cv_md_link = "—"
        status_md_lines.append(
            f"| {row['rank']} | **{row['company']}** | {row['role_title']} | **{row['overall_fit_score']}/100** | {row['priority_band']} | `{row['recommendation']}` | {jd_link} | {cv_pdf_link} | {cv_md_link} | `{row['application_status']}` |"
        )

    status_md_lines.extend([
        "",
        "---",
        "",
        "## 2. Secondary Queue (Batch 2 — 35 Listed Bengaluru / India PM Jobs)",
        "",
        "| # | Job ID | Company | Role Title | Location | LinkedIn URL | Application Status |",
        "| :---: | :--- | :--- | :--- | :--- | :--- | :--- |",
    ])

    for i, sq in enumerate(tracker.get("secondary_queue_batch_2", []), start=1):
        status_md_lines.append(
            f"| {i} | `{sq['job_id']}` | **{sq['company']}** | {sq['role_title']} | {sq['location']} | [LinkedIn]({sq['linkedin_url']}) | `{sq['queue_status']}` |"
        )

    status_md_lines.extend([
        "",
        "---",
        "",
        "## 3. Gate 1 Exclusions & Already Applied Roles",
        "",
        "| Job ID | Company | Role Title | Location | Gate 1 Status | Disposition |",
        "| :--- | :--- | :--- | :--- | :--- | :--- |",
    ])

    for app in tracker.get("already_applied", []):
        status_md_lines.append(
            f"| `{app['job_id']}` | **{app['company']}** | {app['role_title']} | {app['location']} | `ALREADY_APPLIED` | {app['notes']} ({app['applied_date']}) |"
        )

    for exc in tracker.get("gate_1_exclusions", []):
        company = str(exc.get("company", "")).replace("|", "/")[:40]
        title = str(exc.get("role_title", "")).replace("|", "/")[:60]
        loc = str(exc.get("location", "")).replace("|", "/")[:40]
        reason = str(exc.get("reason", "")).replace("|", "/")[:80]
        status_md_lines.append(
            f"| `{exc['job_id']}` | {company} | {title} | {loc} | `{exc['gate_1_status']}` | {reason} |"
        )

    status_md_path = DASHBOARD_DIR / "00_Jobs_Listed_and_Application_Status.md"
    status_md_path.write_text("\n".join(status_md_lines) + "\n", encoding="utf-8")

    # Assemble payload for the interactive UI
    ui_payload = {
        "schema_version": tracker.get("schema_version"),
        "canonical_profile_version": tracker.get("canonical_profile_version"),
        "last_updated": tracker.get("last_updated"),
        "scan_window": tracker.get("scan_window"),
        "dashboard_folder": str(DASHBOARD_DIR),
        "summary": tracker.get("summary", {}),
        "evaluated_batch_1": enriched_batch_1,
        "secondary_queue_batch_2": tracker.get("secondary_queue_batch_2", []),
        "already_applied": tracker.get("already_applied", []),
        "gate_1_exclusions": tracker.get("gate_1_exclusions", []),
        "folder_files_manifest": folder_files_manifest,
    }

    payload_json_str = json.dumps(ui_payload)

    # Write standalone browser index.html into /Users/mineshwadhwa/Documents/Sherpa/dashboard/index.html
    browser_fallback_css = """
    html:not(.light):not(.dark) {
      --background: #0b0f19;
      --card: #111827;
      --foreground: #f8fafc;
      --muted-foreground: #94a3b8;
      --border: #1e293b;
      --primary: #3b82f6;
      --primary-foreground: #ffffff;
    }
    """
    browser_html = (
        HTML_TEMPLATE
        .replace("__FALLBACK_VARS__", browser_fallback_css)
        .replace("__DASHBOARD_JSON_PAYLOAD__", payload_json_str)
    )
    (DASHBOARD_DIR / "index.html").write_text(browser_html, encoding="utf-8")

    # Also write a clean Generative UI version (without local root fallbacks) to /tmp/agy_dashboard_artifact.html for copying to artifact dir
    agy_html = (
        HTML_TEMPLATE
        .replace("__FALLBACK_VARS__", "")
        .replace("__DASHBOARD_JSON_PAYLOAD__", payload_json_str)
    )
    Path("/tmp/agy_dashboard_artifact.html").write_text(agy_html, encoding="utf-8")

    print(
        f"Successfully built dashboard ({DASHBOARD_DIR / 'index.html'}), "
        f"tailored CVs ({TAILORED_CVS_DIR}), and JDs ({JDS_DIR})."
    )


if __name__ == "__main__":
    main()
