#!/bin/sh

pytest tests/test_compute_features.py
pytest tests/test_article_getter.py
rm -rf .pytest_cache
