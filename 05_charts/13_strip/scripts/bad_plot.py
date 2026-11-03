#!/usr/bin/env python3
"""«Плохой» strip plot для раздела 5.13.

Что специально сделано неправильно
----------------------------------
1. Все точки стоят строго по центру группы: overplotting, 30 точек
   сливаются в одну.
2. Радужные точки по группам, крупные и непрозрачные.
3. Ось Y обрезана до 30–70: низкие и высокие значения скрыты.
4. Тяжёлая сетка, полная рамка.
5. Заголовок «Боль по группам» ничего не сообщает.
6. Нет медиан, единиц и n.

Выход: images/05_13_bad_strip.{svg,png}
Запуск: uv run python 05_charts/13_strip/scripts/bad_plot.py
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, save_figure

GROUPS = ["НПВС", "опиоид", "комбинация"]


def main() -> None:
    apply_style()

    df = pd.read_csv(DATA_DIR / "13_dataset.csv")
    fig, ax = plt.subplots(figsize=(6.4, 4.8))

    colors = plt.cm.rainbow(np.linspace(0.0, 1.0, len(GROUPS)))
    for position, (group, color) in enumerate(zip(GROUPS, colors, strict=True), start=1):
        values = df.loc[df["analgesia"] == group, "vas_mm"].to_numpy()
        ax.scatter(
            np.full(len(values), position),
            values,
            s=80,
            color=color,
            alpha=1.0,
            edgecolors="black",
            linewidths=0.6,
            zorder=3,
        )

    ax.set_xlim(0.5, 3.5)
    ax.set_ylim(30, 70)
    ax.grid(True, which="major", axis="both", color="#BDBDBD", linewidth=1.0)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(1.5)
        spine.set_color("black")

    ax.tick_params(labelsize=12, width=1.4, length=5)
    ax.set_xticks([1, 2, 3])
    ax.set_xticklabels(GROUPS, fontsize=11)
    ax.set_title("Боль по группам", fontsize=18, fontweight="bold")
    ax.set_ylabel("ВАШ", fontsize=15)
    ax.set_xlabel("Схема обезболивания", fontsize=15)

    fig.tight_layout()
    save_figure(fig, "05_13_bad_strip", formats=("svg", "png"), dpi=300)


if __name__ == "__main__":
    main()
