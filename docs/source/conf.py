#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# This file is execfile()d with the current directory set to its
# containing dir.

import sys
from pathlib import Path

if sys.platform == 'linux':
    HOME = Path.home()
else:
    HOME = Path(r'D:/Users/Aran-Fey')



# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.intersphinx'
]
intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'programming-advice'
author = 'Aran-Fey'
copyright = '2020, ' + author

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.1'
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
# pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

html_theme = "advice"
html_theme_path = [HOME / "Desktop/folder/coding/python/sphinx_utils/sphinx_utils/themes"]
html_show_copyright = False
html_show_sphinx = False
html_title = "Aran-Fey's (python) programming guides"
# This css file can be generated with the command
#   pygmentize -S STYLE_NAME -f html > _static/pygments-light.css
# html_css_files = [('pygments-light.css', {'media': '(prefers-color-theme: light)'})]
