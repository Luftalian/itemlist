# docs/conf.py
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'ItemList'
author = 'Haruki Nakajima'
release = '0.1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']
