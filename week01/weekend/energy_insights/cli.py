"""CLI tool functions to analyze hourly prices."""

from collections import defaultdict
from datetime import datetime

import numpy as np
from scipy import stats


def daily_average(rows: list[dict[str, str]], ts_col: str, price_col: str) -> dict[str, float]:
    """Average price per day."""
    daily_values: dict[str, list[float]] = defaultdict(list)
    for row in rows:
        timestamp = datetime.fromisoformat(row[ts_col])
        price = float(row[price_col])
        daily_values[timestamp.date().isoformat()].append(price)

    return {date: sum(prices) / len(prices) for date, prices in sorted(daily_values.items())}


def top_spikes(rows: list[dict[str, str]], price_col: str, top: int) -> list[dict[str, str]]:
    """Top N price spikes."""
    return sorted(rows, key=lambda row: float(row[price_col]), reverse=True)[:top]


def anomaly_detection(rows: list[dict[str, str]], price_col: str, threshold: float = 2.0) -> int:
    """Identify outliers using z-score > 2."""
    prices = np.array([float(row[price_col]) for row in rows])

    if len(prices) < 2:
        return 0

    z_scores = stats.zscore(prices)

    if np.isnan(z_scores).all():
        return 0

    return int(np.sum(np.abs(z_scores) > threshold))
