#!/usr/bin/env python3
"""Данные для раздела 5.12: eGFR по стадиям ХБП.

Сценарий
--------
600 пациентов, три стадии хронической болезни почек (ХБП): 1–2, 3, 4–5.
Показатель — СКФ (eGFR, мл/мин/1,73 м²). Распределения сдвигаются вниз
с ростом стадии; в каждой группе 200 человек.

Данные синтетические, но реалистичные:

* ХБП 1–2: eGFR 60–130, около 88;
* ХБП 3: 30–59, около 45;
* ХБП 4–5: 10–29, около 21;
* пол — примерно 50/50 в каждой группе.

Файл: data/12_dataset.csv
Запуск: uv run python 05_charts/12_violin/scripts/make_data.py
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR

SEED = 20240530
N_PER_GROUP = 200

STAGES = [
    ("1–2", 88.0, 14.0, 60.0, 130.0),
    ("3", 45.0, 9.0, 30.0, 59.0),
    ("4–5", 21.0, 5.0, 10.0, 29.0),
]


def truncated_normal(
    rng: np.random.Generator, mean: float, sd: float, low: float, high: float, n: int
) -> np.ndarray:
    """Нормальное распределение, обрезанное до [low, high] без свалки на границах."""
    values: list[float] = []
    while len(values) < n:
        sample = rng.normal(mean, sd, n * 2)
        sample = sample[(sample >= low) & (sample <= high)]
        values.extend(sample.tolist())
    return np.array(values[:n])


def make_dataset(seed: int = SEED) -> pd.DataFrame:
    """Сгенерировать eGFR для трёх стадий ХБП."""
    rng = np.random.default_rng(seed)
    rows = []
    patient = 1

    for stage, mean, sd, low, high in STAGES:
        values = truncated_normal(rng, mean, sd, low, high, N_PER_GROUP)
        sexes = rng.choice(["женский", "мужской"], size=N_PER_GROUP, p=[0.5, 0.5])
        for value, sex in zip(values, sexes, strict=True):
            rows.append(
                {
                    "patient_id": f"R{patient:04d}",
                    "ckd_stage": stage,
                    "sex": sex,
                    "egfr_ml_min_1_73m2": round(float(value), 1),
                }
            )
            patient += 1

    return pd.DataFrame(rows)


def main() -> None:
    df = make_dataset()
    out = DATA_DIR / "12_dataset.csv"
    df.to_csv(out, index=False, encoding="utf-8")

    summary = (
        df.groupby("ckd_stage")["egfr_ml_min_1_73m2"]
        .agg(["count", "median", "mean", "std"])
        .round(1)
    )
    print(f"Данные записаны: {out}")
    print(f"Строк: {len(df)}")
    print(summary.to_string())


if __name__ == "__main__":
    main()
