# Roborobo.4

**Roborobo** is a fast and simple 2D mobile robot simulator loosely based on low-cost mobile robots such as khepera or epuck models. It is targeted for fast single and multi-robots simulation for evolutionary robotics and machine learning in multi-agent systems, collective and swarm robotics.

**Roborobo** combines speed of development _and_ speed of execution. Roborobo can be programmed with python 3.x, with all the core functions written in C++ for super fast execution.

## Version

Roborobo version 4 is currently the **only** supported version. Current official release is (from: _roborobo.cpp_):

* _gVersion = 20210321_
* _gCurrentBuildInfo = Shangri-La build_

## Contributors

### Main contributors

* Nicolas Bredeche: main roborobo developper and project initiator (since 2009)
* [http://pages.isir.upmc.fr/~bredeche/](https://www.isir.upmc.fr/personnel/bredeche/?lang=en)
* contact: nicolas.bredeche(at)sorbonne-universite.fr

* Paul Ecoffet: pyRoborobo, the python interface to Roborobo (2020-2021)
* Evert Haasdijk: properties management library (2010-2012)

### Other contributors

* Jean-Marc Montanier, Berend Weel, Amine Boumaza, Andreas Steyven, Leo Cazenille, Theotime Grohens, and a few others!

## How to cite Roborobo in your work

If you use **Roborobo** in your work, **please cite the following paper**:

_N. Bredeche, J.-M. Montanier, B. Weel, and E. Haasdijk. Roborobo! a fast robot simulator for swarm and collective robotics. CoRR, abs/1304.2888, 2013._

Link to the paper on Arxiv: [Arxiv 1304.2888](http://arxiv.org/abs/1304.2888)

_Scientific papers that cite Roborobo_: [Scholar Citation 7785979290259259170](https://scholar.google.fr/scholar?cites=7785979290259259170)

___

## INSTALLATION

Roborobo basic dependencies are:

* a C++ compiler (GCC or CLANG)
* Python 3.x

Supported platforms:

* Linux-based
* MacOS X

Linux, Windows and MacOS installation instructions are described below. Other platforms are not officially supported, but Roborobo was previously shown to run on: Raspbian and Pandora.

_Remark: if you get a lot of warnings during compilation, this is probably due to already installed pip packages shadowing the newly installed conda packages (e.g. with pybind). Work around for pyBind that may work: conda install -c conda-forge "pybind11>2.6". However the best way is to delete the pip packages and make a clean install of roborobo again__

### Linux

You will need python. Please make sure you have installed some modern version of Python3.

**Note:** Since we are using a ['toml file'](./pyproject.toml), all required `pip` libraries will be installed later automatically.

Install C++ dependencies for Roborobo (Cmake, SDL2, boost and eigen):

```bash
sudo apt install git build-essential cmake 
sudo apt-get install libsdl2-dev libsdl2-image-dev libboost-dev libeigen3-dev
```

Get your local copy of Roborobo:

```bash
git clone https://github.com/nekonaute/roborobo4.git
```

Compile and install Roborobo:

```bash
cd roborobo4

# ============================================
#              Choose one Option
# ============================================
# Now either run the following command if you
# do not want to have a documentation:
py -m pip install .
# or run this command if you want to have the
# documentation:
pip install -U .[docs]

# NOTE: It might be that you have not installed
#       python in a way, that you can use `pip`
#       directly in your cli. In this case use
#       one of these:
#        - py -m pip ...
#        - python -m pip ...
#        - py3 -m pip ...
#        - python3 -m pip ...
```

Check the [QUICK START](#quick-start) section below for running a Roborobo example.

### Mac OS

You will need python. Please make sure you have installed some modern version of Python3.

**Note:** Since we are using a ['toml file'](./pyproject.toml), all required `pip` libraries will be installed later automatically.

Install C++ dependencies for Roborobo (Cmake, SDL2, boost and eigen):

```bash
brew install cmake 
brew install sdl2
brew install sdl2_image
brew install boost
brew install eigen
```

Get your local copy of Roborobo:

```bash
git clone https://github.com/nekonaute/roborobo4.git
```

Compile and install Roborobo:

```bash
cd roborobo4

# ============================================
#              Choose one Option
# ============================================
# Now either run the following command if you
# do not want to have a documentation:
py -m pip install .
# or run this command if you want to have the
# documentation:
pip install -U .[docs]

# NOTE: It might be that you have not installed
#       python in a way, that you can use `pip`
#       directly in your cli. In this case use
#       one of these:
#        - py -m pip ...
#        - python -m pip ...
#        - py3 -m pip ...
#        - python3 -m pip ...
```

Check the [QUICK START](#quick-start) section below for running a Roborobo example.

### Windows

First you need python 3.12 with the corresponding packages:

```bash
# Install python 13
winget install --id Python.Python.3.13 -e
```

**Note:** Since we are using a ['toml file'](./pyproject.toml), all required `pip` libraries will be installed later automatically.

Now you need the VS building tools to get CMake and all other tools required:

```bash
winget install -e --id Microsoft.VisualStudio.2022.BuildTools
# The installation DOES NOT need any "Workloads".
# However you need the following "Individual Components":
#  - MSVC v143 - VS 2022 C++ x64/x86 build tools (Latest)
#  - Windows 11 SDK (10.0.26100.7175)
#  - C++ CMake tools for Windows
# => The "Workloads" and "Individual Components" can be selected
#    during the installation process.

# ============================================
#              Choose one Option
# ============================================
# 1. Use cmake from VS Build Tools:
#    1.1. Open `x64 Native Tools Command Prompt for VS 2022`
#    1.2. Run: where cmake
#    1.3. Add the path (without `cmake.exe`) to
#         your PATH of either the user or the system 
# 2. Install cmake from another source:
#    winget install -e --id Kitware.CMake
```

Install `git`, if not already installed:

```bash
winget install --id Git.Git -e

# If it is already installed, consider this an opportunity
# to update it with either:
git update-git-for-windows
# or
winget update --id Git.Git -e
```

At least, you need `vcpkg` to install the app at the end:

```bash
# Clone the vcpkg repository from microsoft
git clone https://github.com/microsoft/vcpkg

# Install vcpkg.
# Note: You need to run this in a CMD terminal!
cd vcpkg
# You can also not use the flag `-disableMetrics`,
# in case you want Microsoft to collect some usage
# data.
bootstrap-vcpkg.bat -disableMetrics

# Now install all required tools:
vcpkg install sdl2 sdl2-image boost-filesystem boost-system boost-multi-array boost-algorithm boost-random boost-serialization boost-thread eigen3 --triplet x64-windows
vcpkg integrate install
# Note: You need to run the command in the 
#       directory or add the directory to your
#       PATH

# ============================================
#                DON'T SKIP THIS
# ============================================
# Now open up your system or user environment
# variables:
# 1. press Windows Key
# 2. "Edit the system environment variables" or 
#    "Edit environment variables for your user"
# 3. press "Environment Variables..."
# 4. press "New" (be cautions if you press the
#    top or the bottom button, depending of if
#    you want to have it for the user or system
#    wide)
#    Note: Since the vcpkg repository is probably
#          only accessible for your user, it makes
#          more sense to make this only for your
#          user account.
#
#    Variable name: CMAKE_PREFIX_PATH
#    Variable content: <vcpkg-repo-path>\installed\x64-windows
#
#    Note: Replace "<vcpkg-repo-path>" with the
#          actual path.
#    Note: If you have a x86 system, the path might
#          be different.
# 5. Go to you user or system PATH variable and edit
#    it. Add a new entry with:
#    <vcpkg-repo-path>\installed\x64-windows\bin
#
# Optional:
# 6. Add also <vcpkg-repo-path> to PATH, so that you
#    can use vcpkg as a regular cli program.

# ============================================
#            Additional Information
# ============================================
# 1. You can list all installed components of
#    vcpkg with:
#    vcpkg list
# 2. You can uninstall outdated components with:
#    vcpkg remove --outdated
# 3. You can uninstall all components by deleting
#    the following folders in the vcpkg repo
#    to make a clear reinstall:
#     - buildtrees/
#     - downloads/
#     - installed/
#     - packages/
#    Consider also executing:
#    vcpkg integrate remove
```

Now install `roborobo4`:

```bash
# Get your local copy of Roborobo:
git clone https://github.com/nekonaute/roborobo4.git
cd <some-path>/roborobo4

# ============================================
#                DON'T SKIP THIS
# ============================================
# Set compile mode to release
# Note: For some reason a debug build
#       did not work on Windows.
set CMAKE_BUILD_TYPE=Release

# ============================================
#              Choose one Option
# ============================================
# Now either run the following command if you
# do not want to have a documentation:
py -m pip install .
# or run this command if you want to have the
# documentation:
pip install -U .[docs]

# NOTE: It might be that you have not installed
#       python in a way, that you can use `pip`
#       directly in your cli. In this case use
#       one of these:
#        - py -m pip ...
#        - python -m pip ...
#        - py3 -m pip ...
#        - python3 -m pip ...
```

Check the [QUICK START](#quick-start) section below for running a Roborobo example.

#### Building the Documentation

For this you only need to run these two commands:

**Note** This only works if you used `pip install -U .[docs]`.

```bash
# Navigate into the docs folder
cd docs

# Build the documentation
make.bat html
```

#### Checking Python Package Contents

To check the content of the roborobo package, open up the `x64 Native Tools Command Prompt for VS 2022`. There you can execute:

```bash
dumpbin /dependents "%APPDATA%\Python\Python313\site-packages\pyroborobo.cp313-win_amd64.pyd"

# Note: The path might be different, depending
#       on the position of your python installation
#       and the computer architecture:
#       <python-path>\site-packages\pyroborobo.cp<python-version>-win_<architecture>.pyd
```

### Uninstalling RoboRobo if needed

```bash
# Navigate to the roborobo repo in your console of choice
cd <roborobo-repo-path>

# Delete directories with compile artifacts
rmdir /s /q build
rmdir /s /q roborobo.egg-info

# Uninstall the module
pip uninstall roborobo -y
```

___

## QUICK START

It is highly suggested to use the **python** interface to Roborobo, which we refer to as **pyRoborobo**. If you prefer to develop your project in C++, it also possible (check below). pyRoborobo is built as an interface to Roborobo, and though there is of course a cost to use Python instead of pure C++, we empirically consider it worth the ease of development in the context of academic research. For example, the Boids example runs at ~400 fps (pure C++) and ~200 fps (pyRoborobo) on a Macbook pro 13 (early 2019 model).

Roborobo (C++) and pyRoborobo (Python) both uses three important directories, that should be accessible from where your code (C++ binary or python script) is run.

* **_data_** contains image and resources for setting a roborobo environment
* **_config_** contains configuration files for running a roborobo environment
* **_logs_** will contain log files generated during a roborobo run

While running an example, type "h" when the focus is on the Roborobo window. Help tips will be displayed in the console.

## Running a Python example

See [in the installation instructions](#installation) in case you have not already installed roborobo4.

Run a pyRoborobo example:

```bash
cd <your_roborobo_folder>/pyRoborobo_dev/examples/
python tutorial.py
```

Many other examples are available in the **pyRoborobo_dev/examples** folder.

## Build the pyRoborobo API documentation (optional)

Build Roborobo's python API documentation:

```bash
# conda activate roborobo (if not already activated)
python setup.py build_sphinx
```

The pyRoborobo API documentation is now in _build/sphinx/html/index.html_

## Running a C++ example (optional)

If you installed Roborobo for the first time, setup the directory structure for running Roborobo:

Setup the directory structure for both C++ and Python development (done only once):

```bash
# Roborobo C++ code
cd <your_roborobo_folder>/build
ln -s ../data
ln -s ../config
ln -s ../logs
```

See [in the installation instructions](#installation) in case you have not already installed roborobo4.

Run a roborobo example:

```bash
cd <your_roborobo_folder>/build
./roborobo -l config/Tutorial.properties
```

Roborobo (C++) examples are in the <your_roborobo_folder>/prj directory. Note that project selection is achieved from the configuration file (config/filename.properties)

## What next?

* Check _OVERVIEW.TXT for a **quick introduction**.
* Check _FAQ.TXT for **trouble shooting** and **frequently asked questions**.
* Check the examples, and learn by doing.

## Troubleshooting

Roborobo is regularly tested on the most recent Ubuntu LTS. While you should not encounter any problems with an up-to-date Linux distribution, it may be different with non-standard, outdated and/or badly managed Linux distributions. The following covers the most common errors. Note that before trying to fix things, you should be 100% sure that you followed _exactly_ the installation steps provided above.

* First, be sure that conda uses the same Python version as the default one used in the terminal.
  * To check which versions are used:
    * for Python in Conda: _conda list | grep python_
    * for Python in Terminal: _python3 --version_
  * To force conda to use a specific version of Python: _conda create (...) python==3.12_. Updating conda to the latest version if needed.
  * To force that the _python_ or _python3_ alias points to the expected python version, re-define the alias in your profile file. E.g.: with _bash_, edit the .bashrc file and add the following line at the end: _alias python='/usr/bin/python3.xx'_ with _xx_ the preferred version. Restart the terminal after modification.
* When executing _conda activate roborobo_
  * error: the shell (e.g. bash) is not configured.
    * solution 1: _conda init bash_. This may fail if your bash profile has been badly written. Fix: clean your bash profile
    * solution 2: use another shell. E.g. _tcsh_. I.e. restart installation from scratch. In the terminal, type _tcsh_ before the command _conda activate roborobo_ (during installation, and afterwards when coding).
* When executing _python3 -m pip install . --force --user -v_
  * => error during execution "could NOT find SDL2" (hidden somewhere in the very long list of messages)
  * system install of SDL2 (must be super user). See apt commands above.
* When executing _python3 -m pip install . --force --user -v_
  * error referring to Sphinx (Sphinx is used for generating the documentation)
    * easy fix (recommended): remove reference to Sphinx in setup.py (delete line 7 and remove _'build_sphinx': BuildDoc_ from line 64)
    * easy fix (not recommended): switch to a different version of Python (e.g. away from 3.10)
* When executing _python3 -m pip install . --force --user -v_
  * error: problem with missing MESA/GLX (this is related to the OpenGL graphic library and its open-source implementation in Linux systems).
    * solution (see above): apt-get install -y mesa-utils libgl1-mesa-glx
* When executing _python setup.py install --force --use -v_
  * error: "setup.py install is deprecated." (this should not happen if you follow the tutorial)
    * You tried to run setup.py. Contrary to what the message says, setup.py isn't deprecated but can no longer be used directly.
    * Solution (see above): python3 -m pip install . --force --user -v
    * Comment: it can be pretty long. Be sure to use the -v option for verbose mode.
* When executing _python setup.py install --force --use -v_
  * error: "func.h:55:58: error: expected template-name before '<' token" or "Deprecated function in roborobo4/include/contrib/zsu/func.h, line 55"
    * cause: recent compiler may spot a deprecated function in roborobo4/include/contrib/zsu/func.h, line 55
    * solution: roborobo4/include/contrib/zsu/func.h, line 55, replace:
      * new: class unary_function_binder: public std::__unary_function<_Result, _Arg>
      * old: class unary_function_binder: public std::unary_function<_Result, _Arg>
* When executing _python3 tutorial.py_ (or any other examples)
  * error: "no module name 'pyRoborobo'"
    * first, be sure to check that you followed every step of the installation tutorial. If this is the case, then try the following.
    * Solution 1: be sure that you have activated the conda environment (prefix of prompt should read something like _(roborobo)_)
    * Solution 2: this may be a tricky problem of mismatch Python versions from Conda and command-line. Use same python versions (i.e.: update Conda, or use specific Python version in command line). Comment: Conda's Python and default Python command uses different versions. Check with _conda list | grep python_ and _python --version_. They should be the same.
* When executing _python tutorial.py_ (or any other examples)
  * error looks like: ImportError: /lib/x86_64-linux-gnu/libwayland-client.so.0: undefined symbol: ffi_type_uint32, version LIBFFI_BASE_7.0
    * fix looks like: solution: export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libffi.so.7
* As of early 2024, Mac M2 does not seem to be able to run Roborobo. You may use Virtualbox to install a Linux OS but this is still in beta for Mac M1/M2 as of early 2024. Check dedicated [topic on virtualbox forum](https://forums.virtualbox.org/viewtopic.php?f=8&t=107344) for updates on the topic. Alternatively, you can use Parallels Desktop (but it is not free).

___

_Thank you for using Roborobo!_
