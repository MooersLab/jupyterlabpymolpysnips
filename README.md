# jupyterlabpymolpysnips

The jupyterlabpymolpysnips library had PyMOL code written in Python for use in Jupyter Notebooks that source the PyMOL API.
This library is designed for use with the `jupyterlab-snippets-multimenu` [extension](https://github.com/kuanpern/jupyterlab-snippets-multimenus) for Jupyter Lab.
This extension requires *JupyterLab version >= 2.0* and *Node.js*.
Node.js can be installed by one of several different software managers including HomeBrew and Anaconda.

This `jupyterlab-snippets-multimenu` extension can be installed via the left panel in Jupyter (remember to rebuild Juptyer Lab), it can be installed from the terminal, or it can be installed from inside a Jupyter Notebook that has been opened in Jupyter Lab.

```bash
!pip install jupyterlab-snippets-multimenus
!jupyter lab build
```

This repo has one library to ease its cloning into the local Jupyter library on a local machine,  Colab, JupyterHub, or the like for use in JupyterLab.


Enter the following command to find the paths to the Jupyter data directory (use ! if doing this from a Jupyter Notebook cell):

```bash
!jupyter --path
```

This path on Mac OS 10.15 is `/Users/blaine/Library/Jupyter`.
Next make a directory called `multimenus_snippets`.
Then move to this directory and clone the repo to the directory with the shortened name `pymolpysnips`.
The shortened name reduces the space taken in the toolbar menu.

```bash
!mkdir /Users/blaine/Library/Jupyter/multimenus_snippets
!cd /Users/blaine/Library/Jupyter/multimenus_snippets
!git clone https://github.com/MooersLab/jupyterlabpymolpysnips.git pymolpysnips
```

The user can add their home-made snippets to the subfolders inside of the `./multimenus_snippets/pymolpysnips` folder.
