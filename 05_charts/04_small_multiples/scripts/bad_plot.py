#!/usr/bin/env python3
"""«Плохой» график для раздела 5.04: шесть серий на одной оси.

Что специально сделано неправильно
----------------------------------
1. Шесть отделений на одном графике: линии перекрываются, сравнение
   невозможно.
2. Радужная палитра из шести цветов.
3. Ось Y обрезана до 30–140: низкие значения искажены.
4. Толстые линии с тенями и крупными маркерами.
5. Тяжёлая сетка по обеим осям и полная рамка.
6. Заголовок «Потребление антибиотиков» ничего не сообщает.
7. Нет единиц, n и расшифровки отделений.
8. Легенда из шести строк закрывает данные.

Выход: images/05_04_bad_small_multiples.{svg,png}
Запуск: uv run python 05_charts/04_small_multiples/scripts/bad_plot.py
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

MONTHS = ["Янв", "Фев", "Мар", "Апр", "Май", "Июн", "Июл", "Авг", "Сен", "Окт", "Ноя", "Дек"]


def main() -> None:
    apply_style()

    df = pd.read_csv(DATA_DIR / "04_dataset.csv")
    pivot = df.pivot(index="month", columns="department", values="ddd_per_100_bed_days")
    departments = list(pivot.columns)
    x = np.arange(len(MONTHS))
    colors = plt.cm.rainbow(np.linspace(0.0, 1.0, len(departments)))

    fig, ax = plt.subplots(figsize=(6.4, 4.8))

    for department, color in zip(departments, colors, strict=True):
        (line,) = ax.plot(
            x,
            pivot[department].to_numpy(),
            color=color,
            linewidth=3.0,
            marker="o",
            markersize=6,
            markeredgecolor="white",
            markeredgewidth=0.5,
            label=department,
            zorder=3,
        )
        line.set_path_effects(
            [
                pe.SimpleLineShadow(offset=(1.5, -1.5), shadow_color="0.5", alpha=0.5),
                pe.Normal(),
            ]
        )

    ax.set_ylim(30, 140)
    ax.set_yticks(np.arange(30, 141, 10))

    ax.grid(True, which="major", axis="both", color="#BDBDBD", linewidth=1.0)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(1.5)
        spine.set_color("black")

    ax.tick_params(labelsize=11, width=1.4, length=5)
    ax.set_xticks(x)
    ax.set_xticklabels(MONTHS, fontsize=10)

    ax.set_title("Потребление антибиотиков", fontsize=18, fontweight="bold")
    ax.set_ylabel("DDD", fontsize=15)
    ax.set_xlabel("Месяц", fontsize=15)

    ax.legend(
        loc="upper right",
        fontsize=8,
        frameon=True,
        edgecolor="black",
        facecolor="white",
        ncol=1,
    )

    fig.tight_layout()
    save_figure(fig, "05_04_bad_small_multiples", formats=("svg", "png"), dpi=300)


if __name__ == "__main__":
    main()
