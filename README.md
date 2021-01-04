# jupyterlabpymolpysnips

The jupyterlabpymolpysnips library had PyMOL code written in Python for use in Jupyter Notebooks that are being edited by JuptyerLab and that source the PyMOL API.
This library is designed for use with the `jupyterlab-snippets-multimenu` [extension](https://github.com/kuanpern/jupyterlab-snippets-multimenus) for Jupyter Lab.
This extension requires *JupyterLab version >= 2.0* <3.0.0 and *Node.js*.
Note that the default juptyerlab from Anaconda is now 3.0.0 and its too advanced for the `jupyterlab-snippets-multimenu` extension.
Node.js can be installed by one of several different software managers.
The nodejs from Anaconda is often too outdated.
On the Mac, install Node.js with homebrew.
On Linux, use apt install. 

## The are several methods running juptyer and pymol together.

### Create a conda environment with Juptyer and PyMOL

```bash
conda create -n juppymol conda-forge::juptyer schrodinger::pymol-bundle
conda activate juppymol
conda install conda-forge::juptyerlab
pip install jupyter-nbextensions-configurator
jupyter serverextension list
pip install jupyterlab-snippets-multimenus
jupyter lab build 
juputer lab cleam
ipython kernel install --name juppymol --user
pip install jupyter-nbextensions-configurator
jupyter serverextension list
jupyter serverextension enable --py jupyterlab --user
python -c 'from pymol import cmd'
juptyer lab
```


### Install JuptyerLab inside of PyMOL

Open the PyMOL.app applciation and enter one at a time the following commands at the PyMOL prompt:

```bash
conda install conda-forge::jupyter -y
conda install -c conda-forge:: jupyterlab=2.2.0 -y. # this installed jupyterlab-3.0.0
conda install conda-forge::cctbx-base -y
conda install schrodinger::tk
```

In a terminal window, enter the follwoing commands:

```bash
/Applications/PyMOL.app/Contents/bin/pip install jupyterlab-snippets-multimenus
/Applications/PyMOL.app/Contents/bin/jupyter-lab build
/Applications/PyMOL.app/Contents/bin/jupyter-lab clean
/Applications/PyMOL.app/Contents/bin/ipython kernel install --name juppymol --user
/Applications/PyMOL.app/Contents/bin/pip install jupyter-nbextensions-configurator
/Applications/PyMOL.app/Contents/bin/jupyter serverextension list
/Applications/PyMOL.app/Contents/bin/jupyter serverextension enable --py jupyterlab --user
/Applications/PyMOL.app/Contents/bin/python -c 'from pymol import cmd'
/Applications/PyMOL.app/Contents/bin/juptyer-lab
```



### Installing the Snippet Library



The `jupyterlab-snippets-multimenu` extension can be also installed via the left panel in JupyterLab (remember to rebuild Juptyer Lab).
This repo has one library to ease its cloning into the local Jupyter library on a local machine,  Colab, JupyterHub, or the like for use in JupyterLab.
Enter the following command to find the paths to the Jupyter data directory (use ! if doing this from a Jupyter Notebook cell):

```bash
!jupyter --path
```

This path on Mac OS 10.15 is `$home/Library/Jupyter`.
Move to this directory.
Next make a directory called `multimenus_snippets`.
Then move to this directory and clone the repo to the directory with the shortened name `pymol`.
Likewise, git clone the second library with the comments in the snippets to guide the editing of the snippets; it is name `pymol+`
The shortened name reduces the space taken in the toolbar menu.

```bash
mkdir /Users/blaine/Library/Jupyter/multimenus_snippets
cd /Users/blaine/Library/Jupyter/multimenus_snippets
git clone https://github.com/MooersLab/jupyterlabpymolpysnips.git pymol
git clone https://github.com/MooersLab/jupyterlabpymolpysnipsplus.git pymol+
```

The user can add their home-made snippets to the subfolders inside of the `./multimenus_snippets/pymolpysnips` folder.
