#!/usr/bin/env python3
"""Данные для раздела 5.13: послеоперационная боль по трём схемам.

Сценарий
--------
90 пациентов, три схемы обезболивания: НПВС, опиоид, комбинация.
Через 24 часа измерена боль по визуальной аналоговой шкале (ВАШ, 0–100 мм).
По 30 пациентов в группе — достаточно мало, чтобы показать каждую точку.

Данные синтетические, но реалистичные:

* НПВС — около 55 мм;
* опиоид — около 45 мм;
* комбинация — около 35 мм;
* разброс около 12 мм, есть отдельные высокие и низкие значения.

Файл: data/13_dataset.csv
Запуск: uv run python 05_charts/13_strip/scripts/make_data.py
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR

SEED = 20240531
N_PER_GROUP = 30

GROUPS = [
    ("НПВС", 55.0, 12.0),
    ("опиоид", 45.0, 12.0),
    ("комбинация", 35.0, 12.0),
]


def make_dataset(seed: int = SEED) -> pd.DataFrame:
    """Сгенерировать ВАШ для трёх схем обезболивания."""
    rng = np.random.default_rng(seed)
    rows = []
    patient = 1

    for group, mean, sd in GROUPS:
        values = np.clip(rng.normal(mean, sd, N_PER_GROUP), 5.0, 95.0)
        for value in values:
            rows.append(
                {
                    "patient_id": f"P{patient:03d}",
                    "analgesia": group,
                    "vas_mm": int(round(value)),
                }
            )
            patient += 1

    return pd.DataFrame(rows)


def main() -> None:
    df = make_dataset()
    out = DATA_DIR / "13_dataset.csv"
    df.to_csv(out, index=False, encoding="utf-8")

    summary = (
        df.groupby("analgesia")["vas_mm"]
        .agg(["count", "median", "mean", "std"])
        .round(1)
    )
    print(f"Данные записаны: {out}")
    print(f"Строк: {len(df)}")
    print(summary.to_string())


if __name__ == "__main__":
    main()
