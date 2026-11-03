#!/usr/bin/env python3
"""Данные для раздела 5.17: вес до и после программы.

Сценарий
--------
360 пациентов, шесть клиник, по 60 человек. Измерен вес до и через
12 недель программы снижения веса. Slope plot показывает средние
до/после по клиникам и разброс эффекта.

Данные синтетические, но реалистичные:

* средний вес до — 89–101 кг в зависимости от клиники;
* среднее снижение — 4–11 кг;
* индивидуальный разброс — около 5 кг.

Файл: data/17_dataset.csv
Запуск: uv run python 05_charts/17_slope/scripts/make_data.py
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR

SEED = 20240602
N_PER_CLINIC = 60

CLINICS = [
    ("Клиника A", 98.0, 6.5),
    ("Клиника B", 94.0, 5.0),
    ("Клиника C", 101.0, 10.5),
    ("Клиника D", 89.0, 4.0),
    ("Клиника E", 96.0, 6.0),
    ("Клиника F", 92.0, 8.0),
]


def make_dataset(seed: int = SEED) -> pd.DataFrame:
    """Сгенерировать пары «до/после» по клиникам."""
    rng = np.random.default_rng(seed)
    rows = []
    patient = 1

    for clinic, before_mean, loss_mean in CLINICS:
        before = rng.normal(before_mean, 8.0, N_PER_CLINIC)
        after = before - rng.normal(loss_mean, 3.0, N_PER_CLINIC)
        before = np.clip(before, 60.0, 130.0)
        after = np.clip(after, 55.0, 125.0)
        for b, a in zip(before, after, strict=True):
            rows.append(
                {
                    "patient_id": f"W{patient:04d}",
                    "clinic": clinic,
                    "weight_before_kg": round(float(b), 1),
                    "weight_after_kg": round(float(a), 1),
                }
            )
            patient += 1

    return pd.DataFrame(rows)


def main() -> None:
    df = make_dataset()
    out = DATA_DIR / "17_dataset.csv"
    df.to_csv(out, index=False, encoding="utf-8")

    summary = (
        df.groupby("clinic")[["weight_before_kg", "weight_after_kg"]]
        .mean()
        .assign(change=lambda x: x["weight_after_kg"] - x["weight_before_kg"])
        .round(1)
    )
    print(f"Данные записаны: {out}")
    print(f"Строк: {len(df)}")
    print(summary.to_string())


if __name__ == "__main__":
    main()
