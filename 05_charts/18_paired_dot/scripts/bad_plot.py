#!/usr/bin/env python3
"""«Плохой» paired dot для раздела 5.18.

Что специально сделано неправильно
----------------------------------
1. 30 радужных линий: непонятно, где отдельный пациент.
2. Нет точек и средних: видны только линии.
3. Ось Y обрезана до 85–115: высокие значения после лечения скрыты.
4. Тяжёлая сетка, полная рамка.
5. Заголовок «Гемоглобин до и после» ничего не сообщает.
6. Нет единиц, n и среднего изменения.

Выход: images/05_18_bad_paired_dot.{svg,png}
Запуск: uv run python 05_charts/18_paired_dot/scripts/bad_plot.py
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

    df = pd.read_csv(DATA_DIR / "18_dataset.csv")
    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    colors = plt.cm.rainbow(np.linspace(0.0, 1.0, len(df)))

    for (_, row), color in zip(df.iterrows(), colors, strict=True):
        ax.plot(
            [0, 1],
            [row["hemoglobin_before"], row["hemoglobin_after"]],
            color=color,
            linewidth=1.6,
        )

    ax.set_xlim(-0.1, 1.1)
    ax.set_ylim(85, 115)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["1", "2"], fontsize=11)

    ax.grid(True, which="major", axis="both", color="#BDBDBD", linewidth=1.0)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(1.5)
        spine.set_color("black")

    ax.tick_params(labelsize=12, width=1.4, length=5)
    ax.set_title("Гемоглобин до и после", fontsize=18, fontweight="bold")
    ax.set_ylabel("Гемоглобин", fontsize=15)

    fig.tight_layout()
    save_figure(fig, "05_18_bad_paired_dot", formats=("svg", "png"), dpi=300)


if __name__ == "__main__":
    main()
