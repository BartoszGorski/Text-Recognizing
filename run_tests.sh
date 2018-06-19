#!/bin/sh

python3 -m pytest src/tests/test_compute_features.py
rm -rf .pytest_cache
