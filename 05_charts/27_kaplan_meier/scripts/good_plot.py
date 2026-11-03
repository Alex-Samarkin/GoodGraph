#!/usr/bin/env python3
"""«Правильная» кривая Каплана–Мейера с риском."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from goodgraph.palettes import ACCENT_VERMILLION, PRIMARY_BLUE
from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, save_figure

GROUPS = [("Контроль", ACCENT_VERMILLION), ("Лечение", PRIMARY_BLUE)]
RISK_TIMES = [0, 12, 24, 36]


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
    apply_style(font_size=7)
    df = pd.read_csv(DATA_DIR / "27_dataset.csv")
    fig, (ax, ax_risk) = plt.subplots(
        2, 1, figsize=(95 / 25.4, 105 / 25.4),
        height_ratios=[4, 1], sharex=True,
        gridspec_kw={"hspace": 0.08},
    )
    fig.subplots_adjust(left=0.16, right=0.98, top=0.9, bottom=0.16)

    for group, color in GROUPS:
        sub = df[df["group"] == group]
        xs, ys = km(sub["time_months"].to_numpy(), sub["event"].to_numpy())
        ax.step(xs, ys, where="post", color=color, linewidth=1.6)
        cens = sub[sub["event"] == 0]["time_months"].to_numpy()
        for c in cens:
            y = ys[np.searchsorted(xs, c, side="right") - 1]
            ax.plot(c, y, marker="|", color=color, markersize=4, alpha=0.7)
        ax.text(37, ys[-1], group, color=color, fontsize=7, va="center", clip_on=False)

    ax.set_xlim(0, 36)
    ax.set_ylim(0, 1)
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.set_ylabel("Выживаемость")
    ax.set_title("Лечение снижает риск смерти", loc="left", fontsize=9.5, pad=8)
    ax.grid(axis="y", color="#E8E8E8", linewidth=0.6)
    ax.grid(axis="x", visible=False)

    ax_risk.axis("off")
    ax_risk.set_ylim(0, 1)
    ax_risk.text(0.0, 1.02, "Число под риском", transform=ax_risk.transAxes,
                 fontsize=6, ha="left", va="bottom")
    for row, (group, _) in enumerate(GROUPS):
        y = 0.68 if row == 0 else 0.22
        sub = df[df["group"] == group]
        ax_risk.text(-1.5, y, group, fontsize=6, ha="right", va="center")
        for t in RISK_TIMES:
            n = int((sub["time_months"] >= t).sum())
            ax_risk.text(t, y, str(n), fontsize=6, ha="center", va="center")
    for t in RISK_TIMES:
        ax_risk.text(t, 0.95, str(t), fontsize=5.5, ha="center", va="bottom", color="#555555")
    ax_risk.set_xlabel("Месяцы")

    save_figure(fig, "05_27_good_kaplan_meier", formats=("svg", "png"), dpi=600)


if __name__ == "__main__":
    main()
