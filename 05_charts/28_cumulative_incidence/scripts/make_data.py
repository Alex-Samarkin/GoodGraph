#!/usr/bin/env python3
"""Данные для 5.28: конкурирующие риски."""

from __future__ import annotations

import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR

SEED = 20240609
N = 300


def main() -> None:
    rng = np.random.default_rng(SEED)
    event_time = rng.exponential(1 / 0.055, N)
    censor_time = rng.uniform(6, 36, N)
    observed = event_time <= censor_time
    cause = rng.choice([1, 2], N, p=[0.65, 0.35])
    status = np.where(observed, cause, 0)
    time = np.clip(np.minimum(event_time, censor_time), 0.5, 36)
    df = pd.DataFrame({"patient_id": [f"C{i:03d}" for i in range(1, N + 1)],
                       "time_months": np.round(time, 1), "status": status})
    out = DATA_DIR / "28_dataset.csv"
    df.to_csv(out, index=False, encoding="utf-8")
    print(f"Данные записаны: {out}")
    print(df["status"].value_counts().sort_index().to_string())


if __name__ == "__main__":
    main()
