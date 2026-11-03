#!/usr/bin/env python3
"""«Плохой» slope plot для раздела 5.17.

Что специально сделано неправильно
----------------------------------
1. Шесть радужных линий без подписей: непонятно, где какая клиника.
2. Ось Y обрезана до 82–102: нижние значения и размах скрыты.
3. Нет подписей «до/после» и единиц.
4. Тяжёлая сетка, полная рамка.
5. Заголовок «Вес до и после» ничего не сообщает.
6. Нет n и изменения в кг.

Выход: images/05_17_bad_slope.{svg,png}
Запуск: uv run python 05_charts/17_slope/scripts/bad_plot.py
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

    df = pd.read_csv(DATA_DIR / "17_dataset.csv")
    summary = df.groupby("clinic")[["weight_before_kg", "weight_after_kg"]].mean()

    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    colors = plt.cm.rainbow(np.linspace(0.0, 1.0, len(summary)))
    for (_, row), color in zip(summary.iterrows(), colors, strict=True):
        ax.plot(
            [0, 1],
            [row["weight_before_kg"], row["weight_after_kg"]],
            color=color,
            linewidth=3.0,
            marker="o",
            markersize=9,
            markeredgecolor="black",
        )

    ax.set_xlim(-0.1, 1.1)
    ax.set_ylim(82, 102)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["1", "2"], fontsize=11)

    ax.grid(True, which="major", axis="both", color="#BDBDBD", linewidth=1.0)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(1.5)
        spine.set_color("black")

    ax.tick_params(labelsize=12, width=1.4, length=5)
    ax.set_title("Вес до и после", fontsize=18, fontweight="bold")
    ax.set_ylabel("Вес", fontsize=15)

    fig.tight_layout()
    save_figure(fig, "05_17_bad_slope", formats=("svg", "png"), dpi=300)


if __name__ == "__main__":
    main()
