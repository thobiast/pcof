# -*- coding: utf-8 -*-
"""setup.py."""


import setuptools

# Package meta-data.
NAME = "pcof"
DESCRIPTION = "Python Collection Of Functions."
URL = "https://github.com/thobiast/pcof"
AUTHOR = "Thobias Salazar Trevisan"
VERSION = "0.1.1"

# Packages required
REQUIRED = ["prettytable", "pytz"]


def read_file(fname):
    """Read file and return the its content."""
    try:
        with open(fname, "r") as f:
            return f.read()
    except IOError:
        return DESCRIPTION


setuptools.setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    url=URL,
    license="MIT",
    long_description=read_file("README.md"),
    long_description_content_type="text/markdown",
    install_requires=REQUIRED,
    packages=setuptools.find_packages(
        exclude=(["tests", "*.tests", "*.tests.*", "tests.*"])),
    include_package_data=True,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Topic :: Software Development",
        "Topic :: Terminals",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)

# vim: ts=4
