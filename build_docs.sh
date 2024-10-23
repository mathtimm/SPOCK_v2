#!/bin/bash

# Navigate to the docs directory
cd docs || exit

# Build the documentation
sphinx-build -b html docs/ docs/_build/html

# Copy the built HTML files to the docs root
cp -r docs/_build/html/* ./docs

# Clean up the build directory (optional)
rm -rf docs/_build/html
