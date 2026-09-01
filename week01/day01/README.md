# Backup Logs Script
## Description

backup_logs.sh creates a compressed backup archive of a given directory and keeps only the latest N archives.

### Usage
```bash 
./week01/day01/scripts/backup_logs.sh <source_directory> <keep_count>
```

### Example
```bash
./week01/day01/src/scripts/backup_logs.sh ./week01/day01/sample_logs 3
```

### Retention Policy

It keeps the latest N archives and delete the older ones.


### Example Output

![terminal output](./src/output/image.png)
