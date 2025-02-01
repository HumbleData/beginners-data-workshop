# Humble Data Workshop

[![Humble Data Workshop](./media/humble-data-logo-transparent.png)](https://humbledata.org)

## ℹ️ If you would like to know more about this workshop, please [email us](mailto:contact@humbledata.org).

---

## Local environment set up

### Installing Miniconda

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

### Creating and Activating the Environment

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

---

## License

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
