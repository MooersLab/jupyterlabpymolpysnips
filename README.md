# juptyerlabpymolpysnips: Templates for writing PyMOL scripts.



For more details on installing libraries for specific editors, go to the [GitHub Page](https://mooerslab.github.io/juptyerlabpymolpysnips/).



## Animated demo of snippet use in JupyterLab


<p>The animation below demonstrates the use of the <b>ao</b> tab trigger in JuptyerLab <em>Visual Studio Code</em> to insert 17 lines of code for generating the ambient occlusion effect.
</p>

<p align="center"><img src="gifs/JLaoSnip.gif"></p>


The result of applying a variant of the above code to a 27-nucleotide RNA hairpin is shown below.

<p align="center"><img src="./images/5d99AOD.png" alt="HTML5 Icon" style="width:364px;height:630px;"></p>

There is not an option in a pulldown menu in PyMOL to make such an image: A script is required.

This code can be applied to any molecular object in PyMOL's veiwport, not just RNA.

If you are not ready to write PyMOL scripts, please consider using [PyMOL shortcuts](https://github.com/MooersLab/pymolshortcuts) to enhance your productivity in PyMOL interactive sessions.
For example, the above ambient occlussion effect can be invoked at anytime by entering `AO` at the PyMOL prompt, if the pymolshortcuts.py file has been loaded.

## Application Description

The juptyerlabpymolpysnips library contains 260 code fragments (i.e, templates or snippets) written in Python to run PyMOL in JupyterLab via PyMOL's Python API.
This API is only available for recent versions of PyMOL that depend on Python3.

For more details on using the snippets, a gallery of output, the supported text editors, **library installation**, and the content of the library, please see the associated [GitHub Page](https://mooerslab.github.io/jupyterlabpymolpysnips/).


<a id="table-of-contents"><h2>Table of Contents</h2></a>

* [Tech Stack](#technology-stack)
* [Installation](#installation)
* [Configuration Setup](#configuration-setup)
* [Usage](#usage)
* [Testing](#testing)
* [Requests for new snippets and text editors](#requests)
* [Bug reports](#bugreports)
* [License](#license)
* [Contact Information](#contact-information)
* [How to cite](#citation)



<a id="technology-stack"><h2>Technology Stack</h2></a>

| Technology | Description                               |
|------------|-------------------------------------------|
| PyMOL   2.4   | Molecular graphics program         | 
| Python  3.7-3.9     |  Programming language          |
| JupyterLab 2.2      | A IDE for editing Jupyter Notebooks|
| jupyterlab-snippets-multimens  0.12 | Requirement extension |
| Node.js             | Required by Jupyter and many exensions |

The 
Some of the snippets are limited to Python3 code.
If you are using an ancient version of PyMOL that relies on Python2, you can buy a license to the current version of PyMOL, install a free open-source version of PyMOL that depends on Python3 (See the PyMOL Wiki), or you can rewrite the snippet's code to be Python2 compliant. 
This often merely involves replacing print statements in Python2 with print() functions in Python3.
Note that multiple versions of PyMOL can operate side-by-side on a computer: You do not have to delete that ancient version of PyMOL.


[Return to Table of Contents](#table-of-contents)

<a id="installation"><h2>Installation</h2></a>

Unfortunately, GitHub does not yet provide an easy way to download part of a repository. 
It is easier to download the whole repository, pull out the parts that you need, and delete the rest.
Setting up and maintaining 18 separate repositories was too unwieldy.

Download all of the libraries by using the command `git clone https://github.com/MooersLab/pymolsnips.git` in a terminal window if you have *git* installed.
Alternatively, you download the repository as a zip file by clicking on the green **code** button above.

See the [GitHub Page](https://mooerslab.github.io/pymolsnips/) for installation instructions for several operating systems.

[Return to Table of Contents](#table-of-contents)



<a id="configuration-setup"><h2>Configuration Setup</h2></a>

The snippet libraries are independent of PyMOL. 
No modification of PyMOL is required. 

[Return to Table of Contents](#table-of-contents)


<a id="usage"><h2>Usage</h2></a>

Examples of the snippets in use in various editors are found in the animated gifs on the [GitHub Page](https://mooerslab.github.io/jupyterlabpymolpysnips/). 
These gifs convey the essential knowledge in seconds.

[Return to Table of Contents](#table-of-contents)


<a id="testing"><h2>Testing</h2></a>

Try the **ao** snippet. You should get a result similar to the one should in the demo above.

[Return to Table of Contents](#table-of-contents)



<a id="requests"><h2>Requests for new snippets and text editors</h2></a>

Please use the **Issues tab** above to request support for additional text editors, to suggest additional snippets, or to ask questions.
Alternatiley, you can send [e-mail](#contact-information) to me.

Questions about PyMOL should be directed to the [PyMOL Mailing List](https://pymolwiki.org/index.php/PyMOL_mailing_list).

[Return to Table of Contents](#table-of-contents)


<a id="bugreports"><h2>Bug reports</h2></a>

Use the **Issues tab** above to report bugs or send [e-mail](#contact-information) to me.
Refer bugs in the text editors to the developers of the text editors.

[Return to Table of Contents](#table-of-contents)


<a id="license"><h2>License</h2></a>

We use the permissive MIT license.
The license information for this project is found in the License.txt file above. 

[Return to Table of Contents](#table-of-contents)


<a id="contact-information"><h2>Contact Information</h2></a>

I can be reached via the Issue tab above or via e-mail: `blaine-mooers at ouhsc.edu`.

[Return to Table of Contents](#table-of-contents)


<a id="citation"><h2>Citation</h2></a>

If you use this library to make figures for publication, please see the Citation.md file above.




<h3 name="jupyterlab"> Jupyter Lab (Universal) </h3>

Jupyter Lab is an integrated development environment (IDE) that runs in your web browser.
It can read in Jupyter Notebooks.
It supports several kinds of windows including one for text editing.
It is similar to the RStudio, Rodeo, and Spyder IDEs.
Its first stable release was in 2018.

The Jupyter Notebook is an electronic notebook for interactive programming in Python.
It can be extended for use with scores of other programming languages via kernels.
It was released initially in the fall of 2014.
Jupyter Notebooks are very fun to use when developing new code because the interleaved output in the form of beautiful figures provides instant gratification.

The Jupyter Notebook descended from the IPython Notebook project, which was started in 2011.
The Jupyter Notebook has superseded the Ipython Notebook.
The IPython Notebook project emerged out of the IPython project, which was started in 2001 by Fernando Perez when he was a graduate student in Physics as the U of Colorado.
Ipython is run in a terminal rather than in a browser.
Of course, Ipython is still evolving and it still available.

The Jupyter Notebook is composed of cells.
Code cells can be edited.
They contain blocks of code that generally do one thing.
All of the code in a cell is run at once.
The use of executable blocks of code eases debugging.

PyMOL can be imported into an active notebook as a module.
The most robust way to do this is to make a kernel for the Python interpreter inside of PyMOL.
Give it a meaningful name like *pymol.python*.
Select this kernel after the start up of Jupyter.
You can also install pymol in the same python interpreter used for your installation of jupyter.
This does not always work well.
More information is found on the [PyMOL Wiki](https://pymolwiki.org/index.php/Jupyter).

Jupyter Notebooks are also effective for providing training in the classroom and workshops.
It is designed to support reproducible research and literate programming.
The main gotcha is that you have to be aware of the state of the computer.
That is, you have to be mindful of the order in which the cells were executed.

Jupyter Notebook and Jupyter Lab have extensions that extend their capabilities, but their extensions are not interchangeable.
Both have extensions for vim keybindings, which will appeal to vim users.

<details>
<summary><b>Installation of jupyterlabpymolpysnips and jupyterlab2pymolpysnips for Jupyter Lab</b></summary>

This library has only the Python code without tabstops.
JupyterLab does not support tab stops in snippets at this time.
The *jupyterlab2pymolpysnips* library above includes the code with tabstops in a comment.
This commented code can serve as a reference to aid in finding all sites that need to be edited.
This variant of the library also has a caption that describes the purpose of the code.

You need to install Jupyter first.
There many ways of doing so.
To use the conda route, install anaconda or miniconda first for python3.
You also need the nodejs greater than version 12 installed.
This can be done via conda, too.
I installed jupyter in a conda env called jL37 for jupyterLab run with conda python3.7

```bash
conda create --name jL37
conda activate jL37
conda install -c conda-forge jupyter
conda install -c conda-forge nodejs 
```

You might want to create a bash alias of the same name for more rapid startup of Jupyter Lab.
Add this alias to your .bashrc or .zshrc file, and source this file to activate the alias.

```bash
alias jL37='conda activate jL37 && /opt/anaconda/envs/jL37/bin/jupyter lab'
```
I recommend installing the Juyter Lab extnesion *jupyterlab-snippets-multimenus*. 
The is a fork of the *jupyterlab-snippets* project.
It enables the creation of seperate pulldown menus for each snippet library.
This in turn improves access to the snippets and the likelihood that they will be used.
The installation of *jupyterlab-snippets-multimenus* can be done through the JupyterLab gui or in the terminal via these commands:

```bash
pip install jupyterlab-snippets-multimenus 
jupyter lab build
jupyter --path
```

Use the following command to get the possible folders where the snippet library can be stored.

```bash
jupyter --path
```

For me, the best choice was `/Users/blaine/Library/Jupyter` which serves my multiple variants of Jupyter.


You may want to manually install the defualt example snippets for major Python modules.
The easist way is to use git or you can download the files manually.

```bash
git clone https://github.com/kuanpern/jupyterlab-snippets-multimenus.git
cd jupyterlab-snippets-multimenus
cp -r example_snippets/multimenus_snippets /Users/blaine/Library/Jupyter/.
```

The snippet of simply code in files with the appropriate file extension.
Similar snippers can be grouped in a subfolder.
The subfolders can be nested, although it is usually saner to keep directory trees as swallow as possible.
The readme.md file of https://github.com/kuanpern/jupyterlab-snippets-multimenus describes two ways of configuring the snippets.
The first option lists the subfolders and their files in alpabetical order.
The second option requires very tedious editing a json file. 
We followed the first option.

```bash
git clone https://github.com/MooersLab/pymolpysnips
cd pymolpysnips
cp -r ./jupyterlabpymolpysnips /Users/blaine/Library/Jupyter/multimenus_snippets
```
</details>
<A href=#FASTLINKS2>Return to list of editors above.</A>




[JupuyterLab](https://jupyter.org/) aims to be an Integrated Development Environment that can edit Jupyter Notebooks side-by-side with a markdown or LaTeX document in a text editor.
*JupyterLab* has multiple windows like *Rstudio*: a code console, terminal shells, Jupyter Notebook editor, a text editor, and the Jupyter Notebook editor.
In this fashion, JupyterLab has much stronger support for literate programming than the classic *Jupyter Notebook*.

Like *Rstudio*, *JupyterLab* can open and edit a variety of markup documents like markdown, html, and latex files.
The code console can run code interactively and shows the order in which the code was executed.
Tab completion and tooltips work in the code console as they do in Jupyter Notebook.
Selected codes chunks in markdown and latex documents can be connected to a code console.
The tex editor supports vim key bindings.
Some documents can be opened with one of several alternate editors.
Edits of markdown and LaTeX documents are rendered immediately.

*JuputerLab* has several extensions for snippet libraries that is not backward compatible with the *Jupyter Notebook*.
The snippets are accessible from sub-menus, and it is easy to add new snippets.
Snippets in a category are accessible from a sub-menu.
There is no support for tab triggers and tab stops are this time.


<A href=#jupyternotebook>Jupyter Notebook, classic</A>has two extensions for snippet management.
These store the snippets in a JavaScript file, and the snippets are accessed from a pull-down menu.
Jupyter Notebook and JupyterLab also allow the use of clippings as snippets via the `%load` magic.

Jupyter Notebook can be used with ipymol to send commands to PyMOL and to import output from
PyMOL into cells in the notebook.
This module enables literate programming with PyMOL.
See below for more information.

The corresponding functionalities are being rebuilt by many volunteer developers.
The extensions include support for vim keybindings in the text editor as well as in the editor of Jupyter Notebooks.
The latter functionality enables rapid navigation of the notebook cells without using the mouse.
There are two different extensions that support snippet libraries.
They format for these libraries differs from that for the Jupyter Notebook as described below.
The good news is that required format is similar to the clippings for BBEdit, so it is trivial for the user to add new snippets as described below.
The bad news is that there is no support for tab triggers and tab stops.

All-in-all, new Jupyter users should start with JupyterLab, and veteran Jupyter Notebook users should switch to JupyterLab.
<details>
<summary><b>More reasons to switch to JupyterLab</b></summary>

The *JupyterLab* provides many enhancements for the editing of *Jupyter Notebook*.
First, the cells can be dragged and dropped to rearrange them in the notebook.
Second, the cells can be dragged between notebooks to copy the contents. 
Third, multiple views of a single notebook can be opened. Changes in one notebook are synchronized with the remaining notebooks.
Fourth, a blue bar on the blue side of the cell eases the folding and unfolding of the cell.
Fifth, longer outputs are easier to scroll.
Sixth, the cells output can be viewed from additional synchronized views.
Seventh, tab completion includes more information about the matched items.
Eighth, the tooltip, activated with shift-tab, shows information about selected objects.

*JupyterLab* can support manuscript writing of tex or markdown files more directly than *Jupyter Notebook*.
This is the main reason that I would consider using *JupyterLab*.
If you are writing manuscripts that describe computer work, it may be worth the trouble to write the part of the manuscript that refers to that code by editing it JupyterLab.
There is a LaTeX *JupyterLab* extension that supports the writing and compiling of latex documents.
With this extension enabled, the tex editor supports the generation of bibliographies using a BibtTeX file.
With a wide computer screen, you can display in parallel the tex document, a preview of the pdf, and the Jupyter Notebook that you may be describing.
This parallel visualization supports the accurate transfer from of code listings, output tables, and figures from the Jupyter Notebook to the manuscript.
</details>


<details>
<summary><b>Installation of JupyterLab</b></summary>
[*JupyterLab*](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html) can be installed with `conda`, `pip`,`pipenv`, or `docker`.
To install using `conda`, enter the follow command in the bash command line:

```bash
$ conda install -c conda-forge jupyterlab
```

Once installed, enter `jupyter lab` to launch.
*JupyterLab* uses your browser to run and a log of your activity is recorded.

There are no package installers for *JupyterLab*.
However, *JupyterLab* is pre-installed in the full Anaconda Python package.
It is available in the base environment, but Jupyter has to be installed in new environments.
With the Anaconda system installed, activate the desired environment where you want to install *JupyterLab* with `conda activate <env>` and then `conda install jupyter`.
This command will install both *JupyterLab* and the Jupyter Notebook.

Outside of Anaconda, *JupyterLab* is installed with a package manager like any other Python module.
With pip, the install command is simply  `pip install --user jupyter` to install in Jupyter in a local library rather than the system library.
The command for users of MacPorts is `port install py38-jupyterlab`.
Change the version number from Python3.8 to whatever is your current version of Python.

The command for users of Homebrew is `brew install jupyter`.

The command for he user of fink is `fink install jupyter`.
The command for the users of cygwin on Windows is `To be determined`.
The command for the users of Ubuntu is `To be determined`. 
The command for the users fo Centos is  `To be determined`.
</details>

<details>
<summary><b>Installation of *jupyterlab-snippets* for JupyterLab</b></summary>

The kernels are easily installed for a particular python interpreter.
Briefly, the python interpreter for which you want to make a kernel is used as follows to install ipykernel and then install the kernel:

```bash
/Applications/PyMOL.app/Contents/bin/python -m pip install ipykernel
/Applications/PyMOL.app/Contents/bin/python -m ipykernel install
```

On Mac OS, the kernels are stored in `~/Library/jupyter/kernels`.
A python kernel as a separate folder with three files in it.
Two of the files are images of the python logo.
The third file is a JavaScript file, `kernel.json`, that is created by the above ipykernel install operation.
However, it is trivial to manually create a copy of the folder and its contents to create a new kernel for a new Python interpreter.
One has to to edit the path in the kernel.json to the Python interpreter on the third line (see code listing below) and change the `display_name` of the kernel on the ninth line.
The display name can have any format.
There is no need to include a period between PyMOL and python as in the example.
The kernel.json file is a plain text file that can be edited with any text editor.
(JSON represents JavaScript Object Notation.)
The kernel.json file for the Python interpreter inside the PyMOL.app on the Mac is shown below.

```javascript
{
 "argv": [
  "/Applications/7PyMOL.app/Contents/bin/python",
  "-m",
  "ipykernel_launcher",
  "-f",
  "{connection_file}"
 ],
 "display_name": "pymol.python",
 "language": "python"
}

```

The addition of kernels for non-python programs requires different protocols than the one given above.
</details>

<details>
<summary><b>Documentation about using JupyterLab</b></summary>

### Documentation about using JupyterLab<
</details>

<details>
<summary><b>Installation of *jupyterlab-snippets* for JupyterLab</b></summary>

*JupyterLab* has a completely different snippet system enabled with the *JupyterLab* extension called *jupyterlab-snippets*.
The snippets are in individual files in analogy to the code clippings of BBEdit.
The snippets are stored with the appropriate file extension in the directory `./Library/Jupyter/snippets` on the Mac.
Nested submenus are created by making subfolders within the snippets folder.
These nested submenus will appear under the menu pulldown labeled `snippets` between the `Kernel` and `Tabs`.
You have to use the mouse to select the snippet.
There is no support for *MathJax* rendering of LaTeX in the label of snippet, unlike in the classical Jupyter Notebook.

When the jupyterlab-snippets extension is in synch with the current version of *JupyterLab*, the built in *JupyterLab* extension manager eases installation.
First, install node.js.
If you are using Anaconda, you can install node.js with the command `conda install -c conda-forge nodejs`
On the Mac OS, use `brew install node` with homebrew or `port install nodejs14` with macports (or at least nodejs10).
Start Jupyter Lab (e.g., `python3.8 -m jupyter-lab`).
Click on the extension manager button in the left margin.
It looks like a painter's palette.
Then select the enable button to activate the extensions.


Enter `snip` to get a list of the snippet related extensions.
Select ` ` and then click on the install button.
If the install fails, the extension can be installed manually in the terminal with these commands.

If the above commands fail because the version of the extension in PyPi is not available yet for the current version of *JupyterLab*, you might get lucky by installing the development version of the extension.
The current instructions are found on the GitHub page for this project.
This issues tab on the GitHub page can be used to resolve any further difficulties.

This project has three related web pages.
The first page is linked to the notebook extension and is a JavaScript site for the project.
This web page is two years out of date. 
The original developer of the extension is no longer supporting it.
Two other developers have taken over the project because it is so valuable.
There is a PyPi web page for the project that has access to a wheel file for the nbextension and a tar file of the source code.
This page also includes a link to the GitHub page for this project.
The GitHub page has the current information about installation trouble shooting.

You should beware that the upgrading of *JupyterLab* in the future could lead to the breaking of your various *JupyterLab*extensions.
It may be best to delay the *JupyterLab* upgrade until the extensions have been upgraded.
</details>

<details>
<summary><b>Documentation about using JupyterLab</b></summary>

The official documentation for *JupyterLab*is the found on Read the docs.
This documentation can be viewed as html file in a browser, or it can be downloaded as a pdf for printing.
There is a tiny icon in the lower left of the home page for the JupyterLab read-the-docs.
Click on this icon to gain access to the pdf version.

In addition to the books about Jupyter Notebook mentioned in the section about Jupyter notebooks, books have been written about *JupyterLab* exclusively (e.g., *JupyterLab Quick Start Guide*) or describe JupyterLab in detail in context of another topic (e.g., * *).
The book  *JupyterLab Quick Start Guide* has it code available on a dedicated [github site](https://github.com/PacktPublishing/Jupyterlab-Quick-Start-Guide).

```bibtex
@book{Richman2019JupyterLabQuickStartGuide,
  title={JupyterLab Quick Start Guide},
  author={Richman, Lindsay and Ferrari, Melissa and Oladokun, Joseph and Banfield, Wesley and Toomey, Dan },
  year={2019},
  publisher={Packt Publishing Ltd}
}

@Book{Galea2018AppliedDataScienceWithPythonAndJupyter,
  author    = {Galea, Alex},
  publisher = {Packt Publishing Ltd},
  title     = {Applied Data Science with Python and Jupyter},
  year      = {2018},
}

@Book{2018AppliedDataScienceWithPythonAndJupyterUsePowerfulIndustryStandardToolsToUnlockNewActionableInsightsFromYourData,
  publisher = {Packt Publishing Ltd},
  title     = {Applied Data Science with Python and Jupyter: Use powerful industry-standard tools to unlock new, actionable insights from your data},
  year      = {2018},
}
```

As mentioned above, several [JupyterCon](https://conferences.oreilly.com/jupyter/jup-ny) conventions have been held.
The [2020 JupyterCon](https://jupytercon.com) convention is on hold due to the COVID19 pandemic.
</details>