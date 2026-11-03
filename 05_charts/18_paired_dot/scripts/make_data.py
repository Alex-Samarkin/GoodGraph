#!/usr/bin/env python3
"""Данные для раздела 5.18: гемоглобин до и после лечения анемии.

Сценарий
--------
30 пациентов, гемоглобин (г/л) до и через 8 недель лечения. Парные
наблюдения: у большинства уровень вырос, у части — снизился или не
изменился. Paired dot показывает каждую пару.

Данные синтетические, но реалистичные:

* гемоглобин до — около 95 г/л (80–110);
* средний прирост — около 14 г/л;
* индивидуальный разброс прироста — около 8 г/л.

Файл: data/18_dataset.csv
Запуск: uv run python 05_charts/18_paired_dot/scripts/make_data.py
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR

SEED = 20240603
N = 30


def make_dataset(seed: int = SEED) -> pd.DataFrame:
    """Сгенерировать парные измерения гемоглобина."""
    rng = np.random.default_rng(seed)
    before = np.clip(rng.normal(95.0, 8.0, N), 78.0, 112.0)
    change = rng.normal(14.0, 8.0, N)
    after = np.clip(before + change, 75.0, 145.0)

    return pd.DataFrame(
        {
            "patient_id": [f"H{i:02d}" for i in range(1, N + 1)],
            "hemoglobin_before": np.round(before, 1),
            "hemoglobin_after": np.round(after, 1),
        }
    )


def main() -> None:
    df = make_dataset()
    out = DATA_DIR / "18_dataset.csv"
    df.to_csv(out, index=False, encoding="utf-8")

    diff = df["hemoglobin_after"] - df["hemoglobin_before"]
    print(f"Данные записаны: {out}")
    print(f"Строк: {len(df)}")
    print(f"Среднее до: {df['hemoglobin_before'].mean():.1f} г/л")
    print(f"Среднее после: {df['hemoglobin_after'].mean():.1f} г/л")
    print(f"Средний прирост: {diff.mean():.1f} ± {diff.std(ddof=1):.1f} г/л")
    print(f"Снизился: {(diff < 0).sum()} пациентов")


if __name__ == "__main__":
    main()
