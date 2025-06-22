#!/usr/bin/env bash
set -e

if command -v conda >/dev/null 2>&1; then
  echo "Creating conda environment..."
  conda env create -f environments/environment.yml
  echo "Activate with: conda activate learn-tx"
else
  echo "Conda not found. Falling back to venv."
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r environments/requirements.txt
fi
