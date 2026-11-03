#!/usr/bin/env python3
"""«Плохой» clustermap: без кластеризации и z-score."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd

from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, save_figure


def main() -> None:
    apply_style()
    df = pd.read_csv(DATA_DIR / "25_dataset.csv").set_index("gene")
    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    image = ax.imshow(df, cmap="jet", aspect="auto")
    ax.set_xticks(range(df.shape[1]))
    ax.set_xticklabels(df.columns, rotation=90, fontsize=7)
    ax.set_yticks(range(df.shape[0]))
    ax.set_yticklabels(df.index, fontsize=7)
    ax.set_title("Экспрессия генов", fontsize=18, fontweight="bold")
    fig.colorbar(image, ax=ax)
    fig.tight_layout()
    save_figure(fig, "05_25_bad_clustermap", formats=("svg", "png"), dpi=300)


if __name__ == "__main__":
    main()
