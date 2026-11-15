# Independent Fact-Check & Integrity Audit Report — Angel One (`4488924130-angel-one-spm`)

- **Opportunity ID:** `4488924130-angel-one-spm`
- **Target Company / Role:** Angel One — Senior Product Manager
- **Audit Scope:** `cv_tailored.json`, `cv_tailored.md`, `cv_changelog.md`, `requirement_matrix.json`, `dossier.md` (and cross-check of `fit_assessment.json`)
- **Authoritative Baselines:** [canonical_master_profile.md](file:///Users/mineshwadhwa/Documents/Sherpa/canonical_master_profile.md) (`v1.1.0`) and [AGENTS.md](file:///Users/mineshwadhwa/Documents/Sherpa/AGENTS.md)
- **Reviewer Role:** Independent Fact-Check & Integrity Reviewer (Agent 9)
- **Audit Date:** `2026-11-15`

---

## Overall Verdict

| Gate | Review Scope | Verdict |
| :--- | :--- | :--- |
| **Gate 6** | CV Claim Audit & Canonical Profile Integrity | **`FAIL`** |
| **Gate 7** | Confidentiality & Disclosure Review | **`PASS`** |
| **Overall** | **Combined Fact-Check & Integrity Verdict** | **`FAIL`** |

**Summary of Audit Outcome:**  
While locked identity fields, employers, dates, education, certifications, social entrepreneurship, core numerical metrics (`99.99%`, `~$10M`, `$2M`, `20%`, `50%`, `30%`, `4.5+`, `20% CTR`, `80%+`, `35%`, `2.5L+`, `15%`, `5%`), roadmap-target qualifiers (`targeting a 20% reduction in incident volume`), and confidentiality boundaries (Gate 7) are properly preserved, **Gate 6 FAILS** due to a **metric/role-period misattribution in Byju’s `Multiple Roles (Jun 2015 – June 2020)`**, **unsupported `"onboarding"` claims inserted across three CV sections**, and **several ownership/terminology overstatements** relative to `canonical_master_profile.md` (`v1.1.0`) and `AGENTS.md`.

---

## Critical & Material Defects Requiring Correction (Gate 6)

### 1. [CRITICAL] Metric & Launch Misattribution in Byju’s `Multiple Roles (Jun 2015 – June 2020)`
- **Affected Files:**
  - `cv_tailored.json` (`L106–L107`)
  - `cv_tailored.md` (`L48–L49`)
  - `cv_changelog.md` (`L47`)
- **Current Text:**
  - Bullet 1: `"Prototyped and built 300+ *interactive learning experiences* for science/maths and created UX interactions for the *Elevate* internal platform"`
  - Bullet 2: `"Prototyped and launched the *Social Studies* product (500+ hrs video) and led 5 product leads for *BTLA Commerce* development"`
- **Canonical Evidence (`canonical_master_profile.md`):**
  - Under **Product Manager (`July 2020 – Feb 2022`) → Social Studies Product** (`L270–L274`):
    - `Launched Social Studies product`
    - `Built: 500+ hours of video content` and `300+ interactive learning experiences`
  - Under **Multiple Roles (`June 2015 – June 2020`) → Key Achievements** (`L304–L307`):
    - `Developed interactive learning experiences for science and mathematics` *(no `300+` metric)*
    - `Prototyped and developed Social Studies product` *(not launched yet in this period)*
    - `Created UX interactions for Elevate internal tracking platform`
    - `Led team of 5 product leads for Commerce product development`
- **Defect:**
  1. Assigns the `300+` metric (which belongs to `Social Studies Product` in `July 2020 – Feb 2022`) to `science/maths` interactive learning experiences under `Multiple Roles (Jun 2015 – June 2020)`.
  2. Shifts the `Social Studies` product launch and `500+ hrs video` metric (from `Product Manager`, `July 2020 – Feb 2022`) back into `Multiple Roles (Jun 2015 – June 2020)`.
- **Exact Fix Required:**
  - Under `Byju’s — Multiple Roles (Jun 2015 – June 2020)`:
    - Bullet 1: `"Developed interactive learning experiences for science and mathematics and created UX interactions for the *Elevate* internal tracking platform"` *(remove `300+`)*
    - Bullet 2: `"Prototyped and developed the *Social Studies* product and led a team of 5 product leads for *BTLA Commerce* product development"` *(remove `launched` and `500+ hrs video` from 2015–2020)*
  - If retaining `500+ hrs video` and `300+ interactive learning experiences`, add a bullet under `Byju’s — Senior Product Manager (July 2020 – April 2023)` (whose canonical CV display period spans `PM [July 2020 – Feb 2022]` and `SPM [March 2022 – April 2023]` per `L219`, and add `BTLA Social Studies` to `products_line`):
    - `"Launched the *Social Studies* product, building 500+ hours of video content and 300+ interactive learning experiences"`

---

### 2. [MAJOR] Unsupported `"onboarding"` Claims Inserted to Mirror JD Terminology
- **Affected Files:**
  - `cv_tailored.json`: `profile_summary` (`L13`), `Lowe’s India — Infrastructure and Operations BU` Bullet 2 (`L38`), `Byju’s — Senior Product Manager` Bullet 2 (`L95`)
  - `cv_tailored.md` (`L5`, `L20`, `L42`)
  - `cv_changelog.md` (`L29`, `L37`, `L43`)
  - *(Also echoed in `fit_assessment.json` `L24`, `L66`, `L70`)*
- **Current Text:**
  - `profile_summary`: `"owning product roadmaps, KPI frameworks, onboarding and conversion funnels, and complex internal systems"`
  - `Lowe’s Infra & Ops Bullet 2`: `"streamline store setup onboarding, reducing operational cycle times by 20%"`
  - `Byju’s SPM Bullet 2`: `"remove funnel friction across onboarding and engagement flows, improving lead conversion by 35%"`
- **Canonical Evidence (`canonical_master_profile.md`):**
  - The term **`onboarding` does not appear anywhere** in `canonical_master_profile.md` (`v1.1.0`).
  - Lowe’s procurement/catalog system (`L97–L99`) states: `"Improved operational efficiency for store setup teams"` (not `"store setup onboarding"`).
  - Byju’s Xcel Masterclasses (`L235–L237`, `L386–L387`) generated `2.5L+ sales-qualified leads` and optimized `"customer journeys and engagement workflows by identifying friction points across the product funnel"`, improving `"lead conversion by 35%"` — top-of-funnel lead conversion, not documented user onboarding flows.
- **Exact Fix Required:**
  - `profile_summary`: Replace `"onboarding and conversion funnels"` with `"acquisition and conversion funnels"` (or `"customer journeys and conversion funnels"`).
  - `Lowe’s Infra & Ops Bullet 2`: Replace `"streamline store setup onboarding"` with `"streamline procurement workflows for store setup teams"` (or `"improve operational efficiency for store setup teams"`).
  - `Byju’s SPM Bullet 2`: Replace `"across onboarding and engagement flows"` with `"across customer journeys and engagement workflows"` (or `"across the product funnel and engagement flows"`).
  - Update `cv_changelog.md` (and `fit_assessment.json` if regenerated) accordingly.

---

### 3. [MODERATE] Authority Upgrade in Lowe’s `Reliability Engineering` Bullet 5
- **Affected Files:** `cv_tailored.json` (`L30`), `cv_tailored.md` (`L16`), `cv_changelog.md` (`L34`)
- **Current Text:** `"Aligned engineering, product, finance, and operations verticals on core org KPIs by leading VP/CXO monthly business reviews and governance cadences"`
- **Canonical Evidence (`canonical_master_profile.md`):**
  - `L478`: `"Presented monthly business reviews and executive updates to VP/CXO stakeholders"`
  - `L481`: `"Architected operating rhythms, governance systems, and review cadences"`
  - `L485`: `"Coordinated enterprise initiatives across product, engineering, finance, and operations teams"`
- **Defect:** `"leading VP/CXO monthly business reviews"` upgrades `"Presented ... to VP/CXO stakeholders"` into leading/chairing VP/CXO reviews (`AGENTS.md` Section 1: *Never upgrade participation into ownership, influence into formal authority*). In addition, `"core org KPIs"` mirrors JD wording rather than Lowe’s operational/reliability KPIs.
- **Exact Fix Required:**
  - Revise to: `"Aligned engineering, product, finance, and operations teams on shared operational KPIs by presenting VP/CXO monthly business reviews and driving governance cadences"`

---

### 4. [MODERATE] `"agents"` / `"agentic workflows"` Overextension & Precision Issues
- **Affected Files:** `cv_tailored.json` (`L13`, `L29`, `L38`), `cv_tailored.md` (`L5`, `L15`, `L20`), `cv_changelog.md` (`L29`, `L33`, `L37`), `dossier.md` (`L43`)
- **Current Text:**
  - `Lowe’s Reliability Bullet 4` (`L29`): `"by deploying automated recovery agents and incident-handling workflows"`
  - `Lowe’s Infra & Ops Bullet 2` (`L38`): `"AI-driven procurement and catalog platform powered by agentic workflows"`
  - `profile_summary` (`L13`): `"ship AI-enabled agentic workflows and product experiments"`
- **Canonical Evidence & Guardrail (`AGENTS.md:L35–L37`, `canonical_master_profile.md:L87, L97`):**
  - `AGENTS.md` permits `"agents"` / `"agentic workflows"` **for closely aligned roles (e.g., Enterprise Platform / AI Product Manager / Workflow Automation roles)** where it meaningfully describes genuine work (AI-driven procurement/catalog workflows, automated recovery workflows at Lowe’s India).
  - Angel One Senior PM is a **B2C Fintech Consumer Super App** role (onboarding/investing/personalization), not an Enterprise Platform / AI PM / Workflow Automation role, and the JD does not reference agents. Furthermore, `canonical_master_profile.md:L87` calls the ~$10M recovery work `"Automated recovery systems"` (not AI-driven), so `"deploying automated recovery agents"` risks implying autonomous AI agent architectures not confirmed in the profile.
- **Exact Fix Required:**
  - Change `"deploying automated recovery agents and incident-handling workflows"` to `"deploying automated recovery workflows and incident-handling systems"` (and align `dossier.md:L43`).
  - For a B2C Fintech role, prefer `"AI-driven procurement and catalog workflows"` / `"AI-enabled workflows"` over `"agentic workflows"` unless the user explicitly chooses to retain `"agentic workflows"` for the AI-driven procurement system (`L97`).

---

### 5. [MINOR] Missing Qualifier / Unsupported Generalizations
1. **`Byju’s — Senior Product Manager` Bullet 4** (`cv_tailored.json:L97`, `cv_tailored.md:L44`):
   - Current: `"cutting training time by 15%"`
   - Canonical (`L263`, `L390`): `"Reduced instructor training time by 15%"`
   - **Fix:** Restore `"instructor"`: `"cutting instructor training time by 15%"`.
2. **`Hype Marketing & Product Services` (`B2C` generalization & minor phrasing)** (`cv_tailored.json:L53, L61, L63`, `cv_tailored.md:L24, L28, L30`):
   - Current: `"Defined B2C growth, GTM, and lifecycle strategies for clients"` (`L53`), `"Developed and marketed B2C digital learning products by optimizing positioning and discovery"` (`L61`), `"aligned to learner milestones"` (`L63`).
   - Canonical (`L132`, `L148`, `L375`, `L376`): `"Defined GTM, growth, and marketing strategies for clients"`, `"Combined product positioning, content strategy, and digital marketing execution to launch and market Programming Hub's learning products"`, `"by aligning learning experiences to user needs and engagement objectives"`. `"B2C"` is not stated for Hype clients in `canonical_master_profile.md` (and clients like Acadecraft/Gradiant are not verified as B2C there), nor is `"discovery"` or `"learner milestones"`.
   - **Fix:** Change `L53` to `"Defined growth, GTM, and lifecycle strategies for clients"`, `L61` to `"Developed and marketed digital learning products by optimizing positioning and content strategy"`, and `L63` to `"aligned to learner needs and engagement objectives"`.

---

## Claim-by-Claim Verification Table

| Artifact & Location | Audited Claim / Field | Canonical Master Profile Reference (`v1.1.0`) | Gate 6 Status | Notes / Required Action |
| :--- | :--- | :--- | :--- | :--- |
| `cv_tailored.json:L8–12` | Header: Minesh Wadhwa, Bangalore, `w.minesh@gmail.com`, `+91 9035 199 024` | `L8–11` | **PASS** | Matches baseline header identically. |
| `cv_tailored.json:L13` | `11+ years of experience (B.Tech. CS)`, `Byju’s` & `Lowe’s India`, `2.5L+ SQLs, 35% higher conversion, 99.99% reliability, ~$10M revenue protection, $2M cost savings, and 20% faster cycle times` | `L48–100`, `L217–239`, `L286–288`, `L325–328`, `L499–512` | **PASS** (Metrics/Tenure) | June 2015–Nov 2026 = 11+ yrs; metrics exact. |
| `cv_tailored.json:L13` | `"onboarding and conversion funnels"`, `"AI-enabled agentic workflows"` | Not in `canonical_master_profile.md` (`onboarding` absent); `AGENTS.md:L35–37` | **FAIL** | Remove `"onboarding"`; replace `"AI-enabled agentic workflows"` with `"AI-enabled workflows"`. |
| `cv_tailored.json:L16–21` | `Lowe’s India`, `Bangalore, Karnataka`, `Senior Product Manager`, `Sep 2024 – Present` | `L48–50`, `AGENTS.md:L17` | **PASS** | Exact locked fields. |
| `cv_tailored.json:L26` | Lowe’s Reliability B1: Cross-functional platform strategy via automated workflows; `99.99%` reliability | `L65`, `L70`, `L76` | **PASS** | Delivered outcome exact. |
| `cv_tailored.json:L27` | Lowe’s Reliability B2: KPI frameworks & dashboards using internal enterprise analytics tools | `L6`, `L67`, `L77–81`, `L660–663` | **PASS** | Properly cites internal enterprise analytics tools; avoids commercial tools. |
| `cv_tailored.json:L28` | Lowe’s Reliability B3: Annual & quarterly roadmaps `"targeting a 20% reduction in incident volume"` | `L66`, `L82`, `AGENTS.md:L15` | **PASS** | Roadmap target distinction preserved (`targeting`). |
| `cv_tailored.json:L29` | Lowe’s Reliability B4: Revenue protection across order systems; `"automated recovery agents"`; cutting cancellations; saving `~$10M` annually | `L70`, `L85–90`, `AGENTS.md:L35–37` | **FAIL** | Metric (`~$10M`) exact, but `"Automated recovery systems"` (`L87`) should not be overstated as `"automated recovery agents"` for a B2C fintech role. |
| `cv_tailored.json:L30` | Lowe’s Reliability B5: Aligned engineering, product, finance, operations `"on core org KPIs by leading VP/CXO monthly business reviews"` | `L71`, `L478`, `L481`, `L485` | **FAIL** | Canonical `L478` says `"Presented ... to VP/CXO stakeholders"`, not `"leading VP/CXO monthly business reviews"`. |
| `cv_tailored.json:L31` | Lowe’s Reliability B6: Diagnosed bottlenecks across internal procurement, asset, and operational planning systems | `L69–71`, `L91–99`, `L560–561` | **PASS** | Supported. |
| `cv_tailored.json:L37` | Lowe’s Infra & Ops B1: Unified enterprise asset lifecycle platform with finance & operations; `$2M` annual cost savings | `L92–95`, `L502`, `AGENTS.md:L15` | **PASS** | Metric & ownership match `AGENTS.md` and `L92–95`. |
| `cv_tailored.json:L38` | Lowe’s Infra & Ops B2: AI-driven procurement & catalog platform `"powered by agentic workflows"` to `"streamline store setup onboarding"`, `-20%` cycle times | `L97–99` | **FAIL** | `20%` cycle time reduction exact; `"store setup onboarding"` is unsupported (`L99` says `"store setup teams"`). Soften `"agentic workflows"` for non-AI-platform role. |
| `cv_tailored.json:L46–51` | `Hype Marketing & Product Services`, `Bangalore, Karnataka`, `Founder`, `Oct 2023 – Nov 2024` | `L119–121`, `AGENTS.md:L18` | **PASS** | Exact locked fields. |
| `cv_tailored.json:L53–54` | Hype B1–B2: `"B2C growth, GTM, and lifecycle strategies"`, data-driven engagement funnels & customer journey workflows | `L132–137`, `L373`, `L377` | **FAIL (Minor)** | Remove unverified `"B2C"` label across all Hype clients. |
| `cv_tailored.json:L60` | Upraised: `50%` engagement increase, `30%` website traffic increase | `L141–145`, `L373` | **PASS** | Exact metrics & work. |
| `cv_tailored.json:L61` | Programming Hub: `"B2C"` digital learning products, `"positioning and discovery"`, `4.5+` ratings | `L147–150`, `L375` | **FAIL (Minor)** | `4.5+` ratings exact; replace `"B2C"` and `"discovery"` with canonical `"digital learning products"` and `"positioning and content strategy"`. |
| `cv_tailored.json:L62` | Gradiant: Lifecycle & email marketing journeys, `30%` open rates, `20%` CTRs | `L152–156`, `L374` | **PASS** | Exact metrics & work. |
| `cv_tailored.json:L63` | Acadecraft: Structured learning programs `"aligned to learner milestones"`, `80%+` completion rates | `L158–160`, `L376` | **FAIL (Minor)** | `80%+` metric exact; replace `"learner milestones"` with `"learner needs and engagement objectives"`. |
| `cv_tailored.json:L71–81` | `HealthQ Rehab`, `Bangalore, Karnataka`, `Head of Marketing`, `May 2023 – Dec 2023`; `35%` organic traffic, `50%` social engagement, WhatsApp/Telegram/newsletter `20%` brand engagement | `L179–197`, `L379–383`, `AGENTS.md:L19` | **PASS** | Dates, title, and all 3 metrics match verbatim. |
| `cv_tailored.json:L86–92` | `Byju’s - Product Development`, `Bangalore, Karnataka`, `Senior Product Manager`, `July 2020 – April 2023`, products line | `L212–225`, `AGENTS.md:L20` | **PASS** | Exact locked fields & canonical display period. |
| `cv_tailored.json:L94` | Byju’s SPM B1: *Byju’s Xcel Masterclasses* consumer product strategy, `2.5L`+ sales-qualified leads | `L228`, `L235–236`, `L386` | **PASS** | Exact metric & ownership. |
| `cv_tailored.json:L95` | Byju’s SPM B2: Removed funnel friction `"across onboarding and engagement flows"`, `+35%` lead conversion | `L230`, `L237`, `L387` | **FAIL** | `+35%` metric exact, but `"onboarding"` is not in canonical profile (`L387` says `"customer journeys and engagement workflows"`). |
| `cv_tailored.json:L96` | Byju’s SPM B3: `12` cross-product experience prototypes across *Aakash-Byjus*, *Tynker*, *Whitehat Jr.* | `L238`, `L388` | **PASS** | Exact count & products. |
| `cv_tailored.json:L97` | Byju’s SPM B4: *Interactive Learning Experiences* for *Whitehat Jr.*, `"cutting training time by 15%"` | `L262–263`, `L390` | **FAIL (Minor)** | `15%` metric exact, but omits `"instructor"` before `"training time"`. |
| `cv_tailored.json:L98` | Byju’s SPM B5: App redesign for *Tynker* with assessments & DIY modules, `+5%` course completion | `L266–268`, `L389` | **PASS** | Exact metric & work. |
| `cv_tailored.json:L102–107` | `Multiple Roles`, `Jun 2015 – June 2020`; B1: `300+` interactive learning experiences for science/maths + Elevate UX; B2: launched *Social Studies* (`500+ hrs video`) + led `5` product leads for *BTLA Commerce* | `L270–274`, `L286–307`, `AGENTS.md:L14, L20` | **FAIL (CRITICAL)** | Dates/title/5-lead team exact, but `300+` belongs to *Social Studies* (`2020–2022`), NOT science/maths (`2015–2020`); *Social Studies* launch & `500+ hrs video` also occurred in `2020–2022`, not `2015–2020`. |
| `cv_tailored.json:L113–123` | `University of California, Irvine`, `Oct 2020 – Dec 2020`, 3 project management bullets | `L333–343`, `AGENTS.md:L21` | **PASS** | Exact locked fields & baseline bullets. |
| `cv_tailored.json:L124–127` | Social Entrepreneurship: *The Open Door Foundation* (RTC Girls Home, Bangalore) & *Education for All* (10M kids by 2025) | `L348–349`, `AGENTS.md:L22` | **PASS** | Exact locked text. |
| `cv_tailored.json:L128–141` | Education: `Manipal Institute of Technology` (`B. Tech. in Computer Science Engineering`, `2011 – 2015`), `Indian Institute Of Management - Bangalore` (`Executive General Management Program`, `2025 – 2026 (ongoing)`) | `L321–327`, `L588–594`, `AGENTS.md:L23` | **PASS** | Exact locked fields; EGMP properly marked `(ongoing)`. |
| `requirement_matrix.json` & `dossier.md` | 21 JD requirements (`12` Direct, `8` Adjacent, `1` Gap), line citations, tenure math (`~7.8 yrs`, `~1.2 yrs`, `~2.2 yrs`, `~5 yrs` titled PM/SPM, `11+ yrs` total) | `L48–343`, `L478–673` | **PASS (with minor note)** | All 21 classifications, line citations, and gap disclosures (fintech gap, Tier-1 degree nuance, formal usability/A/B/personalization gaps, internal vs. commercial analytics tools) are accurate; `dossier.md:L43` should replace `"automated recovery agents/workflows"` with `"automated recovery workflows"`. |

---

## Gate 7 Confidentiality & Disclosure Review

- **Proprietary Architecture / Security / SDKs / APIs:** None exposed. No connector APIs, authentication protocols, OAuth, RBAC, RAG pipelines, or internal system designs are disclosed.
- **Unapproved Commercial Tools:** None claimed. Explicitly states `"internal enterprise analytics tools"` (`cv_tailored.json:L27`) and avoids prohibited tools (`Amplitude`, `Mixpanel`, `GA4`, `Firebase`, `Optimizely`).
- **Customer / Client Data:** Only approved employer, client, and product names from `canonical_master_profile.md` (`v1.1.0`) appear (`Lowe’s India`, `Upraised`, `Programming Hub`, `Gradiant`, `Acadecraft`, `HealthQ Rehab`, `Byju’s`, `Tynker`, `Whitehat Jr.`, `Aakash-Byjus`, `Elevate`).
- **Gate 7 Outcome:** **`PASS`**

---

## Required Next Step Before Proceeding to Gate 8 / Gate 9

1. Apply the Gate 6 corrections listed above to `cv_tailored.json`, regenerate `cv_tailored.md` and `Minesh_Wadhwa_CV_Angel_One_SPM.pdf`, and update `cv_changelog.md` (plus minor echoes in `dossier.md:L43` and `fit_assessment.json:L24, L66, L70`).
2. Re-run Gate 6 Fact-Check verification on the revised files to achieve a `PASS` prior to finalizing Gate 8 and presenting for user approval (Gate 9).
