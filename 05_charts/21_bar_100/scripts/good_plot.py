#!/usr/bin/env python3
"""«Правильный» 100 % stacked bar."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, figure_size, save_figure

SEVERITY = ["лёгкая", "средняя", "тяжёлая"]
COLORS = ["#0072B2", "#E69F00", "#D55E00"]
ORDER = ["<40", "40–59", "60–74", "75+"]


def main() -> None:
    apply_style(font_size=7)
    df = pd.read_csv(DATA_DIR / "21_dataset.csv")
    pivot = df.pivot(index="age_group", columns="severity", values="patients")[SEVERITY].loc[ORDER]
    share = pivot.div(pivot.sum(axis=1), axis=0) * 100

    fig, ax = plt.subplots(figsize=figure_size("single", height_mm=75), layout="constrained")
    fig.set_constrained_layout_pads(w_pad=0.04, h_pad=0.04)
    left = np.zeros(len(share))
    for severity, color in zip(SEVERITY, COLORS, strict=True):
        bars = ax.barh(share.index, share[severity], left=left, color=color,
                       height=0.62, label=severity)
        for bar, value in zip(bars, share[severity], strict=True):
            if value >= 8:
                ax.text(bar.get_x() + value / 2, bar.get_y() + bar.get_height() / 2,
                        f"{value:.0f}", ha="center", va="center", fontsize=6,
                        color="white" if severity != "средняя" else "#333333")
        left += share[severity].to_numpy()

    for y, total in enumerate(pivot.sum(axis=1)):
        ax.text(101.5, y, f"n={int(total)}", va="center", fontsize=6, color="#333333")

    ax.set_xlim(0, 100)
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.set_xlabel("Доля, %")
    ax.set_title("Тяжёлая степень растёт с возрастом", loc="left", fontsize=9.5, pad=18)
    ax.legend(loc="lower left", bbox_to_anchor=(0, 1.02), ncol=3, frameon=False,
              fontsize=6.5, handlelength=1.2)
    ax.grid(axis="x", color="#E8E8E8", linewidth=0.6)
    ax.grid(axis="y", visible=False)
    save_figure(fig, "05_21_good_bar_100", formats=("svg", "png"), dpi=600)


if __name__ == "__main__":
    main()
