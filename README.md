# Operations Analytics Portfolio

A showcase of operations-analytics tools I designed and built as an Area Manager in a
high-volume fulfillment environment. Each project turned a manual, spreadsheet-driven
reporting process into an automated, self-serve tool — surfacing the right metric to the
right person at the right time so the floor could act on it the same shift.

> **Note on data & privacy:** This is a *public, sanitized* portfolio. All examples use
> **mock data**. Internal system names, URLs, authentication details, facility
> identifiers, and any personally identifiable information have been removed or replaced
> with generic placeholders. The goal here is to demonstrate **engineering approach and
> analytical thinking**, not to reproduce any internal system. See
> [`docs/SANITIZATION.md`](docs/SANITIZATION.md).

---

## Projects

| Project | Problem it solves | Stack |
|---|---|---|
| **[Inbound Ops Dashboard](projects/inbound-ops-dashboard/)** | A single live view of inbound/stow performance — productivity, quality, and coaching — pulled together from several disconnected reporting systems into one page. | HTML/CSS/JS, client-side data joins, userscript data proxy |
| **[Adapts Feedback Tracker](projects/adapts-feedback-tracker/)** | Weekly tracking of behavioral-feedback completion across a site, with trend charts and per-supervisor accountability, replacing a manual weekly roll-up. | Python, pandas, matplotlib |
| **[Quality WoW Tracker](projects/quality-wow-tracker/)** | Week-over-week comparison of associate quality metrics (defect events), automatically ranking the biggest improvers and offenders into shareable reports. | Python, pandas, openpyxl |

**▶ Try it:** the Inbound Ops Dashboard has a fully interactive, synthetic-data demo you
can click through — [`projects/inbound-ops-dashboard/demo/index.html`](projects/inbound-ops-dashboard/demo/index.html).

---

## What these projects have in common

- **Data engineering across messy sources.** Each tool joins data from multiple systems
  on inconsistent keys (employee ID vs. login/alias vs. station), normalizes headers and
  time zones, and handles missing/partial records gracefully.
- **Metrics people actually act on.** Every output maps to a concrete floor decision —
  who to coach, which lane is behind, which process path is slipping.
- **Automation over toil.** Reports that used to take 30–60 minutes of manual
  spreadsheet work now run in seconds and are reproducible week to week.
- **Built for non-technical users.** Setup guides, one-click runs, and plain-language
  outputs so a manager — not an engineer — can operate them.

## Skills demonstrated

`Python` · `pandas` / `numpy` · `data cleaning & joins` · `Excel/openpyxl reporting` ·
`matplotlib data viz` · `JavaScript` · `HTML/CSS dashboards` · `client-side API
integration` · `metric design` · `operations analytics` · `automation of manual workflows`

## Repository layout

```
ops-analytics-portfolio/
├── README.md                     ← you are here
├── LICENSE
├── .gitignore
├── docs/
│   ├── index.html                ← GitHub Pages landing site
│   ├── SANITIZATION.md           ← what was removed and why
│   ├── PUSH_TO_GITHUB.md         ← how to push this repo (+ safety grep)
│   ├── RESUME_BLURBS.md          ← resume / LinkedIn copy
│   └── screenshots/              ← redaction-safe, mock-data charts
└── projects/
    ├── inbound-ops-dashboard/
    │   ├── README.md
    │   ├── demo/index.html       ← interactive mock-data dashboard
    │   └── docs/RANKING.md
    ├── adapts-feedback-tracker/
    │   ├── README.md
    │   ├── adapts_tracker_demo.py
    │   └── mock_feedback_data.csv
    └── quality-wow-tracker/
        ├── README.md
        ├── quality_wow_demo.py
        ├── mock_week_prev.csv
        └── mock_week_curr.csv
```

## Project site & publishing

- A ready-to-serve landing page lives at [`docs/index.html`](docs/index.html) — enable
  **GitHub Pages** from the `/docs` folder to publish it.
- Resume and LinkedIn blurbs are in [`docs/RESUME_BLURBS.md`](docs/RESUME_BLURBS.md).
- Step-by-step push instructions (with a pre-publish safety check) are in
  [`docs/PUSH_TO_GITHUB.md`](docs/PUSH_TO_GITHUB.md).

## About

Built by an Area Manager focused on using lightweight automation to make operational data
actionable. Questions or want to talk shop about ops analytics? Open an issue.
