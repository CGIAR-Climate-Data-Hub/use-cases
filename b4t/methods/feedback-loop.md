# Reviewer feedback loop — B4T Crop Risk Index review

**One Microsoft Form** for feedback on the B4T CRI use-case documentation, reusable across its method sections. Lets readers (champions, data providers, reviewers) raise corrections, concerns, suggestions and questions **without a GitHub account**, and turns each submission into a tracked GitHub issue automatically.

**Stack:** Microsoft Forms (no-account entry, matches CGIAR M365) → Power Automate (native GitHub connector) → GitHub issue in `CGIAR-Climate-Data-Hub/use-cases`.

```text
Reader → MS Form (linked from the rendered report; "💬 Feedback" button)
             ↓  "When a new response is submitted"
        Power Automate → "Get response details"
             ↓  GitHub connector → "Create an issue"
        GitHub issue [review-feedback] in the repo  →  triaged by coordinator
```

No backend runs in the repo (the site is static GitHub Pages), so the automation lives in Power Automate, outside the repo. **The same form is reused across the report's sections** — Q1 records which section, so responses stay distinguishable.

---

## 1. Microsoft Form — questions

Create **one** form in the CGIAR M365 tenant (owner = coordinator / a shared mailbox so it outlives one person). Set **"Anyone can respond"** so external readers need no login. The section list mirrors the B4T CRI report's own headings, so it stays valid as the doc grows.

| # | Question | Type | Required | Notes |
| --- | --- | --- | --- | --- |
| 1 | Which section? | Choice (dropdown) | Yes | The report's sections (below). **Pre-filled** when linked from a given section (see §4); reader can change it. |
| 2 | Type of feedback | Choice | Yes | `Correction / factual error` · `Concern / disagreement` · `Suggestion (incl. new dataset or method)` · `Question` · `General comment` |
| 3 | Your comments | Long text | Yes | The substance. |
| 4 | Your name | Short text | No | For follow-up / attribution. |
| 5 | Your email | Short text | No | Optional confirmation reply. |

**Question 1 options** (the B4T CRI report's method sections):
`Overview & context` · `Decisions at a glance` · `Current inputs` · `CDH integration & licences` · `What this review doesn't solve` · `Dataset details` · `CRI method / formulation` · `Other`

**Screenshots — deliberate omission.** MS Forms file-upload forces the respondent to sign in (OneDrive), which breaks the no-account promise for external readers. So the form does **not** take uploads. Anyone who needs to attach an image uses the **email fallback** (see §4). Q1 already pins *which section* the feedback applies to, which covers most of the need.

### Quick Import seed

Paste into Word → **Save As `.docx`** → Forms **New Form → Quick Import → upload**. Quick Import detects Choice (Q1/Q2) and Text (Q3/Q4/Q5); it does **not** set *required*, *dropdown*, or *long-answer* — fix those after (Q1 → dropdown; Q1/Q2/Q3 → required; Q3 → long answer).

```text
B4T Crop Risk Index review — feedback

1. Which section?
A. Overview & context
B. Decisions at a glance
C. Current inputs
D. CDH integration & licences
E. What this review doesn't solve
F. Dataset details
G. CRI method / formulation
H. Other

2. Type of feedback
A. Correction / factual error
B. Concern / disagreement
C. Suggestion (new dataset or method)
D. Question
E. General comment

3. Your comments

4. Your name

5. Your email
```

---

## 2. Power Automate flow

Cloud flow owned by the same account as the form.

1. **Trigger:** Microsoft Forms — *When a new response is submitted* (select the form).
2. **Action:** Microsoft Forms — *Get response details* (Response Id = trigger output).
3. **Action:** GitHub — *Create an issue*.
   - **Repository owner:** `CGIAR-Climate-Data-Hub`
   - **Repository name:** `use-cases`
   - **Title:** `[<Q1 section>] <Q2 type> — <first ~60 chars of Q3>`
   - **Labels:** `review-feedback` (add a second label per type if desired — see §3)
   - **Body:** (markdown)

     ```text
     **Section:** <Q1>
     **Type:** <Q2>

     <Q3 comments>

     ---
     *Submitted via the B4T CRI review feedback form.*
     *From: <Q4 name or "anonymous"> · <Q5 email or "no email">*
     *Submitted: <trigger submission time>*
     ```

4. *(Optional)* **Action:** Office 365 Outlook — *Send an email* to Q5 confirming receipt, if an email was given (guard with a condition on Q5 non-empty).

The GitHub connector authenticates once via OAuth (an org member or a machine account with issue-write on the repo) — **no personal access token stored in code.**

---

## 3. GitHub labels

Create before first run (Power Automate errors if a label doesn't exist):

```bash
gh label create review-feedback --repo CGIAR-Climate-Data-Hub/use-cases \
  --color 1955A6 --description "Reader/reviewer feedback via the MS feedback form"
# optional per-type:
gh label create feedback:correction --repo CGIAR-Climate-Data-Hub/use-cases --color B60205
gh label create feedback:concern    --repo CGIAR-Climate-Data-Hub/use-cases --color D93F0B
gh label create feedback:suggestion --repo CGIAR-Climate-Data-Hub/use-cases --color 0E8A16
gh label create feedback:question   --repo CGIAR-Climate-Data-Hub/use-cases --color FBCA04
gh label create feedback:comment    --repo CGIAR-Climate-Data-Hub/use-cases --color C5DEF5
```

---

## 4. Report wiring (the reader side)

- A floating **"💬 Feedback"** button sits bottom-right on the rendered report (artifact + Astro). It's a plain link (`target="_blank"`) — works inside the artifact's strict CSP because it only navigates, never posts.
- A **"Feedback & corrections"** section explains the loop and holds the primary form button, plus a **mailto fallback** for feedback that needs a screenshot attached.
- **Live form URL:** <https://forms.office.com/e/ZF59NaT4RN> — wired into the artifact's feedback button (2026-07-03). For the Astro port, reuse the same URL.

**Per-section pre-fill (recommended).** MS Forms can generate a **pre-filled URL** (form → `···` menu → *Get pre-filled URL*) with **Q1 (section)** preset. Generate one per section and point that section's own "comment" link at it, so the reader lands on the form with the section already selected — they only pick the type and comment. The single form-wide link (for the floating button) leaves Q1 for the reader to choose.

---

## 5. Handoff checklist

- [ ] Create the MS Form (§1) in a shared/owned M365 account; set "Anyone can respond".
- [ ] Create the GitHub labels (§3).
- [ ] Build the Power Automate flow (§2); authorise the GitHub connector with an account that has issue-write.
- [ ] Submit one test response → confirm the issue lands with correct title/labels/body.
- [ ] Send the form share link back → `FEEDBACK_FORM_URL` gets swapped in and the report redeployed.
- [ ] *(recommended)* Generate a per-section pre-filled URL (Q1 = section) and wire each section's "comment" link to it.
