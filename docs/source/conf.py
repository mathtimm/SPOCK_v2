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
extensions = ['sphinx_rtd_theme', 'sphinx.ext.todo', 'sphinx.ext.viewcode',
              'sphinx.ext.autodoc', 'numpydoc', 'nbsphinx', 'myst_parser',
              'sphinx.ext.autosectionlabel', 'sphinx.ext.napoleon', 'recommonmark',]

# Templates and static file directories
html_static_path = ['_static']  # Directory for static files like CSS

# Language settings
language = 'en'  # Change to your preferred language if necessary

# -- HTML output configuration -----------------------------------------------
# The theme to use for HTML and HTML Help pages
html_theme = 'sphinx_rtd_theme'  # Read the Docs theme

import sphinx_rtd_theme
# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Theme options
html_theme_options = {
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
}

# Paths to custom CSS files
html_css_files = [
    'css/style.css',  # Add your custom CSS file if needed
]