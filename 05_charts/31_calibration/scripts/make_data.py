#!/usr/bin/env python3
"""Данные для 5.31: калибровка прогноза."""

from __future__ import annotations

import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR

SEED = 20240612
N = 400


def main() -> None:
    rng = np.random.default_rng(SEED)
    p = rng.beta(2, 5, N)
    y = rng.binomial(1, np.clip(p * 1.18, 0, 1))
    df = pd.DataFrame({"patient_id": [f"C{i:03d}" for i in range(1, N + 1)],
                       "predicted_risk": np.round(p, 3), "outcome": y})
    out = DATA_DIR / "31_dataset.csv"
    df.to_csv(out, index=False, encoding="utf-8")
    print(f"Данные записаны: {out}; events={y.sum()}")


if __name__ == "__main__":
    main()
