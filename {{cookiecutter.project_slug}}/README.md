
* TODO: By default the build badge is for Travis CI.  There is a commented example of an Appveyor CI badge you can use instead.
* TODO: Add codecov token to `.travis.yml`

<!-- 
[![Build status](https://ci.appveyor.com/api/projects/status/3jhdnwreqoni1492/branch/master?svg=true)](https://ci.appveyor.com/project/{{cookiecutter.github_project_name}}/branch/master) 
-->
[![Build status](https://travis-ci.com/{{cookiecutter.github_project_name}}.svg?branch=master)](https://travis-ci.com/{{cookiecutter.github_project_name}}?branch=master)
[![codecov](https://codecov.io/gh/{{cookiecutter.github_project_name}}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.github_project_name}})

# Documentation

To generate documentation:
```
cd docs
make html
```

The docs will be under `docs/_build/html`

# Project Setup

1. Create a Python 3.6 Anaconda environment (or your favorite other means of creating a virtual environment): `conda create --name {{cookiecutter.project_slug}} python=3.6` followed by `conda activate {{cookiecutter.project_slug}}`.
2. `pip install -r requirements.txt`

# Contributing

Run `make precommit` before commiting.  

If you are using PyCharm, please set your docstring format to "Google" and your unit test runner to "PyTest"
in `Preferences | Tools | Python Integrated Tools`.
