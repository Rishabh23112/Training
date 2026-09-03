#!/bin/bash

set -euo pipefail

show_help() {
    echo "Usage: $0 <csv_file>"
    echo
    echo "Analyze an energy CSV file."
    echo
    echo "Options:"
    echo "  -h, --help    Show this help message"
}


if [[ $# -eq 0 ]]; then
    show_help
    exit 1
fi


case "$1" in
    -h|--help)
        show_help
        exit 0
        ;;
esac


CSV_FILE="$1"


if [[ ! -f "$CSV_FILE" ]]; then
    echo "Error: file '$CSV_FILE' does not exist." >&2
    exit 1
fi


python3 -m energy_insights --file "$CSV_FILE" 
