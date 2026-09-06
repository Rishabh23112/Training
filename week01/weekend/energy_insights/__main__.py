"""CLI for Energy Insights."""

import argparse
import csv
import sys

from energy_insights.cli import anomaly_detection, daily_average, top_spikes


def main() -> None:
    """Main CLI execution flow."""
    parser = argparse.ArgumentParser(description="Analyze hourly energy price.")

    parser.add_argument("--file", required=True, help="File path to CSV")
    parser.add_argument("--metric", default="price", help="Price column name ")
    parser.add_argument("--top", type=int, default=10, help="Top N spikes to show ")
    parser.add_argument(
        "--timestamp",
        default="timestamp",
        help="Timestamp column name",
    )

    args = parser.parse_args()

    # CSV loading
    try:
        with open(args.file, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
    except FileNotFoundError:
        print(f"Error: File not found at '{args.file}'")
        sys.exit()

    if not rows:
        print("Error: The provided CSV file is empty.")
        sys.exit()

    headers = rows[0].keys()
    if args.metric not in headers:
        print(f"Error: Metric column '{args.metric}' not found in CSV.")
        sys.exit()

    if args.timestamp not in headers:
        print(f"Error: Timestamp column '{args.timestamp}' not found in CSV.")
        sys.exit()

    if args.top < 1:
        print("Error: Top should be greater than 1.")
        sys.exit()

    average = daily_average(rows, args.timestamp, args.metric)
    spikes = top_spikes(rows, args.metric, args.top)
    anomalies = anomaly_detection(rows, args.metric)

    print("Daily Averages:")
    print(f"{'Date'} {'\tAvg_Price'}")

    for date, avg in average.items():
        print(f"{date} ${avg:.2f}")

    print(f"\nTop {args.top} Price Spikes:")
    for row in spikes:
        price_val = float(row[args.metric])
        print(f"{row[args.timestamp]} ${price_val:.2f}")

    print(f"\nAnomalies detected: {anomalies} hours")


if __name__ == "__main__":
    main()
