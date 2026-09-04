"""Energy Insights Analyzer"""

import argparse
import csv

from energy_insights.stats import compute_daily_averages, find_spikes


def main() -> None:
    """Main function to analyze energy insights from a CSV file."""
    parser = argparse.ArgumentParser(
        description="Analyze CSV data for energy insights."
    )

    parser.add_argument("--file", help="Path to the CSV file")

    parser.add_argument(
        "--timestamp", default="timestamp", help="Name of the timestamp column"
    )

    parser.add_argument("--value", default="price", help="Name of the price column")

    parser.add_argument(
        "--top", type=int, default=5, help="Number of top spikes to find"
    )

    args = parser.parse_args()

    with open(args.file, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    daily_averages = compute_daily_averages(rows, args.timestamp, args.value)
    spikes = find_spikes(rows, args.value, args.top)

    print("Daily Averages:")
    for date, avg in daily_averages.items():
        print(f"  {date}: {avg:.2f}")

    print("\nTop Spikes:")
    for row in spikes:
        print(f"  {row[args.timestamp]}: {row[args.value]}")


if __name__ == "__main__":
    main()
