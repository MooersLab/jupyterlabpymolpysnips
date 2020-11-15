# jupyterlabpymolpysnips

The jupyterlabpymolpysnips library had pymol code written in Python for use in Jupyter Notebooks that source the PyMOL api.
This library is designed for use with the multimenu-snippets extension for JupyterLab. 
This repo has one library to ease its cloning into the local Jupyter library on a local machine,  Colab, JupyterHub, or the like for use in JupyterLab.

Enter the following command to find the paths to the jupyter data dictory (use ! if doing this from a Jupyter Notebook cell):

```bash
!jupyter --path
```

This path on Mac OS 10.15 is ```/Users/blaine/Library/Jupyter```.

```bash
!mkdir /Users/blaine/Library/Jupyter/multimenus_snippets
!cd /Users/blaine/Library/Jupyter/multimenus_snippets
!git clone https://github.com/MooersLab/jupyterlabpymolpysnips.git pymolpysnips
```
