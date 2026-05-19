---
description: Bootstrap a new use-case folder from BRIEF_TEMPLATE.md
argument-hint: <kebab-case-slug>
---

You're being asked to create a new use-case scaffold in this repo.

**Slug argument:** `$ARGUMENTS`

Steps:

1. Validate the slug is lowercase kebab-case (letters, digits, hyphens only). If not, push back before doing anything else.
2. Check that `./$ARGUMENTS/` does not already exist. If it does, stop and report — never overwrite.
3. Create the folder `./$ARGUMENTS/`.
4. Copy `BRIEF_TEMPLATE.md` to `./$ARGUMENTS/BRIEF.md`.
5. In the new BRIEF.md:
   - Set the `updated:` field to today's date (YYYY-MM-DD)
   - Replace placeholder "Use Case Name" in the title with the slug in Title Case (e.g. `pastoral-early-warning` → `Pastoral Early Warning`)
   - Leave all other fields as-is or as `_TBC_` — do **not** invent owners, dates, or content
6. Add a new row to the **Master list** table in `README.md` with the use-case's slug-derived title, `_TBC_` for Champion, `Brief` for Status, and a `_TBC_` description.
7. Report back: the new folder path, the line added to README.md, and any remaining fields the champion needs to fill in.

Do not commit the changes. Pete will review the diff and commit.
