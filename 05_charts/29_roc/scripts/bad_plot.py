#!/usr/bin/env python3
"""«Плохая» ROC."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, save_figure


def roc(y, score):
    thresholds = np.r_[np.inf, np.sort(np.unique(score))[::-1]]
    fpr, tpr = [0.0], [0.0]
    for t in thresholds:
        pred = score >= t
        tp = np.sum(pred & (y == 1))
        fp = np.sum(pred & (y == 0))
        tpr.append(tp / np.sum(y == 1))
        fpr.append(fp / np.sum(y == 0))
    return np.array(fpr), np.array(tpr)


def main() -> None:
    apply_style()
    df = pd.read_csv(DATA_DIR / "29_dataset.csv")
    fpr, tpr = roc(df["disease"].to_numpy(), df["score"].to_numpy())
    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    ax.plot(fpr, tpr, color="#D62728", linewidth=3)
    ax.set_xlim(0, 0.8)
    ax.set_ylim(0, 0.8)
    ax.grid(True, axis="both", color="#BDBDBD", linewidth=1.0)
    ax.set_axisbelow(True)
    ax.set_title("ROC", fontsize=18, fontweight="bold")
    ax.set_xlabel("FPR", fontsize=14)
    ax.set_ylabel("TPR", fontsize=14)
    fig.tight_layout()
    save_figure(fig, "05_29_bad_roc", formats=("svg", "png"), dpi=300)


if __name__ == "__main__":
    main()
