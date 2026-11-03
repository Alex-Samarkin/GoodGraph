#!/usr/bin/env python3
"""«Плохой» пример для раздела 5.08: линейная прямая на нелинейных данных.

Что специально сделано неправильно
----------------------------------
1. Линейная регрессия на данных с насыщением: прямая не описывает плато.
2. Точки окрашены по дозе, хотя доза уже на оси X: двойное кодирование
   и радужная шкала.
3. Ось Y обрезана до 10–60: низкие дозы и хвост скрыты.
4. Крупные непрозрачные точки, тяжёлая сетка, полная рамка.
5. Заголовок «Доза и эффект» ничего не сообщает.
6. Нет единиц, n, доверительной полосы и описания модели.

Выход: images/05_08_bad_loess.{svg,png}
Запуск: uv run python 05_charts/08_loess/scripts/bad_plot.py
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

    df = pd.read_csv(DATA_DIR / "08_dataset.csv")
    x = df["dose_mg"].to_numpy()
    y = df["ldl_reduction_pct"].to_numpy()

    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    ax.scatter(
        x,
        y,
        s=40,
        c=x,
        cmap="jet",
        alpha=0.9,
        edgecolors="black",
        linewidths=0.4,
        zorder=3,
    )

    slope, intercept, *_ = stats.linregress(x, y)
    line_x = np.array([0, 80])
    ax.plot(line_x, intercept + slope * line_x, color="#D62728", linewidth=3.0, zorder=4)

    ax.set_xlim(0, 80)
    ax.set_ylim(10, 60)

    ax.grid(True, which="major", axis="both", color="#BDBDBD", linewidth=1.0)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(1.5)
        spine.set_color("black")

    ax.tick_params(labelsize=12, width=1.4, length=5)
    ax.set_title("Доза и эффект", fontsize=18, fontweight="bold")
    ax.set_ylabel("ЛПНП", fontsize=15)
    ax.set_xlabel("Доза", fontsize=15)

    fig.tight_layout()
    save_figure(fig, "05_08_bad_loess", formats=("svg", "png"), dpi=300)


if __name__ == "__main__":
    main()
