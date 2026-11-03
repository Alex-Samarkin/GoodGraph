#!/usr/bin/env python3
"""Данные для 5.27: выживаемость в двух группах."""

from __future__ import annotations

import numpy as np
import pandas as pd

from goodgraph.paths import DATA_DIR

SEED = 20240608
N_PER_GROUP = 120
GROUPS = [("Контроль", 0.045), ("Лечение", 0.028)]


def main() -> None:
    rng = np.random.default_rng(SEED)
    rows = []
    patient = 1
    for group, hazard in GROUPS:
        event_time = rng.exponential(1 / hazard, N_PER_GROUP)
        censor_time = rng.uniform(6, 36, N_PER_GROUP)
        time = np.minimum(event_time, censor_time)
        event = (event_time <= censor_time).astype(int)
        time = np.clip(time, 0.5, 36)
        for t, e in zip(time, event, strict=True):
            rows.append({"patient_id": f"K{patient:03d}", "group": group,
                         "time_months": round(float(t), 1), "event": int(e)})
            patient += 1
    df = pd.DataFrame(rows)
    out = DATA_DIR / "27_dataset.csv"
    df.to_csv(out, index=False, encoding="utf-8")
    print(f"Данные записаны: {out}; {len(df)} строк")
    print(df.groupby("group")["event"].agg(["count", "sum"]).to_string())


if __name__ == "__main__":
    main()
