#!/bin/bash

# Navigate to the docs directory
cd docs || exit

# Build the documentation
sphinx-build -b html source/ build/html

# Copy the built HTML files to the docs root
cp -r build/html/* ./

# Clean up the build directory (optional)
rm -rf build/html
