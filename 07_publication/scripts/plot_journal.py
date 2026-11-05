#!/usr/bin/env python3
"""Журнальный и веб-рисунок раздела 7.

Строит двухпанельный рисунок 170 × 95 мм:
A — средние САД по неделям с 95 % CI;
B — изменение САД к 12-й неделе с 95 % CI.

Экспорт: SVG, PDF, PNG 600 dpi, TIFF LZW; отдельно — web PNG 1x/2x.
Запуск: uv run python 07_publication/scripts/plot_journal.py
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from journal_style import (
    apply_journal_style,
    apply_web_style,
    export_journal,
    export_web,
    web_figsize,
)
from scipy import stats

from goodgraph.palettes import ACCENT_VERMILLION, PRIMARY_BLUE
from goodgraph.paths import DATA_DIR, IMAGES_DIR
from goodgraph.style import panel_label

GROUPS = ["Контроль", "Препарат A", "Препарат B"]
COLORS = {"Контроль": "#777777", "Препарат A": PRIMARY_BLUE, "Препарат B": ACCENT_VERMILLION}


def summarize(df: pd.DataFrame) -> pd.DataFrame:
    out = df.groupby(["group", "week"])["sbp_mm_hg"].agg(["mean", "std", "count"]).reset_index()
    out["ci"] = 1.96 * out["std"] / np.sqrt(out["count"])
    return out


def changes(df: pd.DataFrame) -> pd.DataFrame:
    wide = (
        df.pivot_table(index=["patient_id", "group"], columns="week", values="sbp_mm_hg")
        .reset_index()
    )
    wide["change"] = wide[12] - wide[0]
    rows = []
    for group in GROUPS:
        values = wide.loc[wide["group"] == group, "change"].to_numpy()
        n = len(values)
        half = stats.t.ppf(0.975, n - 1) * values.std(ddof=1) / np.sqrt(n)
        rows.append((group, values.mean(), half))
    return pd.DataFrame(rows, columns=["group", "mean", "half"])


def main() -> None:
    apply_journal_style("nature", base_pt=7)
    df = pd.read_csv(DATA_DIR / "07_publication_dataset.csv")
    summary = summarize(df)
    change = changes(df)

    fig, (ax1, ax2) = plt.subplots(
        1,
        2,
        figsize=(170 / 25.4, 95 / 25.4),
        gridspec_kw={"width_ratios": [1.55, 1.0]},
        layout="constrained",
    )
    fig.set_constrained_layout_pads(w_pad=0.02, h_pad=0.02)

    for group in GROUPS:
        sub = summary[summary["group"] == group]
        ax1.errorbar(
            sub["week"], sub["mean"], yerr=sub["ci"],
            color=COLORS[group], marker="o", markersize=3,
            linewidth=1.0, capsize=2, label=group,
        )
        ax1.text(12.4, sub["mean"].iloc[-1], group, color=COLORS[group],
                 fontsize=6.2, va="center", clip_on=False)

    ax1.set_xlim(0, 15.5)
    ax1.set_ylim(125, 165)
    ax1.set_xticks([0, 4, 8, 12])
    ax1.set_xlabel("Неделя")
    ax1.set_ylabel("САД, мм рт. ст.")
    panel_label(ax1, "A", x=-0.16, y=1.04)

    y = np.arange(len(change))[::-1]
    ax2.axvline(0, color="#999999", linewidth=0.6, linestyle="--")
    for yi, (_, row) in zip(y, change.iterrows(), strict=True):
        color = COLORS[row["group"]]
        ax2.errorbar(row["mean"], yi, xerr=row["half"], fmt="o",
                     color=color, ecolor=color, markersize=3.5,
                     elinewidth=0.9, capsize=2)
    ax2.set_yticks(y)
    ax2.set_yticklabels(change["group"])
    ax2.set_ylim(-0.6, len(change) - 0.4)
    ax2.set_xlim(-25, 5)
    ax2.set_xlabel("Δ САД к 12-й неделе, мм")
    panel_label(ax2, "B", x=-0.22, y=1.04)

    paths = export_journal(
        fig, "07_journal_figure", outdir=IMAGES_DIR,
        formats=("svg", "pdf", "png", "tiff"), dpi=600,
    )
    plt.close(fig)
    print("Журнальные файлы:")
    for path in paths:
        print(" ", path.relative_to(IMAGES_DIR.parent))

    # --- веб-версия: один график, 960 × 480 px, 16 px base -----------------
    apply_web_style(base_px=16, dpi=160)
    web = plt.figure(figsize=web_figsize(960, 480, 160))
    ax = web.add_subplot(111)
    for group in GROUPS:
        sub = summary[summary["group"] == group]
        ax.errorbar(sub["week"], sub["mean"], yerr=sub["ci"],
                    color=COLORS[group], marker="o", linewidth=2, capsize=4, label=group)
    ax.set_xlim(0, 12)
    ax.set_ylim(125, 165)
    ax.set_xticks([0, 4, 8, 12])
    ax.set_xlabel("Неделя")
    ax.set_ylabel("САД, мм рт. ст.")
    ax.legend(loc="upper right", ncol=1)
    web.tight_layout()
    web_paths = export_web(web, "07_journal_web", outdir=IMAGES_DIR, dpi=160)
    plt.close(web)
    print("Веб-файлы:")
    for path in web_paths:
        print(" ", path.relative_to(IMAGES_DIR.parent))


if __name__ == "__main__":
    main()
