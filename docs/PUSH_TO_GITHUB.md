# How to Push This Repo to GitHub

I built the repo folder for you, but I can't push to GitHub on your behalf. Here's the
one-time setup. **Do the pre-publish check first** — this is a public repo.

## 0. Pre-publish safety check (do this first)

From inside the repo folder, confirm nothing internal slipped in:

```bash
# These should all return NOTHING:
git grep -i "amazon.dev"      || echo "clean"
git grep -i "harmony"         || echo "clean"
git grep -i "a2z.com"         || echo "clean"
git grep -i "corp.amazon"     || echo "clean"
# No real data or userscripts:
ls **/*.user.js 2>/dev/null   || echo "no userscripts (good)"
```

Also open `docs/SANITIZATION.md` and tick the checklist at the bottom.

## 1. Create the repo on GitHub

- Go to <https://github.com/new>
- Name it e.g. `ops-analytics-portfolio`
- **Public**
- Do **not** initialize with a README (this folder already has one)

## 2. Initialize and push

From inside this folder:

```bash
git init
git add .
git commit -m "Initial commit: operations analytics portfolio"
git branch -M main
git remote add origin https://github.com/<your-username>/ops-analytics-portfolio.git
git push -u origin main
```

## 3. Make it look good

- Add repo **topics**: `python`, `pandas`, `data-analytics`, `operations`, `dashboard`,
  `automation`
- Set the **description**: *"Operations analytics tools — dashboards and automated
  reporting for a high-volume fulfillment environment (sanitized showcase)."*
- (Optional) Enable GitHub Pages from `/docs` if you want a simple project site.

## 4. Add screenshots

Drop redaction-safe, mock-data screenshots into `docs/screenshots/` and reference them in
the project READMEs. The adapts trend chart (`projects/adapts-feedback-tracker/trend.png`)
is already mock-data-safe and can be shown.

---

**Reminder:** if you ever want the *real* tools in version control, use an **internal**
Git host, never public GitHub.
