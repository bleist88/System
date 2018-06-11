
import os, sys

##  ============================================================================

basic_library = {
    "homebrew":     'ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"',
    "wget":         "brew install wget",
    "git":          "brew install git",
    "coreutils":    "brew install coreutils",
    "xquartz":      "brew install caskroom/cask/xquartz",
    #"java":         "brew cask install java",
    #"R":           "brew install R",
}

scientific_library  = {
    #"latex":      "brew cask install",
    #"latex":      "brew cask install texmaker",
    #"latex":      "brew cask install mactex",
    #"latex":      "brew install caskroom/cask/mactex",
    "ds9":          "brew install ds9",
    "SExtractor":   ""
}

manual_library      = { ##  these must be manually installed
    "python3":  "see anaconda",
    "anaconda": "",
    "acrobat":  "",
}
