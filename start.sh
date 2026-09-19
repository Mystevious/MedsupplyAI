#!/bin/sh
set -eu

PORT="${PORT:-8080}"

printf '%s\n' "[MedSupplyAI] Production startup"
printf '%s\n' "[MedSupplyAI] Port: ${PORT}"

python backend/init_db.py

exec gunicorn \
  --chdir backend \
  --bind "0.0.0.0:${PORT}" \
  --workers 1 \
  --threads 2 \
  --timeout 120 \
  --access-logfile - \
  --error-logfile - \
  app:app
