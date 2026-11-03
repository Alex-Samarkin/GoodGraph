#!/usr/bin/env python3
"""«Правильный» loess для раздела 5.08.

Что улучшено
------------
1. LOESS-сглаживание вместо линейной прямой: видно насыщение.
2. Bootstrap-полоса 95 %: показана неопределённость кривой.
3. Полный диапазон осей 0–80 мг и 0–70 %.
4. Точки полупрозрачные, один цвет; нет двойного кодирования.
5. Единицы, n и подпись плато.
6. Заголовок-вывод, лёгкая сетка, 85 мм.

Выход: images/05_08_good_loess.{svg,png}
Запуск: uv run python 05_charts/08_loess/scripts/good_plot.py
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statsmodels.nonparametric.smoothers_lowess import lowess

from goodgraph.palettes import PRIMARY_BLUE
from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, figure_size, save_figure

FRAC = 0.5
N_BOOT = 200


def main() -> None:
    apply_style()

    df = pd.read_csv(DATA_DIR / "08_dataset.csv")
    x = df["dose_mg"].to_numpy()
    y = df["ldl_reduction_pct"].to_numpy()
    rng = np.random.default_rng(42)

    grid = np.linspace(0, 80, 200)
    fit = lowess(y, x, frac=FRAC, return_sorted=True)
    mean_line = np.interp(grid, fit[:, 0], fit[:, 1])

    boots = []
    n = len(x)
    for _ in range(N_BOOT):
        index = rng.integers(0, n, n)
        boot = lowess(y[index], x[index], frac=FRAC, return_sorted=True)
        boots.append(np.interp(grid, boot[:, 0], boot[:, 1]))
    low, high = np.percentile(boots, [2.5, 97.5], axis=0)

    fig, ax = plt.subplots(
        figsize=figure_size("single", height_mm=72),
        layout="constrained",
    )
    fig.set_constrained_layout_pads(w_pad=0.04, h_pad=0.02)

    ax.scatter(x, y, s=10, color=PRIMARY_BLUE, alpha=0.25, linewidths=0, zorder=2)
    ax.fill_between(grid, low, high, color=PRIMARY_BLUE, alpha=0.15, linewidth=0, zorder=1)
    ax.plot(grid, mean_line, color="#333333", linewidth=1.8, zorder=3)

    ax.text(
        2,
        66,
        f"n = {len(df)}; LOESS, frac = {FRAC}",
        fontsize=7,
        color="#333333",
        va="top",
    )

    ax.set_xlim(0, 80)
    ax.set_ylim(0, 70)
    ax.set_xticks([0, 20, 40, 60, 80])
    ax.set_yticks([0, 20, 40, 60])

    ax.set_xlabel("Доза, мг/сут")
    ax.set_ylabel("Снижение ЛПНП, %")
    ax.set_title("Эффект насыщается после 20 мг", loc="left", fontsize=9.5, pad=6)

    ax.grid(axis="y", color="#E8E8E8", linewidth=0.6)
    ax.grid(axis="x", visible=False)

    save_figure(fig, "05_08_good_loess", formats=("svg", "png"), dpi=600)

    for dose in [10, 20, 40, 80]:
        value = np.interp(dose, grid, mean_line)
        print(f"LOESS при {dose} мг: {value:.1f} %")


if __name__ == "__main__":
    main()
