.. _hidden: http://sphinx-doc.org/markup/toctree.html

**************************
Sphinx Read The Blog Theme
**************************

A fork of Sphinx Read The Docs theme, but for blogs.

- Banner
- Fluid layout
- Optional Disqus threads

Installation
============

Not yet.

Usage
=====

Example ``conf.py``:

.. code:: python

    # -*- coding: utf-8 -*-

    import sys
    import os

    import sphinx_rtb_theme

    source_suffix = '.rst'
    master_doc = 'index'
    copyright = u'2017'
    exclude_patterns = ['_build', 'README.rst']
    pygments_style = 'tango'
    html_show_copyright = False
    # html_favicon = "images/favicon.ico"
    project = "ReadTheBlog"
    html_title = project
    suppress_warnings = ["image.nonlocal_uri"]

    html_theme = 'sphinx_rtb_theme'
    html_theme_path = [sphinx_rtb_theme.get_html_theme_path()]
    html_theme_options = {
        'navigation_depth': 2,
        'blog_url': 'https://github_username.github.io',
        'disqus_comments': True,
        'disqus_username': 'my_username'
    }


Configuration
=============

You can configure different parts of the theme.

Project-wide configuration
--------------------------

The theme's project-wide options are defined in the ``sphinx_rtb_theme/theme.conf``
file of this repository, and can be defined in your project's ``conf.py`` via
``html_theme_options``. For example:

.. code:: python

    html_theme_options = {
        'collapse_navigation': False,
        'display_version': False,
        'navigation_depth': 3,
    }

The following options are available:

* ``typekit_id``: ???
* ``analytics_id``: Your analytics ID.
* ``sticky_navigation``: default = False.
* ``logo_only``: Only display logo in top-left corner (not project name).
* ``collapse_navigation``: default = False.
* ``display_version``: default = False.
* ``navigation_depth``: default = 4.
* ``prev_next_buttons_location``: default = bottom.
* ``canonical_url``: This will specify a `canonical url <https://en.wikipedia.org/wiki/Canonical_link_element>`__
  to let search engines know they should give higher ranking to latest version of the docs.
  The url points to the root of the documentation and requires a trailing slash.
* ``blog_url``: Tell the blog root URL (example https://pawamoy.github.io).
* ``disqus_comments``: default = False.
* ``disqus_username``: Your Disqus username.


Page-level configuration
------------------------

Pages support metadata that changes how the theme renders.
You can currently add the following:

* ``:disqus_comments:`` If True, it will add a Disqus comments thread at the bottom of the page.
  It overrides the ``disqus_comments`` theme option.
* ``:post_date:`` If set, display the date of the post at the right of the breadcrumbs.
