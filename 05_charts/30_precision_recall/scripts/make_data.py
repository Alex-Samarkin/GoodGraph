#!/usr/bin/env python3
"""Данные для 5.30: precision–recall, редкий исход."""

from __future__ import annotations

import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR

SEED = 20240611
N = 600


def main() -> None:
    rng = np.random.default_rng(SEED)
    y = rng.binomial(1, 0.08, N)
    score = rng.normal(1.6 * y, 1.0, N)
    df = pd.DataFrame({"patient_id": [f"P{i:03d}" for i in range(1, N + 1)],
                       "score": np.round(score, 3), "event": y})
    out = DATA_DIR / "30_dataset.csv"
    df.to_csv(out, index=False, encoding="utf-8")
    print(f"Данные записаны: {out}; prevalence={y.mean():.3f}")


if __name__ == "__main__":
    main()
