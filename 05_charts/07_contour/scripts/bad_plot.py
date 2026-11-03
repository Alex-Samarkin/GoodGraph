#!/usr/bin/env python3
"""«Плохой» contour для раздела 5.07.

Что специально сделано неправильно
----------------------------------
1. Радужная палитра `jet` и 20 уровней: ложные границы, шум.
2. Подписи уровней налезают друг на друга.
3. Оси обрезаны до 40–70 и 110–170: хвосты распределения скрыты.
4. Тяжёлая сетка по обеим осям и полная рамка.
5. Заголовок «Возраст и САД» ничего не сообщает.
6. Нет единиц, n, colorbar и порога 140 мм рт. ст.
7. Слишком мелкие бины: карта выглядит «рябой».

Выход: images/05_07_bad_contour.{svg,png}
Запуск: uv run python 05_charts/07_contour/scripts/bad_plot.py
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

    df = pd.read_csv(DATA_DIR / "07_dataset.csv")
    age = df["age_years"].to_numpy()
    sbp = df["sbp_mm_hg"].to_numpy()

    hist, xedges, yedges = np.histogram2d(
        age, sbp, bins=(25, 25), range=[[20, 80], [90, 200]]
    )
    xcenters = 0.5 * (xedges[:-1] + xedges[1:])
    ycenters = 0.5 * (yedges[:-1] + yedges[1:])
    xx, yy = np.meshgrid(xcenters, ycenters)

    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    cs = ax.contour(xx, yy, hist.T, levels=20, cmap="jet")
    ax.clabel(cs, inline=True, fontsize=7, fmt="%d")

    ax.set_xlim(40, 70)
    ax.set_ylim(110, 170)

    ax.grid(True, which="major", axis="both", color="#BDBDBD", linewidth=1.0)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(1.5)
        spine.set_color("black")

    ax.tick_params(labelsize=12, width=1.4, length=5)

    ax.set_title("Возраст и САД", fontsize=18, fontweight="bold")
    ax.set_ylabel("САД", fontsize=15)
    ax.set_xlabel("Возраст", fontsize=15)

    fig.tight_layout()
    save_figure(fig, "05_07_bad_contour", formats=("svg", "png"), dpi=300)


if __name__ == "__main__":
    main()
