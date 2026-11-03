#!/usr/bin/env python3
"""«Плохой» график для раздела 1: типичные ошибки оформления.

Что специально сделано неправильно
----------------------------------
1. Столбцы начинаются не с нуля: ось Y обрезана до 3,5 мм рт. ст.
   Это классический «lie factor»: визуальная разница в 7,7 раза
   при реальной разнице в 2,1 раза.
2. Светофорная палитра «красный — жёлтый — зелёный»: красный и зелёный
   неразличимы при протанопии/дейтеранопии, а цвет не несёт смысла.
3. Тени и псевдо-3D — декор, который не кодирует данные.
4. Тяжёлая сетка по обеим осям, полная рамка, жирные линии.
5. Легенда дублирует подписи по оси X.
6. Заголовок «Результаты исследования» ничего не сообщает.
7. Нет единиц, числа наблюдений, разброса и определения ошибок.
8. Рисунок сделан «под слайд», а не под ширину журнальной колонки.

Файл: images/01_bad_bar_truncated.{svg,png}
Запуск: uv run python 01_principles/scripts/bad_plot.py
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")  # без графического дисплея — важно для серверов и CI

import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, save_figure

# Порядок групп и «светофорные» цвета — намеренно плохой выбор.
GROUP_ORDER = ["Плацебо", "Препарат A 10 мг", "Препарат B 20 мг"]
TRAFFIC_COLORS = ["#D62728", "#FFC000", "#2CA02C"]  # красный, жёлтый, зелёный


def main() -> None:
    apply_style()

    df = pd.read_csv(DATA_DIR / "00_dataset.csv")
    means = (
        df.groupby("group", sort=False)["change_sbp_mm_hg"]
        .mean()
        .reindex(GROUP_ORDER)
    )

    fig, ax = plt.subplots(figsize=(6.4, 4.8))  # «слайдовый» размер, не журнальный

    bars = ax.bar(
        np.arange(len(means)),
        means.to_numpy(),
        color=TRAFFIC_COLORS,
        edgecolor="black",
        linewidth=1.4,
        width=0.68,
        zorder=2,
    )

    # Псевдо-3D: тень под столбцами.
    for bar in bars:
        bar.set_path_effects(
            [pe.withSimplePatchShadow(offset=(2.5, -2.5), shadow_rgbFace="0.45", alpha=0.75)]
        )

    # Обрезанная ось — главная ложь графика.
    ax.set_ylim(3.5, 11.6)
    ax.set_yticks(np.arange(3.5, 11.6, 1.0))

    # Тяжёлая сетка по обеим осям и полная рамка.
    ax.grid(True, which="major", axis="both", color="#BDBDBD", linewidth=1.0)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(1.4)
        spine.set_color("black")

    ax.tick_params(labelsize=13, width=1.4, length=5)
    ax.set_xticks(np.arange(len(means)))
    ax.set_xticklabels(GROUP_ORDER, fontsize=11)

    ax.set_title("Результаты исследования", fontsize=18, fontweight="bold", loc="center")
    ax.set_ylabel("САД", fontsize=15)
    ax.set_xlabel("Группы пациентов", fontsize=15)

    # Легенда дублирует то, что уже написано под столбцами.
    ax.legend(
        bars,
        GROUP_ORDER,
        loc="upper right",
        fontsize=11,
        frameon=True,
        edgecolor="black",
        facecolor="white",
    )

    # Подписи значений — единственное, что позволяет заметить обрезку оси.
    for x, value in enumerate(means.to_numpy()):
        ax.text(
            x,
            value + 0.15,
            f"{value:.1f}".replace(".", ","),
            ha="center",
            va="bottom",
            fontsize=13,
            fontweight="bold",
        )

    # Брекет значимости: p-значение без размера эффекта и доверительного интервала.
    ax.plot([0, 0, 2, 2], [9.55, 9.75, 9.75, 9.55], color="black", linewidth=1.2)
    ax.text(1, 9.8, "p < 0,001", ha="center", va="bottom", fontsize=11)

    fig.tight_layout()
    save_figure(fig, "01_bad_bar_truncated", formats=("svg", "png"), dpi=300)


if __name__ == "__main__":
    main()
