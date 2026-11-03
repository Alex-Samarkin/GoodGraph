#!/usr/bin/env python3
"""«Правильный» area chart для раздела 5.03.

Что улучшено
------------
1. Заливка от 0: площадь под кривой действительно равна AUC.
2. Подпись AUC0–24 со средним ± SD — площадь становится числом.
3. Ось Y 0–12 мг/л: виден пик, хвост и базовая линия.
4. Среднее ± SD в точках; заливка показывает интеграл, а не «украшение».
5. Палитра Okabe–Ito, лёгкая сетка только по Y.
6. Единицы, время в часах, n = 40 в подписи.
7. Заголовок-вывод: площадь — это экспозиция.
8. 85 мм в ширину — конечный журнальный размер.

Выход: images/05_03_good_area.{svg,png}
Запуск: uv run python 05_charts/03_area/scripts/good_plot.py
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


def auc_per_patient(df: pd.DataFrame) -> np.ndarray:
    """AUC0–24 методом трапеций для каждого пациента."""
    values = []
    for _, part in df.groupby("patient_id"):
        part = part.sort_values("time_h")
        values.append(
            np.trapezoid(
                part["conc_mg_l"].to_numpy(),
                part["time_h"].to_numpy(),
            )
        )
    return np.asarray(values)


def main() -> None:
    apply_style()

    df = pd.read_csv(DATA_DIR / "03_dataset.csv")
    summary = (
        df.groupby("time_h")["conc_mg_l"]
        .agg(["mean", "std", "count"])
        .reset_index()
    )
    auc = auc_per_patient(df)

    fig, ax = plt.subplots(
        figsize=figure_size("single", height_mm=72),
        layout="constrained",
    )
    fig.set_constrained_layout_pads(w_pad=0.04, h_pad=0.02)

    time = summary["time_h"].to_numpy()
    mean = summary["mean"].to_numpy()
    sd = summary["std"].to_numpy()

    ax.fill_between(time, 0, mean, color=PRIMARY_BLUE, alpha=0.18, linewidth=0, zorder=1)
    ax.plot(
        time,
        mean,
        color=PRIMARY_BLUE,
        linewidth=1.8,
        marker="o",
        markersize=3.5,
        markeredgecolor="white",
        markeredgewidth=0.6,
        zorder=3,
    )
    ax.errorbar(
        time,
        mean,
        yerr=sd,
        fmt="none",
        ecolor="#666666",
        elinewidth=0.7,
        capsize=2,
        alpha=0.65,
        zorder=2,
    )

    mean_text = f"{auc.mean():.1f}".replace(".", ",")
    sd_text = f"{auc.std(ddof=1):.1f}".replace(".", ",")
    ax.text(
        12.8,
        10.6,
        f"AUC$_{{0–24}}$ = {mean_text} ± {sd_text}\nмг·ч/л",
        ha="left",
        va="top",
        fontsize=7.5,
        color="#333333",
    )

    ax.set_xlim(0, 24)
    ax.set_ylim(0, 12)
    ax.set_xticks([0, 6, 12, 18, 24])
    ax.set_yticks([0, 4, 8, 12])

    ax.set_xlabel("Время, ч")
    ax.set_ylabel("Концентрация, мг/л")
    ax.set_title("Площадь под кривой — экспозиция", loc="left", fontsize=9.5, pad=6)

    ax.grid(axis="y", color="#E8E8E8", linewidth=0.6)
    ax.grid(axis="x", visible=False)

    save_figure(fig, "05_03_good_area", formats=("svg", "png"), dpi=600)

    print(f"AUC0–24: {auc.mean():.1f} ± {auc.std(ddof=1):.1f} мг·ч/л")
    print(summary.round(2).to_string(index=False))


if __name__ == "__main__":
    main()
