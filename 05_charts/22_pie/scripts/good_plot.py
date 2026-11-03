#!/usr/bin/env python3
"""«Правильная» круговая диаграмма."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd

from goodgraph.paths import DATA_DIR
from goodgraph.style import apply_style, save_figure

COLORS = ["#0072B2", "#E69F00", "#D55E00", "#999999"]


def main() -> None:
    apply_style(font_size=7)
    df = pd.read_csv(DATA_DIR / "22_dataset.csv").sort_values("patients", ascending=False)
    total = df["patients"].sum()
    labels = [
        f"{cause.replace('Сердечная недостаточность', 'СН')}\n"
        f"{patients} ({patients / total * 100:.0f} %)"
        for cause, patients in zip(df["cause"], df["patients"], strict=True)
    ]

    fig, ax = plt.subplots(figsize=(95 / 25.4, 80 / 25.4))
    ax.pie(
        df["patients"],
        labels=labels,
        colors=COLORS,
        startangle=90,
        counterclock=False,
        labeldistance=1.12,
        textprops={"fontsize": 6.5},
        wedgeprops={"edgecolor": "white", "linewidth": 1.0},
    )
    ax.set_title(
        "40 % — сердечная недостаточность",
        loc="left", fontsize=8.5, pad=16,
    )
    ax.axis("equal")
    save_figure(fig, "05_22_good_pie", formats=("svg", "png"), dpi=600)


if __name__ == "__main__":
    main()
