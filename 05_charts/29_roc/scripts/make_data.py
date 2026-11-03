#!/usr/bin/env python3
"""Данные для 5.29: ROC-кривая."""

from __future__ import annotations

import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR

SEED = 20240610
N = 500


def main() -> None:
    rng = np.random.default_rng(SEED)
    disease = rng.binomial(1, 0.30, N)
    score = rng.normal(1.2 * disease, 1.0, N)
    df = pd.DataFrame({"patient_id": [f"R{i:03d}" for i in range(1, N + 1)],
                       "score": np.round(score, 3), "disease": disease})
    out = DATA_DIR / "29_dataset.csv"
    df.to_csv(out, index=False, encoding="utf-8")
    print(f"Данные записаны: {out}; prevalence={disease.mean():.2f}")


if __name__ == "__main__":
    main()
