# Independent Fact-Check & Integrity Audit Report (Gates 6 & 7)

- **Opportunity ID:** `4488518380-booking-spm-payments`
- **Target Role:** Booking Holdings — Senior Product Manager (Pay-in Payment Methods)
- **Audit Scope:** `cv_tailored.json`, `cv_tailored.md`, `cv_changelog.md`, `requirement_matrix.json`, and `dossier.md`
- **Authoritative Baselines:** `canonical_master_profile.md` (`v1.1.0`) and `AGENTS.md`
- **Audit Date:** `2026-11-15`
- **Auditor:** Independent Fact-Check & Integrity Reviewer (`fact_check_reviewer`)

---

## Overall Verdict: **`FAIL`**

| Gate | Scope | Verdict | Summary |
| :--- | :--- | :--- | :--- |
| **Gate 6** | CV Claim & Profile Integrity Audit | **`FAIL`** | **2 factual/grounding defects found** in `cv_tailored.json`, `cv_tailored.md`, and `cv_changelog.md` (date/role & product misattribution in Byju's `Multiple Roles`, plus unsupported `"onboarding"` and `"discovery workflows"` additions), alongside 2 minor phrasing tightening recommendations. |
| **Gate 7** | Confidentiality & Disclosure Review | **`PASS`** | Zero proprietary internal architectures, confidential customer data, unapproved internal tool names, or prohibited technical/domain fabrications detected across all audited files. |

---

## 1. Defects Requiring Remediation (Gate 6)

### Defect 1 — Date/Role & Product Misattribution in Byju’s `Multiple Roles` (Material)
- **Affected Files & Lines:**
  - `cv_tailored.json`: `L102–L108`
  - `cv_tailored.md`: `L46–L49`
  - `cv_changelog.md`: `L56`
- **Current Tailored Claims (under `Multiple Roles | Jun 2015 – June 2020`):**
  1. `"Prototyped and built 300+ *interactive learning experiences* for science and maths alongside UX interactions for the *Elevate* internal tracking platform"`
  2. `"Prototyped and launched the *Social Studies* product (500+ hours of video content) and led 5 product leads for *BTLA Commerce* product development"`
- **Canonical Master Profile Evidence (`canonical_master_profile.md` v1.1.0):**
  - Under `Product Manager` (`July 2020 – Feb 2022`, which maps to the canonical CV display period `Senior Product Manager | July 2020 – April 2023` per `L219`):
    - `L270–L274`: `### Social Studies Product` → `Launched Social Studies product` → `Built: 500+ hours of video content` and `300+ interactive learning experiences`.
  - Under `Multiple Roles` (`June 2015 – June 2020`):
    - `L304–L307`: `Developed interactive learning experiences for science and mathematics`; `Prototyped and developed Social Studies product`; `Created UX interactions for Elevate internal tracking platform`; `Led team of 5 product leads for Commerce product development`.
- **Violation:**
  1. Attributes the `July 2020 – Feb 2022` launch of the *Social Studies* product and its `500+ hours of video content` to the `Jun 2015 – June 2020` (`Multiple Roles`) period.
  2. Attaches `300+ interactive learning experiences` (built for *Social Studies Product* in `July 2020 – Feb 2022` per `L270–L274`) to *science and maths* interactive learning experiences in `Jun 2015 – June 2020`.
- **Exact Fix Required:**
  - Restrict `Multiple Roles (Jun 2015 – June 2020)` strictly to `L304–L307`:
    - Bullet 1: `"Prototyped and created *interactive learning experiences* for science and mathematics alongside UX interactions for the *Elevate* internal tracking platform"`
    - Bullet 2: `"Prototyped and developed the *Social Studies* product and led 5 product leads for *BTLA Commerce* product development"`
  - If retaining the `Social Studies` launch, `500+ hours of video content`, or `300+ interactive learning experiences`, move them under `Senior Product Manager (July 2020 – April 2023)` and explicitly tie `300+ interactive learning experiences` to the `Social Studies` product (not science and maths). Update `cv_changelog.md` (`L56`) and re-render the PDF accordingly.

### Defect 2 — Unsupported Specific Workflow/Funnel Terms (`"onboarding"` & `"discovery workflows"`)
- **Affected Files & Lines:**
  - **2a (`"onboarding"`):** `cv_tailored.json` `L95`, `cv_tailored.md` `L42`, `cv_changelog.md` `L52` (`Byju’s — Senior Product Manager`, Bullet 2):
    - Current: `"Diagnosed funnel friction and ran iterative product experiments across onboarding and engagement workflows with cross-functional teams, improving lead conversion rates by 35%"`
    - Canonical Evidence (`L232, L237, L387`): Mentions `"customer journeys and engagement workflows"` and `"identifying friction points across the product funnel"`, with **zero** occurrences of `"onboarding"` in `canonical_master_profile.md` (and Xcel Masterclasses lead conversion was SQL conversion across the customer funnel, not documented as product onboarding).
    - **Exact Fix:** Replace `"across onboarding and engagement workflows"` with `"across customer journeys and engagement workflows"`.
  - **2b (`"discovery workflows"`):** `cv_tailored.json` `L61`, `cv_tailored.md` `L28`, `cv_changelog.md` `L49` (`Hype Marketing & Product Services — Programming Hub`):
    - Current: `"Programming Hub: Developed and marketed digital learning products by optimizing product positioning and discovery workflows, achieving 4.5+ ratings and strong user adoption"`
    - Canonical Evidence (`L147–L150, L375`): States `"Combined product positioning, content strategy, and digital marketing execution to launch and market Programming Hub's learning products, achieving 4.5+ ratings and strong user adoption."` `"Discovery workflows"` does not appear in `canonical_master_profile.md`.
    - **Exact Fix:** Replace `"optimizing product positioning and discovery workflows"` with `"combining product positioning, content strategy, and digital marketing execution"`.

### Advisory Phrasing Tightening Recommendations (Non-Blocking, Recommended Alongside Fixes)
1. **Lowe’s India Bullet 1 (`cv_tailored.json` `L26`):** `"Owned product vision, strategy, and execution..."` — `canonical_master_profile.md` (`L65–L66, L76, L102, L446`) supports `"Owned strategic initiatives"` and `"Enterprise Product Strategy"` / `"Product Strategy"`, without using `"product vision"`. Consider tightening to `"Owned product strategy and execution..."`.
2. **Byju’s SPM Bullet 1 (`cv_tailored.json` `L94`):** `"Led product and GTM strategy for *Byju’s Xcel Masterclasses*..."` — `canonical_master_profile.md` `L386` states `"Led product and customer engagement strategy for Byju’s Xcel Masterclasses..."`. Consider matching `L386` verbatim.
3. **`"agents"` / `"agentic workflows"` Usage (`cv_tailored.json` `L29, L38`):** Both uses occur exclusively on the two Lowe’s India bullets (`automated recovery agents` and `AI-driven procurement and catalog system powered by agentic workflows`) explicitly cited as genuine work in `AGENTS.md` Section 2, without inventing standalone LLM/agent architectures. Note that Booking’s Pay-in Payment Methods role is a payments PM role rather than an AI/Workflow Automation role, so retaining or reverting to `"automated recovery systems"` / `"AI-driven procurement and catalog system"` is acceptable under `AGENTS.md`.

---

## 2. Locked Identity, Dates, Titles, Education & Certifications Audit

| Field / Section | Audited Value (`cv_tailored.json` / `cv_tailored.md`) | Canonical Value (`canonical_master_profile.md` v1.1.0 & `AGENTS.md`) | Status |
| :--- | :--- | :--- | :--- |
| **Candidate Contact** | `Minesh Wadhwa` \| `Bangalore • w.minesh@gmail.com • +91 9035 199 024` | `Bangalore, Karnataka, India` \| `w.minesh@gmail.com` \| `+91 9035 199 024` (`L9–L11`) | `PASS` |
| **Lowe’s India** | `Senior Product Manager` \| `Sep 2024 – Present` \| `Bangalore, Karnataka` | `Lowe’s India` \| `Senior Product Manager` \| `Sep 2024 – Present` \| `Bangalore, Karnataka` (`L48–L50`) | `PASS` |
| **Hype Marketing & Product Services** | `Founder` \| `Oct 2023 – Nov 2024` \| `Bangalore, Karnataka` | `Hype Marketing & Product Services` \| `Founder` \| `Oct 2023 – Nov 2024` \| `Bangalore, Karnataka` (`L119–L121`) | `PASS` |
| **HealthQ Rehab** | `Head of Marketing` \| `May 2023 – Dec 2023` \| `Bangalore, Karnataka` | `HealthQ Rehab` \| `Head of Marketing` \| `May 2023 – Dec 2023` \| `Bangalore, Karnataka` (`L179–L181`) | `PASS` |
| **Byju’s — Senior Product Manager** | `Byju’s - Product Development` \| `Senior Product Manager` \| `July 2020 – April 2023` \| `Bangalore, Karnataka` | `Byju’s — Product Development` \| `Senior Product Manager` \| `July 2020 – April 2023` \| `Bangalore, Karnataka` (`L212–L219`) | `PASS` |
| **Byju’s — Multiple Roles** | `Multiple Roles` \| `Jun 2015 – June 2020` | `Multiple Roles` \| `June 2015 – June 2020` (`AGENTS.md`: `Jun 2015 – June 2020`) | `PASS` |
| **Certifications** | `University of California, Irvine` (`Oct 2020 – Dec 2020`) — 3 specialization bullets | `University of California, Irvine` — `Project Management Specialization` (`Oct 2020 – Dec 2020`) (`L333–L344`) | `PASS` |
| **Social Entrepreneurship** | *The Open Door Foundation* (RTC Girls Home, Bangalore) & *Education for All* by Byju’s (10M kids by 2025) | Matches `L347–L350` verbatim | `PASS` |
| **Education** | `Manipal Institute of Technology` (`B. Tech. in Computer Science Engineering`, `2011 – 2015`); `Indian Institute Of Management - Bangalore` (`Executive General Management Program`, `2025 – 2026 (ongoing)`) | Matches `AGENTS.md` Section 1 & `L321–L327` | `PASS` |

---

## 3. Claim-by-Claim Verification Table (`cv_tailored.json` & `cv_tailored.md`)

| Section / Claim | Metric / Ownership / Technical Claim | Canonical Citation (`v1.1.0`) | Outcome Distinction | Verdict |
| :--- | :--- | :--- | :--- | :--- |
| **Profile Summary** | `10+ years across enterprise platforms, consumer funnels, and GTM product launches`; engineering, design, finance, operations, data; influence without authority; internal analytics; `99.99%`, `~$10M`, `$2M`, `20%` faster AI workflows, `2.5L+` SQLs, `35%` higher lead conversion | `L40–L43, L65–L100, L217–L238, L367, L485–L488, L660` | Delivered (`99.99%`, `~$10M`, `$2M`, `20%`) & Measured (`2.5L+`, `35%`) accurately separated from roadmap target | `PASS` |
| **Lowe’s — Reliability (B1)** | Owned product vision, strategy, execution across eng/ops; `99.99%` reliability | `L65–L76, L446–L452` | Delivered (`99.99%`) | `PASS` *(tighten "vision" -> "product strategy")* |
| **Lowe’s — Reliability (B2)** | KPI frameworks & operational analytics dashboards using internal enterprise reporting tools (adoption, incident resolution, efficiency) | `L67, L77–L81, L660` | Operational capability; zero 3rd-party tool fabrication | `PASS` |
| **Lowe’s — Reliability (B3)** | Annual & quarterly roadmaps, monthly business reviews to VP/CXO, `targeting a 20% reduction in incident volume` | `L66, L82, L478–L481` | **Roadmap Target** explicitly preserved as `targeting` | `PASS` |
| **Lowe’s — Reliability (B4)** | Automated recovery agents & incident-handling workflows; reduced order cancellations; `~$10M` annual savings | `L70, L84–L90, L524–L528`, `AGENTS.md` §2 | Delivered (`~$10M`) | `PASS` |
| **Lowe’s — Reliability (B5)** | Aligned eng, product, finance, operations, IT via governance & operating rhythms without formal authority | `L71, L481, L485–L488, L553–L556` | Direct ownership/influence | `PASS` |
| **Lowe’s — Reliability (B6)** | Prioritized workflow improvements across procurement, asset management, operational planning weighing ROI vs constraints | `L69–L71, L462, L491–L493` | Direct/adjacent capability | `PASS` |
| **Lowe’s — Infra & Ops (B1)** | Spearheaded unified enterprise asset lifecycle platform with finance, ops, infra partners; `$2M` annual cost savings | `L91–L95, L493` | Delivered (`$2M`) | `PASS` |
| **Lowe’s — Infra & Ops (B2)** | Designed & launched AI-driven procurement & catalog system powered by agentic workflows for store setup; `20%` cycle time reduction | `L96–L100, L465–L467, L530–L535`, `AGENTS.md` §2 | Delivered (`20%`) | `PASS` |
| **Hype Marketing (B1–B2)** | End-to-end GTM, launch, lifecycle roadmaps; data-driven customer journey & engagement pipelines | `L124–L137, L373, L377` | Direct | `PASS` |
| **Hype — Upraised** | Social content & GTM launch strategy; `+50%` engagement, `+30%` website traffic | `L141–L145, L373` | Measured (`50%`, `30%`) | `PASS` |
| **Hype — Programming Hub** | Digital learning products; `4.5+` ratings; strong adoption; claims `"discovery workflows"` | `L147–L150, L375` | Measured (`4.5+`); `"discovery workflows"` unsupported | **`FAIL`** *(Defect 2b)* |
| **Hype — Gradiant** | Lifecycle & email marketing journeys; `30%` open rates, `20%` CTRs | `L152–L156, L374` | Measured (`30%`, `20%`) | `PASS` |
| **Hype — Acadecraft** | Structured learning programs; `80%+` completion rates | `L158–L160, L376` | Measured (`80%+`) | `PASS` |
| **HealthQ Rehab (B1–B3)** | SEO/content (`+35%` organic traffic), social (`+50%` engagement), WhatsApp/Telegram/newsletter (`+20%` brand engagement) | `L183–L198, L380–L383` | Measured (`35%`, `50%`, `20%`) | `PASS` |
| **Byju’s — SPM (B1)** | *Byju’s Xcel Masterclasses*; `2.5L+` sales-qualified leads | `L228–L236, L386` | Measured (`2.5L+`) | `PASS` *(tighten "GTM" -> "customer engagement")* |
| **Byju’s — SPM (B2)** | Funnel friction & iterative product experiments `"across onboarding and engagement workflows"`; `+35%` lead conversion | `L232, L237, L387` | Measured (`35%`); `"onboarding"` unsupported | **`FAIL`** *(Defect 2a)* |
| **Byju’s — SPM (B3)** | `12` cross-product prototypes across *Aakash-Byjus*, *Tynker*, *Whitehat Jr.* | `L231, L238, L388` | Measured (`12`) | `PASS` |
| **Byju’s — SPM (B4)** | Launched *Interactive Learning Experiences* for *Whitehat Jr.*; `-15%` instructor training time | `L261–L263, L390` | Measured (`15%`) | `PASS` |
| **Byju’s — SPM (B5)** | *Tynker* app redesign with assessments & DIY modules; `+5%` course completion | `L265–L268, L389` | Measured (`5%`) | `PASS` |
| **Byju’s — Multiple Roles (B1–B2)** | Claims `300+` interactive learning experiences for science & maths (`2015–2020`) and `launched` *Social Studies* (`500+` hours video) in `2015–2020` alongside *Elevate* UX & leading `5` product leads for *BTLA Commerce* | `L270–L275` (`July 2020–Feb 2022`) vs `L303–L308` (`June 2015–June 2020`) | **Date/Role & Product Misattribution** (`2020–2022` Social Studies metrics placed under `2015–2020` Multiple Roles & attached to science/maths) | **`FAIL`** *(Defect 1)* |

---

## 4. Dossier & Requirement Matrix Verification (`dossier.md` & `requirement_matrix.json`)

- **Requirement Classification Integrity:** All 14 JD requirements (`6` Direct, `6` Adjacent, `2` Gap) accurately cite `canonical_master_profile.md` `v1.1.0` lines and avoid disguising adjacent experience as direct ownership.
- **Gap Honesty:** `DM-1` (Pay-in payment methods / APMs / LPMs / travel commerce) and `IM-3` (multi-market payment localization) are explicitly flagged as `Gap`; `MH-1` (`~5` yrs formal PM/SPM titles vs `8–10` yrs), `MH-4` (unverified qualitative UX research studies), `MH-7` (Risk/Legal/Customer Service), `IM-1` (external PSPs), and `IM-2` (fraud/regulatory compliance) are properly bounded as `Adjacent`.
- **Gate 7 Confidentiality Check:** Neither `dossier.md` nor `requirement_matrix.json` nor the tailored CV materials expose confidential architecture, internal customer data, or unapproved disclosures.

---

## 5. Required Actions Before Resubmission
1. Fix **Defect 1** (`Byju’s — Multiple Roles` date/role and product attribution for `300+ interactive learning experiences`, `Launched Social Studies product`, and `500+ hours of video content`) across `cv_tailored.json`, `cv_tailored.md`, and `cv_changelog.md`.
2. Fix **Defect 2a** (`"onboarding"` → `"customer journeys"`) and **Defect 2b** (`"discovery workflows"` → `"content strategy, and digital marketing execution"`) across `cv_tailored.json`, `cv_tailored.md`, and `cv_changelog.md`.
3. Re-render `Minesh_Wadhwa_CV_Booking_Payments.pdf` and resubmit for Gate 6 re-verification.
