
TODO: By default the build badge is for Travis CI.  There is a commented example of an Appveyor CI badge you can use instead.
<!-- 
[![Build status](https://ci.appveyor.com/api/projects/status/3jhdnwreqoni1492/branch/master?svg=true)](https://ci.appveyor.com/project/{{github_project_name}}/branch/master) 
-->
[![Build status](https://travis-ci.com/{{github_project_name}}.svg?branch=master)](https://travis-ci.com/{{github_project_name}}?branch=master)
[![codecov](https://codecov.io/gh/{{github_project_name}}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{github_project_name}})

# Documentation

To generate documentation:
```
cd docs
make html
```

The docs will be under `docs/_build/html`

# Contributing

Run `make precommit` before commiting.  Eventually this will be automated.

If you are using PyCharm, please set your docstring format to "Google" and your unit test runner to "PyTest"
in `Preferences | Tools | Python Integrated Tools`.
