#!/usr/bin/env python3
"""«Плохой» forest plot для раздела 5.16.

Что специально сделано неправильно
----------------------------------
1. Нет доверительных интервалов: только точки OR.
2. Линейная ось 0,4–1,2 вместо логарифмической.
3. Нет линии «нет эффекта» (OR = 1).
4. Радужные точки, тяжёлая сетка, полная рамка.
5. Нет общей оценки (ромба), единиц и n.
6. Заголовок «Эффект лечения» ничего не сообщает.

Выход: images/05_16_bad_forest.{svg,png}
Запуск: uv run python 05_charts/16_forest/scripts/bad_plot.py
"""

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

    df = pd.read_csv(DATA_DIR / "16_dataset.csv")
    sub = df[df["subgroup"] != "Все пациенты"].reset_index(drop=True)
    y = np.arange(len(sub))[::-1]

    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    colors = plt.cm.rainbow(np.linspace(0.0, 1.0, len(sub)))
    for yi, (_, row), color in zip(y, sub.iterrows(), colors, strict=True):
        a = row["events_treatment"]
        b = row["n_treatment"] - a
        c = row["events_control"]
        d = row["n_control"] - c
        odds = (a / b) / (c / d)
        ax.scatter(odds, yi, s=120, color=color, edgecolors="black", linewidths=0.8, zorder=3)

    ax.set_xlim(0.4, 1.2)
    ax.set_ylim(-0.5, len(sub) - 0.5)
    ax.set_yticks(y)
    ax.set_yticklabels(sub["subgroup"], fontsize=10)

    ax.grid(True, which="major", axis="both", color="#BDBDBD", linewidth=1.0)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(1.5)
        spine.set_color("black")

    ax.tick_params(labelsize=11, width=1.3, length=5)
    ax.set_title("Эффект лечения", fontsize=18, fontweight="bold")
    ax.set_xlabel("OR", fontsize=14)

    fig.tight_layout()
    save_figure(fig, "05_16_bad_forest", formats=("svg", "png"), dpi=300)


if __name__ == "__main__":
    main()
