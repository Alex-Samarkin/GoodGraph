#!/usr/bin/env python3
"""Общий учебный набор для приложений A–D.

150 пациентов, три группы, САД на 0/4/8/12-й неделе; возраст, BMI,
глюкоза, время до события, событие и категория нежелательного явления.
Один набор используется в R, Julia и Excel, чтобы сравнение языков было
честным.

Файл: data/09_appendix_dataset.csv
Запуск: uv run python 09_appendices/scripts/make_data.py
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR

SEED = 20240616
N_PER_GROUP = 50
WEEKS = [0, 4, 8, 12]
GROUPS = [
    ("Контроль", 151.0, [0.0, -2.0, -3.0, -4.0], 0.060),
    ("Препарат A", 152.0, [0.0, -5.0, -9.0, -12.0], 0.040),
    ("Препарат B", 153.0, [0.0, -7.0, -13.0, -18.0], 0.028),
]


def make_dataset(seed: int = SEED) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    rows = []
    patient = 1
    for group, baseline, effects, hazard in GROUPS:
        base = rng.normal(baseline, 9.0, N_PER_GROUP)
        age = np.clip(rng.normal(58, 12, N_PER_GROUP), 25, 85)
        bmi = np.clip(rng.normal(27.5, 4.0, N_PER_GROUP), 18, 42)
        glucose = np.clip(4.2 + 0.09 * bmi + rng.normal(0, 0.8, N_PER_GROUP), 3.2, 12)
        event_time = rng.exponential(1 / hazard, N_PER_GROUP)
        censor = rng.uniform(6, 36, N_PER_GROUP)
        event = (event_time <= censor).astype(int)
        time = np.clip(np.minimum(event_time, censor), 0.5, 36)
        adverse = rng.choice(
            ["нет", "лёгкое", "серьёзное"],
            N_PER_GROUP,
            p=[0.55, 0.33, 0.12],
        )
        for i in range(N_PER_GROUP):
            for week, effect in zip(WEEKS, effects, strict=True):
                sbp = base[i] + effect + rng.normal(0, 5)
                rows.append(
                    {
                        "patient_id": f"A{patient:03d}",
                        "group": group,
                        "week": week,
                        "sbp_mm_hg": round(float(np.clip(sbp, 105, 185)), 1),
                        "age_years": int(round(age[i])),
                        "bmi_kg_m2": round(float(bmi[i]), 1),
                        "glucose_mmol_l": round(float(glucose[i]), 1),
                        "time_months": round(float(time[i]), 1),
                        "event": int(event[i]),
                        "adverse_event": str(adverse[i]),
                    }
                )
            patient += 1
    return pd.DataFrame(rows)


def main() -> None:
    df = make_dataset()
    out = DATA_DIR / "09_appendix_dataset.csv"
    df.to_csv(out, index=False, encoding="utf-8")
    print(f"Данные записаны: {out}")
    print(f"Строк: {len(df)}; пациентов: {df['patient_id'].nunique()}")
    print(df.groupby(["group", "week"])["sbp_mm_hg"].mean().round(1).to_string())


if __name__ == "__main__":
    main()
