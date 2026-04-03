#!/usr/bin/env bash

# This script runs any pre-build steps before mkdocs build
echo "Running pre-build steps for MkDocs..."

# Generate docs from chapter directories
python scripts/generate_docs.py

exit 0
