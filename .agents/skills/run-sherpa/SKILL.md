---
name: run-sherpa
description: >-
  Run the full Sherpa LinkedIn Job Application Support workflow on demand (Gmail
  discovery, full LinkedIn JD retrieval, Canonical Master Profile v1.1.0 mapping &
  role fit assessment, tailored PDF CV generation, independent Fact-Check & ATS
  reviews, tracker update, and dashboard rebuild) and automatically move the
  scheduled cron job 3 days ahead from today. Use when the user asks to run
  Sherpa now, run the job application workflow on demand, or triggers /run-sherpa.
---

# Run Sherpa On-Demand (`/run-sherpa`)

Executes the entire Sherpa Job Application Support System on demand and shifts the recurring `linkedin-job-application-workflow` cron schedule to **3 days ahead from today** (`Asia/Kolkata`).

## Execution Steps

1. **Shift the Cron Schedule (+3 Days from Today)**
   Run immediately at the start of an on-demand execution:
   ```bash
   python3 /Users/mineshwadhwa/Documents/Sherpa/scripts/schedule_manager.py advance --mode on_demand
   ```
   This records the run in `tracker/schedule_state.json` and updates `/Users/mineshwadhwa/.gemini/config/sidecars/linkedin-job-application-workflow/sidecar.json` so the next scheduled cron run moves to `today + 3 days` at `12:00 PM Asia/Kolkata` (and repeats every 3 days thereafter).

2. **Execute the Full Sherpa Pipeline**
   Follow [job-application-workflow](../job-application-workflow/SKILL.md), [subagent_prompts.md](../job-application-workflow/references/subagent_prompts.md), and [AGENTS.md](../../../AGENTS.md):
   - **Gate 1 (Email Discovery & Deduplication)**: Initialize Gmail CLI (`/Users/mineshwadhwa/.gemini/config/plugins/gmail/skills/gmail/scripts/gmail --version`), run `gmail readonly search "from:jobs-noreply@linkedin.com newer_than:14d" --max 20` to detect newly submitted applications, and `gmail readonly search "from:jobalerts-noreply@linkedin.com newer_than:7d" --max 20` to discover new LinkedIn PM job alerts. Deduplicate against `tracker/application_tracker.json`.
   - **Gate 2 (Full JD Retrieval)**: Use the `browser` subagent (`Model: "flash"`) to open each new Bengaluru or India Remote PM job URL and save the complete verbatim JD into `applications/<opportunity-id>/jd_full.md`.
   - **Gates 3, 4 & 5 (Profile Mapping & Fit Assessment)**: Run `requirement_mapping_agent` against `canonical_master_profile.md` (`v1.1.0`) and `role_fit_agent` to produce `requirement_matrix.json` and `fit_assessment.json`.
   - **Gates 6, 7 & 8 (CV Tailoring, PDF Rendering & Independent Reviews)**: For roles recommended as `Apply` (`High Priority` or `Consider`), run `cv_tailoring_agent` (`cv_tailored.json`, `cv_changelog.md`), render the 2-page PDF via `scripts/render_cv_pdf.py`, run independent `fact_check_reviewer` (`fact_check_report.md`) and `ats_editorial_reviewer` (`ats_editorial_report.md`), write `dossier.md`, and validate each record via `scripts/validate_opportunity_record.py`.
   - **Gate 10 (Tracker & Dashboard Rebuild)**: Update `tracker/application_tracker.json` and `tracker/application_tracker.md`, then rebuild the consolidated dashboard:
     ```bash
     python3 /Users/mineshwadhwa/Documents/Sherpa/scripts/build_dashboard.py
     ```

3. **Present for User Approval (Gate 9)**
   - Summarize all newly discovered, skipped/applied, and evaluated roles, validation status, and links to tailored PDFs and [index.html](file:///Users/mineshwadhwa/Documents/Sherpa/dashboard/index.html).
   - Never submit applications or send external messages automatically.
   - Include the updated `next_scheduled_date` from `tracker/schedule_state.json`.
