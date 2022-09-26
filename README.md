# jupyterlabpymolpysnips: Templates for writing and running PyMOL in Jupyter Notebooks.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4429717.svg)](https://doi.org/10.5281/zenodo.4429717)
![Version](https://img.shields.io/static/v1?label=jupyterlabpymolpysnips&message=0.2&color=brightcolor)

There are many ways to get **PyMOL** running in **JupyterLab**. For details on installing **JupyterLab** and **PyMOL**, go to the [GitHub Page](https://mooerslab.github.io/jupyterlabpymolpysnips/) associated with this project.
For a list of the snippets and their descriptions, also go to the [GitHub Page](https://mooerslab.github.io/jupyterlabpymolpysnips/) associated with this project.

<a id="table-of-contents"><h2>Table of Contents</h2></a>

* [Motivation](#motivation)
* [New to scripting in PyMOL](#new)
* [Tech Stack](#technology-stack)
* [Installation](#installation)
* [Configuration Setup](#configuration-setup)
* [Usage](#usage)
* [Testing](#testing)
* [Requests for new snippets and text editors](#requests)
* [Bug reports](#bugreports)
* [Roadmaps](#roadmap)
* [License](#license)
* [Contact Information](#contact-information)
* [How to cite](#citation)


<a id="motivation"><h2>Motivations for this project</h2></a>

### Use jupyterlabpymolpysnips to be more productive while running PyMOL in Jupyter


<p>The animation below demonstrates the use of the <b>ao.py</b> snippet in <em>JupyterLab</em> to insert 17 lines of code for generating the ambient occlusion effect.</p>

<p align="center"><img src="gifs/aoUbuntu.gif"></p>


The result of applying a variant of the above code to a 27-nucleotide RNA hairpin is shown below.

<p align="center"><img src="./images/5d99AOD.png" alt="HTML5 Icon" style="width:364px;height:630px;"></p>

There is no option in a pulldown menu in **PyMOL** to make such an image. 
A script file with 17 commands is required.
This code can be applied to any molecular object that has been loaded into **PyMOL**.

[Return to Table of Contents](#table-of-contents)


### Why run PyMOL in a Jupyter Notebook?


#### Streamlines the management of images for a project
You can store the images generated by PyMOL in one **Jupyter Notebook** file instead of having dozens of script and images files squirreled away in dozens of subfolders.
Using one file eases finding the code to make a particular figure because the code can be placed above the image.
This ability to quickly find the required code at a later time reduces the resistance to remaking a figure for manuscript resubmission, journal cover artwork, posters, platform presentations, lectures, book chapters, review articles, websites, and wall hangings.

The use of one file also eases the sharing of images with collaborators because only one file needs to be shared.
You can reformt the notebook as a static HTML or PDF file if your collaborators are not **PyMOL** or **Jupyter Notebook** users.


#### Facilitates combining PyMOL with other software in molecular structure analysis

During a molecular structure analysis project, you can run additional software from the same notebook (e.g., bio3d, ProDy, cctbx, phenix, ccp4, ccpem, XDS).
This can improve the reproducibility of the computational aspects of your research.

The primary caveat is that the nonPython software will require different kernels. 
This caveat means that you will have to switch kernels to use these packages in the same notebook and that you cannot run software with different kernels in the same cell.
These are minor limitations.

A secondary caveat is that, sadly, some heavily used structural biology programs have yet to migrate from Python2 to Python3. 
You may have trouble running a Python2 kernel in **JupyterLab** installed to run with Python3.
Fortunately, you can run many of these programs by using the shell magic in the notebook.
This cell magic allows you to store the input and output in the notebook.
This workaround enables you to carry on with your modern reproducible research practices with legacy code.

[Return to Table of Contents](#table-of-contents)


### But I will miss the interactive viewport in PyMOL!

1. There is nothing stopping you from running the PyMOL GUI next to your **JupyterLab** session. You can adjust the molecule's orientation manual, run the **get_view** command, and copy the output in the command history window from PyMOL and paste it into a cell in the **Jupyter Notebook**. The one line of settings return by the **rv** shortcut are much easier to use. 

2. You really do not need the viewport. With 10-15 minutes of practice, you can master the rapid iterating of rotate and translate commands to adjust the molecule's orientation with greater precision than via manipulation of the mouse.

[Return to Table of Contents](#table-of-contents)


<a id="new"><h2>New to PyMOL scripting?</h2></a>

If you are not ready to write PyMOL scripts, please consider using [PyMOL shortcuts](https://github.com/MooersLab/pymolshortcuts) to enhance your productivity in **PyMOL** interactive sessions.
For example, the above ambient occlusion effect can be invoked at any time by entering `AO` at the **PyMOL** prompt if the *pymolshortcuts.py* file has been loaded.
These shortcuts can also be invoked in a **Jupyter Notebook** by submitting them as arguments to the cmd.do() method, (e.g., cmd.do("AO") to generate the ambient occlusion effect.)## Application Description

The **jupyterlabpymolpysnips** library contains 260 code fragments (i.e., templates or snippets) written in Python to run PyMOL in **JupyterLab** via **PyMOL**'s **Python** API.
This API is only available for recent versions of **PyMOL** that depend on Python3.
This API is available for both the incentive and open-source versions of **PyMOL**.

[Return to Table of Contents](#table-of-contents)


<a id="technology-stack"><h2>Technology Stack for </h2></a>

| Technology                                                                                 | Version  | Description                                                                                        |
|--------------------------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------|
| [PyMOL](https://pymol.org/2/)                                                              | 2.4.0    | Molecular graphics program                                                                         |
| Python                                                                                     | 3.7-3.8  | Programming language                                                                               |
| [JupyterLab](https://pypi.org/project/jupyterlab/)                                          | >=2.0    | A IDE for editing Jupyter Notebooks.                                                              |
| [jupyterlab-snippets](https://github.com/QuantStack/jupyterlab-snippets)                    | 0.4.0 or 0.4.1    | Required extension                                                                                |
| Node.js                                                                                    | >=10.0.0 | Required by Jupyter and many extensions.                                                           |
| git                                                                                        | 2.25.1   | Eases the downloading and updating of the libraries.                                               |


## or use this alternate set of programs  

You may have to create a new conda env to install the older version of JupyterLab. 

| Technology                                                                                 | Version  | Description                                                                                        |
|--------------------------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------|
| [PyMOL](https://pymol.org/2/)                                                              | >2.4.0    | Molecular graphics program                                                                         |
| Python                                                                                     | 3.7-3.8  | Programming language                           
| [JupyterLab](https://pypi.org/project/jupyterlab/)                                         | >2.2.0    | A IDE for editing Jupyter Notebooks. Version 3.0 does not work with jupyterlab-snippets-multimenus |
| [jupyterlab-snippets-multimenus](https://github.com/QuantStack/jupyterlab-snippets       ) | 0.4.0    | Required extension                                                                                 |
| Node.js                                                                                    | >=10.0.0 | Required by Jupyter and many extensions.                                                           |
| git                                                                                        | 2.25.1   | Eases the downloading and updating of the libraries.                                               |


Some of the snippets are limited to Python3 code.
Suppose you use an outdated version of **PyMOL** that relies on Python2. In that case, you can buy a license to the current version of **PyMOL**; install a free, open-source version of **PyMOL** that depends on Python3 (See the [PyMOL Wiki](https://pymolwiki.org/index.php/Main_Page)); or you can rewrite the snippet's code to be Python2 compliant. 
The latter task involves replacing print statements in Python2 with print() functions in Python3.
The command-line program **2to3** automates this process. 
Note that multiple versions of **PyMOL** can operate side-by-side on a computer, so you do not have to delete that old version of **PyMOL**.

JupyterLab can use the **jupyterlab-snippets** extension to make the snippets available via a **snippets** pull-down menu.
Conda, pip, or the extension manager in **Jupyter Lab** can install the extension.

Assuming that **JupyterLab**, **jupyterlab-snippets**, and **PyMOL** are already installed, run the following commands one line at a time,

```bash
jupyter --path
cd ~/.local/share/jupyter # change as per output from prior line. Use cd ~/Library/Jupyter on the Mac.
mkdir snippets
cd snippets
git clone https://github.com/MooersLab/jupyterlabpymolpysnips.git pymol
git clone https://github.com/MooersLab/jupyterlabpymolpysnipsplus.git pymol+
```

When you open **JupyterLab**, you will find a **snippet** pull-down menu on the JupyterLab menu bar.
There will be a **pymol** sub-menu and a **pymol+** sub-menu under this pull-down.

JupyterLab needs to be version >=2.2.0 for **jupyterlab-snippets** to run. 
The current version of **JupyterLab** is 3.3.4.

You can install **Node.js** from the Node.js developer's web site or with a package manager.
It needs to be more recent than version 10.0.0. 
Be ware that Anaconda has in the past installed ancient versions of node and that you may have to set the version number to install a newer version of node via Anaconda.
You may have better luck using the installer from the developer. 
Run it in the active conda env where you want to run jupyterlab.

[Return to Table of Contents](#table-of-contents)

<a id="installation"><h2>Installation of the snippet library</h2></a>

Alternatively, you can use the **jupyterlab-snippets-multimenus** package.
The package will appear on the menu bar as separate pull-down menus: **pymol** and **pymol+**.
This approach removes a layer of hierarchy in the pull-down menus so that you can select the snippet of interest faster.
The downside is that you must use an older version of JupyterLab.

Assuming that **JupyterLab**, **jupyterlab-snippets-multimenus**, and PyMOL are already installed, run the following commands one line at a time:

```bash
jupyter --path
cd ~/.local/share/jupyter # change as per output from prior line. Use cd ~/Library/Jupyter on the Mac.
mkdir multimenus_snippets
cd multimenus_snippets
git clone https://github.com/MooersLab/jupyterlabpymolpysnips.git pymol
git clone https://github.com/MooersLab/jupyterlabpymolpysnipsplus.git pymol+
```

The snippets in the **pymolpysnips+** library have a second copy of the code in a comment with the tab stops marked as follows `${1:default value}`.
Tab stops are sites of parameter values that may need to be edited to customize the snippet.
In most text editors, you hit the tab to advance to the next tab stop.
**JupyterLab** does not yet support tab stops.
(If you want to use tab stops in a text editor, visit the [pymolsnips project](https://github.com/MooersLab/pymolsnips)).
Use the **pymol+** library when you need guidance in editing a snippet.
The content of the active part of the snippet is the same in both libraries.
The commented code in the **pymol+** snip library may annoy experienced users who do not need help with editing.


Alternatively, you can download the repository as a zip file by clicking on the green **code** button above.
However, **git** eases the updating of the libraries are a later time.
You would navigate to the `multimenus_snippets/pymol` folder and then enter `git pull` to update the library.
This is far less painful than down downloading the library as a zip file.
Repeat for `pymol+` if needed.
Navigate back to your home directory before running **JupyterLab** (e.g., `cd` or `cd ~/`).

Now, fire up **JupyterLab**. 

```bash
jupyter lab
```


[Return to Table of Contents](#table-of-contents)


<a id="configuration-setup"><h2>Configuration Setup</h2></a>

The snippet library is independent of PyMOL. 
No modification of PyMOL is required. 

[Return to Table of Contents](#table-of-contents)


<a id="usage"><h2>Usage</h2></a>

The animation at the top of the page conveys the essential knowledge for usage. 

[Return to Table of Contents](#table-of-contents)


<a id="testing"><h2>Testing</h2></a>

Try the **ao.py** snippet. You should get a result similar to the one should in the animation above.

[Return to Table of Contents](#table-of-contents)


<a id="requests"><h2>Requests for new snippets</h2></a>

Please use the **Issues tab** above to request support for additional snippets or to ask questions.
Alternatively, you can send [e-mail](#contact-information) to me.

Questions about PyMOL should be directed to the [PyMOL Mailing List](https://pymolwiki.org/index.php/PyMOL_mailing_list).

[Return to Table of Contents](#table-of-contents)


<a id="requests"><h2>Contributing</h2></a>

Snippets of new code are most welcome. Send to [e-mail](#contact-information).

- Submit the Python code in a plain text file.
- Write the filenames and function names in camelCase.
- Provide a description of what the code does in one to several sentences, an examples of usage, and any citations or links to further information.

[Return to Table of Contents](#table-of-contents)


<a id="bugreports"><h2>Bug reports</h2></a>

Use the **Issues tab** above to report bugs or send [e-mail](#contact-information) to me.

[Return to Table of Contents](#table-of-contents)


<a id="roadmap"><h2>Roadmap</h2></a>

I plan to expand the library to cover with examples the 500 commands and 600 settings in PyMOL.

[Return to Table of Contents](#table-of-contents)


<a id="license"><h2>License</h2></a>

We use the permissive MIT license.
The license information for this project is found in the *License.txt* file above. 

[Return to Table of Contents](#table-of-contents)


<a id="contact-information"><h2>Contact Information</h2></a>

I can be reached via the Issue tab above or via e-mail: `blaine-mooers at ouhsc.edu`.

[Return to Table of Contents](#table-of-contents)


<a id="citation"><h2>Citation</h2></a>

If you use this library to make figures for publication, please see the *Citation.md* file above.

A paper describing this library was published in April 2021.


```bibtex
@Article{Mooers2021APyMOLSnippetLibraryForJupyterToBoostResearcherProductivity,
  author    = {Mooers, Blaine HM},
  journal   = {Computing in Science \& Engineering},
  title     = {A PyMOL snippet library for Jupyter to boost researcher productivity},
  year      = {2021},
  pages     = {47-53},
  volume    = {23},
  publisher = {IEEE},
  doi       = {10.1109/MCSE.2021.3059536},
}
```

[Return to Table of Contents](#table-of-contents)

## Related Repos

- [easypymol](https://github.com/MooersLab/EasyPyMOL/edit/master/README.md)
- [pymolshortcuts](https://github.com/MooersLab/pymolshortcuts)
- [pymolsnips](https://github.com/MooersLab/pymolsnips)
- [orgpymolpysnips](https://github.com/MooersLab/orgpymolpysnips)
- [rstudiopymolpysnips](https://github.com/MooersLab/rstudiopymolpysnips)
- [taggedpymolpysnips](https://github.com/MooersLab/taggedpymolpysnips)
- [jupyterlabpymolpysnips](https://github.com/MooersLab/jupyterlabpymolpysnips)
- [colabOpenSourcePyMOLpySnips](https://github.com/MooersLab/colabOpenSourcePyMOLpySnips)
- [colabPyMOLpySnips](https://github.com/MooersLab/colabPyMOLpySnips)
- [PyMOLwallhangings](https://github.com/MooersLab/PyMOLwallhangings)
