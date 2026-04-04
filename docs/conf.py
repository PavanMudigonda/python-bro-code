"""Sphinx configuration for Python Bro Code documentation."""

project = "Python Bro Code"
copyright = "2024, Pavan Mudigonda"
author = "Pavan Mudigonda"
release = "1.0.0"

extensions = [
    "myst_nb",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_thebe",
]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]
myst_heading_anchors = 3

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "myst-nb",
    ".ipynb": "myst-nb",
}

templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "**/.ipynb_checkpoints",
    "**/__pycache__",
]

suppress_warnings = [
    "myst.header",
    "myst.xref_missing",
]

html_theme = "furo"
html_title = "Python Bro Code"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#306998",
        "color-brand-content": "#306998",
    },
    "dark_css_variables": {
        "color-brand-primary": "#FFD43B",
        "color-brand-content": "#FFD43B",
    },
    "source_repository": "https://github.com/PavanMudigonda/python-bro-code",
    "source_branch": "main",
    "source_directory": "docs/",
}

# ---------------------------------------------------------------------------
# myst-nb: notebook execution settings
# ---------------------------------------------------------------------------
nb_execution_mode = "off"  # "off" renders existing outputs; switch to "auto" or
                           # "cache" to execute cells during the build.
nb_execution_timeout = 30
nb_execution_raise_on_error = False

# ---------------------------------------------------------------------------
# sphinx-thebe: live "Run" button (connects to Binder for a free kernel)
# ---------------------------------------------------------------------------
thebe_config = {
    "repository_url": "https://github.com/PavanMudigonda/python-bro-code",
    "repository_branch": "main",
    "path_to_docs": "docs/",
}

# sphinx-copybutton already provides the "Copy" button on every code block.
# No extra config needed — both Run and Copy are now available.
