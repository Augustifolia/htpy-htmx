#!/usr/bin/env bash
for version in 3.10 3.11 3.12 3.13 3.14; do
    echo "=== Python $version ==="
    uv run --python $version pytest
    uv run --python $version mypy .
done

black --check .
