# -- Path setup --------------------------------------------------------------
import os
import sys

# Add the project's root directory to the system path
sys.path.insert(0, os.path.abspath('.'))  # Change this if needed

# -- Project information -----------------------------------------------------
project = 'SPOCK'
author = 'Your Name'
release = '2.0'  # Update this with your project version

master_doc = 'index'  # or the name of your main documentation file

# -- General configuration ---------------------------------------------------
# Extensions to be loaded
extensions = [
    'sphinx.ext.autodoc',   # Include documentation from docstrings
    'sphinx.ext.viewcode',   # Include highlighted source code
    'sphinx.ext.napoleon',   # Support for Google style docstrings
]

# Templates and static file directories
templates_path = ['_templates']
html_static_path = ['_static']  # Directory for static files like CSS

# Language settings
language = 'en'  # Change to your preferred language if necessary

# -- HTML output configuration -----------------------------------------------
# The theme to use for HTML and HTML Help pages
html_theme = 'sphinx_rtd_theme'  # Read the Docs theme

# Theme options
html_theme_options = {
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
}

# Paths to custom CSS files
html_css_files = [
    'css/custom.css',  # Add your custom CSS file if needed
]

# Output file base name for HTML help builder
htmlhelp_basename = f'{project}Doc'

# -- Options for LaTeX output -----------------------------------------------
latex_engine = 'pdflatex'  # Use pdflatex for LaTeX output

# -- Options for manual page output -----------------------------------------
man_pages = [
    (master_doc, project.lower(), f'{project} Documentation',
     [author], 1)
]

# -- Options for Texinfo output ---------------------------------------------
texinfo_documents = [
    (master_doc, project, f'{project} Documentation',
     author, project, 'One line description of project.',
     'Miscellaneous'),
]

# -- Options for Epub output ------------------------------------------------
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = '2024, Your Name'  # Update with the current year

# Additional settings
html_show_sourcelink = True  # Show link to source code
html_show_copyright = True     # Show copyright information
