#!/usr/bin/env python3
"""«Правильная» кумулятивная заболеваемость с конкурирующим риском."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from goodgraph.palettes import ACCENT_VERMILLION, PRIMARY_BLUE
from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, figure_size, save_figure


def cif(time, status, cause):
    order = np.argsort(time)
    t, s = time[order], status[order]
    xs, ys = [0.0], [0.0]
    surv, inc, at_risk = 1.0, 0.0, len(t)
    for u in np.unique(t):
        n = at_risk
        d1 = int(np.sum((t == u) & (s == 1)))
        d2 = int(np.sum((t == u) & (s == 2)))
        d = d1 if cause == 1 else d2
        inc += surv * d / n
        if d:
            xs.append(u)
            ys.append(inc)
        surv *= 1 - (d1 + d2) / n
        at_risk -= d1 + d2
    return np.array(xs), np.array(ys)


def main() -> None:
    apply_style(font_size=7)
    df = pd.read_csv(DATA_DIR / "28_dataset.csv")
    time = df["time_months"].to_numpy()
    status = df["status"].to_numpy()
    fig, ax = plt.subplots(figsize=figure_size("single", height_mm=75), layout="constrained")
    fig.set_constrained_layout_pads(w_pad=0.04, h_pad=0.02)
    for cause, color, label in [(1, ACCENT_VERMILLION, "Кардиальная смерть"),
                                (2, PRIMARY_BLUE, "Некардиальная смерть")]:
        xs, ys = cif(time, status, cause)
        ax.step(xs, ys, where="post", color=color, linewidth=1.7, label=label)
        ax.text(36.8, ys[-1], label, color=color, fontsize=6.5, va="center", clip_on=False)
    ax.set_xlim(0, 36)
    ax.set_ylim(0, 0.55)
    ax.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5])
    ax.set_xlabel("Месяцы")
    ax.set_ylabel("Кумулятивная incidence")
    ax.set_title("Кардиальная смерть — 35 % к 36 месяцам", loc="left", fontsize=9, pad=6)
    ax.grid(axis="y", color="#E8E8E8", linewidth=0.6)
    ax.grid(axis="x", visible=False)
    save_figure(fig, "05_28_good_cumulative_incidence", formats=("svg", "png"), dpi=600)


if __name__ == "__main__":
    main()
