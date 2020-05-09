# Beginner's Data Workshop

Would you like to learn to code but don’t know where to start? Taking your first steps in programming can seem like an impossible task so we’ve decided to put on a workshop to show 60 beginners how it can be done and share our passion for the world of data science!

> _"We want our community to be more diverse: whoever you are, and whatever your background, we welcome you."_ – [Python Software Foundation's Diversity Statement](https://www.python.org/psf/diversity/)

We invite those from underrepresented groups in data to apply to join us on **Saturdays 9th and 16th May 2020** for the **PyCon 2020 Beginners Data Workshop for Minorities**. In this two-part online workshop you will learn the basics of programming in Python, as well as how to use tools such as Jupyter Notebook to analyse data.

You will be learning in small groups, each with an assigned mentor to guide you through the workshop materials and answer your questions. This will all be facilitated online through the wonders of modern technology. You can expect plenty of exercises, quizzes and games, and inspiring talks from those who were once in your shoes. Key details as follows:

- **When?**   You must attend both sessions on **Saturday 9th May 2020** _and_ **Saturday 16th May 2020** at **9:00am - 12:30pm EDT** (6:00am - 9:30am PDT / 2:00pm - 5:30pm BST).
- **Where?  What do I need to bring?**   Online! You will need a computer with internet access. You will not be required to install anything. 
- **What do I need to know?**   If you have zero programming experience, this workshop is made for you! If you already have some experience but are new to Python, we've got you covered too – the materials are designed for attendees to progress through the materials at their own rate.
- **How is this free?**   This workshop is being run by data scientists and software engineers dedicated to the spirit of open source. Every day we benefit from the hard work of others when we use free open tools. This is our way of giving back. We thank [PyCon US](https://us.pycon.org/2020/) and the [Python Software Foundation](https://www.python.org/) for their support in facilitating this workshop.


### If you would like to attend this workshop, please [apply here](https://docs.google.com/forms/d/1LhEX9veEfWgvymYVqMMo8m6ryIJdD_gHp6mAa821uu8/) .

---

**We are looking for volunteers to help mentor the attendees!** If you are interested, [please apply here](https://docs.google.com/forms/d/1akNaTEsHvJA5iiGhYntAjQyvn5Bcv_R4vA0NtrhDjkM/). You don't need to be an expert in programming or Python – we're teaching the basics! You do need:

* Lots of patience, smiles and a friendly attitude.
* The ability to answer all sorts of questions in a beginner-friendly way (even if that means the explanation isn’t technically precise) throughout the duration of the workshop.
* Curiosity!

In return, you'll meet interesting new people outside your usual developer group, eternal gratitude from your group of attendees, and you'll be helping to break down stereotypes around what a developer "looks like". Plus you can add all that on your CV!

---

![Beginners Data Workshop.png](https://pycon-assets.s3.amazonaws.com/2020/media/images/uploads/83db521722-Beginners-Data-Workshop.png)


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
pip-compile requirements.in
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
```

---

## License

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
