#!/usr/bin/env python3
"""
Quality WoW Tracker — public demo (mock data)
=============================================
Compares two weekly quality CSVs (previous vs. current) across several defect
metrics and writes a ranked Excel report per metric into a per-week folder.

Sanitized, self-contained demo. Runs on bundled mock CSVs — no internal
systems, URLs, or PII.

Usage:
    pip install pandas numpy openpyxl
    python quality_wow_demo.py
"""

import os
import re
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
PREV_CSV = os.path.join(HERE, "mock_week_prev.csv")
CURR_CSV = os.path.join(HERE, "mock_week_curr.csv")
REPORTS_BASE = os.path.join(HERE, "reports")

# metric key -> (csv_column, short_label, mode)
#   'improvers' -> fewer is better; lead report = top improvers
#   'offenders' -> more is worse;   lead report = top offenders
METRICS = {
    "DefectA":   ("defect_events_a",       "Defect A",      "improvers"),
    "DropExc":   ("drop_to_exception",     "Drop-Exception", "offenders"),
    "QtyDefect": ("quantity_defect_events", "Qty Defect",    "improvers"),
    "BinViol":   ("bin_violation",         "Bin Violation", "improvers"),
}

MIN_OPPORTUNITIES = 0  # include everyone in the demo


def load_week(path):
    """Load a weekly quality CSV with forgiving header matching."""
    df = pd.read_csv(path)
    df.columns = [str(c).strip() for c in df.columns]
    norm = {c.lower(): c for c in df.columns}
    needed = ["userId", "supervisor", "Opportunities"] + [m[0] for m in METRICS.values()]
    rename = {}
    missing = []
    for want in needed:
        if want in df.columns:
            continue
        if want.lower() in norm:
            rename[norm[want.lower()]] = want
        else:
            missing.append(want)
    if rename:
        df = df.rename(columns=rename)
    if missing:
        raise ValueError(f"Missing columns {missing}; found {list(df.columns)}")
    return df


def wow_compare(prev_df, curr_df, metric_col):
    """Per-associate week-over-week delta for one metric (lower = better)."""
    p = prev_df[prev_df["Opportunities"] >= MIN_OPPORTUNITIES]
    c = curr_df[curr_df["Opportunities"] >= MIN_OPPORTUNITIES]
    merged = pd.merge(
        c[["userId", "supervisor", metric_col]],
        p[["userId", metric_col]],
        on="userId", how="inner", suffixes=("_curr", "_prev"),
    )
    merged["delta"] = merged[f"{metric_col}_curr"] - merged[f"{metric_col}_prev"]
    # negative delta = improvement (fewer defects)
    return merged


def week_num_from_filename(path):
    m = re.search(r"[Ww]eek[ _]?(\d+)", os.path.basename(path))
    return m.group(1) if m else "NN"


def main():
    prev_df = load_week(PREV_CSV)
    curr_df = load_week(CURR_CSV)
    week = week_num_from_filename(CURR_CSV)

    out_dir = os.path.join(REPORTS_BASE, "weekly", f"Week {week}")
    os.makedirs(out_dir, exist_ok=True)

    for key, (col, label, mode) in METRICS.items():
        cmp = wow_compare(prev_df, curr_df, col)
        if mode == "improvers":
            lead = cmp.sort_values("delta").head(25)          # most negative = best improvers
            lead_name = "Top Improvers"
        else:
            lead = cmp.sort_values("delta", ascending=False).head(25)  # most positive = worst
            lead_name = "Top Offenders"

        out_path = os.path.join(out_dir, f"Week {week} {label} report.xlsx")
        with pd.ExcelWriter(out_path, engine="openpyxl") as xl:
            lead.to_excel(xl, sheet_name=lead_name[:31], index=False)
            cmp.sort_values("delta").to_excel(xl, sheet_name="All", index=False)

        print(f"[{label}] {lead_name}: {len(lead)} rows -> {out_path}")
        preview = lead[["userId", "supervisor", "delta"]].head(3).to_string(index=False)
        print(preview + "\n")


if __name__ == "__main__":
    main()
