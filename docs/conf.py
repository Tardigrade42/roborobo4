# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

from importlib.metadata import version as pkg_version

# -- Project information -----------------------------------------------------

project = 'Pyroborobo'
copyright = '2021, Paul Ecoffet, Nicolas Bredeche'
author = 'Paul Ecoffet, Nicolas Bredeche'

# Pull version from installed package
release = pkg_version("roborobo")
version = release

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
    "numpydoc",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

master_doc = 'index'
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- MyST configuration ------------------------------------------------------

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "tasklist",
    "substitution",
]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static'] # <= only use this if you really need it and the folder exists

# -- Intersphinx -------------------------------------------------------------

intersphinx_mapping = {
    'python': ('http://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'pybind11': ('http://pybind11.readthedocs.io/en/stable/', None)
}

default_role = 'any'

# Since this is not easily possible for dynamic bindings,
# this disables generating automatic stubs:
autosummary_generate = False
autosummary_generate = False
numpydoc_show_class_members = False
