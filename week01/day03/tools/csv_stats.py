"""CSV Statistics script for analyzing numeric columns in CSV files."""

import argparse
import csv
from pathlib import Path


class CSVstatsError(Exception):
    """Custom base exception for CSV statistics errors."""


class MissingColumnError(CSVstatsError):
    """Column is missing from the dataset."""


class InvalidValueError(CSVstatsError):
    """Value is not valid for numeric calculations."""


def load_csv(file_path: str) -> list[dict[str, str]]:
    """Load a CSV file and return the rows as dictionaries."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"The file '{file_path}' doesn't exist.")

    if not path.is_file():
        raise ValueError(f"'{file_path}' is not a file.")

    with open(path, mode="r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        if reader.fieldnames is None:
            raise ValueError("File doesn't contain any headers or is empty.")
        return list(reader)


def get_numeric_values(rows: list[dict[str, str]], column: str) -> list[float]:
    """Convert valid string values from a specified column to floats."""
    if not rows:
        raise ValueError("No data available in file.")

    if column not in rows[0]:
        raise MissingColumnError(f"Column '{column}' not found in CSV.")

    numeric_values = []
    for row in rows:
        value = row.get(column)
        if value is not None and value.strip() != "":
            try:
                numeric_values.append(float(value))
            except ValueError:
                pass

    if not numeric_values:
        raise InvalidValueError(f"No valid numeric data found in column '{column}'.")

    return numeric_values


def summarize_numeric(rows: list[dict[str, str]], column: str) -> dict[str, float]:
    """Summarize the numeric values to return the minimum, maximum, and mean."""
    numeric_values = get_numeric_values(rows, column)
    return {
        "min": min(numeric_values),
        "max": max(numeric_values),
        "mean": sum(numeric_values) / len(numeric_values),
    }


def top_n(rows: list[dict[str, str]], column: str, n: int) -> list[dict[str, str]]:
    """Return the top n rows based on numeric column values."""
    if n < 1:
        raise ValueError("Parameter '--top' must be greater than 0.")

    get_numeric_values(rows, column)

    def parse_key(row: dict[str, str]) -> float:
        try:
            return float(row.get(column, 0))
        except ValueError:
            return float("-inf")

    sorted_rows = sorted(rows, key=parse_key, reverse=True)
    return sorted_rows[:n]


def parse_arguments() -> argparse.Namespace:
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(description="CSV Statistics Tool")
    parser.add_argument("--file", required=True, type=str, help="Path to the CSV file")
    parser.add_argument(
        "--column", 
        
        default="price",
        type=str, 
        help="Numeric column to analyze"
    )
    parser.add_argument(
        "--top",
        
        type=int,
        default=3,
        help="Number of top rows to display (default: 3)",
    )

    return parser.parse_args()


def main() -> int:
    """Main application execution flow."""
    args = parse_arguments()

    try:
        rows = load_csv(args.file)
        summary = summarize_numeric(rows, args.column)
        top_rows = top_n(rows, args.column, args.top)
    except (
        FileNotFoundError,
        ValueError,
        OSError,
        CSVstatsError,
    ) as e:
        print(f"Error: {e}")
        return 1

    print("\nCSV Statistics\n")

    print(f"File:   {args.file}")
    print(f"Rows:   {len(rows)}")
    print(f"Column: {args.column}")

    print("\nNumeric Summary\n")

    print(f"Min:  {summary['min']:.2f}")
    print(f"Max:  {summary['max']:.2f}")
    print(f"Mean: {summary['mean']:.2f}")

    print(f"\nTop {args.top} Rows\n")

    for index, row in enumerate(top_rows, start=1):
        print(f"{index}. {row}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
