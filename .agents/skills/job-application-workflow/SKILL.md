---
name: job-application-workflow
description: >-
  Orchestrates the end-to-end evidence-led Job Application Support System for LinkedIn
  Product Manager opportunities. Use this skill whenever discovering LinkedIn PM job alerts
  from Gmail, retrieving full LinkedIn job descriptions, mapping requirements to the Canonical
  Master Profile, evaluating role fit, tailoring CVs into formatted PDFs, running independent
  fact-check and ATS reviews, or updating the application tracker.
---

# Job Application Support Workflow (`job-application-workflow`)

This skill implements the 9-step workflow, 11 specialized agent roles, and 10 mandatory review gates defined in [job_application_support_model.md](file:///Users/mineshwadhwa/Documents/Sherpa/job_application_support_model.md).

## 1. Directory & Artifact Structure

Every discovered opportunity is assigned a slug `<opportunity-id>` (format: `YYYY-MM-DD-<company-slug>-<role-slug>`) and stored in its own folder under `applications/<opportunity-id>/`:

```text
/Users/mineshwadhwa/Documents/Sherpa/
├── canonical_master_profile.md                  # Single Source of Truth (v1.1.0)
├── job_application_support_model.md             # Operating Model Specification
├── AGENTS.md                                    # Always-on Workspace Guardrails
├── templates/
│   ├── cv_base_schema.json                      # Baseline CV structure matching PDF
│   └── opportunity_dossier_template.md          # Standard 8-section Dossier template
├── scripts/
│   ├── build_dashboard.py                       # Generates dashboard/, tailored_cvs/, and jds/
│   ├── render_cv_pdf.py                         # Deterministic PDF CV renderer (Chrome headless)
│   └── validate_opportunity_record.py           # Gate 1–8 & 10 automated validator
├── dashboard/
│   ├── index.html                               # Interactive UI Dashboard
│   └── 00_Jobs_Listed_and_Application_Status.md # Status overview linking to tailored_cvs/ & jds/
├── tailored_cvs/
│   ├── <rank>_<Company>_<Role>_CV.pdf           # Finished submission-ready PDF CVs
│   └── md/                                      # Markdown CV copies
├── jds/
│   └── <rank>_<Company>_<Role>_JD.md            # Full Job Descriptions
├── tracker/
│   ├── application_tracker.md                   # Master Markdown dashboard
│   └── application_tracker.json                 # Structured JSON audit log
└── applications/
    └── <opportunity-id>/
        ├── jd_full.md                           # Full retrieved JD + metadata (Gate 1 & 2)
        ├── requirement_matrix.json              # Requirement-to-Evidence mapping (Gate 3 & 4)
        ├── fit_assessment.json                  # Role fit score & disposition (Gate 5)
        ├── cv_tailored.json                     # Tailored CV structured source
        ├── cv_tailored.md                       # Readable Markdown CV
        ├── cv_changelog.md                      # Bullet-by-bullet diff & evidence links
        ├── fact_check_report.md                 # Independent Gate 6 & 7 audit report
        ├── ats_editorial_report.md              # Gate 8 ATS & editorial review report
        ├── dossier.md                           # Consolidated 8-section user dossier
        └── Minesh_Wadhwa_CV_<Company>_<Role>.pdf # Final tailored PDF CV
```

## 2. Sub-Agent Orchestration Protocol

Read [references/subagent_prompts.md](./references/subagent_prompts.md) for the exact system prompts and required output schemas for each sub-agent role:

1. **Agent 1 — Orchestrator / Application Manager** (Main Agent): Owns state, invokes subagents, runs validation scripts, and enforces Gates 1–10.
2. **Agent 2 — Email & Opportunity Discovery Agent**: Uses the `gmail` CLI to search LinkedIn PM job-alert emails (`newer_than:7d`), extracts role metadata and LinkedIn job URLs, and deduplicates against `tracker/application_tracker.json` (**Gate 1**).
3. **Agent 3 — LinkedIn JD Research Agent**: Uses the `browser` subagent (`Model: "flash"`) to open each LinkedIn job URL, expand "See more" / full description sections, and capture the complete JD text, requirements, and application mode into `jd_full.md` (**Gate 2**).
4. **Agent 4 — Canonical Profile Retrieval Agent**: Validates `canonical_master_profile.md` is at the latest approved version (`v1.1.0`) and packages relevant sections (**Gate 3**).
5. **Agent 5 — Requirement Mapping Agent** (`requirement_mapping_agent`): Maps every JD requirement to `Direct`, `Adjacent / Transferable`, or `Gap / Not Evidenced` with exact line numbers from `canonical_master_profile.md` (**Gate 4**).
6. **Agent 6 — Role Fit & Prioritisation Agent** (`role_fit_agent`): Evaluates substance, seniority, scope, domain, and evidence strength to classify the role as **High Priority**, **Consider**, or **Not Suitable** (**Gate 5**).
7. **Agent 7 — CV Tailoring Agent** (`cv_tailoring_agent`): For recommended roles, modifies `templates/cv_base_schema.json` into `cv_tailored.json` using **what was done → how it was done → measurable result**, incorporating `"agents"` where genuinely supported, and writes `cv_changelog.md`.
8. **Agent 8 — Application Content Agent** (`application_content_agent`): Drafts cover letters or screening responses when required or useful.
9. **Agent 9 — Independent Fact-Check & Integrity Reviewer** (`fact_check_reviewer`): **Must be a separate subagent invocation from Agent 7.** Audits every claim, metric, date, title, and confidentiality boundary against `canonical_master_profile.md` (`v1.1.0`) and writes `fact_check_report.md` (**Gate 6 & Gate 7**).
10. **Agent 10 — ATS & Editorial Reviewer** (`ats_editorial_reviewer`): Checks readability, keyword naturalness, repetition, and consistency across CV, dossier, and fit assessment, writing `ats_editorial_report.md` (**Gate 8**).
11. **Agent 11 — Application Tracker Agent**: Updates `tracker/application_tracker.json` and `tracker/application_tracker.md` (**Gate 10**).

## 3. Execution Commands

### Render Tailored CV to PDF
```bash
python3 /Users/mineshwadhwa/Documents/Sherpa/scripts/render_cv_pdf.py \
  --input /Users/mineshwadhwa/Documents/Sherpa/applications/<opportunity-id>/cv_tailored.json \
  --output /Users/mineshwadhwa/Documents/Sherpa/applications/<opportunity-id>/Minesh_Wadhwa_CV_<Company>_<Role>.pdf \
  --markdown /Users/mineshwadhwa/Documents/Sherpa/applications/<opportunity-id>/cv_tailored.md
```

### Validate Opportunity Record (Gates 1–8 & 10)
```bash
python3 /Users/mineshwadhwa/Documents/Sherpa/scripts/validate_opportunity_record.py \
  /Users/mineshwadhwa/Documents/Sherpa/applications/<opportunity-id>
```

### Rebuild Consolidated Dashboard
```bash
python3 /Users/mineshwadhwa/Documents/Sherpa/scripts/build_dashboard.py
```

### Shift Cron Schedule (+3 Days from Today)
```bash
python3 /Users/mineshwadhwa/Documents/Sherpa/scripts/schedule_manager.py advance --mode on_demand
```
