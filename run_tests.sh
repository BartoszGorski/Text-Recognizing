#!/bin/sh

pytest src/base_gen/tests/test_compute_features.py
pytest src/base_gen/tests/test_article_getter.py
rm -rf .pytest_cache
