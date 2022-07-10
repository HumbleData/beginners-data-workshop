# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<!-- TOWNCRIER -->

## [1.1.0] - 2022-07-10

- Various upgrades ([#40](https://github.com/HumbleData/beginners-data-workshop/pull/40))
- **Behind-the-scenes**
  - Upgrade Python to 3.9.13
  - Upgrade all dependencies to latest with NumPy/pandas/Matplotlib/scikit-learn matching CoCalc versions.
  - Switch from `pip-tools` to Poetry (configuration in `pyproject.toml`)
  - Update Development Setup guidance in `README.md`
  - Integrate & configure flake8, pylint, black & other linters.
  - Added pre-commit configuration.
  - Updated VS Code `settings.json`
  - Added `linestripper.py` to keep EOF newlines out of solutions code (better attendee UX) yet black-compliant.
  - Added `CHANGELOG.md` and started versioning releases.
- **Workshop materials**
  - Reviewed all workshop materials for deprecations.
  - Replaced all single quotes in solutions with double quotes for black compliance.
  - Added EOF newlines to datasets.
  - Other minor changes: trailing whitespace, trailing commas, isort compliant solution code.


## [1.0.0] - 2021-07-23
Final version used for Humble Data workshops in 2021.
