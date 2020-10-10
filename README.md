# Changelog
Here is the changelog of every update. For further details you can always check https://github.com/swanux/hsuite/releases

**Website:** https://swanux.github.io/hsuite.html

**v0.8 | Quake**
*Note: Hopefully a long term release*

    * Fixed a lots of bugs
	* Fixed GUI problems
	* Optimized HSwitcher
	* Dependency fixes
	* Depracted Ubuntu 19.10
	* New unified feedback platform
	* Added partial support for Pantheon (hswitcher)
	* Added partial support for Cinnamon (hswitcher + hcontrol)
	* Added partial support for XFCE (hswitcher + hcontrol)
	* Added partial support for Budgie (hswitcher + hcontrol)
	* Added partial support for MATE (hswitcher + hcontrol)
	* Added USB creation option to Distro Boutique
	* Extended Distro Boutique
	* Optimized and modernized code
	* Extended App Spotlight
	* Added secure feedback daemon

# Compatibility

#### Distros

Every distro is supported which is based on **Ubuntu bionic/focal** (18/20) or **Debian 10**.

#### Desktops

- The mainline DE is **Gnome** (including custom versions, eg. from Ubuntu/PoP_OS).
- Partial compatibility with **MATE, XFCE, Budgie, Pantheon, Cinnamon**.
- If you use an unsupported DE, you can still use the non-DE specific parts of the program

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

# Feedbacks
Did you find any bugs? Do you have some feature requests/new ideas? Or just some questions? Feel free to provide your feedback using [hsuite](https://github.com/swanux/hsuite) or my [website](https://swanux.github.io/feedbacks.html).

# For developers

Here's the file hierarchy of the program with explanations:

    hsuite/                     # The root directory
    ├── BUILD                   # Folder for installer pkg build
    │   └── hsuite-0.8.0.5       # the build folder for the program
    │       ├── debian             # debian folder with config files
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
    │                   └── ...     # program files
    ├── DEV_FILES       # development folder
    │   ├── colors.css
    │   ├── config.yml
    │   ├── details.py
    │   ├── fusuma.desktop
    │   ├── htransfer.py    # Self written file transfer backend
    │   ├── husb.py         # USB helper
    │   ├── sfdaemon        # Secure feedback daemon binary
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
    │   └── hsuite_0.8.0.5-1_amd64.deb          # debian/ubuntu/linux mint
    └── README.md                              # this readme file


# Why is the Beta better than the alpha, and why got the program a new name?

**1)** The application is now completely rewritten in Python3 and it has a standalone GUI using GTK3+ and CSS. It has/will have got a lots of new features and tools included.

**2)** The name change is because it's now more than an extra big Bash script. Now, it's an independent program with more and more features coming. It's now something like a "tool center" or a "Swiss-army". **NOTE:** The name is HSuite, **not** HiSuite (which is the property of Huawei™).

# What is HSuite?

*Be SSU (Simple, Small, Useful)*

HSuite (previously Helen) is the SSU (Simple, Small, Useful) toolkit for the Linux operating system. Features include powerful built-in custom tools, easy installation of the best quality programs, choosing Linux distribution, helping in everyday tasks and more features are coming. **ATTENTION!** This program is currently in Beta stage (v0.7). **NOTE:** Currently works on Debian/Ubuntu based distros.

# Development process

Here are some small demos of the beta versions. Work in progress...

https://www.youtube.com/playlist?list=PL1e4zYtM_xvf_R4ggIu64BUf33XSHkTzz
