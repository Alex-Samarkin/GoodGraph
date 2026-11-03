#!/usr/bin/env python3
"""Данные для раздела 5.11: BMI по трём уровням активности.

Сценарий
--------
450 взрослых, три группы физической активности: низкая, умеренная,
высокая. Показатель — BMI (кг/м²). В каждой группе 150 человек.
Распределения сдвинуты: чем выше активность, тем ниже BMI.

Данные синтетические, но реалистичные:

* низкая активность — около 29,5 кг/м²;
* умеренная — около 27,0;
* высокая — около 25,0;
* есть правый хвост и отдельные выбросы.

Файл: data/11_dataset.csv
Запуск: uv run python 05_charts/11_box/scripts/make_data.py
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR

SEED = 20240529
N_PER_GROUP = 150

GROUPS = [
    ("низкая", 29.5, 4.5),
    ("умеренная", 27.0, 3.8),
    ("высокая", 25.0, 3.4),
]


def make_dataset(seed: int = SEED) -> pd.DataFrame:
    """Сгенерировать BMI для трёх групп активности."""
    rng = np.random.default_rng(seed)
    rows = []
    patient = 1

    for group, mean, sd in GROUPS:
        values = np.clip(rng.normal(mean, sd, N_PER_GROUP), 17.0, 45.0)
        for value in values:
            rows.append(
                {
                    "patient_id": f"A{patient:04d}",
                    "activity": group,
                    "bmi_kg_m2": round(float(value), 1),
                }
            )
            patient += 1

    return pd.DataFrame(rows)


def main() -> None:
    df = make_dataset()
    out = DATA_DIR / "11_dataset.csv"
    df.to_csv(out, index=False, encoding="utf-8")

    summary = (
        df.groupby("activity")["bmi_kg_m2"]
        .agg(["count", "median", "mean", "std"])
        .round(1)
    )
    print(f"Данные записаны: {out}")
    print(f"Строк: {len(df)}")
    print(summary.to_string())


if __name__ == "__main__":
    main()
