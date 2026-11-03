#!/usr/bin/env python3
"""«Плохая» кривая Каплана–Мейера."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, save_figure


def km(time, event):
    order = np.argsort(time)
    t, e = time[order], event[order]
    xs, ys = [0.0], [1.0]
    surv, at_risk = 1.0, len(t)
    for u in np.unique(t):
        n = at_risk
        d = int(np.sum((t == u) & (e == 1)))
        c = int(np.sum((t == u) & (e == 0)))
        if d:
            surv *= 1 - d / n
            xs.append(u)
            ys.append(surv)
        at_risk -= d + c
    return np.array(xs), np.array(ys)


def main() -> None:
    apply_style()
    df = pd.read_csv(DATA_DIR / "27_dataset.csv")
    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    colors = ["#D62728", "#2CA02C"]
    for (group, sub), color in zip(df.groupby("group"), colors, strict=True):
        xs, ys = km(sub["time_months"].to_numpy(), sub["event"].to_numpy())
        ax.step(xs, ys, where="post", color=color, linewidth=3, label=group)
    ax.set_xlim(0, 36)
    ax.set_ylim(0.5, 1.0)
    ax.grid(True, axis="both", color="#BDBDBD", linewidth=1.0)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_linewidth(1.5)
    ax.set_title("Выживаемость", fontsize=18, fontweight="bold")
    ax.set_xlabel("Месяцы", fontsize=14)
    ax.set_ylabel("Выживаемость", fontsize=14)
    ax.legend(loc="lower left", fontsize=9, edgecolor="black")
    fig.tight_layout()
    save_figure(fig, "05_27_bad_kaplan_meier", formats=("svg", "png"), dpi=300)


if __name__ == "__main__":
    main()
