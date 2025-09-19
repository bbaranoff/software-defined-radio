# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Software Defined Radio'
copyright = '2025, Bastien Baranoff'
author = 'Bastien Baranoff'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_static_path = ['_static']
extensions = [
    "myst_parser",
    'sphinx_wagtail_theme'
    # ... (autres extensions éventuelles)
]
html_theme = 'sphinx_wagtail_theme'

# Pour Sphinx >=4.2, tu peux utiliser master_doc (sinon: root_doc)
master_doc = "index"
