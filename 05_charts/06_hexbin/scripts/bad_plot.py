#!/usr/bin/env python3
"""«Плохой» пример для раздела 5.06: 8 000 точек обычным scatter.

Что специально сделано неправильно
----------------------------------
1. 8 000 непрозрачных точек: overplotting, вместо плотности — пятно.
2. Оси обрезаны до 5–9 и 4–12: хвосты распределения скрыты.
3. Тяжёлая сетка по обеим осям и полная рамка.
4. Заголовок «Связь HbA1c и глюкозы» ничего не сообщает.
5. Нет единиц, n и коэффициента корреляции.
6. Чёрные точки не показывают, где наблюдений больше, а где меньше.

Выход: images/05_06_bad_hexbin.{svg,png}
Запуск: uv run python 05_charts/06_hexbin/scripts/bad_plot.py
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd

from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, save_figure


def main() -> None:
    apply_style()

    df = pd.read_csv(DATA_DIR / "06_dataset.csv")
    x = df["hba1c_pct"].to_numpy()
    y = df["glucose_mmol_l"].to_numpy()

    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    ax.scatter(x, y, s=6, color="#1F1F1F", alpha=0.9, linewidths=0, rasterized=True)

    ax.set_xlim(5, 9)
    ax.set_ylim(4, 12)

    ax.grid(True, which="major", axis="both", color="#BDBDBD", linewidth=1.0)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(1.5)
        spine.set_color("black")

    ax.tick_params(labelsize=12, width=1.4, length=5)
    ax.set_title("Связь HbA1c и глюкозы", fontsize=18, fontweight="bold")
    ax.set_ylabel("Глюкоза", fontsize=15)
    ax.set_xlabel("HbA1c", fontsize=15)

    fig.tight_layout()
    save_figure(fig, "05_06_bad_hexbin", formats=("svg", "png"), dpi=300)


if __name__ == "__main__":
    main()
