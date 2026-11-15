# Sherpa — Job Application Support System Guardrails (`AGENTS.md`)

These workspace rules enforce the **Job Application Support Model** defined in `job_application_support_model.md`. Every agent and sub-agent operating in `/Users/mineshwadhwa/Documents/Sherpa` must comply with these rules at all times.

---

## 1. Canonical Master Profile Integrity (Gate 3)

- **Single Source of Truth**: `canonical_master_profile.md` (currently **Version 1.1.0**) is the sole authoritative source for Minesh Wadhwa's experience, achievements, skills, metrics, dates, titles, and qualifications.
- **Read-Only During Runs**: Never silently edit, overwrite, or reinterpret `canonical_master_profile.md`.
- **Locked Facts (Zero Fabrication)**:
  - Never invent employers, role titles, dates, responsibilities, team sizes, budgets, technologies, qualifications, or results.
  - Never upgrade participation into ownership, influence into formal authority, or exposure into expertise.
  - Never claim formal people management, hands-on technical implementation, or domain expertise unless explicitly supported in `canonical_master_profile.md` (e.g., managing 5 product leads for Commerce at Byju's is supported; engineering people management at Lowe's is not).
  - Preserve the exact distinction between **delivered outcomes** (e.g., `~$10M` annual revenue protection savings, `$2M` annual cost savings, `20%` cycle time reduction, `99.99%` platform reliability), **measured outcomes** (`2.5L+` SQLs, `35%` lead conversion improvement, `35%` organic traffic increase, `50%` social engagement increase, `30%` open rate, `20%` CTR, `15%` instructor training time reduction, `5%` course completion increase, `80%+` completion rates, `4.5+` ratings), and **roadmap targets** (e.g., roadmaps *targeting* `20%` reduction in incident volume).
- **Canonical Dates & Sections (Reconciled v1.1.0)**:
  - **Lowe's India**: `Senior Product Manager` (`Sep 2024 – Present`), Bangalore, Karnataka
  - **Hype Marketing & Product Services**: `Founder` (`Oct 2023 – Nov 2024`), Bangalore, Karnataka
  - **HealthQ Rehab**: `Head of Marketing` (`May 2023 – Dec 2023`), Bangalore, Karnataka
  - **Byju's - Product Development**: `Senior Product Manager` (`July 2020 – April 2023`) and `Multiple Roles` (`Jun 2015 – June 2020`), Bangalore, Karnataka
  - **Certifications**: `University of California, Irvine` (`Oct 2020 – Dec 2020`) — Project Management Specialization
  - **Social Entrepreneurship**: *The Open Door Foundation* (RTC Girls Home, Bangalore) and *Education for All* initiative by Byju's
  - **Education**: `Manipal Institute of Technology` (`B. Tech. in Computer Science Engineering`, `2011 – 2015`) and `Indian Institute Of Management - Bangalore` (`Executive General Management Program`, `2025 – 2026 (ongoing)`)

---

## 2. Evidence-Led Tailoring & Positioning Rules (Gates 4, 5, 6)

- **Mandatory Requirement Classification**: Every requirement extracted from a Job Description (JD) must be mapped to `canonical_master_profile.md` with explicit line references and classified into one of three categories:
  1. **Direct evidence** — explicitly supported by `canonical_master_profile.md`.
  2. **Adjacent / transferable evidence** — supported experience that is relevant/transferable but not identical. Never disguise adjacent experience as identical hands-on experience; bridge it explicitly.
  3. **Gap / not evidenced** — no defensible supporting evidence found.
- **Achievement Structure**: Tailor CV experience bullets using the structure:
  **what was done → how it was done → measurable result**
- **Incorporating `"agents"`**:
  - Incorporate the term **"agents"** (or **agentic workflows**) into relevant CV bullets for closely aligned roles (e.g., Enterprise Platform / AI Product Manager / Workflow Automation roles) **only** where it meaningfully describes genuine work (such as AI-driven procurement/catalog workflows, automated recovery workflows, and intelligent operational orchestration at Lowe's India).
  - Never invent standalone LLM/agent engineering architectures or insert `"agents"` as keyword stuffing in unrelated bullets.
- **Prohibited Technical & Domain Fabrications**:
  - Do **not** fabricate connector APIs, authentication protocols, SDKs, security architecture, permission systems, OAuth, RBAC, RAG pipelines, vector databases, commercial third-party product analytics tools (`Amplitude`, `Mixpanel`, `GA4`, `Firebase`, `Optimizely` — user confirmed using internal analytics tools at Lowe's India for similar analysis), RCS marketing, production ML decisioning model ownership, ROAS/incrementality ownership, loyalty platforms, merchandising platforms, or DAM platform ownership unless explicitly validated by the user.

---

## 3. Confidentiality & Disclosure (Gate 7)

- Do not expose confidential employer, client, customer, internal architecture, operational, or commercially sensitive details beyond the approved public-safe descriptions in `canonical_master_profile.md`.

---

## 4. Research Integrity (Gates 1 & 2)

- Always open and read the **complete available LinkedIn JD** (using the `browser` subagent when needed) before scoring fit or tailoring materials.
- Never assess role fit from email previews, subject lines, or search snippets alone.
- Record retrieval failures, expired/closed jobs, or incomplete JDs explicitly in the dossier and tracker; never guess missing requirements.

---

## 5. Separation of Duties & User Control (Gates 8, 9, 10)

- **Independent Fact-Check**: The **Fact-Check & Integrity Reviewer** (`fact_check_reviewer`) must independently audit every claim, metric, date, skill, and ownership statement in the tailored CV against `canonical_master_profile.md` (`v1.1.0`). The CV Tailoring Agent may never self-approve Gate 6 or Gate 7.
- **Strict User Approval Gate (Gate 9)**: Agents may research, assess, draft, compare, render PDFs, and recommend. Agents must **never** submit job applications, fill external application forms, send recruiter messages, or commit on the user's behalf without explicit user approval.
- **Traceability (Gate 10)**: Maintain the full chain (`email → LinkedIn JD → requirement → profile evidence → fit decision → tailored material → review → user approval`) in `applications/<opportunity-id>/` and `tracker/application_tracker.md`.
