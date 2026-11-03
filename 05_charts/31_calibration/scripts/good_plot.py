#!/usr/bin/env python3
"""«Правильная» калибровка: диагональ, Wilson CI, Brier."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from goodgraph.palettes import PRIMARY_BLUE
from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, figure_size, save_figure


def wilson(k, n, z=1.96):
    p = k / n
    den = 1 + z**2 / n
    mid = (p + z**2 / (2 * n)) / den
    half = z * np.sqrt(p * (1 - p) / n + z**2 / (4 * n**2)) / den
    return mid - half, mid + half


def main() -> None:
    apply_style(font_size=7)
    df = pd.read_csv(DATA_DIR / "31_dataset.csv")
    df["bin"] = pd.qcut(df["predicted_risk"], 8, labels=False, duplicates="drop")
    rows = []
    for _, sub in df.groupby("bin"):
        k, n = int(sub["outcome"].sum()), len(sub)
        low, high = wilson(k, n)
        rows.append((sub["predicted_risk"].mean(), k / n, low, high))
    x = np.array([r[0] for r in rows])
    y = np.array([r[1] for r in rows])
    low = np.array([r[2] for r in rows])
    high = np.array([r[3] for r in rows])
    brier = np.mean((df["predicted_risk"] - df["outcome"]) ** 2)

    fig, ax = plt.subplots(figsize=figure_size("single", height_mm=75), layout="constrained")
    fig.set_constrained_layout_pads(w_pad=0.04, h_pad=0.02)
    ax.plot([0, 1], [0, 1], color="#999999", linestyle="--", linewidth=0.8)
    ax.errorbar(x, y, yerr=[y - low, high - y], fmt="o", color=PRIMARY_BLUE,
                ecolor=PRIMARY_BLUE, markersize=4.5, elinewidth=1.0, capsize=0)
    ax.text(0.03, 0.92, f"Brier = {brier:.3f}".replace(".", ","), fontsize=7.5)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1])
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
    ax.set_xlabel("Прогнозируемый риск")
    ax.set_ylabel("Наблюдаемая частота")
    ax.set_title("Калибровка: небольшая недооценка риска", loc="left", fontsize=9, pad=6)
    ax.grid(axis="y", color="#E8E8E8", linewidth=0.6)
    ax.grid(axis="x", visible=False)
    save_figure(fig, "05_31_good_calibration", formats=("svg", "png"), dpi=600)
    print(f"Brier={brier:.3f}")


if __name__ == "__main__":
    main()
