#!/usr/bin/env python3
"""Данные для раздела 5.16: forest plot по подгруппам.

Сценарий
--------
Рандомизированное исследование, 800 пациентов: 400 в группе лечения,
400 в контроле. Исход — осложнение. Эффект — отношение шансов (OR)
с 95 % доверительным интервалом Уолфа.

Подгруппы: пол, возраст, диабет, ХБП. В каждой — свои counts.
Строка «Все пациенты» — общая оценка для ромба.

Файл: data/16_dataset.csv
Запуск: uv run python 05_charts/16_forest/scripts/make_data.py
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR

ROWS = [
    ("Мужчины", 220, 55, 210, 75),
    ("Женщины", 180, 45, 190, 65),
    ("<65 лет", 250, 40, 240, 60),
    ("≥65 лет", 150, 60, 160, 80),
    ("Сахарный диабет", 120, 35, 130, 55),
    ("Без диабета", 280, 65, 270, 85),
    ("ХБП", 90, 30, 95, 45),
    ("Без ХБП", 310, 70, 305, 95),
    ("Все пациенты", 400, 100, 400, 140),
]


def odds_ratio(a: int, n1: int, c: int, n2: int) -> tuple[float, float, float]:
    """OR и 95 % CI Уолфа для таблицы 2×2."""
    b = n1 - a
    d = n2 - c
    odds = (a / b) / (c / d)
    se = np.sqrt(1 / a + 1 / b + 1 / c + 1 / d)
    low = np.exp(np.log(odds) - 1.96 * se)
    high = np.exp(np.log(odds) + 1.96 * se)
    return odds, low, high


def main() -> None:
    df = pd.DataFrame(
        ROWS,
        columns=[
            "subgroup",
            "n_treatment",
            "events_treatment",
            "n_control",
            "events_control",
        ],
    )
    out = DATA_DIR / "16_dataset.csv"
    df.to_csv(out, index=False, encoding="utf-8")

    for row in df.itertuples(index=False):
        or_value, low, high = odds_ratio(
            row.events_treatment,
            row.n_treatment,
            row.events_control,
            row.n_control,
        )
        print(f"{row.subgroup:18s} OR = {or_value:.2f} ({low:.2f}–{high:.2f})")

    print(f"\nДанные записаны: {out}")
    print(f"Строк: {len(df)}")


if __name__ == "__main__":
    main()
