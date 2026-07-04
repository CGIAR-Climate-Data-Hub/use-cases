# B4T Evidence Store

Purpose:

- keep local copies of public methods papers used in B4T dataset review
- keep screengrabs of official dataset pages when paper or direct methods document is not accessible
- avoid duplicate storage for shared dataset families such as `Aqueduct 4.0`, `Aqueduct Floods`, `GAEZ v5`, `WorldClim CMIP6`, and `CHIRPS v3`

Rules:

- prefer methods paper or official technical documentation PDF
- if no stable public document can be downloaded, save screengrab of official page
- reuse shared family bundle instead of duplicating same document for multiple rows
- every saved artifact must also be indexed in [evidence-index.csv](../evidence-index.csv)
- local artifact paths should be repo-relative and safe to publish
- each bundle should include a short `MANIFEST.md` linking source URLs, saved files, supported claims, and unresolved gaps

Suggested layout:

- `shared/<family-key>/`
- `current/<code>/`
- `improved/<candidate-id>/`

Examples:

- `shared/aqueduct-4/`
- `shared/gaez-v5/`
- `current/D-01/`
- `improved/chirps-v3-3month-family/`
