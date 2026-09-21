# -*- coding: utf-8 -*-
"""Installer for the plonetheme.imioapps package."""

from setuptools import find_packages
from setuptools import setup


version = "3.0.0.dev0"

long_description = "{0}\n{1}".format(
    open("README.rst").read(),
    open("CHANGES.rst").read(),
)

setup(
    name="plonetheme.imioapps",
    version=version,
    description="Plone 6 Classic UI theme for the iMio applications",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 6.1",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: Theme",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    keywords="plone theme imio bootstrap barceloneta",
    author="IMIO",
    author_email="support@imio.be",
    url="https://github.com/IMIO/plonetheme.imioapps",
    license="GPL",
    packages=find_packages("src"),
    package_dir={"": "src"},
    namespace_packages=["plonetheme"],
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.10",
    install_requires=[
        "setuptools",
        "Products.CMFPlone",
        "plone.app.theming",
        "plonetheme.barceloneta",
    ],
    extras_require={
        "test": [
            "plone.app.testing",
            "plone.testing",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
