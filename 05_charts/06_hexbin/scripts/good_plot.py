#!/usr/bin/env python3
"""«Правильный» hexbin для раздела 5.06.

Что улучшено
------------
1. Hexbin вместо scatter: цвет кодирует число пациентов в шестиугольнике.
2. Логарифмическая шкала плотности: видны и плотное ядро, и хвосты.
3. mincnt=1: пустые ячейки остаются белыми.
4. Полный диапазон осей 4,5–12,5 % и 2–20 ммоль/л.
5. Цветовая шкала подписана: «Пациенты (лог. шкала)».
6. Единицы, n и r; заголовок-вывод.
7. 85 мм, cividis — шкала, читаемая при дальтонизме.

Выход: images/05_06_good_hexbin.{svg,png}
Запуск: uv run python 05_charts/06_hexbin/scripts/good_plot.py
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd

from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, figure_size, save_figure


def main() -> None:
    apply_style()

    df = pd.read_csv(DATA_DIR / "06_dataset.csv")
    x = df["hba1c_pct"].to_numpy()
    y = df["glucose_mmol_l"].to_numpy()
    r = df["hba1c_pct"].corr(df["glucose_mmol_l"])

    fig, ax = plt.subplots(
        figsize=figure_size("single", height_mm=72),
        layout="constrained",
    )
    fig.set_constrained_layout_pads(w_pad=0.04, h_pad=0.02)

    hexbin = ax.hexbin(
        x,
        y,
        gridsize=32,
        cmap="cividis",
        mincnt=1,
        bins="log",
        linewidths=0,
    )
    cbar = fig.colorbar(hexbin, ax=ax, fraction=0.05, pad=0.02, shrink=0.85)
    cbar.set_label("Пациенты (лог. шкала)", fontsize=7)
    cbar.set_ticks([1, 3, 10, 30, 100])
    cbar.ax.set_yticklabels(["1", "3", "10", "30", "100"])
    cbar.ax.tick_params(labelsize=6.5)

    r_text = f"{r:.2f}".replace(".", ",")
    ax.text(
        4.7,
        15.4,
        f"n = {len(df)}; r = {r_text}",
        ha="left",
        va="top",
        fontsize=7.5,
        color="#333333",
    )

    ax.set_xlim(4.5, 11.0)
    ax.set_ylim(2, 16)
    ax.set_xticks([5, 7, 9, 11])
    ax.set_yticks([5, 10, 15])

    ax.set_xlabel("HbA1c, %")
    ax.set_ylabel("Глюкоза, ммоль/л")
    ax.set_title("Плотность пациентов: HbA1c и глюкоза", loc="left", fontsize=9.5, pad=6)

    ax.grid(False)

    save_figure(fig, "05_06_good_hexbin", formats=("svg", "png"), dpi=600)

    print(f"n = {len(df)}, r = {r:.3f}")
    print(f"Максимум в бине: {hexbin.get_array().max():.0f} пациентов")


if __name__ == "__main__":
    main()
