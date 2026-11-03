#!/usr/bin/env python3
"""Данные для раздела 2: HbA1c до и после 12 недель терапии.

Сценарий
--------
Гипотетическое исследование: 132 пациента с сахарным диабетом 2-го типа,
три группы, 12 недель терапии. Первичная конечная точка — изменение
гликированного гемоглобина (HbA1c), %.

Данные синтетические, но реалистичные:

* исходный HbA1c — около 8,1 % (SD ≈ 0,9);
* среднее изменение — от −0,3 % (плацебо) до −1,2 % (препарат B);
* индивидуальный разброс — SD ≈ 0,55–0,75 %, поэтому у части пациентов
  показатель может не измениться или даже немного вырасти;
* n ≈ 44 в группе.

Это отдельный набор: раздел 2 не переиспользует данные раздела 1.
Файл: data/02_python_dataset.csv
Запуск: uv run python 02_python/scripts/make_data.py
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR

SEED = 20240518

GROUP_SPECS = [
    {"group": "Плацебо", "mean_change": -0.30, "sd_change": 0.55, "n": 44},
    {"group": "Препарат A 10 мг", "mean_change": -0.80, "sd_change": 0.70, "n": 45},
    {"group": "Препарат B 20 мг", "mean_change": -1.20, "sd_change": 0.75, "n": 43},
]

BASELINE_MEAN = 8.1
BASELINE_SD = 0.9


def make_dataset(seed: int = SEED) -> pd.DataFrame:
    """Сгенерировать таблицу «пациент — группа — HbA1c до/после»."""
    rng = np.random.default_rng(seed)
    frames: list[pd.DataFrame] = []

    for spec in GROUP_SPECS:
        n = spec["n"]

        # HbA1c измеряют с точностью до 0,1 %, поэтому округляем.
        baseline = rng.normal(BASELINE_MEAN, BASELINE_SD, n)
        baseline = np.clip(np.round(baseline, 1), 5.5, 11.0)

        change = rng.normal(spec["mean_change"], spec["sd_change"], n)
        change = change - change.mean() + spec["mean_change"]
        change = np.round(change, 1)

        followup = np.clip(np.round(baseline + change, 1), 4.8, 11.5)
        change = np.round(followup - baseline, 1)

        frames.append(
            pd.DataFrame(
                {
                    "group": spec["group"],
                    "baseline_hba1c_pct": baseline,
                    "followup_hba1c_pct": followup,
                    "change_hba1c_pct": change,
                }
            )
        )

    df = pd.concat(frames, ignore_index=True)
    df.insert(0, "patient_id", [f"H{i:03d}" for i in range(1, len(df) + 1)])
    return df.sample(frac=1, random_state=seed).reset_index(drop=True)


def main() -> None:
    df = make_dataset()
    out = DATA_DIR / "02_python_dataset.csv"
    df.to_csv(out, index=False, encoding="utf-8")

    summary = (
        df.groupby("group", sort=False)["change_hba1c_pct"]
        .agg(["count", "mean", "std", "min", "max"])
        .round(2)
    )
    print(f"Данные записаны: {out}")
    print(f"Строк: {len(df)}, пациентов: {df['patient_id'].nunique()}")
    print("\nСводка по изменению HbA1c, %:")
    print(summary.to_string())


if __name__ == "__main__":
    main()
