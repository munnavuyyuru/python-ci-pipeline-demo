#!/bin/bash
# Pre-warm caches for faster CI runs

set -e

# Warm pip cache
echo " Warming pip cache..."
pip install --upgrade pip setuptools wheel
pip install -r requirements-dev.txt

# Warm pylint cache
echo " Warming pylint cache..."
pylint src/ --persistent=yes || true

# Warm mypy cache
echo " Warming mypy cache..."
mypy src/ --incremental --cache-dir=.mypy_cache || true

# Warm pytest cache
echo " Warming pytest cache..."
pytest --collect-only

echo "✅ Cache warming complete!"
