#!/bin/sh

pytest src/base_gen/tests/test_compute_features.py
rm -rf .pytest_cache
