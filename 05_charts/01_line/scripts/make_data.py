#!/usr/bin/env python3
"""Данные для раздела 5.01: линейный график динамики САД.

Сценарий
--------
Гипотетическое 12-недельное исследование: 120 пациентов с артериальной
гипертензией, три группы, САД измеряют на 0, 4, 8 и 12-й неделе.

Данные синтетические, но реалистичные:

* исходное САД — около 152 мм рт. ст. (SD ≈ 9);
* плацебо — небольшое снижение, до 148;
* препарат A 10 мг — до 139;
* препарат B 20 мг — до 132;
* индивидуальные траектории различаются: у части пациентов САД
  меняется слабо или даже растёт.

Формат — long: одна строка = один пациент × одна неделя.
Файл: data/01_dataset.csv
Запуск: uv run python 05_charts/01_line/scripts/make_data.py
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR

SEED = 20240519
WEEKS = [0, 4, 8, 12]
N_PER_GROUP = 40

GROUP_SPECS = [
    {"group": "Плацебо", "curve": [152, 150, 149, 148]},
    {"group": "Препарат A 10 мг", "curve": [152, 146, 142, 139]},
    {"group": "Препарат B 20 мг", "curve": [152, 143, 136, 132]},
]


def make_dataset(seed: int = SEED) -> pd.DataFrame:
    """Сгенерировать long-таблицу «пациент — группа — неделя — САД»."""
    rng = np.random.default_rng(seed)
    frames: list[pd.DataFrame] = []
    patient_number = 1

    for spec in GROUP_SPECS:
        n = N_PER_GROUP
        curve = np.asarray(spec["curve"], dtype=float)

        # Индивидуальный исходный уровень и индивидуальный наклон.
        baseline = rng.normal(curve[0], 9.0, n)
        baseline = baseline - baseline.mean() + curve[0]
        slope_dev = rng.normal(0.0, 2.2, n)
        slope_dev = slope_dev - slope_dev.mean()

        rows = []
        for i in range(n):
            for week_index, week in enumerate(WEEKS):
                value = (
                    baseline[i]
                    + (curve[week_index] - curve[0])
                    + slope_dev[i] * (week / WEEKS[-1])
                    + rng.normal(0.0, 3.5)
                )
                rows.append(
                    {
                        "patient_id": f"P{patient_number:03d}",
                        "group": spec["group"],
                        "week": week,
                        "sbp_mm_hg": int(np.clip(np.rint(value), 90, 200)),
                    }
                )
            patient_number += 1

        frames.append(pd.DataFrame(rows))

    return pd.concat(frames, ignore_index=True)


def main() -> None:
    df = make_dataset()
    out = DATA_DIR / "01_dataset.csv"
    df.to_csv(out, index=False, encoding="utf-8")

    summary = (
        df.groupby(["group", "week"], sort=False)["sbp_mm_hg"]
        .agg(["count", "mean", "std"])
        .round(1)
    )
    print(f"Данные записаны: {out}")
    print(f"Строк: {len(df)}, пациентов: {df['patient_id'].nunique()}")
    print("\nСреднее САД по группам и неделям:")
    print(summary.to_string())


if __name__ == "__main__":
    main()
