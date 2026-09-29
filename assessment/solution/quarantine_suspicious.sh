
#!/bin/bash

#  --help
if [[ "$1" == "-h" || "$1" == "--help" ]]; then
    echo "Usage: $0 [--dry-run] <target_dir>"
    exit 0
fi

dry_run=false

if [[ "$1" == "--dry-run" ]]; then
    dry_run=true
    shift
fi

if [[ $# -ne 1 ]]; then
    echo "Usage: $0 [--dry-run] <target_dir>"
    exit 1
fi

target="$1"
quarantine="$target/quarantine"

if [[ ! -d "$target" ]]; then
    echo "Error: directory not found"
    exit 1
fi

if ! $dry_run; then
    mkdir -p "$quarantine"
fi

find "$target" -maxdepth 1 -type f -perm -111 -perm -002 -print0 |
while IFS= read -r -d '' file; do
    name=$(basename "$file")

    if $dry_run; then
        echo "WOULD MOVE: $name"
    else
        mkdir -p "$quarantine"
        mv "$file" "$quarantine/$name"

        echo "MOVED: $name"
        printf '%s\t%s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$file" \
            >> "$quarantine/manifest.log"
    fi
done

