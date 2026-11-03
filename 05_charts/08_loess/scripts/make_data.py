#!/usr/bin/env python3
"""Данные для раздела 5.08: доза статина и снижение ЛПНП.

Сценарий
--------
300 пациентов, фиксированные дозы 0, 5, 10, 20, 40 и 80 мг/сут.
Эффект — снижение ЛПНП (%), насыщается с ростом дозы (Emax-модель).
Связь нелинейная, поэтому линейная регрессия недооценивает плато.

Данные синтетические, но реалистичные:

* Emax ≈ 55 %, ED50 ≈ 12 мг;
* при 10 мг эффект ≈ 25 %, при 40 мг ≈ 42 %, при 80 мг ≈ 48 %;
* остаточный разброс ≈ 5 %.

Файл: data/08_dataset.csv
Запуск: uv run python 05_charts/08_loess/scripts/make_data.py
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR

SEED = 20240526
DOSES = [0, 5, 10, 20, 40, 80]
N_PER_DOSE = 50
EMAX = 55.0
ED50 = 12.0


def make_dataset(seed: int = SEED) -> pd.DataFrame:
    """Сгенерировать таблицу «пациент — доза — снижение ЛПНП»."""
    rng = np.random.default_rng(seed)
    rows = []
    patient = 1

    for dose in DOSES:
        for _ in range(N_PER_DOSE):
            effect = EMAX * dose / (ED50 + dose) + rng.normal(0.0, 5.0)
            rows.append(
                {
                    "patient_id": f"L{patient:04d}",
                    "dose_mg": dose,
                    "ldl_reduction_pct": round(float(np.clip(effect, 0.0, 70.0)), 1),
                }
            )
            patient += 1

    return pd.DataFrame(rows)


def main() -> None:
    df = make_dataset()
    out = DATA_DIR / "08_dataset.csv"
    df.to_csv(out, index=False, encoding="utf-8")

    summary = (
        df.groupby("dose_mg")["ldl_reduction_pct"]
        .agg(["count", "mean", "std"])
        .round(1)
    )
    print(f"Данные записаны: {out}")
    print(f"Строк: {len(df)}, пациентов: {df['patient_id'].nunique()}")
    print("\nСнижение ЛПНП по дозам:")
    print(summary.to_string())


if __name__ == "__main__":
    main()
