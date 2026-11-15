# Fact-Check & Integrity Audit Report (Gates 6 & 7)

- **Opportunity ID:** `4455922216-amazon-spm-now-payments`
- **Target Company & Role:** Amazon — Senior Product Manager, Amazon Now (Payments Experience)
- **Canonical Master Profile Baseline:** `/Users/mineshwadhwa/Documents/Sherpa/canonical_master_profile.md` (`v1.1.0`)
- **Guardrails Baseline:** `/Users/mineshwadhwa/Documents/Sherpa/AGENTS.md`
- **Audited Artifacts:**
  - `cv_tailored.json` (`tailored-amazon-spm-now-payments-v1.0`)
  - `cv_tailored.md`
  - `cv_changelog.md`
  - `requirement_matrix.json`
  - `dossier.md` (with cross-check against `fit_assessment.json`)
- **Reviewer Role:** Independent Fact-Check & Integrity Reviewer (Agent 9)
- **Audit Date:** `2026-11-15`

---

## Overall Verdict

| Gate | Scope | Verdict | Summary |
| :--- | :--- | :--- | :--- |
| **Gate 6** | CV & Artifact Claim Audit (Facts, Metrics, Dates, Titles, Ownership, Guardrails) | **`FAIL`** | **1 factual tenure error** in `dossier.md` (`~6 years` vs. actual `5 years, 1 month` / `~5 years` in formal PM/Senior PM titles at Lowe's India and Byju's) and **2 precision/guardrail defects** in `cv_tailored.json` / `cv_tailored.md` (unqualified `+35% conversion lift` in Profile Summary; unvalidated `audience segments` phrasing under Upraised). All metrics, dates, titles, employers, education, certifications, roadmap targets, and `"agentic workflows"` usage are otherwise verified. |
| **Gate 7** | Confidentiality & Disclosure Review | **`PASS`** | Zero exposure of confidential employer/client internals, proprietary architectures, customer data, or unapproved disclosures beyond `canonical_master_profile.md` (`v1.1.0`). |

**Combined Gate 6 & Gate 7 Verdict: `FAIL`** (requires exact fixes listed below before final approval / PDF re-render).

---

## Defects Found & Exact Fixes Required

### Defect 1 — Factual Tenure Overstatement (`dossier.md`, Critical)
- **Location:**
  - `dossier.md:L70` (`~6 years in formal PM/Senior PM titles at Lowe's India and Byju's`)
  - `dossier.md:L75` (`~6 years PM/Senior PM`)
  - *(Mirrored in `fit_assessment.json:L36, L59, L66`)*
- **Issue:** Summing formal PM/Senior PM tenure from `canonical_master_profile.md`:
  - Byju's (`July 2020 – April 2023`, spanning Product Manager and Senior Product Manager): **2 years, 10 months** (34 months inclusive; 33 months exclusive).
  - Lowe's India (`Sep 2024 – Present`, as of `2026-11-15`): **2 years, 3 months** (27 months inclusive; 26 months exclusive).
  - **Actual combined tenure:** **5 years, 1 month** (61 months inclusive; 4 years, 11 months / 59 months exclusive), i.e., **`~5 years`** (`5+ years`), not `~6 years`. Overstating formal PM/Senior PM tenure by ~11 months violates `AGENTS.md` Section 1 (Locked Facts).
- **Exact Fix Required:**
  - Update `dossier.md:L70` from `(~6 years in formal PM/Senior PM titles at Lowe's India and Byju's)` to `(~5 years in formal PM/Senior PM titles at Lowe's India and Byju's)`.
  - Update `dossier.md:L75` from `(~6 years PM/Senior PM)` to `(~5 years PM/Senior PM)`.
  - Update corresponding references in `fit_assessment.json:L36, L59, L66` from `~6 years` to `~5 years`.

### Defect 2 — Ambiguous Conversion Metric Qualifier (`cv_tailored.json` & `cv_tailored.md`, Moderate)
- **Location:**
  - `cv_tailored.json:L13` (`Profile Summary`)
  - `cv_tailored.md:L5` (`Profile Summary`)
  - `cv_changelog.md:L30`
- **Issue:** Reads `removing customer-funnel friction (+35% conversion lift)`. Per `canonical_master_profile.md:L237, L387, L507`, the measured outcome at Byju's is specifically **lead conversion** (`35% improvement in lead conversion`). Because the target JD is **Amazon Now (Payments Experience)** focused on checkout conversion, omitting `lead` in the Profile Summary risks misinterpreting a lead-funnel metric as checkout/e-commerce conversion (`AGENTS.md` Section 2 — Adjacent experience must not be disguised as identical).
- **Exact Fix Required:**
  - Replace `removing customer-funnel friction (+35% conversion lift)` with `removing customer-funnel friction (+35% lead conversion lift)` in `cv_tailored.json:L13`, `cv_tailored.md:L5`, and `cv_changelog.md:L30` (and re-render the tailored PDF CV).

### Defect 3 — Unvalidated `audience segments` Phrasing (`cv_tailored.json` & `cv_tailored.md`, Moderate)
- **Location:**
  - `cv_tailored.json:L59` (`Hype Marketing & Product Services` — `Upraised`)
  - `cv_tailored.md:L26` (`Upraised`)
- **Issue:** Reads `Upraised: Crafted social content and GTM strategy for new offerings by aligning messaging to audience segments, increasing engagement by 50% and website traffic by 30%`. `canonical_master_profile.md:L141-145, L373` does not attribute `audience segments` work to Upraised, and `canonical_master_profile.md:L418, L433, L649` explicitly flags `Audience Segmentation` as an unvalidated target-JD term (`specific production audience-segmentation ownership should be validated`). Additionally, `cv_changelog.md:L84` does not document introducing `audience segments`.
- **Exact Fix Required:**
  - Replace `by aligning messaging to audience segments` with canonical phrasing supported at `canonical_master_profile.md:L141-145, L373`, e.g.:
    `Upraised: Crafted social content and GTM strategy for new offerings by translating business goals into campaign and content roadmaps, increasing engagement by 50% and website traffic by 30%`
  - Update `cv_tailored.json:L59`, `cv_tailored.md:L26`, and document the exact text in `cv_changelog.md:L84` (and re-render the tailored PDF CV).

---

## Claim-by-Claim Verification Table

### A. Locked Profile Facts (`cv_tailored.json` & `cv_tailored.md`)

| Section / Item | Audited Text | Canonical Profile Reference (`v1.1.0`) | Status | Notes |
| :--- | :--- | :--- | :--- | :--- |
| Metadata | `profile_version: 1.1.0`, `Amazon`, `Senior Product Manager, Amazon Now (Payments Experience)` | `L4` (`Version: 1.1.0`), `jd_full.md:L6-7` | `PASS` | Exact match. |
| Header & Contact | `Minesh Wadhwa`, `Bangalore • w.minesh@gmail.com • +91 9035 199 024` | `L1, L9-11` | `PASS` | Exact match to `cv_base_schema.json`. |
| Lowe's India — Header | `Lowe’s India`, `Bangalore, Karnataka`, `Senior Product Manager`, `Sep 2024 – Present` | `L48-50`, `AGENTS.md:L17` | `PASS` | Exact canonical employer, location, title, dates. |
| Hype — Header | `Hype Marketing & Product Services`, `Bangalore, Karnataka`, `Founder`, `Oct 2023 – Nov 2024` | `L119-121`, `AGENTS.md:L18` | `PASS` | Exact canonical employer, location, title, dates. |
| HealthQ Rehab — Header | `HealthQ Rehab`, `Bangalore, Karnataka`, `Head of Marketing`, `May 2023 – Dec 2023` | `L179-181`, `AGENTS.md:L19` | `PASS` | Exact canonical employer, location, title, dates. |
| Byju's — Senior PM Header | `Byju’s - Product Development`, `Bangalore, Karnataka`, `Senior Product Manager`, `July 2020 – April 2023` | `L212-219`, `AGENTS.md:L20` | `PASS` | Uses canonical CV display period per `L219`. |
| Byju's — Multiple Roles Header | `Multiple Roles`, `Jun 2015 – June 2020` | `L286-287`, `AGENTS.md:L20` | `PASS` | Exact canonical title and dates. |
| Certifications | `University of California, Irvine`, `Oct 2020 – Dec 2020` (3 topics) | `L333-343`, `AGENTS.md:L21` | `PASS` | Exact match. |
| Social Entrepreneurship | *The Open Door Foundation* (RTC Girls Home, Bangalore); *Education for All* (10M kids by 2025) | `L348-349`, `AGENTS.md:L22` | `PASS` | Exact match. |
| Education — MIT | `Manipal Institute of Technology`, `Manipal, Karnataka`, `B. Tech. in Computer Science Engineering`, `2011 – 2015` | `L325-327`, `AGENTS.md:L23` | `PASS` | Exact match (`cv_base_schema.json:L129-133`). |
| Education — IIMB | `Indian Institute Of Management - Bangalore`, `Executive General Management Program`, `2025 – 2026 (ongoing)` | `L321-323`, `AGENTS.md:L23` | `PASS` | Exact match (`cv_base_schema.json:L135-139`). |

### B. CV Claims, Metrics, Ownership & Guardrails (`cv_tailored.json` & `cv_tailored.md`)

| Claim Location | Audited Claim / Metric | Canonical Reference (`v1.1.0`) | Outcome Type | Status | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Profile Summary (`L13`) | `9+ years of experience owning end-to-end technology product delivery, roadmap strategy, and product tradeoffs` | `L48-100, L119-160, L217-315, L343, L462, L491` | Tenure / Capability | `PASS` | Total career Jun 2015–Nov 2026 is 11+ yrs (~10+ yrs in product/tech/consulting); `9+ years` is conservative and accurate. |
| Profile Summary (`L13`) | `99.99% platform reliability`, `~$10M annual revenue protection`, `automated recovery workflows` | `L76, L85-89, L500-501, L525` | Delivered | `PASS` | Delivered outcomes accurately stated. |
| Profile Summary (`L13`) | `removing customer-funnel friction (+35% conversion lift)` | `L237, L387, L507` | Measured | **`FAIL` (Precision)** | Canonical metric is `lead conversion` (`35%`). Must specify `+35% lead conversion lift` to avoid conflating with checkout conversion. |
| Profile Summary (`L13`) | `KPI frameworks, internal enterprise analytics, AI-enabled agentic workflows, data-driven VP/CXO stakeholder alignment` | `L67, L77, L96-99, L465-466, L478, L660, L663` | Capability | `PASS` | Respects internal analytics guardrail; `agentic workflows` complies with `AGENTS.md`. |
| Lowe's Reliability B1 | `Led revenue-protection initiatives... automated recovery systems and incident-handling workflows... saving ~$10M annually` | `L84-90, L501, L525-526` | Delivered | `PASS` | Exact ownership (`Led`), mechanism, and delivered savings (`~$10M`). |
| Lowe's Reliability B2 | `Owned end-to-end enterprise technology platform initiatives... SLA workflows, maintaining 99.99% reliability` | `L65, L68-70, L76, L500, L527` | Delivered | `PASS` | Accurate ownership (`Owned`) and delivered reliability (`99.99%`). |
| Lowe's Reliability B3 | `Defined annual and quarterly product roadmaps and tradeoffs... VP/CXO stakeholders via monthly business reviews, targeting 20% incident volume reduction` | `L66, L82, L478, L480` | **Roadmap Target** | `PASS` | Correctly preserves `targeting 20% incident volume reduction` as a roadmap target, not a delivered result. |
| Lowe's Reliability B4 | `Designed KPI frameworks and dashboards using internal enterprise analytics tools tracking incident resolution, cost savings, and adoption to guide C-suite decision support` | `L67, L77-81, L484, L660, L663` | Capability | `PASS` | Explicitly cites `internal enterprise analytics tools`; zero prohibited commercial analytics claims (`Amplitude`, `Mixpanel`, `GA4`, `Firebase`, `Optimizely`). |
| Lowe's Reliability B5 | `Coordinated finance, operations, and IT stakeholders across procurement and operational planning... without formal authority` | `L71, L485-487` | Influence | `PASS` | Explicitly preserves `without formal authority`. |
| Lowe's Infra & Ops B1 | `Designed and launched an AI-driven procurement and catalog platform orchestrating automated agentic workflows for store setup teams, reducing operational cycle times by 20%` | `L96-99, L503` | Delivered | `PASS` | `20%` delivered outcome verified; `agentic workflows` meaningfully describes genuine AI-driven procurement/catalog work per `AGENTS.md`. |
| Lowe's Infra & Ops B2 | `Spearheaded a unified enterprise asset lifecycle platform... delivering ~$2M in annual cost savings` | `L91-94, L502` | Delivered | `PASS` | `~$2M` delivered outcome verified. |
| Hype B1 & B2 | GTM, product marketing, execution roadmaps; data-driven customer journey & engagement workflows across email, social, content | `L132-137, L163-165, L373, L377, L422` | Capability | `PASS` | Supported by `canonical_master_profile.md`. |
| Hype — Upraised | `by aligning messaging to audience segments, increasing engagement by 50% and website traffic by 30%` | `L141-145, L373, L418, L433, L649` | Measured | **`FAIL` (Precision)** | Metrics (`50%`, `30%`) are accurate, but `audience segments` is not evidenced for Upraised and touches unvalidated `Audience Segmentation`. |
| Hype — Programming Hub | `courses + content... achieving 4.5+ ratings and strong user adoption` | `L147-150`, `cv_base_schema.json:L61` | Measured | `PASS` | Verified. |
| Hype — Gradiant | `lifecycle and email marketing workflows... 30% open rates and 20% CTRs` | `L152-156, L374` | Measured | `PASS` | Verified. |
| Hype — Acadecraft | `structured learning programs... over 80% completion rates` | `L158-160, L376` | Measured | `PASS` | Verified. |
| HealthQ B1–B3 | `35% growth in organic traffic`; `social media engagement by 50%`; `WhatsApp, Telegram, and newsletter... overall brand engagement by 20%` | `L184-197, L380-382` | Measured | `PASS` | All three metrics and channels verified. |
| Byju's SPM B1 | `Byju’s Xcel Masterclasses... generating over 2.5L sales-qualified leads` | `L235-236, L386` | Measured | `PASS` | Verified. |
| Byju's SPM B2 | `Eliminated customer-funnel friction... lifting lead conversion rates by 35%` | `L237, L387` | Measured | `PASS` | Verified. |
| Byju's SPM B3 | `Developed 12 cross-product experience prototypes across Aakash-Byjus, Tynker, and Whitehat Jr.` | `L238, L388` | Delivered | `PASS` | Verified. |
| Byju's SPM B4 | `Launched Interactive Learning Experiences feature for Whitehat Jr.... reducing instructor training time by 15%` | `L261-263, L390` | Measured | `PASS` | Verified. |
| Byju's SPM B5 | `app redesign and product experimentation for Tynker... increasing course completion by 5%` | `L265-268, L389` | Measured | `PASS` | Verified. |
| Byju's Multiple Roles B1 | `Prototyped and developed interactive learning experiences for science and mathematics and the Social Studies product` | `L304-305` | Delivered | `PASS` | Correctly avoids pulling 2020–2022 launch volume metrics (`500+ hrs`, `300+ experiences`) into 2015–2020. |
| Byju's Multiple Roles B2 | `Led a team of 5 product leads for Commerce product development and created UX interactions for the Elevate internal tracking platform` | `L306-307`, `AGENTS.md:L14` | Leadership / Delivered | `PASS` | People management of 5 product leads explicitly verified (`L307`, `AGENTS.md:L14`). |

### C. Supporting Audit of `requirement_matrix.json`, `cv_changelog.md`, and `dossier.md`

| Artifact | Audited Scope | Status | Notes |
| :--- | :--- | :--- | :--- |
| `requirement_matrix.json` | 16 JD requirements (`10 Direct`, `2 Adjacent`, `4 Gap`), line citations, gap boundaries (`DM-1`, `DM-3`, `DM-5`, `IM-1`), internal analytics guardrail (`IM-2`) | `PASS` | All counts, classifications, line numbers, and prohibited-claim boundaries match `canonical_master_profile.md` `v1.1.0`. |
| `cv_changelog.md` | Baseline-to-tailored diff tracking & citations | **`FAIL` (Minor Sync)** | Must be updated in sync after fixing Defect 2 (`+35% lead conversion lift`) and Defect 3 (`Upraised` wording) in `cv_tailored.json`. |
| `dossier.md` | Section 1–8 facts, metrics, requirement table, fit score (`77/100`), gaps & bridges | **`FAIL` (Defect 1)** | Lines `70` and `75` state `~6 years` in formal PM/Senior PM titles at Lowe's India and Byju's; actual duration is **5 years, 1 month (`~5 years`)**. All other metrics, citations, and gap disclosures pass. |
| Prohibited Tech & Domain Check | Payments instruments (UPI/cards/wallets/COD/pay-later), quick-commerce, fraud mitigation, multi-country launches, commercial analytics tools (`Amplitude`, `Mixpanel`, `GA4`, `Firebase`, `Optimizely`), OAuth/RBAC/RAG/vector DBs | `PASS` | None fabricated or claimed across any audited file. |
| Gate 7 Confidentiality | Employer/client/customer/internal architecture secrecy | `PASS` | All descriptions remain strictly within approved public-safe wording in `canonical_master_profile.md` (`v1.1.0`). |

---

## Summary of Required Actions Before Gate 6/7 Sign-Off

1. Fix `dossier.md` (`L70`, `L75`) and `fit_assessment.json` (`L36`, `L59`, `L66`) to state `~5 years` (not `~6 years`) in formal PM/Senior PM titles at Lowe's India and Byju's.
2. Fix `cv_tailored.json` (`L13`), `cv_tailored.md` (`L5`), and `cv_changelog.md` (`L30`) to specify `(+35% lead conversion lift)` in the Profile Summary.
3. Fix `cv_tailored.json` (`L59`), `cv_tailored.md` (`L26`), and `cv_changelog.md` (`L84`) to replace `by aligning messaging to audience segments` under Upraised with canonical wording (`by translating business goals into campaign and content roadmaps`).
4. Re-render `Minesh_Wadhwa_CV_Amazon_Now_Payments.pdf` after CV edits and re-verify Gate 6.
