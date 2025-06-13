# Humble Data Workshop

[![Humble Data Workshop](./media/humble-data-logo-transparent.png)](https://humbledata.org)

## ℹ️ If you would like to know more about this workshop, please [email us](mailto:contact@humbledata.org).

---
## Table of Contents
* [Accessing the materials in browser](#accessing-the-materials-in-browser)
* [Local environment setup](#local-environment-setup)
	+ [UV Installation](#uv-installation)
	+ [Installing Miniconda](#installing-miniconda)
 		- [Windows](#windows)
 		- [Unix (Linux/macOS)](#unix-linuxmacos)
+ [Creating and Activating the Environment](#creating-and-activating-the-environment)

* [License](#license)
---

### Accessing the materials in browser

During the workshop, we provide the materials for beginners using a JupyterLite server. The materials are currently available in [English](https://humbledata.org/online-workshop/lab/index.html), [Spanish](https://humbledata.org/online_workshop_spanish/lab/index.html) and [Italian](https://humbledata.org/online-workshop-italian-v2/lab/index.html). Please contact us if you'd like to help out the project by translating the materials into other languages!  
**The easiest way to access the materials for beginners is to use our [JupyterLite](https://jupyterlite.readthedocs.io/en/stable/) server.** Select a language below to get started:

The materials can also be cloned from our [GitHub repo](https://github.com/HumbleData/beginners-data-workshop). If you want to use the materials this way, you will need to install them locally. Instructions on how to do this are provided below. Don't worry if you've never done this before—these instructions are designed for complete beginners and will walk you through each step.
- [English](https://humbledata.org/online-workshop/lab/index.html)
- [Spanish](https://humbledata.org/online_workshop_spanish/lab/index.html)
- [Italian](https://humbledata.org/online-workshop-italian-v2/lab/index.html).

Please contact us if you'd like to help out the project by translating the materials into other languages! 

## Local environment setup

To run these notebooks on on your machine you must set up a *Python environment*. This document contains instructions on how to run the workshop using either `uv` or `conda` (Miniconda).

Start by cloning the repository and then entering the directory:
```bash
git clone https://github.com/HumbleData/beginners-data-workshop.git
cd beginners-data-workshop
```
Then follow either the "UV Installation" or "Miniconda Installation" instructions below.

### UV Installation
To run this workshop locally using `uv`, first you will need to [install uv](https://docs.astral.sh/uv/getting-started/installation/) on your computer.

Once it is done, follow the instructions below:

1. Create a virtual python virtual environment 3.10+
	* `uv venv humble-data-workshop --python 3.10`
2. Activate the virtual environment.
	* `source humble-data-workshop/bin/activate`
3. Install Dependencies
	* `uv pip install -r requirements.txt`

### Miniconda Installation

#### Windows
1. Download the Miniconda installer for Windows from the [official website](https://docs.conda.io/en/latest/miniconda.html)
2. Double-click the downloaded `.exe` file
3. Follow the installation prompts:
   - Click "Next"
   - Accept the license terms
   - Select "Just Me" for installation scope
   - Choose an installation directory (default is recommended)
   - In "Advanced Options", check "Add Miniconda3 to my PATH environment variable"
   - Click "Install"

#### Unix (Linux/macOS)
1. Download the Miniconda installer for your system from the [official website](https://docs.conda.io/en/latest/miniconda.html)
2. Open Terminal
3. Navigate to the directory containing the downloaded file
4. Make the installer executable:
   ```bash
   chmod +x Miniconda3-latest-*-x86_64.sh
   ```
5. Run the installer:
   ```bash
   ./Miniconda3-latest-*-x86_64.sh
   ```
6. Follow the prompts:
   - Press Enter to review the license agreement
   - Type "yes" to accept the license terms
   - Confirm the installation location (default is recommended)
   - Type "yes" to initialize Miniconda3

#### Creating and Activating the Environment

1. Open a new terminal (Windows: Anaconda Prompt, Unix: Terminal)
2. Create a new environment named 'humble-data':
   ```bash
   conda create -n humble-data python=3.8
   ```
3. Activate the environment:
   - Windows:
     ```bash
     conda activate humble-data
     ```
   - Unix:
     ```bash
     conda activate humble-data
     ```
4. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

5. Start Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
   This will open Jupyter Notebook in your default web browser. You can now navigate to and open any of the workshop notebooks.

## Contributing

1. Fork this repository
2. Clone your fork locally
3. Create a branch for your changes:
```git checkout -b improve-notebook-x```

4. Make your changes:

- Keep explanations simple and beginner-friendly
- Test notebooks in both Google Colab and local environments
- Follow existing code style and formatting


5. Commit with a clear message:
```git commit -m "Fix typo in data visualization notebook"```

6. Push and create a pull request

---

## License

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
