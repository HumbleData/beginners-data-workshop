# Beginner's Data Workshop

### If you would like to know more about this workshop, please [apply here](https://forms.gle/t5F6iXLsqeNszt3aA) .

---

## Load the environment using pip-tools
```
# Activate environment
workon beginners-data-workshop

# Update packages from requirements.txt
# If this is the first time, then pip install pip-tools
pip-sync
 
# Install new package & update requirements.txt
pip install new-package-name
pip freeze  # to check version number

# copy paste package & version to requirements.in
pip-compile
pip-sync
```

## Setup
```
# Install virtualenv
pip install virtualenv


# Install virtualenvwrapper (http://virtualenvwrapper.readthedocs.org/en/latest/index.html)
pip install virtualenvwrapper
# Tell shell to source virtualenvwrapper.sh and where to put the virtualenvs by adding following to .zshrc
zshconfig
#    # "Tell shell to source virtualenvwrapper.sh and where to put the virtualenvs"
#    export WORKON_HOME=$HOME/.virtualenvs
#    export PROJECT_HOME=$HOME/code
#    source /usr/local/bin/virtualenvwrapper.sh
source ~/.zshrc
source /usr/local/bin/virtualenvwrapper.sh
# Now let's make a virtualenv
mkvirtualenv venv
workon venv
# Commands `workon venv`, `deactivate`, `lsvirtualenv` and `rmvirtualenv` are useful
# WARNING: When you brew install formulae that provide Python bindings, you should not be in an active virtual environment.
# (https://github.com/Homebrew/homebrew/blob/master/share/doc/homebrew/Homebrew-and-Python.md)
deactivate


# Create virtualenv & install packasges
mkvirtualenv beginners-data-workshop
pip install pip-tools
pip-sync
python -m ipykernel install --user --name beginners-data-workshop --display-name "Python (beginners-data-workshop)"

# Install Jupyter Extensions static files
jupyter contrib nbextension install --user
# More info: https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/install.html
```

---

## License

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
