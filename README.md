# Humble Data Workshop (Taller de datos humildes)

[![Humble Data Workshop](./media/humble-data-logo-transparent.png)](https://humbledata.org)

## ℹ️ Si desea saber más sobre este taller, por favor [solicite aquí](https://forms.gle/t5F6iXLsqeNszt3aA).

---

## Cargue el entorno usando pip-tools

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

## Configuración de asistentes

1. Visite [https://bit.ly/humble-python-setup] para instalar Python en su máquina.
2. Los cuadernos de este proyecto deberían funcionar muy bien con Anaconda lista para usar. Si quieres crear tu propia virtual
   ambiente para este taller, su mentor lo guiará a través de la configuración más simple.

> Nota: la configuración de desarrollo que se describe a continuación funcionará para usted, pero es más compleja de lo que necesita para seguir este
  taller. Esta configuración está diseñada para facilitar la actualización de las dependencias de Python (por ejemplo, pandas, Seaborn) y ejecutar
  verificaciones automáticas para resaltar si algún código en los cuadernos está roto (lo llamamos "conjunto de pruebas").

## Configuración de desarrollo

Este proyecto utiliza [pyenv](https://github.com/pyenv/pyenv), [pyenv-virtualenvwrapper](https://github.com/pyenv/pyenv-virtualenvwrapper)
y [Poetry](https://python-poetry.org/docs/). Consulte [aquí](https://github.com/CoefficientSystems/coefficient-cookiecutter/blob/develop/%7B%7Bcookiecutter.repo_name%7D%7D/docs/getting_started.md)  para obtener una guía de instalación paso a paso.

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

## Licencia

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />Esta obra está licenciada bajo un<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"> Creative Commons Reconocimiento-NoComercial-CompartirIgual 4.0 Licencia Internacional</a>.
