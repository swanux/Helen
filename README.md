# Changelog
Here is the changelog of every update. For further details you can always check https://github.com/swanux/hsuite/releases

**Website:** https://swanux.github.io/hsuite.html

**v0.7 | Sinara**
*Note: First "complete" release without useless buttons and severe bugs*

    * New: You can now choose flavour for Mint, Ubuntu, Debian, Solus, fedora and opensuse
    * Fix: Distrou Boutique newest version script
    * Fix: Global variable hell in python code
    * New: Email adress is now optional in feedback
    * New: General dialog constructor, got rid of zenity
    * Optimized codebase (~500 lines spared)
    * New: HControl with Cron UI and Theme switcher
    * New: Finally a proper website for my projects
    * New: Feedback is now for all of my future projects
    * Fix: HSwitcher simplified app list
    * New: HSwitcher now backups gpg keys and restore optimization
    * New: HSwitcher also pulls proper gnome extensions from official site
    * Fix: translation compatibility
    * New: Python dependencies now from self built packages
    * Fix: Now completely relying on system theme (only patch for inactive buttons)
    * Fixed a lots of bugs
    * Fixed UI design

# Compatibility

**Note:** Currently supported distributions (and everything dpkg/apt based):

    Debian 10 (buster)
    Ubuntu : 18.04 (bionic), 19.10 (eoan), 20.04 (focal)
    Linux Mint 19.x
    PoP_OS : 18.04, 19.10, 20.04

**Note:** Currently supported desktop environments:

    Gnome
    Ubuntu (the ubuntu specifc version of Gnome)
    PoP (the PoP_OS specifc version of Gnome)

**Note:** These are just the recommended values. You can always extend compatibility on your own.
**Tipp:** You can use this program on ANY desktop environment, only some desktop agonistic features will be disabled.

# Get things working

To find out your codename on Ubuntu just run:

    source /etc/lsb-release \
    echo $DISTRIB_CODENAME

**Tipp:** If you are using a distro that's not in the list but it is based on Debian/Ubuntu, then use the version of Ubuntu/Debian which is the base of it.
E.g.: Use bionic for Linux Mint 19 and buster for Deepin.

To install run:

    CODENAME=YOURDISTNAME
    sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys D0E48B8490DC4A21
    echo "deb https://gitlab.com/swanux/hrepo/raw/master $CODENAME main" | sudo tee -a /etc/apt/sources.list
    sudo apt update
    sudo apt install hsuite

**Note:** You only need to execute the last line if you already have my repository added to your system.

And to remove, execute:

    sudo apt purge hsuite && sudo apt autoremove

**Debugging and updating**

The package will get updates together with the system on Ubuntu/Debian.

On Arch run the installation commands again when there's a new release to update.

To debug the program, open the terminal and type:

    hsuite

You will see the logs in the terminal then.

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
    │                   ├── hsuite.hspec    # build file for own automated build system
    │                   ├── hsuite.glade    # the UI file
    │                   ├── HSuite.py       # the main file
    │                   ├── hsuite.sh       # the file to run hsuite from terminal
    │                   ├── icons           # all the icons
    │                   │   └── ...
    │                   ├── osLayer.py      # extra module
    │                   └── htransfer.py     # own file transfer backend
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

HSuite (previously Helen) is the SSU (Simple, Small, Useful) Swiss army for the Linux operating system. Features include powerful built-in custom tools, easy installation of the best quality programs, choosing Linux distribution, helping in everyday tasks and more features are coming. **ATTENTION!** This program is currently in Beta stage (v0.7). **NOTE:** Currently works on Debian/Ubuntu based distros.

# Development process

Here are some small demos of the beta versions. Lots of work in progress...

https://www.youtube.com/playlist?list=PL1e4zYtM_xvf_R4ggIu64BUf33XSHkTzz
