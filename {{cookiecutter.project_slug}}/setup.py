#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

from os.path import abspath, dirname, join

with open(join(dirname(abspath(__file__)), 'FILL_ME_IN', 'version.py')) as version_file:
    exec(compile(version_file.read(), "version.py", 'exec'))

setup(name='vistautils',
      version=version,
      author='FILL_ME_IN',
      author_email='FILL_ME_IN',
      description="FILL_ME_IN",
      url='FILL_ME_IN',
      packages=['FILL_ME_IN'],
      # 3.6 and up, but not Python 4
      python_requires='~=3.6',
      install_requires=[
      ],
      scripts=[
          ],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
      )
