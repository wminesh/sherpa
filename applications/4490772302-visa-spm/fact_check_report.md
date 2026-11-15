# Independent Fact-Check & Confidentiality Audit Report — Visa (`4490772302-visa-spm`)

- **Opportunity ID:** `4490772302-visa-spm`
- **Target Company / Role:** Visa — Sr Product Manager
- **Audited Artifacts:** `cv_tailored.json` (`tailored-visa-spm-1.0`), `cv_tailored.md`, `cv_changelog.md`, `requirement_matrix.json`, `dossier.md`
- **Authoritative Baselines:** `canonical_master_profile.md` (`v1.1.0`), `AGENTS.md`, `templates/cv_base_schema.json`
- **Audit Date:** `2026-11-15`
- **Auditor:** Independent Fact-Check & Integrity Reviewer (Agent 9)

---

## Executive Verdict

- **Overall Audit Verdict:** **`FAIL`**
- **Gate 6 (CV Claim Audit & Profile Integrity):** **`FAIL`** — 1 material factual/period misattribution defect and 1 summary causal-pairing inaccuracy identified in `cv_tailored.json` / `cv_tailored.md` (and mirrored in `cv_changelog.md`).
- **Gate 7 (Confidentiality & Disclosure Review):** **`PASS`** — No proprietary architectures, internal confidential customer data, internal tool vendor names, or unapproved disclosures appear in any tailored artifact.

> **Action Required:** Remediate the Gate 6 defects listed in Section 4 below across `cv_tailored.json`, `cv_tailored.md`, and `cv_changelog.md`, regenerate `Minesh_Wadhwa_CV_Visa_SPM.pdf`, and re-run Gate 6 verification before proceeding.

---

## 1. Locked Identity, Dates, Titles, Employers & Credentials Audit

| Field / Entity | Tailored CV Value (`cv_tailored.json` / `cv_tailored.md`) | Canonical Profile Value (`canonical_master_profile.md` `v1.1.0`) | Status |
| :--- | :--- | :--- | :--- |
| **Name & Contact** | `Minesh Wadhwa` \| `Bangalore • w.minesh@gmail.com • +91 9035 199 024` | `Bangalore, Karnataka, India` \| `w.minesh@gmail.com` \| `+91 9035 199 024` (`L9–L11`) | **PASS** |
| **Lowe’s India** | `Senior Product Manager` \| `Bangalore, Karnataka` \| `Sep 2024 – Present` | `Senior Product Manager` \| `Bangalore, Karnataka` \| `Sep 2024 – Present` (`L48–L50`) | **PASS** |
| **Hype Marketing & Product Services** | `Founder` \| `Bangalore, Karnataka` \| `Oct 2023 – Nov 2024` | `Founder` \| `Bangalore, Karnataka` \| `Oct 2023 – Nov 2024` (`L119–L121`) | **PASS** |
| **HealthQ Rehab** | `Head of Marketing` \| `Bangalore, Karnataka` \| `May 2023 – Dec 2023` | `Head of Marketing` \| `Bangalore, Karnataka` \| `May 2023 – Dec 2023` (`L179–L181`) | **PASS** |
| **Byju’s — Senior Product Manager** | `Byju’s - Product Development` \| `Bangalore, Karnataka` \| `July 2020 – April 2023` | `Byju’s — Product Development` \| `Bangalore, Karnataka` \| `July 2020 – April 2023` (`L212–L219`, `AGENTS.md`) | **PASS** |
| **Byju’s — Multiple Roles** | `Multiple Roles` \| `Jun 2015 – June 2020` | `Multiple Roles` \| `June 2015 – June 2020` (`L286–L287`; `Jun 2015 – June 2020` in `AGENTS.md`) | **PASS** |
| **Certifications** | `University of California, Irvine` \| `Oct 2020 – Dec 2020` (3 course bullets verbatim) | `University of California, Irvine` \| `Project Management Specialization` \| `Oct 2020 – Dec 2020` (`L333–L344`) | **PASS** |
| **Social Entrepreneurship** | *The Open Door Foundation* (RTC Girls Home, Bangalore); *Education for All* initiative by Byju’s (10M kids by 2025) | Matches verbatim (`L348–L349`) | **PASS** |
| **Education (MIT)** | `Manipal Institute of Technology`, `Manipal, Karnataka` — `B. Tech. in Computer Science Engineering` (`2011 – 2015`) | `Manipal Institute of Technology` — `B.Tech. in Computer Science Engineering` (`2011 – 2015`) (`L325–L327`, `AGENTS.md`) | **PASS** |
| **Education (IIM-B)** | `Indian Institute Of Management - Bangalore` — `Executive General Management Program` (`2025 – 2026 (ongoing)`) | `Indian Institute Of Management Bangalore` — `Executive General Management Program` (`2025 – 2026 (Ongoing)`) (`L321–L323`, `AGENTS.md`) | **PASS** |

---

## 2. Claim-by-Claim Verification Table (Gate 6)

| Location | Audited Claim / Metric / Term | Canonical Evidence & Line Ref (`v1.1.0`) | Ownership / Outcome / Terminology Check | Verdict |
| :--- | :--- | :--- | :--- | :--- |
| `cv_tailored.json:L13` (Profile Summary) | `10+ years of experience directing product strategy from conception to implementation across enterprise platforms, operational systems, and customer acquisition funnels` | `Jun 2015 – Present` (~11+ years as of Nov 2026); Lowe’s enterprise/ops platforms (`L48–L100`); Byju’s funnel (`L235–L238`) | Accurate tenure and scope across enterprise platforms and acquisition funnels | **PASS** |
| `cv_tailored.json:L13` (Profile Summary) | `partnering across engineering, IT, marketing, finance, and operations to define roadmaps, manage cost and profit control (P&L, forecasting, ROI), and apply Agile delivery` | Cross-functional teams (`L65`, `L71`, `L230`, `L367`, `L485`); roadmaps (`L66`, `L82`); P&L/forecasting/ROI (`L459–L462`, `L490–L493`); Agile Product Delivery (`L450`) | Supported in canonical profile; no QA/testing engineering ownership claimed | **PASS** |
| `cv_tailored.json:L13` (Profile Summary) | `Delivered ~$10M annual revenue protection, $2M cost savings, 99.99% reliability via automated recovery agents, 20% faster AI-driven workflows, and 2.5L+ SQLs with 35% higher conversion` | `~$10M` (`L86`: via automated recovery systems, incident handling workflows, reliability improvements); `$2M` (`L94`); `99.99%` (`L76`: through strategic operational initiatives); `20%` cycle time reduction (`L98`); `2.5L+` SQLs (`L236`); `35%` conversion lift (`L237`) | **Causal mispairing:** `99.99% reliability via automated recovery agents` links `99.99%` specifically to recovery agents rather than `~$10M` revenue protection (`L86–L87`) and strategic operational initiatives (`L76`). Also `20% faster AI-driven workflows` should explicitly reference `20% cycle-time reduction`. | **FAIL** (Minor / Tighten) |
| `cv_tailored.json:L26` (Lowe’s Reliability Bullet 1) | `Directed end-to-end enterprise platform strategy across engineering and operations teams by identifying points of failure and governing reliability initiatives, ensuring 99.99% platform reliability` | `L65`, `L68`, `L76` (`99.99%`), `L85–L90`, `L524–L529` | Delivered outcome (`99.99%`) accurately preserved; failure-point & reliability governance supported | **PASS** |
| `cv_tailored.json:L27` (Lowe’s Reliability Bullet 2) | `Designed KPI frameworks and dashboards using internal enterprise analytics tools by tracking incident resolution, cost savings, and adoption to guide roadmap tradeoffs` | `L67` (`internal enterprise analytics and reporting tools`), `L77–L81`, `L455–L458` | Compliant with `AGENTS.md`: no prohibited third-party analytics tools (`Amplitude`, `Mixpanel`, `GA4`, etc.) named | **PASS** |
| `cv_tailored.json:L28` (Lowe’s Reliability Bullet 3) | `Formulated annual/quarterly roadmaps and monthly VP/CXO business reviews by aligning P&L, budgeting, and ROI priorities with business goals, targeting a 20% reduction in incident volume` | `L66`, `L82` (`targeting 20% reduction in incident volume`), `L459–L462`, `L478–L482`, `L490–L493` | Properly preserves **`targeting`** distinction (roadmap target, not delivered outcome) | **PASS** |
| `cv_tailored.json:L29` (Lowe’s Reliability Bullet 4) | `Identified order-cancellation failure modes and deployed automated recovery agents with SLA escalation workflows across systems and operations teams, saving ~$10M annually` | `L70`, `L85–L90` (`~$10M`), `L525–L528` (`Automated recovery workflows`, `SLA and escalation workflows`) | Delivered outcome (`~$10M`) accurate; `"automated recovery agents"` aligns with `AGENTS.md` rule permitting `"agents"` for genuine automated recovery workflows without inventing LLM/RAG architectures | **PASS** |
| `cv_tailored.json:L30` (Lowe’s Reliability Bullet 5) | `Served as a central cross-functional resource across product, engineering, finance, operations, and IT teams by establishing executive governance cadences to drive alignment without formal authority` | `L65`, `L71`, `L481`, `L485–L488`, `L553–L556` | Accurate; explicitly preserves alignment without formal authority | **PASS** |
| `cv_tailored.json:L31` (Lowe’s Reliability Bullet 6) | `Prioritized workflow improvements across procurement, asset management, and operational planning by balancing engineering scope against ROI constraints to boost efficiency` | `L69`, `L91–L100`, `L340–L343`, `L462`, `L491–L492` | Supported by asset lifecycle, procurement, and ROI-driven prioritization evidence | **PASS** |
| `cv_tailored.json:L37` (Lowe’s Infra & Ops Bullet 1) | `Spearheaded a unified enterprise asset lifecycle platform from conception to rollout by partnering with finance, operations, and infrastructure teams on cost control, delivering ~$2M in annual savings` | `L54`, `L92–L94` (`~$2M` annual cost savings), `L493` | Delivered outcome (`~$2M`) accurate; no engineering people management claimed | **PASS** |
| `cv_tailored.json:L38` (Lowe’s Infra & Ops Bullet 2) | `Designed and launched an AI-driven procurement and catalog platform powered by agentic workflows by streamlining store-setup and catalog workflows, reducing operational cycle times by 20%` | `L97–L99` (`20%` operational cycle times reduction) | Delivered outcome (`20%`) accurate; `"agentic workflows"` explicitly permitted by `AGENTS.md` for Lowe’s AI-driven procurement/catalog workflows | **PASS** |
| `cv_tailored.json:L53` (Hype Bullet 1) | `Identified market opportunities and defined GTM, product, and lifecycle roadmaps for clients by translating audience demand into structured business and campaign execution plans` | `L132–L133`, `L136`, `L373` (`translating business goals into campaign, content, and communication roadmaps`) | Supported by Founder consulting scope across new offerings (`Upraised`, `Programming Hub`); note `"client growth and campaign execution plans"` would mirror `L132–L133` even more tightly than `"business and campaign execution plans"` | **PASS** (Advisory note) |
| `cv_tailored.json:L54` (Hype Bullet 2) | `Built data-driven customer journey and engagement workflows by evaluating conversion and channel metrics across email, social, and content touchpoints to drive iterative optimization` | `L134–L137`, `L377` | Exact match | **PASS** |
| `cv_tailored.json:L60` (Hype — Upraised) | `50%` engagement increase, `30%` website traffic increase | `L142–L145`, `L373` | Exact metric and engagement match | **PASS** |
| `cv_tailored.json:L61` (Hype — Programming Hub) | `4.5+ ratings` and strong user adoption | `L148–L150`, `L375` | Exact metric and engagement match | **PASS** |
| `cv_tailored.json:L62` (Hype — Gradiant) | `30% open rates` and `20% CTRs` | `L153–L156`, `L374` | Exact metric and engagement match | **PASS** |
| `cv_tailored.json:L63` (Hype — Acadecraft) | `80%+ completion rates` | `L159–L160`, `L376` | Exact metric and engagement match | **PASS** |
| `cv_tailored.json:L78–L80` (HealthQ Rehab) | `35%` organic traffic growth; `50%` social media engagement boost; `20%` overall brand engagement increase via WhatsApp, Telegram, and newsletter workflows | `L184–L197`, `L380–L382` | Exact metrics and channels match | **PASS** |
| `cv_tailored.json:L94–L98` (Byju’s — Senior PM, `July 2020 – April 2023`) | `2.5L+` SQLs (`Byju’s Xcel Masterclasses`); `35%` lead conversion improvement; `12` cross-product prototypes (`Aakash-Byjus`, `Tynker`, `Whitehat Jr.`); `15%` instructor training time reduction (`Whitehat Jr. Interactive Learning Experiences`); `5%` course completion increase (`Tynker` redesign) | `L219` (canonical CV display period spans PM `July 2020 – Feb 2022` & SPM `March 2022 – April 2023`), `L228–L238`, `L261–L268`, `L386–L390` | All 5 metrics and product attributions verified within canonical `July 2020 – April 2023` display period | **PASS** |
| `cv_tailored.json:L106` (Byju’s — Multiple Roles, `Jun 2015 – June 2020`) | `Prototyped 300+ *interactive learning experiences* for science and maths and designed UX interactions for the *Elevate* internal tracking platform` | `L304` (`Developed interactive learning experiences for science and mathematics` — **no `300+` count**); `L270–L274` (`Social Studies Product` under `July 2020 – Feb 2022` lists `300+ interactive learning experiences`); `L306` (`Elevate`) | **Factual misattribution:** `300+` in `canonical_master_profile.md:L274` belongs to the **Social Studies** product (`July 2020 – Feb 2022`), NOT science and mathematics under `Multiple Roles (Jun 2015 – June 2020)`. | **FAIL** |
| `cv_tailored.json:L107` (Byju’s — Multiple Roles, `Jun 2015 – June 2020`) | `Prototyped and launched the *Social Studies* product (500+ hours of video content) and managed a team of 5 product leads for *BTLA Commerce* development` | `L305` (`Prototyped and developed Social Studies product`); `L271–L273` (`Product Manager: July 2020 – Feb 2022` lists `Launched Social Studies product` and `500+ hours of video content`); `L307` (`Led team of 5 product leads for Commerce product development`) | **Period conflation:** Places the `July 2020 – Feb 2022` launch and `500+ hours of video content` metric under `Jun 2015 – June 2020` (`Multiple Roles`). `5 product leads` for `BTLA Commerce` is verified (`L293`, `L307`). | **FAIL** |
| `requirement_matrix.json` & `dossier.md` | `15 Direct`, `3 Adjacent`, `2 Gap` (Total `20`); Fit `81/100` (`Consider`, `Apply`); explicit gaps for `DM-1` (Payments) and `PR-2` (CSM/CSPO); explicit `Adjacent` bridging for `MH-8` (sales/service/CRM), `MH-10` (sales team collaboration), `IM-2` | `canonical_master_profile.md` `v1.1.0` & `jd_full.md` | Accurate counts (`10+3+1+1=15` Direct, `2+1=3` Adjacent, `1+1=2` Gap), accurate line citations, transparent gaps, no fabricated ChatGPT/Copilot/CRM/Agile-cert/payments claims | **PASS** |

---

## 3. Prohibited Fabrications & Confidentiality Check (Gates 6 & 7)

1. **Prohibited Technical & Domain Claims (`AGENTS.md` §2):**
   - Checked for fabricated mentions of connector APIs, authentication protocols, SDKs, security architecture, permission systems, OAuth, RBAC, RAG pipelines, vector databases, commercial third-party analytics tools (`Amplitude`, `Mixpanel`, `GA4`, `Firebase`, `Optimizely`), RCS marketing, production ML decisioning models, ROAS/incrementality, loyalty platforms, merchandising platforms, DAM platforms, CSM/CSPO certifications, commercial CRM (Salesforce) ownership, or ChatGPT/Copilot tool usage.
   - **Result:** **0 violations found.**
2. **Confidentiality & Disclosure (`AGENTS.md` §3 / Gate 7):**
   - Verified all employer names, Hype client names (`Upraised`, `Programming Hub`, `Gradiant`, `Acadecraft`), Byju’s product names (`Byju’s Xcel Masterclasses`, `Tynker`, `Whitehat Jr.`, `Aakash-Byjus`, `Social Studies`, `Interactive Learning Experiences`, `Byju’s Exam Prep`, `BTLA Commerce`, `BTLA Science`, `Elevate`), and financial/operational metrics (`~$10M`, `~$2M`/`$2M`, `99.99%`, `20%`, etc.) against `canonical_master_profile.md` `v1.1.0`.
   - No internal vendor/tool names, proprietary architecture details, customer PII, or unapproved disclosures appear in `cv_tailored.json`, `cv_tailored.md`, `cv_changelog.md`, `requirement_matrix.json`, or `dossier.md`.
   - **Gate 7 Verdict:** **`PASS`**.

---

## 4. Exact Fixes Required to Pass Gate 6

1. **Fix `Byju’s - Product Development` → `Multiple Roles (Jun 2015 – June 2020)` (`cv_tailored.json:L106–L107`, `cv_tailored.md:L48–L49`, `cv_changelog.md:L48`):**
   - **Bullet 1 (`L106`):** Remove `300+` from science and maths (since `300+ interactive learning experiences` belongs to `Social Studies` in `2020–2022`). Update to:
     > `"Prototyped and developed *interactive learning experiences* for science and maths and designed UX interactions for the *Elevate* internal tracking platform"`
   - **Bullet 2 (`L107`):** Remove the `2020–2022` `launched` and `(500+ hours of video content)` attribution from `Multiple Roles (Jun 2015 – June 2020)`. Update to:
     > `"Prototyped and developed the *Social Studies* product and managed a team of 5 product leads for *BTLA Commerce* development"`
     *(Note: If the `Social Studies` launch, `500+ hours of video content`, and `300+ interactive learning experiences` are desired on the CV, place them in a bullet under `Senior Product Manager | July 2020 – April 2023`, which is the canonical display period covering `Product Manager [July 2020 – Feb 2022]`.)*
   - Update `cv_changelog.md:L48` to remove the `L271–L274` citation from `Multiple Roles` (or move it to `Senior Product Manager` if `Social Studies` launch metrics are moved there).

2. **Fix Profile Summary Causal Pairing (`cv_tailored.json:L13`, `cv_tailored.md:L5`, `cv_changelog.md:L30`):**
   - Replace `"Delivered ~$10M annual revenue protection, $2M cost savings, 99.99% reliability via automated recovery agents, 20% faster AI-driven workflows, and 2.5L+ SQLs with 35% higher conversion."` with:
     > `"Delivered ~$10M annual revenue protection via automated recovery agents, ~$2M cost savings, 99.99% platform reliability, 20% cycle-time reduction via AI-driven workflows, and 2.5L+ SQLs with 35% higher conversion."`

3. **Optional Tightening (`cv_tailored.json:L53`):**
   - Consider changing `"structured business and campaign execution plans"` to `"structured growth and campaign execution plans"` to stay strictly aligned with `canonical_master_profile.md:L132–L133, L373`.
