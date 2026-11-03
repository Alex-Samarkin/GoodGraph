#!/usr/bin/env python3
"""«Плохая» круговая диаграмма."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, save_figure


def main() -> None:
    apply_style()
    df = pd.read_csv(DATA_DIR / "22_dataset.csv")
    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    colors = plt.cm.rainbow(np.linspace(0, 1, len(df)))
    explode = [0.12, 0.05, 0.05, 0.05]
    ax.pie(df["patients"], colors=colors, explode=explode, shadow=True,
           startangle=20, wedgeprops={"edgecolor": "black", "linewidth": 2})
    ax.set_title("Причины", fontsize=18, fontweight="bold")
    ax.legend(df["cause"], loc="center left", bbox_to_anchor=(1.0, 0.5), fontsize=9)
    fig.tight_layout()
    save_figure(fig, "05_22_bad_pie", formats=("svg", "png"), dpi=300)


if __name__ == "__main__":
    main()
