"""Implement the function below. It should return the top N records from records, sorted by field, highest first.

def top_n(records: list[dict], field: str, n: int) -> list[dict]:
    ..."""


def top_n(records: list[dict], field: str, n: int) -> list[dict]:
    if n <= 0:
        return []

    return sorted(
        records,
        key=lambda record: record[field],
        reverse=True
    )[:n]

