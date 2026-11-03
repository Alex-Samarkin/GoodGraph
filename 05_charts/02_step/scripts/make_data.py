#!/usr/bin/env python3
"""Данные для раздела 5.02: ступенчатый график дозы варфарина.

Сценарий
--------
Три пациента на варфарине, 12 недель наблюдения. Дозу меняют на визитах
раз в неделю, шагом 0,5 мг/сут; INR измеряют на каждом визите, целевой
диапазон — 2,0–3,0.

Данные синтетические, но реалистичные:

* дозы 3,0–7,5 мг/сут, шаг 0,5 мг;
* INR 1,6–3,4 в зависимости от дозы и пациента;
* у одного пациента доза стабильна, у двух — титруется.

Формат — long: одна строка = пациент × неделя.
Файл: data/02_dataset.csv
Запуск: uv run python 05_charts/02_step/scripts/make_data.py
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR

SEED = 20240520
WEEKS = list(range(13))  # 0..12


def dose_curve(values: list[tuple[int, int, float]]) -> list[float]:
    """Развернуть интервалы (start, end, dose) в недельную последовательность."""
    result = []
    for start, end, dose in values:
        result.extend([dose] * (end - start + 1))
    return result


PATIENTS = [
    {
        "patient_id": "P01",
        "offset": 0.10,
        "doses": dose_curve([(0, 12, 4.5)]),
    },
    {
        "patient_id": "P02",
        "offset": -0.10,
        "doses": dose_curve([(0, 2, 3.0), (3, 5, 4.0), (6, 12, 5.0)]),
    },
    {
        "patient_id": "P03",
        "offset": 0.20,
        "doses": dose_curve([(0, 1, 7.5), (2, 3, 7.0), (4, 6, 6.0), (7, 9, 5.0), (10, 12, 5.5)]),
    },
]


def make_dataset(seed: int = SEED) -> pd.DataFrame:
    """Сгенерировать long-таблицу «пациент — неделя — доза — INR»."""
    rng = np.random.default_rng(seed)
    rows = []

    for patient in PATIENTS:
        for week, dose in zip(WEEKS, patient["doses"], strict=True):
            inr = 2.4 + 0.18 * (dose - 5.0) + patient["offset"] + rng.normal(0.0, 0.12)
            rows.append(
                {
                    "patient_id": patient["patient_id"],
                    "week": week,
                    "dose_mg": dose,
                    "inr": round(float(np.clip(inr, 1.2, 4.0)), 1),
                }
            )

    return pd.DataFrame(rows)


def main() -> None:
    df = make_dataset()
    out = DATA_DIR / "02_dataset.csv"
    df.to_csv(out, index=False, encoding="utf-8")

    print(f"Данные записаны: {out}")
    print(f"Строк: {len(df)}, пациентов: {df['patient_id'].nunique()}")
    print("\nДозы и INR по неделям:")
    print(df.pivot(index="week", columns="patient_id", values="dose_mg").to_string())
    print("\nINR:")
    print(df.pivot(index="week", columns="patient_id", values="inr").to_string())


if __name__ == "__main__":
    main()
