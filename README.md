# jupyterlabpymolpysnips

The jupyterlabpymolpysnips library has PyMOL code written in Python for use in Jupyter Notebooks that are being edited by JuptyerLab and that source the PyMOL API.
JupyterLab is browser-based like Juptyer Notebooks. 
It is a lightweight Integrated Development Environment for Jupyter Notebooks.
This library is designed for use with the `jupyterlab-snippets-multimenus` [extension](https://github.com/kuanpern/jupyterlab-snippets-multimenus) for Jupyter Lab.
This extension requires *JupyterLab version >= 2.0 <3.0.0* and *Node.js*.
Note that the default JuptyerLab from Anaconda is now 3.0.0.
This version is too advanced for the `jupyterlab-snippets-multimenu` extension.
Node.js can be installed by one of several different software managers.
The nodejs from Anaconda is often too outdated.
On the Mac, install Node.js with homebrew.
On Linux, use apt install. 

## The are several methods installing juptyer and pymol together.

### Create a conda environment with Juptyer and PyMOL

```bash
conda create -n juppymol conda-forge::juptyer schrodinger::pymol-bundle
conda activate juppymol
conda install conda-forge::juptyerlab=2.2.0 -y
pip install jupyter-nbextensions-configurator
jupyter serverextension list
pip install jupyterlab-snippets-multimenus
jupyter lab build 
juputer lab clean
mkdir /Users/blaine/Library/Jupyter/multimenus_snippets
cd /Users/blaine/Library/Jupyter/multimenus_snippets
git clone https://github.com/MooersLab/jupyterlabpymolpysnips.git pymol
git clone https://github.com/MooersLab/jupyterlabpymolpysnipsplus.git pymol+
ipython kernel install --name juppymol --user
pip install jupyter-nbextensions-configurator
jupyter serverextension list
jupyter serverextension enable --py jupyterlab --user
python -c 'from pymol import cmd'
juptyer lab
```

The penultimate command is a quick test the environment's python interpreter can load the pymol API.
Select the kernel named juppymol after starting JuptyerLab.
You should be a pymol menu in the menu toolbar of the JuptyerLab GUI.
This menu leads to a cascade of submenus and the individual snippet files.


### Install JuptyerLab inside of PyMOL

Open the PyMOL.app applciation and enter one at a time the following commands at the PyMOL prompt:

```bash
conda install conda-forge::jupyter -y
conda install -c conda-forge:: jupyterlab=2.2.0 -y. # this installed jupyterlab-3.0.0
conda install conda-forge::cctbx-base -y
conda install schrodinger::tk
```

In a terminal window, enter the following commands:

```bash
/Applications/PyMOL.app/Contents/bin/pip install jupyterlab-snippets-multimenus
/Applications/PyMOL.app/Contents/bin/jupyter-lab build
/Applications/PyMOL.app/Contents/bin/jupyter-lab clean
mkdir /Users/blaine/Library/Jupyter/multimenus_snippets
cd /Users/blaine/Library/Jupyter/multimenus_snippets
git clone https://github.com/MooersLab/jupyterlabpymolpysnips.git pymol
git clone https://github.com/MooersLab/jupyterlabpymolpysnipsplus.git pymol+
/Applications/PyMOL.app/Contents/bin/ipython kernel install --name juppymol --user
/Applications/PyMOL.app/Contents/bin/pip install jupyter-nbextensions-configurator
/Applications/PyMOL.app/Contents/bin/jupyter serverextension list
/Applications/PyMOL.app/Contents/bin/jupyter serverextension enable --py jupyterlab --user
/Applications/PyMOL.app/Contents/bin/python -c 'from pymol import cmd'
/Applications/PyMOL.app/Contents/bin/juptyer-lab
```

The penultimate command is a quick test the environment's python interpreter can load the pymol API.
Select the kernel named juppymol after starting JuptyerLab.
You should be a pymol menu in the menu toolbar of the JuptyerLab GUI.
This menu leads to a cascade of submenus and the individual snippet files.

