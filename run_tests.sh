#!/bin/sh

cd src
python3 -m pytest tests/test_compute_features.py
rm -rf .pytest_cache
