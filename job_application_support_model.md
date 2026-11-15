# Job Application Support Model

## High-Level Agent Workflow, Sub-Agent Design, and Quality Controls

### 1. Objective

Build an evidence-led job application support system that discovers
relevant Product Manager opportunities from LinkedIn email alerts,
evaluates each role against the **Canonical Master Profile**, and
prepares tailored, credible application materials.

**Core principle:** The Canonical Master Profile is the single source of
truth for the user's experience, achievements, skills, metrics, dates,
and qualifications. Tailoring may change emphasis and wording; it must
not create facts.

------------------------------------------------------------------------

## 2. End-to-End Workflow

1.  **Discover opportunities from email**
    -   Search the connected email account for LinkedIn Product Manager
        job-alert emails.
    -   Extract the role title, company, location, date, and LinkedIn
        job URL.
    -   Deduplicate repeated alerts and retain the source email/link.
2.  **Retrieve the complete job description**
    -   Open the LinkedIn job URL for each selected opportunity.
    -   Read the entire available job description, not just the email
        preview or search snippet.
    -   Capture responsibilities, must-have requirements, preferred
        qualifications, experience level, domain, skills, and
        application instructions.
    -   Record access failures or missing sections; never fill gaps by
        guessing.
3.  **Load and validate against the Canonical Master Profile**
    -   Retrieve the current canonical profile and its supporting
        evidence.
    -   Map each job requirement to specific profile evidence.
    -   Classify each requirement as:
        -   **Direct evidence** --- explicitly supported by the profile.
        -   **Adjacent / transferable evidence** --- supported
            experience that is relevant but not identical.
        -   **Gap / not evidenced** --- no defensible supporting
            evidence found.
    -   Preserve important context, scope, ownership, dates, and metric
        qualifiers.
4.  **Assess role fit**
    -   Evaluate role scope, seniority, product discipline, domain
        relevance, skills, leadership expectations, and evidence
        strength.
    -   Produce an explainable fit assessment, including strengths,
        gaps, risks, and any assumptions.
    -   Recommend a disposition: **High Priority**, **Consider**, or
        **Not Suitable**.
    -   Do not let keyword overlap alone determine fit.
5.  **Prioritise opportunities**
    -   Rank roles using fit, evidence strength, seniority alignment,
        role relevance, and practical constraints.
    -   Surface duplicate roles and roles with incomplete or
        inaccessible descriptions.
    -   Keep the rationale visible so the user can challenge or override
        the recommendation.
6.  **Tailor application materials**
    -   Create a role-specific CV from the canonical profile.
    -   Tailor the summary, skills, and experience bullets to the role's
        actual requirements.
    -   Use natural, evidence-led ATS terminology; avoid keyword
        stuffing.
    -   Prefer outcome-led, differentiated bullets that show leadership,
        ownership, KPI/data management, roadmaps, transformation,
        innovation, and measurable impact where supported.
    -   Use the user's preferred achievement structure: **what was done
        → how it was done → measurable result**.
    -   Prepare a cover letter and application-question drafts only
        where useful or required.
7.  **Run factual, quality, and disclosure reviews**
    -   Check every statement against the canonical profile or an
        explicitly approved source.
    -   Verify metrics, dates, role titles, scope, ownership,
        technologies, and qualifications.
    -   Remove unsupported claims and protect confidential
        employer/client information.
    -   Ensure the final materials are coherent, concise, role-relevant,
        and internally consistent.
8.  **Present for user approval**
    -   Share the job description summary, fit assessment, gaps,
        tailored CV, and any other application drafts.
    -   Highlight uncertain wording or claims requiring confirmation.
    -   Do not submit an application, send messages, or represent the
        user externally without explicit approval.
9.  **Track the opportunity**
    -   Record the job URL, company, role, source email/date, full-JD
        retrieval status, fit assessment, decision, CV version, approval
        status, application status, and follow-up notes.
    -   Keep a clear link between each application and the exact
        tailored materials approved for it.

------------------------------------------------------------------------

## 3. Suggested Agent / Sub-Agent Structure

A coordinator agent should own the workflow, delegate bounded tasks, and
enforce the review gates. Sub-agents should return structured outputs to
the coordinator rather than independently changing the canonical profile
or submitting applications.

  -------------------------------------------------------------------------
  Agent / sub-agent       Responsibility          Required output
  ----------------------- ----------------------- -------------------------
  **1. Orchestrator /     Runs the workflow,      One consolidated
  Application Manager**   manages state,          opportunity record and
                          delegates tasks,        workflow status.
                          resolves hand-offs, and 
                          enforces approval       
                          gates.                  

  **2. Email &            Finds LinkedIn PM       Structured job queue with
  Opportunity Discovery   alerts, extracts job    source email and URL.
  Agent**                 links and metadata, and 
                          detects duplicates.     

  **3. LinkedIn JD        Opens each job link and Full JD text, structured
  Research Agent**        captures the complete   requirements, retrieval
                          available JD and        status, and source link.
                          application details.    

  **4. Canonical Profile  Retrieves the latest    Versioned
  Retrieval Agent**       canonical profile and   profile/evidence package;
                          relevant supporting     no edits to the source
                          evidence.               profile.

  **5. Requirement        Maps each JD            Requirement-to-evidence
  Mapping Agent**         requirement to direct,  matrix with precise
                          adjacent, or missing    supporting profile
                          evidence.               references.

  **6. Role Fit &         Assesses seniority,     Explainable fit
  Prioritisation Agent**  scope, domain, skills,  score/rationale and High
                          strengths, gaps, and    Priority / Consider / Not
                          overall suitability.    Suitable recommendation.

  **7. CV Tailoring       Produces the            Tailored CV plus a change
  Agent**                 role-specific CV while  log linking edits to JD
                          preserving factual      requirements and profile
                          accuracy and the user's evidence.
                          preferred positioning.  

  **8. Application        Drafts cover letters,   Role-specific drafts with
  Content Agent**         recruiter messages, and evidence references and
                          application-question    uncertainty flags.
                          responses when          
                          relevant.               

  **9. Fact-Check &       Independently audits    Pass/fail review, flagged
  Integrity Reviewer**    every claim, metric,    claims, and required
                          date, skill, and        corrections.
                          ownership statement.    

  **10. ATS & Editorial   Checks readability,     Final editorial/ATS
  Reviewer**              relevance, keyword      review and suggested
                          coverage, structure,    corrections.
                          consistency, and        
                          unnecessary repetition. 

  **11. Application       Maintains opportunity   Updated application
  Tracker Agent**         records, approved       tracker and audit trail.
                          document versions,      
                          decisions, and          
                          application status.     
  -------------------------------------------------------------------------

**Recommended design:** Keep the Orchestrator, JD Research, Requirement
Mapping, CV Tailoring, and Fact-Check roles distinct. The fact-check
reviewer should not simply approve its own work or rely only on the
tailoring agent's assertions.

------------------------------------------------------------------------

## 4. Non-Negotiable Instructions and Guardrails

### A. Canonical profile integrity

-   Treat the latest approved Canonical Master Profile as the single
    source of truth.
-   Never silently edit, overwrite, or reinterpret the canonical
    profile.
-   Do not invent employers, titles, dates, responsibilities, team
    sizes, budgets, technologies, qualifications, or results.
-   Do not upgrade participation into ownership, influence into formal
    authority, or exposure into expertise.
-   Do not claim formal people management, technical implementation, or
    domain expertise unless supported.
-   Preserve the distinction between delivered outcomes, measured
    outcomes, estimates, and roadmap targets.

### B. Evidence-led tailoring

-   Every material CV claim must map to evidence in the canonical
    profile or another source explicitly approved by the user.
-   Classify evidence as direct, adjacent/transferable, or a gap; do not
    present adjacent experience as identical experience.
-   Use JD keywords naturally when the underlying experience supports
    them.
-   The user prefers the term **"agents"** to be incorporated into
    relevant CV bullets for closely aligned roles where it meaningfully
    describes genuine work. This is not permission to invent
    agent-related experience or insert the term as keyword stuffing.
-   Keep bullets outcome-led, specific, differentiated, and defensible.
-   Do not overstate backup, self-service, ownership, outcomes, or
    technical depth.

### C. Positioning guidance

-   For closely aligned enterprise platform / AI Product Manager roles,
    consider the user's credible positioning around platform strategy,
    AI-enabled and agentic workflows, orchestration, reliability,
    observability, governance, lifecycle management, enterprise
    operations, executive alignment, and measurable outcomes.
-   Use this positioning only where the JD and profile evidence support
    it.
-   Do not fabricate connector APIs, authentication, SDKs, security
    architecture, permission systems, OAuth/RBAC/RAG, or other
    unsupported technical specificity.
-   Bridge adjacent experience explicitly rather than disguising gaps.

### D. Confidentiality and disclosure

-   Do not expose confidential employer, client, customer, architecture,
    operational, or commercially sensitive details.
-   Sanitize examples and artifacts where necessary.
-   Do not disclose proprietary implementation details in CVs, cover
    letters, portfolios, or recruiter messages.
-   Use only approved, defensible descriptions of impact.

### E. Research integrity

-   Read the complete available LinkedIn JD for each role.
-   Do not assess fit from the email preview alone.
-   Do not treat search snippets, inferred requirements, or generic
    company information as JD facts.
-   Mark inaccessible, incomplete, or ambiguous information explicitly.
-   Keep the source URL and retrieval date with the job record.

### F. User control

-   The agent may research, assess, draft, compare, and recommend.
-   The agent must not apply, submit forms, send recruiter messages, or
    make commitments on the user's behalf without explicit approval.
-   Ask the user only for genuinely missing facts that materially affect
    accuracy.
-   Never resolve a factual ambiguity by guessing.

------------------------------------------------------------------------

## 5. Mandatory Review Gates

  -----------------------------------------------------------------------
  Gate                    Review question         Required action if it
                                                  fails
  ----------------------- ----------------------- -----------------------
  **1. Opportunity        Is this a relevant      Hold, deduplicate, or
  validation**            LinkedIn Product        flag for review.
                          Manager role, and is    
                          the job link valid and  
                          unique?                 

  **2. JD completeness**  Has the agent read the  Retry retrieval or mark
                          entire available JD and incomplete; do not
                          captured all            score as if complete.
                          requirements?           

  **3. Profile version    Is the latest approved  Stop and retrieve the
  check**                 Canonical Master        current version.
                          Profile being used?     

  **4. Evidence mapping** Does every assessed     Return unsupported
                          requirement have a      mappings for
                          direct, adjacent, or    correction.
                          gap classification with 
                          supporting evidence?    

  **5. Fit rationale**    Is the recommendation   Reassess and explain
                          based on role substance the recommendation.
                          and evidence rather     
                          than keyword matching   
                          alone?                  

  **6. CV claim audit**   Can every factual       Remove, qualify, or ask
                          claim, metric, date,    the user to verify it.
                          skill, and ownership    
                          statement be defended?  

  **7. Confidentiality    Is the content safe to  Sanitize or remove the
  review**                share externally and    content.
                          free of sensitive       
                          proprietary detail?     

  **8. Final consistency  Are the CV, cover       Reconcile differences
  review**                letter, application     before presenting.
                          answers, and fit        
                          assessment consistent   
                          with one another?       

  **9. Approval gate**    Has the user explicitly Do not submit or send
                          approved the final      anything.
                          materials and any       
                          external action?        

  **10. Tracking and      Are the source JD,      Complete the record
  audit**                 decision, approved      before closing the
                          document version, and   workflow.
                          status recorded?        
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 6. Standard Output for Every Opportunity

Each job record should contain:

1.  **Opportunity:** Company, role, location, LinkedIn URL, source
    email, and date found.
2.  **JD review:** Complete-JD retrieval status and structured
    requirements.
3.  **Requirement matrix:** Requirement, priority, evidence, evidence
    classification, and gap.
4.  **Fit assessment:** Score, recommendation, strengths, gaps, and
    risks.
5.  **Application recommendation:** Apply / Hold / Do Not Apply, with
    rationale.
6.  **Tailored materials:** CV and any relevant cover letter or
    application responses.
7.  **Review status:** Fact-check, confidentiality, editorial, and
    user-approval outcomes.
8.  **Tracking:** Decision, application status, document version, and
    next action.

------------------------------------------------------------------------

## 7. Operating Rules for the Orchestrator

-   Process opportunities independently; do not mix requirements or
    evidence between companies and roles.
-   Maintain a traceable chain: **email → LinkedIn JD → requirement →
    profile evidence → fit decision → tailored material → review → user
    approval**.
-   Pass structured outputs between agents; do not rely on unverified
    summaries.
-   Preserve the original JD and the exact approved application-document
    version.
-   Re-run affected reviews whenever a material change is made to the JD
    interpretation or CV.
-   Treat conflicting agent conclusions as issues to resolve, not as
    permission to choose the most favourable answer.
-   Stop and ask the user when a missing fact, ambiguous claim, or
    approval decision could materially change the application.
-   Optimise for truthful, high-quality applications---not maximum
    application volume.

**Definition of done:** An opportunity is complete only when its JD has
been reviewed, fit has been assessed, application materials (if
recommended) have passed factual and disclosure checks, the user has
made the application decision, and the tracker reflects the outcome.
