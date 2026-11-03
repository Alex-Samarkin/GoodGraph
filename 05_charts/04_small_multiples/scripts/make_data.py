#!/usr/bin/env python3
"""Данные для раздела 5.04: малые кратные по отделениям.

Сценарий
--------
Шесть отделений больницы, 12 месяцев. Показатель — потребление
антибиотиков в DDD на 100 койко-дней. Зимой потребление выше,
летом ниже; уровень различается между отделениями.

Данные синтетические, но реалистичные:

* ОРИТ — самый высокий уровень, около 110 DDD/100 койко-дней;
* кардиология — самый низкий, около 45;
* сезонная амплитуда 8–20 %;
* шум около 5 %.

Формат — long: одна строка = отделение × месяц.
Файл: data/04_dataset.csv
Запуск: uv run python 05_charts/04_small_multiples/scripts/make_data.py
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR

SEED = 20240522
MONTHS = list(range(1, 13))

DEPARTMENTS = [
    ("Терапия", 55.0, 0.15),
    ("Хирургия", 70.0, 0.12),
    ("ОРИТ", 110.0, 0.18),
    ("Кардиология", 45.0, 0.10),
    ("Пульмонология", 80.0, 0.20),
    ("Урология", 50.0, 0.08),
]


def make_dataset(seed: int = SEED) -> pd.DataFrame:
    """Сгенерировать long-таблицу «отделение — месяц — DDD»."""
    rng = np.random.default_rng(seed)
    rows = []

    for department, base, amplitude in DEPARTMENTS:
        for month in MONTHS:
            seasonal = 1.0 + amplitude * np.cos(2.0 * np.pi * (month - 1) / 12.0)
            value = base * seasonal * np.exp(rng.normal(0.0, 0.05))
            rows.append(
                {
                    "department": department,
                    "month": month,
                    "ddd_per_100_bed_days": round(float(np.clip(value, 10.0, 140.0)), 1),
                }
            )

    return pd.DataFrame(rows)


def main() -> None:
    df = make_dataset()
    out = DATA_DIR / "04_dataset.csv"
    df.to_csv(out, index=False, encoding="utf-8")

    pivot = df.pivot(index="month", columns="department", values="ddd_per_100_bed_days")
    print(f"Данные записаны: {out}")
    print(f"Строк: {len(df)}, отделений: {df['department'].nunique()}")
    print("\nDDD/100 койко-дней по месяцам:")
    print(pivot.to_string())
    print("\nСреднее по отделениям:")
    print(df.groupby("department")["ddd_per_100_bed_days"].mean().round(1).to_string())


if __name__ == "__main__":
    main()
