# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SPOCK'
copyright = '2024, Elsa Ducrot'
author = 'Elsa Ducrot'
release = '2.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Sphinx extensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx_rtd_theme',  # Add this for ReadTheDocs theme
]

# Paths to templates
templates_path = ['_templates']

# HTML options
html_theme = 'sphinx_rtd_theme'  # Using ReadTheDocs theme
html_static_path = ['_static']