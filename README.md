# Humble Data Workshop (Taller de datos humildes)

[![Humble Data Workshop](./media/humble-data-logo-transparent.png)](https://humbledata.org)

## ℹ️ Sí deseas saber más sobre este taller, por favor [solicítala aquí](https://forms.gle/t5F6iXLsqeNszt3aA).

---

## Carga el entorno usando pip-tools

```bash
# Activa el entorno
workon beginners-data-workshop

# Actualiza paquetes desde el requirements.txt
# Sí esta es la primera vez, entonces corre pip install pip-tools
pip-sync

# Instalando un nuevo paquete, no olvides actualizar requirements.txt
pip install new-package-name
pip freeze  # to check version number

# Copia y pega el paquete y la versión a requirements.in
pip-compile
pip-sync
```

## Configuración para asistentes del taller

1. Visita [https://bit.ly/humble-python-setup] para instalar Python en su máquina.
2. Los notebooks de este proyecto deberían funcionar correctamente con Anaconda, están listos para usar. Si quieres crear tu propio ambiente virtual para este taller, su mentora lo guiará a través de la configuración más simple.

> Nota: La configuración de desarrollo que se describe a continuación funcionará para ti, pero es más compleja de lo que necesita para seguir este taller. Esta configuración está diseñada para facilitar la actualización de las dependencias de Python (por ejemplo, pandas, Seaborn) y ejecutar verificaciones automáticas para resaltar si algún código en los cuadernos está roto (lo llamamos "conjunto de pruebas").

## Configuración de desarrollo

Este proyecto utiliza [pyenv](https://github.com/pyenv/pyenv), [pyenv-virtualenvwrapper](https://github.com/pyenv/pyenv-virtualenvwrapper) y [Poetry](https://python-poetry.org/docs/).

Consulta [aquí](https://github.com/CoefficientSystems/coefficient-cookiecutter/blob/develop/%7B%7Bcookiecutter.repo_name%7D%7D/docs/getting_started.md) para obtener una guía de instalación paso a paso.

```bash
# Instala Python
pyenv install $(cat .python-version)
pyenv shell $(cat .python-version)
python -m pip install --upgrade pip
python -m pip install virtualenvwrapper
pyenv virtualenvwrapper

# Configura el virtualenv
mkvirtualenv -p python$(cat .python-version) $(cat .venv)
python -V
python -m pip install --upgrade pip

# Instala las dependencias con Poetry
poetry self update
poetry install --no-root --remove-untracked

# Crea un Jupyter Kernel
python -m ipykernel install --user --name beginners-data-workshop --display-name "Python (beginners-data-workshop)"

# Instala Jupyter Extensions static files
jupyter contrib nbextension install --user
# Mas info: https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/install.html
```

---

## Licencia

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />Esta obra está licenciada bajo una <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"> Creative Commons Reconocimiento-NoComercial-CompartirIgual 4.0 Licencia Internacional</a>.
