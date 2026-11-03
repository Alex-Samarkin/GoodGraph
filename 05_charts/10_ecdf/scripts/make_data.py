#!/usr/bin/env python3
"""Данные для раздела 5.10: длительность госпитализации.

Сценарий
--------
1 200 госпитализаций: 600 плановых и 600 экстренных. Длительность
в днях скошена вправо; экстренные госпитализации в среднем длиннее.
ECDF показывает сдвиг распределения и позволяет точно прочитать медианы.

Данные синтетические, но реалистичные:

* плановые: медиана около 6 дней;
* экстренные: медиана около 9 дней;
* правый хвост до 20–25 дней.

Файл: data/10_dataset.csv
Запуск: uv run python 05_charts/10_ecdf/scripts/make_data.py
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR

SEED = 20240528
N_PER_GROUP = 600


def make_dataset(seed: int = SEED) -> pd.DataFrame:
    """Сгенерировать длительности плановых и экстренных госпитализаций."""
    rng = np.random.default_rng(seed)
    rows = []
    patient = 1

    for group, mean_log, sigma in [
        ("плановое", 1.75, 0.42),
        ("экстренное", 2.15, 0.48),
    ]:
        values = rng.lognormal(mean=mean_log, sigma=sigma, size=N_PER_GROUP)
        values = np.clip(np.round(values), 1, 30).astype(int)
        for value in values:
            rows.append(
                {
                    "patient_id": f"B{patient:04d}",
                    "admission_type": group,
                    "los_days": int(value),
                }
            )
            patient += 1

    return pd.DataFrame(rows)


def main() -> None:
    df = make_dataset()
    out = DATA_DIR / "10_dataset.csv"
    df.to_csv(out, index=False, encoding="utf-8")

    summary = (
        df.groupby("admission_type")["los_days"]
        .agg(["count", "median", "mean"])
        .round(1)
    )
    print(f"Данные записаны: {out}")
    print(f"Строк: {len(df)}")
    print(summary.to_string())


if __name__ == "__main__":
    main()
