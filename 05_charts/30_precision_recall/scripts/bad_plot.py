#!/usr/bin/env python3
"""«Плохой» PR: без baseline и AP, обрезанные оси."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, save_figure


def pr(y, score):
    thresholds = np.r_[np.inf, np.sort(np.unique(score))[::-1]]
    recall, precision = [0.0], [1.0]
    for t in thresholds:
        pred = score >= t
        tp = np.sum(pred & (y == 1))
        fp = np.sum(pred & (y == 0))
        fn = np.sum((~pred) & (y == 1))
        recall.append(tp / (tp + fn))
        precision.append(tp / (tp + fp) if tp + fp else 1.0)
    return np.array(recall), np.array(precision)


def main() -> None:
    apply_style()
    df = pd.read_csv(DATA_DIR / "30_dataset.csv")
    recall, precision = pr(df["event"].to_numpy(), df["score"].to_numpy())
    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    ax.plot(recall, precision, color="#D62728", linewidth=3)
    ax.set_xlim(0.2, 1.0)
    ax.set_ylim(0.2, 1.0)
    ax.grid(True, axis="both", color="#BDBDBD", linewidth=1.0)
    ax.set_axisbelow(True)
    ax.set_title("Precision–recall", fontsize=18, fontweight="bold")
    ax.set_xlabel("Recall", fontsize=14)
    ax.set_ylabel("Precision", fontsize=14)
    fig.tight_layout()
    save_figure(fig, "05_30_bad_precision_recall", formats=("svg", "png"), dpi=300)


if __name__ == "__main__":
    main()
