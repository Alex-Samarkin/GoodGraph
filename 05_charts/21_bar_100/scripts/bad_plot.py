#!/usr/bin/env python3
"""«Плохой» 100 % stacked bar."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, save_figure

SEVERITY = ["лёгкая", "средняя", "тяжёлая"]


def main() -> None:
    apply_style()
    df = pd.read_csv(DATA_DIR / "21_dataset.csv")
    pivot = df.pivot(index="age_group", columns="severity", values="patients")[SEVERITY]
    share = pivot.div(pivot.sum(axis=1), axis=0) * 100

    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    left = np.zeros(len(share))
    colors = plt.cm.rainbow(np.linspace(0, 1, len(SEVERITY)))
    for severity, color in zip(SEVERITY, colors, strict=True):
        bars = ax.barh(share.index, share[severity], left=left, color=color,
                       edgecolor="black", linewidth=2, label=severity)
        for bar in bars:
            bar.set_path_effects([pe.withSimplePatchShadow(offset=(2, -2), alpha=0.5)])
        left += share[severity].to_numpy()

    ax.set_xlim(0, 100)
    ax.grid(True, axis="both", color="#BDBDBD", linewidth=1.0)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_linewidth(1.5)
    ax.tick_params(labelsize=11)
    ax.set_title("Тяжесть по возрасту", fontsize=18, fontweight="bold")
    ax.set_xlabel("%", fontsize=14)
    ax.legend(loc="lower right", fontsize=9, edgecolor="black")
    fig.tight_layout()
    save_figure(fig, "05_21_bad_bar_100", formats=("svg", "png"), dpi=300)


if __name__ == "__main__":
    main()
