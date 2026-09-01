#!/bin/bash

set -e

# Check arguments
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <directory> <number_of_archives_to_keep>"
    exit 1
fi

SOURCE_DIR="$1"
KEEP_COUNT="$2"

# source directory
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Directory '$SOURCE_DIR' does not exist."
    exit 1
fi

# N
if ! [[ "$KEEP_COUNT" =~ ^[0-9]+$ ]] || [ "$KEEP_COUNT" -lt 1 ]; then
    echo "Error: Number of archives to keep must be a positive integer."
    exit 1
fi

# Extract directory name
DIR_NAME=$(basename "$SOURCE_DIR")

# archive directory
ARCHIVE_DIR="./week01/day01/archives"
mkdir -p "$ARCHIVE_DIR"

# Current date
DATE=$(date +%F)

# Archive filename
ARCHIVE_FILE="$ARCHIVE_DIR/${DIR_NAME}-${DATE}.tar.gz"

# Create archive
tar -czf "$ARCHIVE_FILE" "$SOURCE_DIR"

echo "Created archive:"
echo "  $ARCHIVE_FILE"

# Find existing archives for this directory, newest first
mapfile -t ARCHIVES < <(
    find "$ARCHIVE_DIR" -maxdepth 1 -type f \
    -name "${DIR_NAME}-*.tar.gz" \
    -printf '%T@ %p\n' |
    sort -nr |
    cut -d' ' -f2-
)

DELETED_COUNT=0

# Delete archives beyond KEEP_COUNT
if [ "${#ARCHIVES[@]}" -gt "$KEEP_COUNT" ]; then
    for ((i=KEEP_COUNT; i<${#ARCHIVES[@]}; i++)); do
        echo "Deleted archive:"
        echo "  ${ARCHIVES[$i]}"

        rm -f "${ARCHIVES[$i]}"
        ((DELETED_COUNT+=1))
    done
fi

echo
echo "Backup Summary"
echo "Created : $ARCHIVE_FILE"
echo "Deleted : $DELETED_COUNT archive(s)"
