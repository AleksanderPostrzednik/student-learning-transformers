#!/usr/bin/env bash
set -e
DATA_DIR="data"
DATASET="adilshamim8/student-performance-and-learning-style"
mkdir -p "$DATA_DIR"

kaggle datasets download -d "$DATASET" -p "$DATA_DIR" --force
unzip -o "$DATA_DIR"/*.zip -d "$DATA_DIR"
rm "$DATA_DIR"/*.zip

echo "Dataset downloaded to $DATA_DIR"
