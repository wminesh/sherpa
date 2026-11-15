# Independent Fact-Check & Confidentiality Audit Report (Gates 6 & 7)

- **Opportunity ID**: `4455913458-amazon-spm-now-selection`
- **Target Role**: Amazon — Senior Product Manager, Amazon Now (Selection Quality, Health & Seller Tools) (`A10499561`)
- **Audit Date**: `2026-11-15`
- **Authoritative Sources Checked**:
  - `canonical_master_profile.md` (`v1.1.0`)
  - `AGENTS.md`
  - `templates/cv_base_schema.json` (`baseline-1.0`)
- **Audited Artifacts**:
  - `cv_tailored.json` (`tailored-4455913458-1.0`)
  - `cv_tailored.md`
  - `cv_changelog.md`
  - `requirement_matrix.json`
  - `dossier.md`

---

## Overall Audit Verdicts

- **Gate 6 (CV Claim & Profile Integrity Audit)**: **`FAIL`** (1 blocking ownership-overstatement defect found; 1 minor phrasing advisory)
- **Gate 7 (Confidentiality & Disclosure Review)**: **`PASS`**

> **Summary**: All locked identity facts, employers, titles, dates, locations, education items, certifications, social entrepreneurship entries, metrics, delivered-vs-roadmap-target distinctions, internal enterprise analytics tool attribution, and "agentic workflows" framing are compliant. However, **Gate 6 fails** because `cv_tailored.json` (line 42) and `cv_tailored.md` (line 16) upgrade `"Supported C-suite decision-making"` (`canonical_master_profile.md:L484`) to `"Drove C-suite decision-making"`, violating `AGENTS.md` Section 1 (*"Never upgrade participation into ownership, influence into formal authority, or exposure into expertise"*).

---

## Blocking Defects Requiring Fix (Gate 6)

| Defect ID | Artifact & Location | Current Claim | Canonical Source & Rule Violated | Required Fix |
| :--- | :--- | :--- | :--- | :--- |
| **G6-01 (Blocking)** | `cv_tailored.json:L42`, `cv_tailored.md:L16`, `cv_changelog.md:L45` | `"Drove C-suite decision-making and operational planning by preparing board-level narratives and coordinating procurement, asset management, and platform workflows"` | `canonical_master_profile.md:L484` explicitly states **`"Supported C-suite decision-making through KPI-driven reporting and operational insights"`** (`L479`: `"decision-support materials"`, `L487`: `"Drove enterprise alignment without formal authority"`). Upgrading `"Supported"` to `"Drove C-suite decision-making"` violates `AGENTS.md` §1 (*"Never upgrade participation into ownership, influence into formal authority, or exposure into expertise"*). | Replace `"Drove C-suite decision-making and operational planning..."` with **`"Supported C-suite decision-making and operational planning by preparing board-level narratives and coordinating procurement, asset management, and platform workflows"`** (or `"Informed C-suite decision-making and drove operational alignment..."`) across `cv_tailored.json`, `cv_tailored.md`, `cv_changelog.md`, and re-render `Minesh_Wadhwa_CV_Amazon_Now_Selection.pdf`. |

### Minor Advisory (Non-Blocking Recommended Tightening)

| Advisory ID | Artifact & Location | Current Claim | Canonical Source | Recommendation |
| :--- | :--- | :--- | :--- | :--- |
| **G6-ADV-01** | `cv_tailored.json:L109`, `cv_tailored.md:L44`, `cv_changelog.md:L79` | `"Led app redesign and feature tradeoffs for *Tynker* by adding assessments and DIY modules guided by completion signals, increasing course completion by 5%"` | `canonical_master_profile.md:L266-L268`, `L389` document `"Led app redesign initiative"`, `"Added assessments and DIY learning modules"`, and `"product experimentation and experience optimization"`, rather than explicitly stating `"feature tradeoffs"` for Tynker (though ROI-driven prioritization and scope management are documented at `L66`, `L343`, `L462`). | Optionally tighten `"Led app redesign and feature tradeoffs for *Tynker*"` to **`"Led app redesign and feature additions for *Tynker*"`** or **`"Led app redesign and experience optimization for *Tynker*"`** to stay strictly literal to `L266-L268` and `L389`. |

---

## Claim-by-Claim Verification Table

### 1. Locked Identity Facts, Employers, Titles, Dates, Education & Certifications

| Item | Audited Value (`cv_tailored.json` / `cv_tailored.md`) | Canonical Reference (`canonical_master_profile.md` v1.1.0 & `AGENTS.md`) | Status |
| :--- | :--- | :--- | :--- |
| **Name & Contact** | `Minesh Wadhwa`, `Bangalore • w.minesh@gmail.com • +91 9035 199 024` | `L9-L11` (`Bangalore, Karnataka, India`, `w.minesh@gmail.com`, `+91 9035 199 024`) | `PASS` |
| **Lowe’s India** | `Senior Product Manager`, `Bangalore, Karnataka`, `Sep 2024 – Present` | `L48-L50`, `AGENTS.md` §1 | `PASS` |
| **Hype Marketing & Product Services** | `Founder`, `Bangalore, Karnataka`, `Oct 2023 – Nov 2024` | `L119-L121`, `AGENTS.md` §1 | `PASS` |
| **HealthQ Rehab** | `Head of Marketing`, `Bangalore, Karnataka`, `May 2023 – Dec 2023` | `L179-L181`, `AGENTS.md` §1 | `PASS` |
| **Byju’s - Product Development (SPM)** | `Senior Product Manager`, `Bangalore, Karnataka`, `July 2020 – April 2023`; Products: `Byju’s Xcel Masterclasses, Tynker, Whitehat Jr., Aakash-Byjus` | `L212-L225` (`L219` explicitly authorizes `July 2020 – April 2023` canonical CV display period covering PM + SPM) | `PASS` |
| **Byju’s - Product Development (Multiple Roles)** | `Multiple Roles`, `Bangalore, Karnataka`, `Jun 2015 – June 2020`; Products: `Social Studies, Interactive Learning Experiences, Byju's Exam Prep, BTLA Commerce, BTLA Science` | `L286-L294`, `AGENTS.md` §1 (`Jun 2015 – June 2020`) | `PASS` |
| **Certifications** | `University of California, Irvine`, `Oct 2020 – Dec 2020`, 3 course bullets unchanged | `L333-L343`, `templates/cv_base_schema.json:L113-L123` | `PASS` |
| **Social Entrepreneurship** | *The Open Door Foundation* (RTC Girls Home, Bangalore) & *Education for All* (10 million kids by 2025) | `L348-L349` | `PASS` |
| **Education** | `Manipal Institute of Technology` (`B. Tech. in Computer Science Engineering`, `2011 – 2015`); `Indian Institute Of Management - Bangalore` (`Executive General Management Program`, `2025 – 2026 (ongoing)`) | `L321-L327`, `AGENTS.md` §1 | `PASS` |

### 2. Profile Summary, Core Competencies & Experience Claims

| Location | Claim / Metric Audited | Canonical Citation | Outcome Type / Guardrail Check | Status |
| :--- | :--- | :--- | :--- | :--- |
| `cv_tailored.json:L13`, `cv_tailored.md:L5` | `10+ years of experience (~5 years in formal PM/Senior PM roles)` | `L48-L50`, `L217-L220`, `L251-L253`, `L286-L288` (Jun 2015–Nov 2026 = ~11.4 yrs; Jul 2020–Apr 2023 + Sep 2024–Nov 2026 = ~5.1 yrs) | Accurate tenure math | `PASS` |
| `cv_tailored.json:L13`, `cv_tailored.md:L5` | `AI-driven procurement and catalog systems, agentic workflows, automated recovery mechanisms, and KPI dashboards (using internal enterprise analytics tools) to protect ~$10M annually, ensure 99.99% reliability, and cut cycle times by 20%` | `L6`, `L61`, `L67`, `L76`, `L86-L88`, `L97-L98`, `L531`, `L660`, `L663`; `AGENTS.md` §2 | Delivered outcomes accurately stated; internal analytics tools properly specified; `agentic workflows` authorized per `AGENTS.md` §2 | `PASS` |
| `cv_tailored.json:L14-L25` | 10 `core_competencies` (JSON metadata layer) | `L65-L115`, `L232-L247`, `L445-L488`, `L524-L534` | Directly supported; no fabricated tools/skills | `PASS` |
| `cv_tailored.json:L38`, `cv_tailored.md:L12` | `Owned end-to-end technology product delivery across engineering and operations by scaling workflow automation, ensuring 99.99% reliability for key enterprise platforms` | `L65`, `L70`, `L76`, `L449-L450` | Delivered outcome (`99.99%`) | `PASS` |
| `cv_tailored.json:L39`, `cv_tailored.md:L13` | `Led revenue-protection initiatives by deploying automated recovery systems, agentic workflows, and incident-handling escalation mechanisms, reducing order cancellations and saving ~$10M annually` | `L70`, `L84-L90`, `L524-L527`; `AGENTS.md` §2 | Delivered outcome (`~$10M`); genuine Lowe's recovery workflow context for `agentic workflows` | `PASS` |
| `cv_tailored.json:L40`, `cv_tailored.md:L14` | `Built KPI frameworks and dashboards using internal enterprise analytics tools to track incident resolution, adoption, and cost savings, guiding ROI-driven tradeoffs and VP/CXO reviews` | `L66-L67`, `L77-L81`, `L462`, `L478-L484`, `L660` | Explicitly attributes internal enterprise analytics tools; avoids third-party analytics tool fabrication | `PASS` |
| `cv_tailored.json:L41`, `cv_tailored.md:L15` | `Defined annual and quarterly roadmaps by aligning engineering, finance, operations, and IT stakeholders without formal authority, targeting 20% reduction in incident volume` | `L65-L66`, `L71`, `L82`, `L485-L487` | Roadmap target explicitly preserved as `"targeting 20% reduction in incident volume"` | `PASS` |
| `cv_tailored.json:L42`, `cv_tailored.md:L16` | `Drove C-suite decision-making and operational planning by preparing board-level narratives and coordinating procurement, asset management, and platform workflows` | `L479`, `L484` (`"Supported C-suite decision-making"`), `L485` | **Defect `G6-01`**: Upgrades `"Supported"` to `"Drove C-suite decision-making"` | **`FAIL`** |
| `cv_tailored.json:L48`, `cv_tailored.md:L18` | `Spearheaded a unified enterprise asset lifecycle platform end to end... delivering $2M in annual cost savings` | `L69`, `L92-L95`, `L502` | Delivered outcome (`$2M` / `~$2M`) | `PASS` |
| `cv_tailored.json:L49`, `cv_tailored.md:L19` | `Designed and launched an AI-driven procurement and catalog system with agentic workflow orchestration for store setup teams, streamlining adoption and cutting operational cycle times by 20%` | `L96-L100`, `L530-L534`; `AGENTS.md` §2 | Delivered outcome (`20%` cycle time cut); genuine Lowe's AI procurement/catalog workflow context for `agentic workflow orchestration` | `PASS` |
| `cv_tailored.json:L64-L74`, `cv_tailored.md:L23-L29` | Hype Marketing & Product Services: GTM/campaign roadmaps, engagement pipelines, Upraised (`50%` engagement, `30%` website traffic), Programming Hub (`4.5+` ratings), Gradiant (`30%` open rates, `20%` CTRs), Acadecraft (`80%+` completion rates) | `L132-L160`, `L373-L377` | Exact measured outcomes preserved | `PASS` |
| `cv_tailored.json:L89-L91`, `cv_tailored.md:L33-L35` | HealthQ Rehab: `35%` organic traffic growth, `50%` social media engagement, `20%` overall brand engagement (WhatsApp, Telegram, newsletter) | `L184-L197`, `L380-L382` | Exact measured outcomes preserved | `PASS` |
| `cv_tailored.json:L105-L108`, `cv_tailored.md:L40-L43` | Byju's SPM: Xcel Masterclasses (`2.5L+` SQLs), `35%` lead conversion lift, `12` cross-product prototypes (Aakash-Byju's, Tynker, WhiteHat Jr.), Whitehat Jr. ILE (`15%` instructor training time reduction) | `L228-L238`, `L261-L263`, `L386-L388`, `L390` | Exact measured outcomes preserved | `PASS` |
| `cv_tailored.json:L109`, `cv_tailored.md:L44` | Tynker: `Led app redesign and feature tradeoffs for *Tynker* by adding assessments and DIY modules guided by completion signals, increasing course completion by 5%` | `L265-L268`, `L389` | Metric (`5%`) accurate; see `G6-ADV-01` regarding `"feature tradeoffs"` phrasing | `PASS (Advisory)` |
| `cv_tailored.json:L117-L118`, `cv_tailored.md:L47-L48` | Byju's Multiple Roles: science/maths interactive learning experiences, Social Studies product, Elevate UX interactions, `led a team of 5 product leads for Commerce product development` | `L297-L307`, `AGENTS.md` §1 | Directly supported (including 5 product leads at Byju's) | `PASS` |

### 3. Prohibited Fabrications, Evidence Mapping & Dossier Consistency

| Check Area | Findings | Status |
| :--- | :--- | :--- |
| **Prohibited Technical / Domain Fabrications (`AGENTS.md` §2)** | Zero occurrences of connector APIs, OAuth, RBAC, permission systems, SDKs, RAG, vector DBs, Amplitude, Mixpanel, GA4, Firebase, Optimizely, RCS, production ML decisioning model ownership, ROAS/incrementality ownership, loyalty platforms, merchandising platforms, or DAM platform ownership. No fabricated ASIN defect, seller tool, demand-sensing, or assortment recommendation claims in CV. | `PASS` |
| **Requirement Mapping & Citations (`requirement_matrix.json`)** | All 15 JD requirements (`10 Direct`, `3 Adjacent`, `2 Gap`) have verified `canonical_master_profile.md` line citations; domain gaps (`DM-2` demand sensing/assortment, `DM-4` seller onboarding/ASIN defect/pricing/search tools) and adjacent partner mixes (`IM-2`, `DM-1`, `DM-3`) are honestly flagged without disguising adjacent work as direct experience. | `PASS` |
| **Dossier Consistency & Math (`dossier.md`)** | Weighted score arithmetic verified exact (`22.0 + 13.0 + 15.2 + 13.5 + 8.4 + 4.3 + 4.6 = 81.0 / 100`). LinkedIn header anomaly (`AWS IN` vs `Amazon Now` / `A10499561`) accurately documented. | `PASS` |
| **Gate 7 Confidentiality & Disclosure** | No proprietary Lowe's/Byju's/client architectures, confidential customer data, internal tool names, or unapproved commercial disclosures appear beyond approved public-safe items in `canonical_master_profile.md` `v1.1.0`. | `PASS` |
