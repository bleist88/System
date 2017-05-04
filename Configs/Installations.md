# Startup Installations

##  Initial Packages

*   Homebrew
    -   ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

*   wget
    -   brew install wget

*   git
    -   brew install git

*   coreutils
    -   brew install coreutils

*   XCode
    -   xcode-select --install

*   Quartz
    -   brew install Caskroom/cask/quartz

*   DS9
    -   brew install ds9

*   Atom
    -   go to www.atom.io
    -   download for mac
    -   install
    -   use once before it is accessible
        through the terminal
*   LaTeX
    #-   brew cask install mactex           -> This didn't work.
    #_   brew cask install texmaker         
    #-   brew install Caskroom/cask/mactex   
    -   brew cask install

##  Python + Packages

*   Python and Python3
    -   brew install python
    -   brew install python3

*   Scipy ( + Numpy + gcc )
    -   pip3 install scipy
    -   pip2 install scipy

*   MatPlotLib
    -   pip3 install matplotlib
    -   pip2 install matplotlib

*   Astropy
    -   pip3 install astropy
    -   pip2 install astropy

*   Cython
    - pip3 install cython
    - pip2 install cython

*   PhotUtils
    - pip3 install photutils
    - pip2 install photutils

*   Django
    -   pip3 install django
    -   pip2 install django

*   iPython
    -   pip3 install ipython
    -   pip2 install ipython

*   Kohonen SOM
    -   still no solutions yet (python2 only)

##  Java

*   Java
    -   brew cask install java

##  R

*   R
    -   brew install R

*   In R-Terminal, install LAMBDAR + dependencies:
    -   install.packages("<package_name>", dependencies=TRUE)
    -   install_github("AngusWright/LAMBDAR", dependencies=TRUE)
