# -*- coding: utf-8 -*-
"""`sphinx_rtb_theme` lives on `Github`_.

.. _github: https://github.com/Pawamoy/sphinx_rtb_theme

"""
from setuptools import setup
from sphinx_rtb_theme import __version__


setup(
    name='sphinx_rtb_theme',
    version=__version__,
    url='https://github.com/Pawamoy/sphinx_rtb_theme',
    license='MIT',
    author='Timothee Mazzucotelli',
    author_email='timothee.mazzucotelli@gmail.com',
    description='ReadTheBlog theme for Sphinx (ReadTheDoc theme fork).',
    long_description=open('README.rst').read(),
    zip_safe=False,
    packages=['sphinx_rtb_theme'],
    package_data={'sphinx_rtb_theme': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/js/*.js',
        'static/font/*.*'
    ]},
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
    entry_points = {
        'sphinx.html_themes': [
            'sphinx_rtb_theme = sphinx_rtb_theme',
        ]
    }
)
