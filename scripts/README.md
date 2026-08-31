# Backup Logs Script
## Description

backup_logs.sh creates a compressed backup archive of a given directory and keeps only the latest N archives.

### Usage
```bash 
./scripts/backup_logs.sh <source_directory> <keep_count>
```

### Example
```bash
./scripts/backup_logs.sh ./sample_logs 3
```

### Retention Policy

It keeps the latest N archives and delete the older ones.


### Example Output

![alt text](image.png)