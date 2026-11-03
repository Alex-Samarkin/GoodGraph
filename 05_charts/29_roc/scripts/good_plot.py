#!/usr/bin/env python3
"""«Правильная» ROC."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from goodgraph.palettes import PRIMARY_BLUE
from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, figure_size, save_figure


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
    apply_style(font_size=7)
    df = pd.read_csv(DATA_DIR / "29_dataset.csv")
    y = df["disease"].to_numpy()
    fpr, tpr = roc(y, df["score"].to_numpy())
    auc = np.trapezoid(tpr, fpr)

    fig, ax = plt.subplots(figsize=figure_size("single", height_mm=72), layout="constrained")
    fig.set_constrained_layout_pads(w_pad=0.04, h_pad=0.02)
    ax.plot([0, 1], [0, 1], color="#999999", linestyle="--", linewidth=0.8)
    ax.plot(fpr, tpr, color=PRIMARY_BLUE, linewidth=1.8)
    ax.text(0.03, 0.95, f"AUC = {auc:.2f}".replace(".", ","), fontsize=7.5,
            va="top", color="#333333")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1])
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
    ax.set_xlabel("FPR (1 − специфичность)")
    ax.set_ylabel("TPR (чувствительность)")
    ax.set_title(f"ROC: AUC = {auc:.2f}".replace(".", ","), loc="left", fontsize=9.5, pad=6)
    ax.grid(axis="y", color="#E8E8E8", linewidth=0.6)
    ax.grid(axis="x", visible=False)
    save_figure(fig, "05_29_good_roc", formats=("svg", "png"), dpi=600)
    print(f"AUC={auc:.3f}")


if __name__ == "__main__":
    main()
