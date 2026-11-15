# Independent Fact-Check & Integrity Audit Report — Amazon Business (`4490321867-amazon-spm-in-prime`)

- **Audit Scope:** `cv_tailored.json`, `cv_tailored.md`, `cv_changelog.md`, `requirement_matrix.json`, and `dossier.md`
- **Authoritative Baseline:** `/Users/mineshwadhwa/Documents/Sherpa/canonical_master_profile.md` (`v1.1.0`) and `/Users/mineshwadhwa/Documents/Sherpa/AGENTS.md`
- **Auditor Role:** Independent Fact-Check & Integrity Reviewer (Agent 9)
- **Audit Date:** `2026-11-15`

---

## Overall Verdict: **`FAIL`**

| Gate | Scope | Verdict | Summary |
| :--- | :--- | :--- | :--- |
| **Gate 6** | CV Claim Audit & Profile Integrity | **`FAIL`** | **2 factual product/date misattributions** in `Byju’s — Multiple Roles` (`cv_tailored.json:L106-107`, `cv_tailored.md:L48-49`), **1 unsupported workflow claim** (`user onboarding` at Lowe’s India, `cv_tailored.json:L38`), and **3 minor phrasing/ownership precision defects** (`L61`, `L94`, `L95`). All metrics, employers, dates, titles, education, certifications, `"agents"` usage, and roadmap target distinctions are otherwise accurate. |
| **Gate 7** | Confidentiality & Disclosure Review | **`PASS`** | No confidential employer/client data, proprietary architecture, unauthorized internal details, or prohibited disclosures appear beyond approved public-safe descriptions in `canonical_master_profile.md` (`v1.1.0`). |

---

## 1. Required Fixes (Blocking Gate 6 Pass)

### Defect 1 (Critical — Factual Product & Date Misattribution): `300+ interactive learning experiences` attributed to `Elevate` platform
- **Location:** `cv_tailored.json:L106`, `cv_tailored.md:L48`, `cv_changelog.md:L47`
- **Current Text:** `Prototyped 300+ *interactive learning experiences* and UX flows for the *Elevate* platform` (under `Byju’s - Product Development` → `Multiple Roles` | `Jun 2015 – June 2020`)
- **Audit Finding:** In `canonical_master_profile.md`:
  - `300+ interactive learning experiences` (`L274`) were built for the **Social Studies Product** under `Product Manager` (`July 2020 – Feb 2022`), not for `Elevate`.
  - `Elevate` (`L306`, under `Multiple Roles` `June 2015 – June 2020`) is an **internal tracking platform** (`Created UX interactions for Elevate internal tracking platform`).
  - Combining these two bullets implies `300+ interactive learning experiences` were prototyped for the `Elevate` platform.
- **Required Fix:** Separate the two facts accurately. Under `Multiple Roles` (`Jun 2015 – June 2020`), state:
  > `"Prototyped interactive learning experiences (science and mathematics) and created UX interactions for the *Elevate* internal tracking platform"`
  (And if retaining `300+ interactive learning experiences`, place it with `Social Studies` under the `July 2020 – April 2023` display block per `L219` and `L270–274`.)

### Defect 2 (Critical — Role/Date Period Misattribution): `Launched Social Studies (500+ hrs video)` placed under `Jun 2015 – June 2020`
- **Location:** `cv_tailored.json:L107`, `cv_tailored.md:L49`, `cv_changelog.md:L47`
- **Current Text:** `Launched *Social Studies* (500+ hrs video) and led 5 product leads for *BTLA Commerce*` (under `Multiple Roles` | `Jun 2015 – June 2020`)
- **Audit Finding:** In `canonical_master_profile.md`:
  - Under `Multiple Roles` (`June 2015 – June 2020`, `L305`, `L307`), Minesh `"Prototyped and developed Social Studies product"` and `"Led team of 5 product leads for Commerce product development"`.
  - Under `Product Manager` (`July 2020 – Feb 2022`, `L270–274` — which maps to the canonical display block `Senior Product Manager | July 2020 – April 2023` per `L219`), Minesh `"Launched Social Studies product"` with `"500+ hours of video content"` and `"300+ interactive learning experiences"`.
  - Placing the `Launched Social Studies (500+ hrs video)` outcome in `Jun 2015 – June 2020` shifts a `2020–2022` launch/metric into the `2015–2020` period.
- **Required Fix:** Under `Multiple Roles` (`Jun 2015 – June 2020`), revise to:
  > `"Prototyped and developed the *Social Studies* product and led 5 product leads for *BTLA Commerce*"`
  (If `Launched Social Studies (500+ hrs video, 300+ interactive learning experiences)` is retained, place it under `Senior Product Manager | July 2020 – April 2023`.)

### Defect 3 (Major — Unsupported Claim): `user onboarding` at Lowe’s India
- **Location:** `cv_tailored.json:L38`, `cv_tailored.md:L20`
- **Current Text:** `Designed and launched an AI-driven procurement and catalog system powered by agentic workflows to simplify user onboarding and guided task orchestration for store setup teams, reducing operational cycle times by 20%`
- **Audit Finding:** Neither `canonical_master_profile.md` (`L96–100`) nor `templates/cv_base_schema.json` (`L38`) supports `"user onboarding"` or `"guided task orchestration"` for Lowe’s AI-driven procurement and catalog system. `canonical_master_profile.md` (`L97–99`) states it improved operational efficiency for store setup teams and reduced operational cycle times by `20%`; `cv_base_schema.json` (`L38`) states it streamlined `"workflow orchestration, operational coordination, user workflows, and product adoption for enterprise store setup teams"`.
- **Required Fix:** Replace `"to simplify user onboarding and guided task orchestration"` with evidenced phrasing such as:
  > `"to streamline workflow orchestration, user workflows, and product adoption for store setup teams"`

### Defect 4 (Minor — Precision / Ownership & Unsupported Term Alignment)
1. **`cv_tailored.json:L61` / `cv_tailored.md:L28` (`Programming Hub`):** `"by optimizing product positioning and discovery workflows"` → `canonical_master_profile.md` (`L148–150`, `L375`) cites `"product positioning, content strategy, and digital marketing execution"`, not `"discovery workflows"`. **Fix:** Replace `"discovery workflows"` with `"content strategy and digital marketing execution"`.
2. **`cv_tailored.json:L94` / `cv_tailored.md:L41` (`Byju’s Xcel Masterclasses`):** `"Owned B2C product and acquisition funnel strategy"` → `canonical_master_profile.md` (`L235`, `L386`) uses `"Led Byju’s Xcel Masterclasses product"` and `"Led product and customer engagement strategy... across the customer funnel"`. **Fix:** Use `"Led"` instead of `"Owned"` (`AGENTS.md:L13`) and `"B2C product and customer engagement strategy across the acquisition funnel"` (or `"customer funnel"`).
3. **`cv_tailored.json:L95` / `cv_tailored.md:L42` (`Byju’s SPM Bullet 2`):** `"across onboarding and user engagement workflows"` → `canonical_master_profile.md` (`L387`) cites `"customer journeys and engagement workflows... across the product funnel"`, not explicitly `"onboarding"`. **Fix:** Replace `"onboarding and user engagement workflows"` with `"customer journey and engagement workflows"`.

---

## 2. Claim-by-Claim Verification Table

### A. Locked Identity, Employers, Titles, Dates, Locations, Education, Certifications & Social Entrepreneurship

| Field / Section | Tailored CV Value (`cv_tailored.json` / `cv_tailored.md`) | Canonical Source (`canonical_master_profile.md` v1.1.0 & `AGENTS.md`) | Status |
| :--- | :--- | :--- | :--- |
| **Header** | `Minesh Wadhwa` \| `Bangalore • w.minesh@gmail.com • +91 9035 199 024` | `L1`, `L9–11` | `PASS` |
| **Lowe’s India** | `Lowe’s India` \| `Senior Product Manager` \| `Sep 2024 – Present` \| `Bangalore, Karnataka` | `L48–50`, `AGENTS.md:L17` | `PASS` |
| **Hype Marketing & Product Services** | `Hype Marketing & Product Services` \| `Founder` \| `Oct 2023 – Nov 2024` \| `Bangalore, Karnataka` | `L119–121`, `AGENTS.md:L18` | `PASS` |
| **HealthQ Rehab** | `HealthQ Rehab` \| `Head of Marketing` \| `May 2023 – Dec 2023` \| `Bangalore, Karnataka` | `L179–181`, `AGENTS.md:L19` | `PASS` |
| **Byju’s — Senior Product Manager** | `Byju’s - Product Development` \| `Senior Product Manager` \| `July 2020 – April 2023` \| `Bangalore, Karnataka` | `L212–219` (canonical CV display period), `AGENTS.md:L20` | `PASS` |
| **Byju’s — Multiple Roles** | `Multiple Roles` \| `Jun 2015 – June 2020` \| `Bangalore, Karnataka` | `L286–287`, `AGENTS.md:L20` | `PASS` |
| **Certifications** | `University of California, Irvine` \| `Oct 2020 – Dec 2020` (3 module bullets) | `L333–343`, `AGENTS.md:L21` | `PASS` |
| **Social Entrepreneurship** | *The Open Door Foundation* (RTC Girls Home, Bangalore); *Education for All* initiative by Byju’s (train 10 million kids by 2025) | `L347–349`, `AGENTS.md:L22` | `PASS` |
| **Education** | `Manipal Institute of Technology`, `Manipal, Karnataka` — `B. Tech. in Computer Science Engineering` (`2011 – 2015`); `Indian Institute Of Management - Bangalore` — `Executive General Management Program` (`2025 – 2026 (ongoing)`) | `L321–327`, `AGENTS.md:L23` | `PASS` |

### B. Bullet, Metric, Technical/Domain Claim & Ownership Verification

| Location | Claim / Metric Audited | Canonical Line Reference | Classification / Outcome Type | Verdict |
| :--- | :--- | :--- | :--- | :--- |
| `cv_tailored.json:L13` | `10+ years of experience` (Jun 2015–Present = 11+ yrs) | `L48–50`, `L286–287` | Direct fact | `PASS` |
| `cv_tailored.json:L13` | `2.5L+ SQLs`, `35% higher lead conversion`, `~$10M annual revenue protection`, `$2M cost savings`, `20% faster AI-driven workflows` | `L86`, `L94`, `L98`, `L236–237` | Delivered / Measured outcomes | `PASS` |
| `cv_tailored.json:L26` | `99.99% reliability for core business platforms` | `L65`, `L68`, `L76` | Delivered outcome | `PASS` |
| `cv_tailored.json:L27` | KPI frameworks & operational analytics dashboards using **internal enterprise reporting tools** (no commercial 3P tools claimed) | `L67`, `L77–81`, `L660–663` | Direct fact | `PASS` |
| `cv_tailored.json:L28` | Annual/quarterly roadmaps, monthly business reviews to VP/CXO, **targeting a 20% reduction in incident volume** | `L66`, `L82`, `L478–480` | Roadmap target (properly qualified as `targeting`) | `PASS` |
| `cv_tailored.json:L29` | Revenue protection via **automated recovery agents** and incident-handling workflows, reducing order cancellations, **saving ~$10M annually** | `L70`, `L85–89`, `AGENTS.md:L36` | Delivered outcome + permitted `"agents"` framing for Lowe’s recovery workflows | `PASS` |
| `cv_tailored.json:L30` | Aligned engineering, product, finance, operations, and IT teams via governance/review cadences **without formal authority** | `L65–71`, `L481`, `L485–487` | Direct fact (no authority upgrade) | `PASS` |
| `cv_tailored.json:L31` | Prioritized workflow improvements across procurement, asset management, and operational planning via business ROI vs. constraints | `L66`, `L69–71`, `L462`, `L492` | Direct fact | `PASS` |
| `cv_tailored.json:L37` | Unified enterprise asset lifecycle platform across finance, operations, infrastructure; **delivering $2M in annual cost savings** | `L54`, `L92–95`, `L502` | Delivered outcome | `PASS` |
| `cv_tailored.json:L38` | AI-driven procurement & catalog system powered by **agentic workflows**, **reducing operational cycle times by 20%**; claims **`user onboarding and guided task orchestration`** | `L97–99`, `AGENTS.md:L36`, `cv_base_schema.json:L38` | Delivered outcome (`20%`) + permitted `"agentic workflows"`, **unsupported `user onboarding`** | **`FAIL`** (Defect 3) |
| `cv_tailored.json:L53–54` | Hype GTM, acquisition, lifecycle marketing roadmaps & data-driven engagement pipelines | `L124–137`, `L373`, `L377` | Direct / Adjacent | `PASS` |
| `cv_tailored.json:L60` | `Upraised`: **50% engagement**, **30% website traffic** | `L141–145`, `L373` | Measured outcome | `PASS` |
| `cv_tailored.json:L61` | `Programming Hub`: **4.5+ ratings**; claims **`discovery workflows`** | `L147–150`, `L375` | Measured outcome (`4.5+`); **`discovery workflows` unverified** | **`FAIL`** (Defect 4.1) |
| `cv_tailored.json:L62` | `Gradiant`: **30% open rates**, **20% CTRs** | `L152–156`, `L374` | Measured outcome | `PASS` |
| `cv_tailored.json:L63` | `Acadecraft`: **80%+ completion rates** | `L158–160`, `L376` | Measured outcome | `PASS` |
| `cv_tailored.json:L78–80` | `HealthQ Rehab`: **35% organic traffic**, **50% social media engagement**, **20% brand engagement** (WhatsApp, Telegram, newsletter) | `L184–197`, `L380–382` | Measured outcomes | `PASS` |
| `cv_tailored.json:L92` | Products: `Byju’s Xcel Masterclasses, Tynker, Whitehat Jr., Aakash-Byjus` | `L222–225` | Direct fact | `PASS` |
| `cv_tailored.json:L94` | `Byju’s Xcel Masterclasses`: **2.5L+ sales-qualified leads**; uses **`Owned`** instead of **`Led`** | `L235–236`, `L386`, `AGENTS.md:L13` | Measured outcome (`2.5L+`); minor ownership wording upgrade | **`FAIL`** (Defect 4.2) |
| `cv_tailored.json:L95` | Funnel friction & experiments improving **lead conversion rates by 35%**; cites **`onboarding`** | `L230–232`, `L237`, `L387` | Measured outcome (`35%`); **`onboarding` unverified** | **`FAIL`** (Defect 4.3) |
| `cv_tailored.json:L96` | **12 cross-product experience prototypes** across `Aakash-Byjus`, `Tynker`, `Whitehat Jr.` | `L238`, `L388` | Direct / Adjacent bridge | `PASS` |
| `cv_tailored.json:L97` | `Whitehat Jr.` *Interactive Learning Experiences* via live-coding workflow redesign, **reducing instructor training time by 15%** | `L262–263`, `L390` | Measured outcome | `PASS` |
| `cv_tailored.json:L98` | `Tynker` app redesign with assessments & DIY modules, **increasing course completion by 5%** | `L266–268`, `L389` | Measured outcome | `PASS` |
| `cv_tailored.json:L104` | Products: `Social Studies, Interactive Learning Experiences, Byju's Exam Prep, BTLA Commerce, BTLA Science` | `L290–294` | Direct fact | `PASS` |
| `cv_tailored.json:L106` | `Prototyped 300+ interactive learning experiences and UX flows for the Elevate platform` (`Jun 2015–June 2020`) | `L274` (Social Studies, 2020–2022), `L306` (Elevate internal tracking platform, 2015–2020) | **Factual product & date misattribution** | **`FAIL`** (Defect 1) |
| `cv_tailored.json:L107` | `Launched Social Studies (500+ hrs video) and led 5 product leads for BTLA Commerce` (`Jun 2015–June 2020`) | `L271–273` (`Launched`/`500+ hrs` under 2020–2022), `L305`, `L307` | **Role/date misattribution** (`5 product leads` is `PASS`) | **`FAIL`** (Defect 2) |

### C. Prohibited Fabrications & Supporting Document Audit (`requirement_matrix.json`, `dossier.md`, `cv_changelog.md`)

- **Prohibited Terms Check (`AGENTS.md:L38-39`):** Zero occurrences of connector APIs, authentication protocols, SDKs, security architecture, permission systems, OAuth, RBAC, RAG pipelines, vector databases, commercial 3P analytics tools (`Amplitude`, `Mixpanel`, `GA4`, `Firebase`, `Optimizely`), RCS marketing, production ML decisioning model ownership, ROAS/incrementality ownership, loyalty platforms, merchandising platforms, or DAM platform ownership. (`PASS`)
- **`requirement_matrix.json` & `dossier.md`:** Line citations to `canonical_master_profile.md` `v1.1.0` are accurate (`14 Direct`, `4 Adjacent`, `1 Gap`). Adjacent experiences (`DM-1`, `DM-3`, `DM-5`, `IM-3`) and Gap (`IM-2`) are transparently flagged without disguising adjacent work as direct subscription/e-commerce/global-locale ownership. (`PASS`)
- **`cv_changelog.md`:** Accurately logs changes, except row `Byju’s — Multiple Roles (Bullets 1–2)` (`L47`) replicates Defects 1 & 2 from `cv_tailored.json`. (`FAIL` — update alongside CV fix)
- **JSON/Markdown Parity:** `cv_tailored.json` and `cv_tailored.md` are 100% synchronized in text and structure. (`PASS` — both require the same Defect 1–4 edits before re-rendering PDF)

---

## 3. Gate 7 Confidentiality & Disclosure Audit (`PASS`)

- **Employer / Client Confidentiality:** Only approved public-safe employer, business unit, product, and Hype consulting client names (`Upraised`, `Programming Hub`, `Gradiant`, `Acadecraft`) from `canonical_master_profile.md` `v1.1.0` appear.
- **Internal Architecture & Financial Boundaries:** No proprietary codebases, internal tool names beyond `Elevate` (`L306`), internal infrastructure topology, customer PII, or unapproved financial details beyond `~$10M` and `$2M` appear.
- **Verdict:** **`PASS`**
