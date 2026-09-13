"""Build the guide without importing any robot software."""

project = "Working with the G1"
author = "sri299792458"
copyright = "2026, sri299792458 and contributors"
extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinxcontrib.mermaid",
    "sphinx.ext.githubpages",
]
source_suffix = {".md": "markdown"}
root_doc = "index"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
myst_heading_anchors = 3
myst_enable_extensions = ["colon_fence"]
html_theme = "furo"
html_title = "Working with the G1"
html_baseurl = "https://sri299792458.github.io/g1-research-docs/"
html_theme_options = {
    "source_repository": "https://github.com/sri299792458/g1-research-docs/",
    "source_branch": "main",
    "source_directory": "docs/",
    "light_css_variables": {"color-brand-primary": "#176b65", "color-brand-content": "#176b65"},
    "dark_css_variables": {"color-brand-primary": "#74c9bf", "color-brand-content": "#74c9bf"},
}
html_static_path = ["assets/stylesheets"]
html_css_files = ["extra.css"]
html_show_sourcelink = True
html_show_sphinx = False
html_permalinks_icon = "#"
pygments_style = "friendly"
pygments_dark_style = "monokai"
