"""Functions for computing average daily values along with timestamp and price spikes."""

from collections import defaultdict
from datetime import datetime


def compute_daily_averages(
    rows: list[dict[str, str]], ts_col: str, value_col: str
) -> dict[str, float]:
    """Compute the average value for each day based on the provided timestamp and price column."""
    daily_values: dict[str, list[float]] = defaultdict(list)

    for row in rows:
        timestamp = datetime.fromisoformat(row[ts_col])
        value = float(row[value_col])

        date = timestamp.date().isoformat()
        daily_values[date].append(value)

    return {date: sum(values) / len(values) for date, values in daily_values.items()}


def find_spikes(
    rows: list[dict[str, str]], value_col: str, top: int
) -> list[dict[str, str]]:
    """Find the top N spikes in the provided price column."""
    sorted_rows = sorted(rows, key=lambda row: float(row[value_col]), reverse=True)
    return sorted_rows[:top]
