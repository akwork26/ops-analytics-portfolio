# Sanitization & Privacy Policy for this Repository

This portfolio is **public**. It is a sanitized demonstration of engineering and
analytics approach. The real, working tools remain private. This document records exactly
what was removed so the repository stays safe to publish.

## What was removed / replaced

| Category | In the private version | In this public repo |
|---|---|---|
| **Internal system URLs** | Live internal hostnames and prototype URLs | Removed entirely or shown as `https://<internal-reporting-system>/...` placeholders |
| **Authentication** | Single-sign-on cookie / session logic, CORS-proxy userscript | Removed. Described only conceptually ("a userscript proxies authenticated requests"). No endpoints, no auth flow. |
| **System / tool names** | Specific internal application names | Generalized ("workforce reporting system", "labor-tracking system", "quality system") |
| **Facility identifiers** | Specific building/site codes | Shown as `SITE` / `<site-code>` |
| **People** | Associate names, logins, employee IDs, manager names | Replaced with mock values (`Associate A`, `login01`, `ID001`) |
| **Real metric values** | Live performance numbers | Replaced with synthetic/mock data |
| **Org structure** | Reporting lines, headcount by area | Removed |

## Rules for anyone extending this repo

1. **Never commit a real data export.** The `.gitignore` blocks `*.csv` / `*.xlsx` by
   default; only files prefixed `sample_` or `mock_` are allowed.
2. **No internal URLs, hostnames, or endpoints** in code, comments, or docs.
3. **No authentication logic** — no cookies, tokens, session handling, or proxy configs.
4. **No PII** — no names, logins, employee IDs, or badge data, even in screenshots.
5. **Screenshots must use mock data** and have any identifiers blurred/removed.
6. When in doubt, leave it out. The purpose is to show *how I think and build*, not to
   reproduce an internal system.

## Pre-publish checklist

- [ ] `git grep` for internal hostnames → 0 results
- [ ] `git grep` for the facility code → 0 results
- [ ] No `*.user.js` / proxy files committed
- [ ] No real `.csv` / `.xlsx` committed (only `sample_*` / `mock_*`)
- [ ] Screenshots reviewed for names, IDs, and real values
- [ ] README examples use placeholder values only
