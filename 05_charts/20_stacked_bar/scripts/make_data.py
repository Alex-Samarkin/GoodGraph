#!/usr/bin/env python3
"""Данные для раздела 5.20: исходы госпитализации по отделениям.

Сценарий
--------
Четыре отделения, три исхода: выписан, переведён, умер. Числа —
абсолютные количества; stacked bar показывает состав и общий объём.

Файл: data/20_dataset.csv
Запуск: uv run python 05_charts/20_stacked_bar/scripts/make_data.py
"""

from __future__ import annotations

import pandas as pd

from goodgraph.paths import DATA_DIR

ROWS = [
    ("Терапия", "выписан", 820),
    ("Терапия", "переведён", 120),
    ("Терапия", "умер", 60),
    ("Хирургия", "выписан", 640),
    ("Хирургия", "переведён", 90),
    ("Хирургия", "умер", 50),
    ("Кардиология", "выписан", 700),
    ("Кардиология", "переведён", 110),
    ("Кардиология", "умер", 90),
    ("ОРИТ", "выписан", 180),
    ("ОРИТ", "переведён", 220),
    ("ОРИТ", "умер", 100),
]


def main() -> None:
    df = pd.DataFrame(ROWS, columns=["department", "outcome", "patients"])
    out = DATA_DIR / "20_dataset.csv"
    df.to_csv(out, index=False, encoding="utf-8")
    print(f"Данные записаны: {out}")
    print(f"Строк: {len(df)}")
    print(df.pivot(index="department", columns="outcome", values="patients").to_string())


if __name__ == "__main__":
    main()
