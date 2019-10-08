#!/usr/bin/env python

from distutils.core import setup
from os.path import abspath, dirname, join

from setuptools import find_packages

with open(
    join(dirname(abspath(__file__)), "{{cookiecutter.project_slug}}", "version.py")
) as version_file:
    exec(compile(version_file.read(), "version.py", "exec"))

setup(
    name="{{cookiecutter.project_slug}}",
    version=version,  # noqa
    author="{{cookiecutter.full_name}}",
    author_email="{{cookiecutter.email}}",
    description="{{cookiecutter.project_short_description}}",
    url="{{cookiecutter.github_url}}",
    packages=[],
    # 3.6 and up, but not Python 4
    python_requires="~=3.6",
    install_requires=[],
    scripts=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
