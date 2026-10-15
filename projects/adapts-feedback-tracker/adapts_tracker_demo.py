#!/usr/bin/env python3
"""
Adapts Feedback Tracker — public demo (mock data)
=================================================
Summarizes weekly behavioral-feedback completion and plots a WoW trend.

This is a sanitized, self-contained demo. It runs entirely on the bundled
mock CSV — no internal systems, URLs, or PII involved.

Usage:
    pip install pandas matplotlib
    python adapts_tracker_demo.py
"""

import os
import matplotlib
matplotlib.use("Agg")  # headless-safe
import matplotlib.pyplot as plt
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
MOCK_CSV = os.path.join(HERE, "mock_feedback_data.csv")


def summarize_feedback(csv_path):
    """Summarize a weekly feedback CSV into compliance metrics.

    Expected columns (case-insensitive, whitespace-tolerant):
        week, supervisor, status  where status in {completed, pending, exempted}
    """
    df = pd.read_csv(csv_path)
    df.columns = [str(c).strip().lower() for c in df.columns]
    df["status"] = df["status"].str.strip().str.lower()

    total = len(df)
    completed = int((df["status"] == "completed").sum())
    pending = int((df["status"] == "pending").sum())
    exempted = int((df["status"] == "exempted").sum())
    completion_pct = round(100 * completed / total, 1) if total else 0.0

    pending_by_sup = (
        df[df["status"] == "pending"]
        .groupby("supervisor")
        .size()
        .sort_values(ascending=False)
    )

    return {
        "total": total,
        "completed": completed,
        "pending": pending,
        "exempted": exempted,
        "completion_pct": completion_pct,
        "pending_by_supervisor": pending_by_sup,
    }


def plot_trend(weeks, completion_pcts, pending, exempted, output_path):
    """Completion % line + pending/exempted bars across recent weeks."""
    fig, ax1 = plt.subplots(figsize=(9, 5))
    x = range(len(weeks))

    ax1.bar([i - 0.2 for i in x], pending, width=0.4, label="Pending",
            color="#E8A33D")
    ax1.bar([i + 0.2 for i in x], exempted, width=0.4, label="Exempted",
            color="#9AA0A6")
    ax1.set_ylabel("Count")
    ax1.set_xticks(list(x))
    ax1.set_xticklabels(weeks)

    ax2 = ax1.twinx()
    ax2.plot(x, completion_pcts, "o-", linewidth=2.5, color="#2E7D32",
             label="Completion %")
    ax2.set_ylabel("Completion %")
    ax2.set_ylim(0, 100)

    ax1.set_title("Adapts Feedback Completion — WoW Trend (mock data)")
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")
    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    print(f"Saved trend chart -> {output_path}")


def main():
    res = summarize_feedback(MOCK_CSV)
    print("\nWeek 38 Feedback Compliance — SITE (mock data)")
    print(f"  Total items ....... {res['total']}")
    print(f"  Completed ......... {res['completed']}  ({res['completion_pct']}%)")
    print(f"  Pending ........... {res['pending']}")
    print(f"  Exempted .......... {res['exempted']}")
    print("\nPending by supervisor:")
    for sup, n in res["pending_by_supervisor"].items():
        print(f"  {sup} ...... {n}")

    # Illustrative multi-week trend (mock)
    weeks = ["W35", "W36", "W37", "W38"]
    completion_pcts = [76.8, 56.8, 51.2, 57.5]
    pending = [22, 72, 77, 12]
    exempted = [38, 14, 29, 5]
    plot_trend(weeks, completion_pcts, pending, exempted,
               os.path.join(HERE, "trend.png"))


if __name__ == "__main__":
    main()
