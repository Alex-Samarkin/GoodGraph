#!/usr/bin/env python3
"""«Правильный» scatter для раздела 5.05.

Что улучшено
------------
1. Полный диапазон осей: 15–45 кг/м² и 3–12 ммоль/л; точки не обрезаны.
2. Полупрозрачные точки одного цвета: видна плотность, нет overplotting.
3. Линия регрессии только в диапазоне данных, без экстраполяции.
4. Подпись r и n: связь quantified, а не «на глаз».
5. Единицы на осях, заголовок-вывод.
6. Лёгкая сетка только по Y, без верхней и правой рамок.
7. 85 мм — конечный журнальный размер.

Выход: images/05_05_good_scatter.{svg,png}
Запуск: uv run python 05_charts/05_scatter/scripts/good_plot.py
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

from goodgraph.palettes import PRIMARY_BLUE
from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, figure_size, save_figure


def main() -> None:
    apply_style()

    df = pd.read_csv(DATA_DIR / "05_dataset.csv")
    x = df["bmi_kg_m2"].to_numpy()
    y = df["glucose_mmol_l"].to_numpy()

    fig, ax = plt.subplots(
        figsize=figure_size("single", height_mm=72),
        layout="constrained",
    )
    fig.set_constrained_layout_pads(w_pad=0.04, h_pad=0.02)

    ax.scatter(
        x,
        y,
        s=12,
        color=PRIMARY_BLUE,
        alpha=0.35,
        linewidths=0,
        zorder=2,
    )

    slope, intercept, r_value, p_value, _ = stats.linregress(x, y)
    line_x = np.array([x.min(), x.max()])
    ax.plot(
        line_x,
        intercept + slope * line_x,
        color="#333333",
        linewidth=1.4,
        zorder=3,
    )

    r_text = f"{r_value:.2f}".replace(".", ",")
    ax.text(
        16.5,
        11.8,
        f"r = {r_text}; n = {len(df)}",
        ha="left",
        va="top",
        fontsize=7.5,
        color="#333333",
    )

    ax.set_xlim(15, 45)
    ax.set_ylim(3, 12)
    ax.set_xticks([15, 25, 35, 45])
    ax.set_yticks([3, 6, 9, 12])

    ax.set_xlabel("BMI, кг/м²")
    ax.set_ylabel("Глюкоза, ммоль/л")
    ax.set_title("Глюкоза растёт с BMI", loc="left", fontsize=9.5, pad=6)

    ax.grid(axis="y", color="#E8E8E8", linewidth=0.6)
    ax.grid(axis="x", visible=False)

    save_figure(fig, "05_05_good_scatter", formats=("svg", "png"), dpi=600)

    print(f"r = {r_value:.3f}, p = {p_value:.3g}, n = {len(df)}")
    print(f"Наклон: {slope:.3f} ммоль/л на 1 кг/м²")


if __name__ == "__main__":
    main()
