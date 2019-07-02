
[![Build status](https://ci.appveyor.com/api/projects/status/3jhdnwreqoni1492/branch/master?svg=true)](https://ci.appveyor.com/project/{{github_project_name}}/branch/master)

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
