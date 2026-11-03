#!/usr/bin/env python3
"""«Плохой» scatter для раздела 5.05.

Что специально сделано неправильно
----------------------------------
1. Оси обрезаны до 20–38 и 4–10: часть точек и хвосты скрыты.
2. Точки окрашены по BMI, хотя BMI уже на оси X: двойное кодирование
   и радужная шкала.
3. Крупные непрозрачные маркеры с чёрной обводкой: overplotting.
4. Красная линия регрессии без доверительной полосы и без статистики.
5. Тяжёлая сетка по обеим осям и полная рамка.
6. Заголовок «Связь BMI и глюкозы» ничего не сообщает.
7. Нет единиц, n и коэффициента корреляции.
8. Цветовая шкала BMI дублирует ось X.

Выход: images/05_05_bad_scatter.{svg,png}
Запуск: uv run python 05_charts/05_scatter/scripts/bad_plot.py
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, save_figure


def main() -> None:
    apply_style()

    df = pd.read_csv(DATA_DIR / "05_dataset.csv")
    x = df["bmi_kg_m2"].to_numpy()
    y = df["glucose_mmol_l"].to_numpy()

    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    scatter = ax.scatter(
        x,
        y,
        s=90,
        c=x,
        cmap="jet",
        edgecolors="black",
        linewidths=0.6,
        zorder=3,
    )

    slope, intercept, *_ = stats.linregress(x, y)
    line_x = np.array([20, 38])
    ax.plot(line_x, intercept + slope * line_x, color="#D62728", linewidth=3.0, zorder=4)

    ax.set_xlim(20, 38)
    ax.set_ylim(4, 10)

    ax.grid(True, which="major", axis="both", color="#BDBDBD", linewidth=1.0)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(1.5)
        spine.set_color("black")

    ax.tick_params(labelsize=12, width=1.4, length=5)
    ax.set_title("Связь BMI и глюкозы", fontsize=18, fontweight="bold")
    ax.set_ylabel("Глюкоза", fontsize=15)
    ax.set_xlabel("BMI", fontsize=15)

    cbar = fig.colorbar(scatter, ax=ax)
    cbar.set_label("BMI", fontsize=12)
    cbar.ax.tick_params(labelsize=10)

    fig.tight_layout()
    save_figure(fig, "05_05_bad_scatter", formats=("svg", "png"), dpi=300)


if __name__ == "__main__":
    main()
