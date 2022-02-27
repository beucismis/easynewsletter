# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys


sys.path.insert(0, os.path.abspath(".."))
src_dir = os.path.realpath(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, src_dir)

import easynewsletter as enl


project = "easynewsletter"
version = enl.__version__
release = enl.__version__
author = "beucismis"
copyright = f"2022, {author}"

extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "alabaster"
html_theme_options = {
    "logo": "pigeon.png",
    "logo_name": True,
    "fixed_sidebar": True,
    "page_width": "1000px",
    "sidebar_width": "270px",
    "description": enl.__description__,
}

html_static_path = ["_static"]
