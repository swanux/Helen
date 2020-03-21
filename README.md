# Changelog
Here is the changelog of every update. For further details you can always check https://github.com/swanux/hsuite/releases

**v0.6 | Apollo**
*Note: This version targets stability and performance improvements, alongside with tweaks on user experience.*

    * Resolved a LOTS of bugs with Apt Spotlight, Distro Boutique, hrepo, etc...
    * New modern UI redesign with CSS, better text placement
    * Dropped support for flashplayer
    * Rewritten Apt Spotlight backend with aptdaemon
    * Built in basic error handling
    * Added notifications when window is in background and task completed
    * Added proper description to the installer package
    * Added native feedback page
    * Added internet connection checking and offline mode
    * Added config file to store distro name, and notify when updated
    * Dropped support for Ubuntu 19.04 (disco)
    * Added Hungarian translation, prepared for more translations
    * Now using custom packaging and build system
    * Updated hrepo, demos, readme and added description for developers


# Get things working

**For Ubuntu/Debian:**

**Note:** Currently supported versions:

    Debian 10 (buster)
    Ubuntu 18.04 (bionic)
    ABANDONED: Ubuntu 19.04 (disco)
    -> Use *eoan* or *bionic* instead
    Ubuntu 19.10 (eoan)

To find out your codename on Ubuntu just run:

    source /etc/lsb-release \
    echo $DISTRIB_CODENAME

**Tipp:** If you are using a distro that's not in the list but it is based on Debian/Ubuntu, then use the oldest codename.
E.g.: Use bionic for Ubuntu derivatives and buster for Debian derivatives.

To install run:

    CODENAME=YOURDISTNAME
    sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys D0E48B8490DC4A21
    echo "deb https://gitlab.com/swanux/hrepo/raw/master $CODENAME main" | sudo tee -a /etc/apt/sources.list
    sudo apt update && sudo apt install hsuite

And to remove, execute:

    sudo apt purge hsuite && sudo apt autoremove

**For Arch:**

To install:

    wget https://github.com/swanux/hsuite/raw/master/PKGS/hsuite-0.6.1-1-x86_64.pkg.tar.xz \
    sudo pacman -U hsuite-0.6.1-1-x86_64.pkg.tar.xz \
    rm hsuite-0.6.1-1-x86_64.pkg.tar.xz && sudo pacman -Sy
    
And to remove:

    sudo pacman -Runs hsuite

**Debugging and updating**

The package will get updates together with the system on Ubuntu/Debian.

On Arch run the installation commands again when there's a new release to update.

To debug the program, open the terminal and type:

    hsuite

You will see the logs in the terminal then.

# Development process

Here are some small demos of the beta versions. Lots of work in progress...

https://www.youtube.com/playlist?list=PL1e4zYtM_xvf_R4ggIu64BUf33XSHkTzz

# For developers

Here's the file hierarchy of the program with explanations:

    hsuite/                     # The root directory
    ├── BUILD                   # Folder for installer pkg build
    │   └── hsuite-0.6          # the build folder for the program
    │       ├── debian          # debian folder with config files
    │       │   ├── changelog
    │       │   ├── compat
    │       │   ├── control
    │       │   ├── copyright
    │       │   ├── install
    │       │   ├── postinst
    │       │   ├── postrm
    │       │   ├── rules
    │       │   └── source
    │       │       └── format
    |       |   └── ...
    │       └── usr
    │           └── share
    │               ├── applications
    │               │   └── hsuite.desktop
    │               └── hsuite
    │                   ├── colors.css      # CSS design
    │                   ├── config.yml      # for fusuma
    │                   ├── details.py      # extra module
    │                   ├── fusuma.desktop
    │                   ├── hsuite.glade    # the UI file
    │                   ├── HSuite.py       # the main file
    │                   ├── hsuite.sh       # the file to run hsuite from terminal
    │                   ├── icons           # all the icons
    │                   │   └── ...
    │                   ├── osLayer.py      # extra module
    │                   └── pacman.conf     # for Arch
    ├── _config.yml     # just for the theme of the github page
    ├── DEV_FILES       # development folder
    │   ├── colors.css
    │   ├── config.yml
    │   ├── details.py
    │   ├── fusuma.desktop
    │   ├── hsuite.desktop
    │   ├── hsuite.glade
    │   ├── hsuite.glade~   # autosaved version
    │   ├── HSuite.py
    │   ├── hsuite.sh
    │   ├── icons
    │   │   └── ...
    │   ├── osLayer.py
    │   ├── others          # not the part of the program, just some experiments
    │   │   ├── daemon.py
    │   │   ├── hsuite.srctrlbm
    │   │   ├── hsuite.srctrldb
    │   │   ├── hsuite.srctrlprj
    │   │   ├── mega.sh
    │   │   └── tester.py
    │   ├── pacman.conf
    │   └── translations    # translation folder
    │       ├── mo          # ready translations
    │       │   └── hu_HU
    │       │       └── LC_MESSAGES
    │       │           └── hsuite.mo
    │       └── po          # ongoing translations
    │           ├── hsuite.pot
    │           └── hu_HU.po
    ├── hsuite.hspec                        # config file for henv (my own pkg builder)
    ├── LICENSE                             # GPL-3 license
    ├── PKGS                                # build pkgs
    │   ├── hsuite_0.6-1_amd64.deb          # debian/ubuntu/linux mint
    │   └── hsuite-0.6-1-x86_64.pkg.tar.xz  # arch/manjaro
    └── README.md                              # this readme file


# Why is the Beta better than the alpha, and why got the program a new name?

**1)** The application is now completely rewritten in Python3 and it has a standalone GUI using GTK3+ and CSS. It has/will have got a lots of new features and tools included.

**2)** The name change is because it's now more than an extra big Bash script. Now, it's an independent program with more and more features coming. It's now something like a "tool center" or a "Swiss-army". **NOTE:** The name is HSuite, **not** HiSuite (which is the property of Huawei™).

# What is HSuite?

*Be SSU (Simple, Small, Useful)*

HSuite (previously Helen) is the SSU (Simple, Small, Useful) Swiss army for the Linux operating system. Features include powerful built-in custom tools, easy installation of the best quality programs, choosing Linux distribution, helping in everyday tasks and more features are coming. **ATTENTION!** This program is currently in Beta stage (v0.5). **NOTE:** Currently works on Debian/Ubuntu and Arch based distros.
