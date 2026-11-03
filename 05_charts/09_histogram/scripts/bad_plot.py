#!/usr/bin/env python3
"""«Плохая» гистограмма для раздела 5.09.

Что специально сделано неправильно
----------------------------------
1. Пять бинов: форма распределения скрыта, правый хвост исчез.
2. Ось X обрезана до 10–40: низкие и высокие значения не видны.
3. Радужные столбцы, чёрные края и тени: декор вместо данных.
4. Тяжёлая сетка по обеим осям и полная рамка.
5. Заголовок «Витамин D» ничего не сообщает.
6. Нет единиц, n, медианы и порога дефицита.

Выход: images/05_09_bad_histogram.{svg,png}
Запуск: uv run python 05_charts/09_histogram/scripts/bad_plot.py
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, save_figure


def main() -> None:
    apply_style()

    df = pd.read_csv(DATA_DIR / "09_dataset.csv")
    values = df["vitamin_d_ng_ml"].to_numpy()

    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    counts, bins, patches = ax.hist(
        values,
        bins=5,
        edgecolor="black",
        linewidth=2.0,
        zorder=3,
    )

    colors = plt.cm.jet(np.linspace(0.0, 1.0, len(patches)))
    for patch, color in zip(patches, colors, strict=True):
        patch.set_facecolor(color)
        patch.set_path_effects(
            [pe.withSimplePatchShadow(offset=(3, -3), shadow_rgbFace="0.5", alpha=0.6)]
        )

    ax.set_xlim(10, 40)
    ax.grid(True, which="major", axis="both", color="#BDBDBD", linewidth=1.0)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(1.5)
        spine.set_color("black")

    ax.tick_params(labelsize=12, width=1.4, length=5)
    ax.set_title("Витамин D", fontsize=18, fontweight="bold")
    ax.set_ylabel("Частота", fontsize=15)
    ax.set_xlabel("Уровень", fontsize=15)

    fig.tight_layout()
    save_figure(fig, "05_09_bad_histogram", formats=("svg", "png"), dpi=300)


if __name__ == "__main__":
    main()
