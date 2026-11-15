# Independent Fact-Check & Confidentiality Audit Report

- **Opportunity ID:** `4489848810-jobgether-pm-learning`
- **Target Role:** Product Manager, Global Learning & Knowledge Platforms — Jobgether (Partner Company)
- **Canonical Baseline:** `/Users/mineshwadhwa/Documents/Sherpa/canonical_master_profile.md` (`v1.1.0`) & `/Users/mineshwadhwa/Documents/Sherpa/AGENTS.md`
- **Audited Artifacts:** `cv_tailored.json`, `cv_tailored.md`, `cv_changelog.md`, `requirement_matrix.json`, `dossier.md`
- **Audit Date:** `2026-11-15`

---

## Overall Audit Verdict: **FAIL** (Actionable Minor Fixes Required)

| Gate | Scope | Verdict | Summary |
| :--- | :--- | :--- | :--- |
| **Gate 6** | CV Claim Audit & Profile Integrity | **FAIL** | All 14 metrics, dates, titles, employers, education, certifications, roadmap target distinction (`targeting 20% incident volume reduction`), `"agents"` usage, internal analytics framing, and `Adjacent`/`Gap` boundaries are accurate. However, **1 unsupported domain/audience claim** was introduced for **Upraised** (`"aligned with learner demand"` is not documented in `canonical_master_profile.md` `v1.1.0`), alongside **2 minor paraphrasing stretches** (**Acadecraft**: `"and milestones"`; **HealthQ Rehab**: `"content discovery strategy"`). |
| **Gate 7** | Confidentiality & Disclosure Review | **PASS** | Zero confidential employer, client, customer PII, internal architecture, or commercially sensitive disclosures beyond approved public-safe descriptions in `canonical_master_profile.md` (`v1.1.0`). |

---

## Defects & Exact Fixes Required

### Defect 1 (Blocking — Unsupported Claim, Gate 6)
- **Location:** `cv_tailored.json:L60`, `cv_tailored.md:L27`, `cv_changelog.md:L40`
- **Current Text:**
  > `Upraised: Crafted social content and growth strategy for new offerings aligned with learner demand, increasing engagement by 50% and traffic by 30%`
- **Issue:** `canonical_master_profile.md` (`L141-L145`, `L373`) documents Upraised only as `"new offerings"` / `"client offerings"` and does not state that Upraised's offerings were for learners or aligned with `"learner demand"`. Importing external knowledge or JD terminology (`"learner demand"`) into a client bullet without profile support violates `AGENTS.md` Section 1 (`Single Source of Truth`).
- **Exact Fix:** Replace `"new offerings aligned with learner demand"` with `"new offerings"` (or `"new client offerings aligned with business goals"` per `L373`), e.g.:
  > `Upraised: Crafted social content and growth strategy for new offerings, increasing engagement by 50% and traffic by 30%`

### Defect 2 (Non-Blocking Recommended Tightening — Minor Paraphrasing, Gate 6)
- **Location A (`Acadecraft`):** `cv_tailored.json:L63`, `cv_tailored.md:L30`, `cv_changelog.md:L40`
  - **Current Text:** `Built structured digital learning programs around learner needs and milestones, achieving 80%+ completion rates`
  - **Issue:** `canonical_master_profile.md:L159-L160, L376` states `"Built structured learning programs"` and `"by aligning learning experiences to user needs and engagement objectives"`, without mentioning `"milestones"`.
  - **Recommended Fix:** Replace `"learner needs and milestones"` with `"user needs and engagement objectives"`.
- **Location B (`HealthQ Rehab`):** `cv_tailored.json:L78`, `cv_tailored.md:L34`, `cv_changelog.md:L41`
  - **Current Text:** `Revamped SEO and content discovery strategy aligned with audience demand, driving 35% organic traffic growth`
  - **Issue:** `canonical_master_profile.md:L184, L380` states `"Revamped SEO and content marketing strategy by aligning content themes and digital distribution with audience demand"`. `"content discovery strategy"` shifts `"content marketing strategy"` toward the JD term (`DM-2`).
  - **Recommended Fix:** Use `"Revamped SEO and content marketing strategy aligned with audience demand, driving 35% organic traffic growth"`.

---

## Claim-by-Claim Verification Table

### A. Locked Identity, Employers, Dates, Titles, Certifications, Social & Education

| Item | Audited Value (`cv_tailored.json` / `cv_tailored.md`) | Canonical Source (`canonical_master_profile.md` `v1.1.0` & `AGENTS.md`) | Status |
| :--- | :--- | :--- | :--- |
| **Header / Contact** | `Minesh Wadhwa`, `Bangalore • w.minesh@gmail.com • +91 9035 199 024` | `L1`, `L9-L11` | **PASS** |
| **Lowe's India** | `Senior Product Manager` \| `Sep 2024 – Present` \| `Bangalore, Karnataka` | `L48-L50`, `AGENTS.md:L17` | **PASS** |
| **Hype Marketing & Product Services** | `Founder` \| `Oct 2023 – Nov 2024` \| `Bangalore, Karnataka` | `L119-L121`, `AGENTS.md:L18` | **PASS** |
| **HealthQ Rehab** | `Head of Marketing` \| `May 2023 – Dec 2023` \| `Bangalore, Karnataka` | `L179-L181`, `AGENTS.md:L19` | **PASS** |
| **Byju's - Product Development (SPM)** | `Senior Product Manager` \| `July 2020 – April 2023` \| `Bangalore, Karnataka` | `L212-L219`, `AGENTS.md:L20` | **PASS** |
| **Byju's - Product Development (Multiple Roles)** | `Multiple Roles` \| `Jun 2015 – June 2020` \| `Bangalore, Karnataka` | `L286-L287`, `AGENTS.md:L20` | **PASS** |
| **Certifications** | `University of California, Irvine` \| `Oct 2020 – Dec 2020` (3 course bullets) | `L333-L343`, `AGENTS.md:L21` | **PASS** |
| **Social Entrepreneurship** | *The Open Door Foundation* (RTC Girls Home, Bangalore); *Education for All* by Byju's (10 million kids by 2025) | `L347-L350`, `AGENTS.md:L22` | **PASS** |
| **Education (MIT)** | `Manipal Institute of Technology`, `Manipal, Karnataka` — `B. Tech. in Computer Science Engineering` (`2011 – 2015`) | `L325-L327`, `AGENTS.md:L23` | **PASS** |
| **Education (IIM-B)** | `Indian Institute Of Management - Bangalore` — `Executive General Management Program` (`2025 – 2026 (ongoing)`) | `L321-L323`, `AGENTS.md:L23` | **PASS** |

---

### B. Profile Summary & Experience Bullet Audit

| Section / Bullet | Claim / Metric / Technical Term Audited | Canonical Evidence & Line Citation | Verdict |
| :--- | :--- | :--- | :--- |
| **Profile Summary** | `10+ years of experience` (Jun 2015 – Nov 2026 = ~11.4 yrs); `Byju's, Tynker, WhiteHat Jr., Programming Hub, and Lowe's India`; `AI-enabled agentic workflows`; `internal analytics`; `500+ hours of learning content`, `80%+ completion rates`, `15% lower instructor training time`, `35% higher conversion`, `20% faster AI-driven catalog cycle times` | `L18-L43`, `L67`, `L97-L98`, `L148`, `L160`, `L217-L316`, `L660`; `"agents"` permitted for Lowe's AI/automation workflows per `AGENTS.md:L36` | **PASS** |
| **Lowe's — RE Team (Bullet 1)** | Owned enterprise platform reliability initiatives; scalable workflow automation & SLA governance; `99.99% reliability` (delivered outcome) | `L65`, `L68`, `L76`, `L527` | **PASS** |
| **Lowe's — RE Team (Bullet 2)** | KPI frameworks and dashboards using `internal enterprise analytics tools` tracking adoption, workflow efficiency, incident resolution | `L67`, `L77-L81`, `L660` (no prohibited commercial third-party analytics tools claimed) | **PASS** |
| **Lowe's — RE Team (Bullet 3)** | Annual and quarterly product roadmaps; **`targeting 20% incident volume reduction`** | `L66`, `L82`, `L480` — properly preserved as a **roadmap target**, not a delivered outcome (`AGENTS.md:L15`) | **PASS** |
| **Lowe's — RE Team (Bullet 4)** | Revenue protection initiatives; `automated recovery agents and incident-handling workflows`; cutting order cancellations; saving **`~$10M annually`** (delivered outcome) | `L70`, `L85-L90`, `L525-L528`; `"automated recovery agents"` aligned with `AGENTS.md:L36` | **PASS** |
| **Lowe's — RE Team (Bullet 5)** | Facilitated technical & non-technical alignment across product, engineering, finance, operations via business reviews & KPI governance | `L71`, `L478-L488` (no formal authority or people management over engineering claimed) | **PASS** |
| **Lowe's — RE Team (Bullet 6)** | Diagnosed operational pain points across planning & lifecycle programs with operations, IT, and business teams | `L69-L71`, `L560-L563` | **PASS** |
| **Lowe's — I&O BU (Bullet 1)** | Spearheaded unified enterprise asset lifecycle platform with finance, operations, infrastructure stakeholders; **`$2M in annual savings`** (delivered outcome) | `L91-L95`, `L502`, `AGENTS.md:L15` | **PASS** |
| **Lowe's — I&O BU (Bullet 2)** | Designed and launched AI-driven procurement and catalog platform `powered by agentic workflows`; **`20%` cycle time reduction** (delivered outcome) | `L96-L100`, `L465-L467`, `L530-L535`; `"agentic workflows"` aligned with `AGENTS.md:L36` | **PASS** |
| **Hype (Bullets 1–2)** | Defined product, content, and GTM roadmaps across concurrent digital learning and consumer clients; data-driven user engagement and learning journeys | `L124-L138`, `L373`, `L377` | **PASS** |
| **Hype — Upraised** | `"new offerings aligned with learner demand"`; `50%` engagement, `30%` traffic (measured outcomes) | Metrics match `L144-L145`, `L373`; however **`"aligned with learner demand"`** is **not supported** in `L141-L145` or `L373` | **FAIL** |
| **Hype — Programming Hub** | Digital learning products (courses + content); **`4.5+ ratings`** (measured outcome) | `L148-L150`, `L375` | **PASS** |
| **Hype — Gradiant** | Lifecycle and email engagement programs; **`30% open rates`**, **`20% CTRs`** (measured outcomes) | `L153-L156`, `L374` | **PASS** |
| **Hype — Acadecraft** | Structured digital learning programs; **`80%+ completion rates`** (measured outcome) | Metrics match `L160`, `L376`; minor wording `"and milestones"` not explicit in `L376` (`"user needs and engagement objectives"`) | **WARN (Tighten)** |
| **HealthQ Rehab (Bullet 1)** | `35% organic traffic growth` (measured outcome) | Metric matches `L191`, `L380`; minor wording `"content discovery strategy"` vs canonical `"content marketing strategy"` (`L184`, `L380`) | **WARN (Tighten)** |
| **HealthQ Rehab (Bullets 2–3)** | `50%` social media engagement; WhatsApp, Telegram, newsletter workflows; `20%` brand engagement (measured outcomes) | `L186-L197`, `L381-L382` | **PASS** |
| **Byju's — SPM (Bullet 1)** | *Byju's Xcel Masterclasses*; **`2.5L+ sales-qualified leads`** (measured outcome) | `L222`, `L228`, `L235-L236`, `L386` | **PASS** |
| **Byju's — SPM (Bullet 2)** | Funnel friction & user engagement workflows; **`35%` lead conversion improvement** (measured outcome) | `L230-L237`, `L387` | **PASS** |
| **Byju's — SPM (Bullet 3)** | `12 cross-product learning prototypes` (*Aakash-Byjus*, *Tynker*, *Whitehat Jr.*); *Social Studies* (`500+ hrs video`, `300+ interactive experiences`) | `L238`, `L271-L274`, `L388` (both occurred within July 2020–April 2023 display period per `L219`) | **PASS** |
| **Byju's — SPM (Bullet 4)** | *Interactive Learning Experiences* for *Whitehat Jr.*; redesigned live coding workflows; **`15%` instructor training time reduction** (measured outcome) | `L261-L263`, `L390` | **PASS** |
| **Byju's — SPM (Bullet 5)** | *Tynker* app redesign with assessments & DIY modules guided by completion signals; **`5%` course completion increase** (measured outcome) | `L265-L269`, `L389` | **PASS** |
| **Byju's — Multiple Roles (Bullets 1–2)** | Interactive learning experiences (science & maths); UX journeys for *Elevate* internal tracking platform; *Social Studies* content-led product; led team of `5 product leads` for *BTLA Commerce* | `L290-L308`, `AGENTS.md:L14` | **PASS** |

---

### C. Requirement Matrix, Dossier & Prohibited Fabrications Audit

| Check | Audit Finding | Status |
| :--- | :--- | :--- |
| **JD Requirement Gaps (`MH-5`, `PR-3`)** | Both confirmed Gaps (external software vendor management / formal technical specs; Spanish/French/Arabic fluency) are explicitly recorded as `Gap` in `requirement_matrix.json` and `dossier.md`, and **absent** from `cv_tailored.json` / `cv_tailored.md`. | **PASS** |
| **Adjacent vs. Direct Boundaries (`MH-4`, `MH-6`, `PR-2`, `PR-4`, `IM-1`, `IM-2`, `DM-2`)** | No formal PRD/user-story artifacts, formal qualitative user research studies, LMS/alumni portal ownership, enterprise KM taxonomy, GenAI/LLM coding, or external tool integrations are fabricated in the CV or dossier. | **PASS** |
| **Prohibited Technical & Domain Claims (`AGENTS.md:L39`)** | Zero mentions of connector APIs, OAuth, RBAC, RAG pipelines, vector databases, commercial analytics tools (`Amplitude`, `Mixpanel`, `GA4`, `Firebase`, `Optimizely`), RCS marketing, ML decisioning models, ROAS/incrementality, loyalty, merchandising, or DAM ownership. | **PASS** |
| **Tenure Arithmetic in Dossier** | `8+ years` EdTech (`dossier.md:L79`: Jun 2015–Apr 2023 + Oct 2023–Nov 2024 learning clients = ~8 yrs 11 mos) and `~6 years formal PM/SPM, ~11 years total` (`dossier.md:L59`) are mathematically consistent with `canonical_master_profile.md` `v1.1.0`. | **PASS** |
| **Gate 7 Confidentiality** | Only public-safe employer/client names, product names, and metrics approved in `canonical_master_profile.md` `v1.1.0` appear across all files. | **PASS** |
