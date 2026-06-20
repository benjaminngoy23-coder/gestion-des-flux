#!/bin/sh
set -eu

# Port interne fixe pour éviter les anciennes valeurs PORT de Dokploy.
export PORT=8000
export PYTHONUNBUFFERED=1
export PYTHONDONTWRITEBYTECODE=1

# Utilise le volume persistant s'il est accessible, sinon démarre quand même.
DATA_DIR="${DATA_DIR:-/app/data}"
if ! mkdir -p "$DATA_DIR" 2>/dev/null || [ ! -w "$DATA_DIR" ]; then
  DATA_DIR="/tmp/fundflow_data"
  mkdir -p "$DATA_DIR"
fi
export DATA_DIR
export DB_FILE="${DB_FILE:-fundflow_stable.db}"

exec python -u main.py
