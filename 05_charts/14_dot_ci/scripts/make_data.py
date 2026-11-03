#!/usr/bin/env python3
"""Данные для раздела 5.14: осложнения по шести центрам.

Сценарий
--------
600 пациентов, шесть центров, по 100 человек. Бинарный исход —
осложнение (1/0). Доли различаются: от 8 до 22 %. Для каждой доли
строится 95 % доверительный интервал Уилсона.

Данные синтетические, но реалистичные:

* Центр A — около 8 %;
* Центр B — около 12 %;
* Центр C — около 15 %;
* Центр D — около 18 %;
* Центр E — около 10 %;
* Центр F — около 22 %.

Файл: data/14_dataset.csv
Запуск: uv run python 05_charts/14_dot_ci/scripts/make_data.py
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR

SEED = 20240601
N_PER_CENTER = 100

CENTERS = [
    ("Центр A", 0.08),
    ("Центр B", 0.12),
    ("Центр C", 0.15),
    ("Центр D", 0.18),
    ("Центр E", 0.10),
    ("Центр F", 0.22),
]


def make_dataset(seed: int = SEED) -> pd.DataFrame:
    """Сгенерировать бинарный исход «осложнение» по центрам."""
    rng = np.random.default_rng(seed)
    rows = []
    patient = 1

    for center, probability in CENTERS:
        events = rng.binomial(1, probability, N_PER_CENTER)
        for event in events:
            rows.append(
                {
                    "patient_id": f"D{patient:04d}",
                    "center": center,
                    "complication": int(event),
                }
            )
            patient += 1

    return pd.DataFrame(rows)


def main() -> None:
    df = make_dataset()
    out = DATA_DIR / "14_dataset.csv"
    df.to_csv(out, index=False, encoding="utf-8")

    summary = (
        df.groupby("center")["complication"]
        .agg(["count", "sum", "mean"])
        .assign(percent=lambda x: (x["mean"] * 100).round(1))
        .round(3)
    )
    print(f"Данные записаны: {out}")
    print(f"Строк: {len(df)}")
    print(summary.to_string())


if __name__ == "__main__":
    main()
