# Humble Data Workshop

[![Humble Data Workshop](./media/humble-data-logo-transparent.png)](https://humbledata.org)

## ℹ️ If you would like to know more about this workshop, please [apply here](https://forms.gle/t5F6iXLsqeNszt3aA).

---

## Load the environment using pip-tools

```bash
# Activate environment
workon beginners-data-workshop

# Update packages from requirements.txt
# If this is the first time, then pip install pip-tools
pip-sync

# Install new package & update requirements.txt
pip install new-package-name
pip freeze  # to check version number

# Copy paste package & version to requirements.in
pip-compile
pip-sync
```

## Attendee Setup

1. Visit [https://bit.ly/humble-python-setup] to install Python onto your machine.
2. The notebooks in this project should work great with Anaconda out of the box. If you want to create your own virtual
   environment for this workshop, your mentor will guide you through the simplest setup.

> Note: The Development Setup outlined below will work for you, but is more complex than what you need to follow this
  workshop. This setup is designed to make it easy to upgrade Python dependencies (e.g. pandas, Seaborn), and run
  automated checks to highlight if any code in the notebooks is broken (we call this a "test suite").

## Development Setup

This project uses [pyenv](https://github.com/pyenv/pyenv), [pyenv-virtualenvwrapper](https://github.com/pyenv/pyenv-virtualenvwrapper)
and [Poetry](https://python-poetry.org/docs/). Please [see here](https://github.com/CoefficientSystems/coefficient-cookiecutter/blob/develop/%7B%7Bcookiecutter.repo_name%7D%7D/docs/getting_started.md) for a step-by-step installation guide.

```bash
# Install Python
pyenv install $(cat .python-version)
pyenv shell $(cat .python-version)
python -m pip install --upgrade pip
python -m pip install virtualenvwrapper
pyenv virtualenvwrapper

# Setup the virtualenv
mkvirtualenv -p python$(cat .python-version) $(cat .venv)
python -V
python -m pip install --upgrade pip

# Install dependencies with Poetry
poetry self update
poetry install --no-root --remove-untracked

# Create Jupyter Kernel
python -m ipykernel install --user --name beginners-data-workshop --display-name "Python (beginners-data-workshop)"

# Install Jupyter Extensions static files
jupyter contrib nbextension install --user
# More info: https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/install.html
```

---

## License

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
