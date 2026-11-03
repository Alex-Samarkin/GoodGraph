#!/usr/bin/env python3
"""«Плохой» treemap."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import squarify

from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, save_figure


def main() -> None:
    apply_style()
    df = pd.read_csv(DATA_DIR / "23_dataset.csv")
    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    colors = plt.cm.rainbow(np.linspace(0, 1, len(df)))
    squarify.plot(
        sizes=df["cost_mln_rub"],
        label=df["program"],
        color=colors,
        ax=ax,
        text_kwargs={"fontsize": 14, "color": "black"},
        bar_kwargs={"edgecolor": "black", "linewidth": 3},
    )
    for rect in ax.patches:
        rect.set_path_effects([pe.withSimplePatchShadow(offset=(3, -3), alpha=0.5)])
    ax.set_title("Затраты", fontsize=18, fontweight="bold")
    ax.axis("off")
    save_figure(fig, "05_23_bad_treemap", formats=("svg", "png"), dpi=300)


if __name__ == "__main__":
    main()
