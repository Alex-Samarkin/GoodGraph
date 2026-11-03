#!/usr/bin/env python3
"""«Правильные» малые кратные для раздела 5.04.

Что улучшено
------------
1. Каждое отделение — своя панель: линии не перекрываются.
2. Общая шкала Y 0–150: панели честно сравнимы.
3. Один цвет для всех панелей; сравнение идёт по форме и уровню.
4. Общие деления X: Янв/Апр/Июл/Окт/Дек.
5. Подписи осей только по краям сетки, без дублирования.
6. Заголовок-вывод: ОРИТ потребляет в 2,4 раза больше кардиологии.
7. Лёгкая сетка по Y, без верхней и правой рамок.
8. 170 мм — две журнальные колонки.

Выход: images/05_04_good_small_multiples.{svg,png}
Запуск: uv run python 05_charts/04_small_multiples/scripts/good_plot.py
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from goodgraph.palettes import PRIMARY_BLUE
from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, figure_size, save_figure

MONTHS = ["Янв", "Фев", "Мар", "Апр", "Май", "Июн", "Июл", "Авг", "Сен", "Окт", "Ноя", "Дек"]
TICKS = [0, 3, 6, 9, 11]


def main() -> None:
    apply_style(font_size=7)

    df = pd.read_csv(DATA_DIR / "04_dataset.csv")
    pivot = df.pivot(index="month", columns="department", values="ddd_per_100_bed_days")
    departments = list(pivot.columns)
    x = np.arange(len(MONTHS))

    fig, axes = plt.subplots(
        2,
        3,
        figsize=figure_size("double", height_mm=100),
        sharex=True,
        sharey=True,
        layout="constrained",
    )
    fig.set_constrained_layout_pads(w_pad=0.04, h_pad=0.04)
    axes = axes.ravel()

    for index, (ax, department) in enumerate(zip(axes, departments, strict=True)):
        ax.plot(
            x,
            pivot[department].to_numpy(),
            color=PRIMARY_BLUE,
            linewidth=1.6,
            marker="o",
            markersize=2.6,
            markeredgecolor="white",
            markeredgewidth=0.5,
        )
        ax.set_title(department, loc="left", fontsize=8, pad=3)
        ax.set_ylim(0, 150)
        ax.set_yticks([0, 50, 100, 150])
        ax.set_xticks(TICKS)
        ax.set_xticklabels([MONTHS[i] for i in TICKS])
        ax.grid(axis="y", color="#E8E8E8", linewidth=0.5)
        ax.grid(axis="x", visible=False)

        if index % 3 == 0:
            ax.set_ylabel("DDD/100 койко-дней")
        if index >= 3:
            ax.set_xlabel("Месяц")

    mean_by_department = df.groupby("department")["ddd_per_100_bed_days"].mean()
    ratio = mean_by_department["ОРИТ"] / mean_by_department["Кардиология"]
    fig.suptitle(
        f"ОРИТ потребляет в {ratio:.1f} раза больше кардиологии".replace(".", ","),
        x=0.01,
        ha="left",
        fontsize=9.5,
    )

    save_figure(fig, "05_04_good_small_multiples", formats=("svg", "png"), dpi=600)

    print("Среднее по отделениям:")
    print(mean_by_department.round(1).to_string())
    print(f"Отношение ОРИТ / Кардиология: {ratio:.2f}")


if __name__ == "__main__":
    main()
