# Contributing

Thanks for your interest! This is primarily a **portfolio showcase**, but issues and
suggestions are welcome.

## Ground rules (non-negotiable — this is a public repo)

This repository is a **sanitized, public** showcase. Before any change is committed:

1. **No internal data.** No internal URLs, hostnames, endpoints, or system names.
2. **No authentication logic.** No cookies, tokens, sessions, or proxy configs.
3. **No PII.** No real names, logins, employee IDs, or badge data — in code, data,
   comments, commit messages, or screenshots.
4. **Mock data only.** Data files must be prefixed `mock_` or `sample_`. Real `.csv` /
   `.xlsx` are blocked by `.gitignore` by default.
5. **Screenshots must use mock data** and be free of identifiers.

See [`docs/SANITIZATION.md`](docs/SANITIZATION.md) for the full policy and pre-publish
checklist.

## Dev setup

```bash
# Python projects
pip install pandas numpy matplotlib openpyxl

# Run a demo
cd projects/adapts-feedback-tracker && python adapts_tracker_demo.py
cd projects/quality-wow-tracker && python quality_wow_demo.py
```

The dashboard demo is static — just open
`projects/inbound-ops-dashboard/demo/index.html` in a browser.

## Opening an issue

- **Bug / question:** use the templates under `.github/ISSUE_TEMPLATE/`.
- Please don't paste any internal or confidential content into issues.

## Commit style

Short, imperative subject lines (e.g. `Add trend chart to adapts tracker`). Keep commits
focused.
