# Humble Data Workshop

[![Humble Data Workshop](./media/humble-data-logo-transparent.png)](https://humbledata.org)

## ℹ️ If you would like to know more about this workshop, please [email us](mailto:contact@humbledata.org).

---
## Table of Contents
* [Google Colab setup](#google-colab-setup)
* [Local environment setup](#local-environment-setup)
	+ [UV Installation](#uv-installation)
	+ [Installing Miniconda](#installing-miniconda)
 		- [Windows](#windows)
 		- [Unix (Linux/macOS)](#unix-linuxmacos)
+ [Creating and Activating the Environment](#creating-and-activating-the-environment)

* [License](#license)
---

## Google Colab setup

1. Go to [https://githubtocolab.com/HumbleData/beginners-data-workshop](https://githubtocolab.com/HumbleData/beginners-data-workshop)  
2. Choose the notebook that you want to open  
   ![open a notebook in colab](media/colab/image10.png)
3. Click on the file icon <img src="media/colab/image9.png" alt="file icon" width="30"/> on the left  
4. If you haven’t logged in to your Google account, you will be asked to do so  
   ![sign in to Google](media/colab/image2.png)  
5. At the beginning of the notebook, add a cell by clicking the <img src="media/colab/image8.png" alt="add code icon" width="60"/> button at the top  
   ![adding a code block](media/colab/image1.png) 
6. After that copy and paste the following codes in the new cell:  
   ``` 
   !git clone https://github.com/HumbleData/beginners-data-workshop.git  
   !cp -r beginners-data-workshop/media/ .  
   !cp -r beginners-data-workshop/data/ .  
   !cp -r beginners-data-workshop/solutions/ .  
   !rm -r beginners-data-workshop/  
   ``` 
   > NOTE: You will need to add this code cell to every notebook you start.

   ![adding the script shown above](media/colab/image7.png)  
7. Run the cell by clicking the play button on the left of the cell or press shift \+ enter on your keyboard  
   ![running the script shown above](media/colab/image4.png)
8. You may get this warning when running the first code block. Click “Run anyway” when asked (because you trust us not giving you malicious code).
   ![warning about running code in colab](media/colab/image3.png)
9. When the code is finished (it may take a moment), you should see that three folders are added to your files. Consider the preparation work done and you may now start using the notebook.
   
   <img src="media/colab/image5.png" alt="new files added" width="40%"/>
10. Note that when you disconnect from the notebook (or leave it inactive for a long time) the files we just download with the code and your work is not saved.

    Consider downloading or saving your work in drive before you leave this notebook. You can do so by clicking on the “File” button at the bottom.

    <img src="media/colab/image6.png" alt="saving or downloading file to keep your work" width="60%"/>

---

## Local environment setup

This document contains instructions on how to run the workshop using either `uv` or `conda` (Miniconda).

### UV Installation
To run this workshop locally using `uv`, first you will need to [install uv](https://docs.astral.sh/uv/getting-started/installation/) on your computer.

Once it is done, follow the instructions below:

1. Create a virtual python virtual environment 3.10+
	* `uv venv humble-data-workshop --python 3.10`
2. Activate the virtual environment.
	* `source humble-data-workshop/bin/activate`
3. Install Dependencies 
	* `uv pip install -r requirements.txt`

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
