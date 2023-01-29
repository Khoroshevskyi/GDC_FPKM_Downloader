#! /usr/bin/env python

import os
from setuptools import setup
import sys

PACKAGE = "fpkmfetcher"
REQDIR = "requirements"

# Additional keyword arguments for setup().
extra = {}

# Ordinary dependencies


def read_reqs(reqs_name):
    deps = []
    with open(os.path.join(REQDIR, "requirements-{}.txt".format(reqs_name)), "r") as f:
        for l in f:
            if not l.strip():
                continue
            # deps.append(l.split("=")[0].rstrip("<>"))
            deps.append(l)
    return deps


DEPENDENCIES = read_reqs("all")
extra["install_requires"] = DEPENDENCIES

scripts = None

with open("{}/_version.py".format(PACKAGE), "r") as versionfile:
    version = versionfile.readline().split()[-1].strip("\"'\n")

with open("README.md") as f:
    long_description = f.read()

setup(
    name=PACKAGE,
    packages=[PACKAGE],
    version=version,
    description="Program for downloading FPKM data and metadata from Genomic Data Commons Data Portal.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    keywords="project, bioinformatics, sequencing, ngs, workflow, GUI",
    url="https://github.com/Khoroshevskyi/{}/".format(PACKAGE),
    author="Oleksandr Khoroshevskyi",
    license="BSD2",
    entry_points={
        "console_scripts": [
            "fpkmfetcher = fpkmfetcher:main",
        ],
    },
    package_data={PACKAGE: ["templates/*"]},
    scripts=scripts,
    include_package_data=True,
    test_suite="tests",
    tests_require=read_reqs("all"),
    setup_requires=(
        ["pytest-runner"] if {"test", "pytest", "ptr"} & set(sys.argv) else []
    ),
    **extra
)
