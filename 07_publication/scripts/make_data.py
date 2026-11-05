#!/usr/bin/env python3
"""Данные для раздела 7: САД по трём группам за 12 недель.

Сценарий
--------
90 пациентов, три группы по 30 человек. САД измерено на 0, 4, 8 и 12-й
неделе. Контроль меняется слабо, препарат A снижает САД умеренно,
препарат B — сильнее. Данные используются для «журнального» рисунка
с панелями A/B.

Файл: data/07_publication_dataset.csv
Запуск: uv run python 07_publication/scripts/make_data.py
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR

SEED = 20240615
N_PER_GROUP = 30
WEEKS = [0, 4, 8, 12]

GROUPS = [
    ("Контроль", 152.0, [0.0, -2.0, -3.0, -4.0]),
    ("Препарат A", 151.0, [0.0, -5.0, -9.0, -12.0]),
    ("Препарат B", 153.0, [0.0, -7.0, -13.0, -18.0]),
]


def make_dataset(seed: int = SEED) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    rows = []
    patient = 1
    for group, baseline, effects in GROUPS:
        base = rng.normal(baseline, 9.0, N_PER_GROUP)
        for i in range(N_PER_GROUP):
            for week, effect in zip(WEEKS, effects, strict=True):
                value = base[i] + effect + rng.normal(0, 5.0)
                rows.append(
                    {
                        "patient_id": f"J{patient:03d}",
                        "group": group,
                        "week": week,
                        "sbp_mm_hg": round(float(np.clip(value, 105, 185)), 1),
                    }
                )
            patient += 1
    return pd.DataFrame(rows)


def main() -> None:
    df = make_dataset()
    out = DATA_DIR / "07_publication_dataset.csv"
    df.to_csv(out, index=False, encoding="utf-8")
    print(f"Данные записаны: {out}")
    print(f"Строк: {len(df)}; пациентов: {df['patient_id'].nunique()}")
    print(df.groupby(["group", "week"])["sbp_mm_hg"].mean().round(1).to_string())


if __name__ == "__main__":
    main()
