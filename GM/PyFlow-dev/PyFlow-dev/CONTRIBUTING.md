# PyFlow - Contributing guide

[![Pytest badge](https://github.com/Bycelium/Pyflow/actions/workflows/python-tests.yml/badge.svg?branch=master)](https://github.com/MathisFederico/Pyflow/actions/workflows/python-tests.yml) [![Pylint badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fgist.githubusercontent.com%2FMathisFederico%2F00ce73155619a4544884ca6d251954b3%2Fraw%2Fpyflow_pylint_badge.json)](https://github.com/MathisFederico/Pyflow/actions/workflows/python-pylint.yml) [![Unit coverage badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fgist.githubusercontent.com%2FMathisFederico%2F00ce73155619a4544884ca6d251954b3%2Fraw%2Fpyflow_unit_coverage_badge.json)](https://github.com/MathisFederico/Pyflow/actions/workflows/python-coverage.yml) [![Integration coverage badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fgist.githubusercontent.com%2FMathisFederico%2F00ce73155619a4544884ca6d251954b3%2Fraw%2Fpyflow_integration_coverage_badge.json)](https://github.com/MathisFederico/Pyflow/actions/workflows/python-coverage.yml)

Whenever you encounter a :beetle: **bug** or have :tada: **feature request**,
report this via [GitHub issues](https://github.com/Bycelium/PyFlow/issues).

We are happy to receive contributions in the form of **pull requests** via GitHub.

Feel free to fork the repository, implement your changes and create a merge request to the **dev** branch.

## Getting started

First, make sure you have `python` installed. You will need to install all the `requirements` and the `requirements-dev` using the following commands:

-   `pip install -r requirements.txt`
-   `pip install -r requirements-dev.txt`

You can run the program with `python main.py`

Before doing your **pull request**, check using `pylint` and `pytest` that there were no code regressions.

```bash
pylint .\pyflow\
```

Some `pylint` issues can be fixed automatically using `black`, with the following command:

```bash
black .
```

```bash
pytest --cov=pyflow --cov-report=html tests/unit
```

We want to keep the _Pylint_ score above _9.0_.

The comments and docstrings should preferably follow [these](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) guidelines.

## Git Commit Messages

Commits should start with a Capital letter and should be written in present tense (e.g. `:tada: Add cool new feature` instead of `:tada: Added cool new feature`).
You should also start your commit message with one or two applicable emoji. This does not only look great but also makes you rethink what to add to a commit. Make many but small commits!

| Emoji                                                     | Description                                        |
| --------------------------------------------------------- | -------------------------------------------------- |
| :tada: `:tada:`                                           | When you add a cool new feature                    |
| :beetle: `:beetle:`                                       | When you fixed a bug                               |
| :fire: `:fire:`                                           | When you removed something                         |
| :truck: `:truck:`                                         | When you moved/renamed something                   |
| :wrench: `:wrench:`                                       | When you improved/refactored a small piece of code |
| :hammer: `:hammer:`                                       | When you improved/refactored a large piece of code |
| :sparkles: `:sparkles:`                                   | When you improved code quality (pylint, PEP, ...)  |
| :art: `:art:`                                             | When you improved/added design assets              |
| :rocket: `:rocket:`                                       | When you improved performance.                     |
| :memo: `:memo:`                                           | When you wrote documentation.                      |
| :umbrella: `:umbrella:`                                   | When you improved coverage                         |
| :twisted_rightwards_arrows: `:twisted_rightwards_arrows:` | When you merge a branch                            |

This section was inspired by [This repository](https://github.com/schneegans/dynamic-badges-action).

## Creating a new block type

You can checkout [this commit](https://github.com/Bycelium/Pyflow/commits/2305e3c92d88d2fd32644e7eab4c4e40246675d3) which contains the minimal amount of code required to
create a new block type.

## Version Numbers

Version numbers will be assigned according to the [Semantic Versioning](https://semver.org/) scheme.
This means, given a version number MAJOR.MINOR.PATCH, we will increment the:

1.  MAJOR version when we make incompatible API changes,
2.  MINOR version when we add functionality in a backwards compatible manner, and
3.  PATCH version when we make backwards compatible bug fixes.
