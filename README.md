# Changelog
Here is the changelog of every update. For further details you can always check https://github.com/swanux/hsuite/releases

**v0.5 | Hermes**
*Note: This version is the most polished new release yet with lots of under-the-hood improvements for the new year.*

    * More logical program structure (using modules)
    * Removed fullscreen spinner & placed indicator in buttons
    * Decluttered codebase
    * Added colored buttons
    * Added Distro Boutique
    * Added new apps
    * Fixes depraction warnings
    * Optimized security & performance
    * Fixed link opening error
    * Updated AUR manager script
    * Migration from launchpad to own git repo (hrepo)
    * Implementation of some GTK theming with CSS


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

    sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys D0E48B8490DC4A21
    echo "deb https://gitlab.com/swanux/hrepo/raw/master $CODENAME main" | sudo tee -a /etc/apt/sources.list
    sudo apt update && sudo apt install hsuite

And to remove, execute:

    sudo apt purge hsuite && sudo apt autoremove

**For Arch:**

To install:

    wget https://github.com/swanux/hsuite/raw/master/PKGS/hsuite-0.5-1-x86_64.pkg.tar.xz \
    sudo pacman -U hsuite-0.5-1-x86_64.pkg.tar.xz \
    rm hsuite-0.5-1-x86_64.pkg.tar.xz && sudo pacman -Sy
    
And to remove:

    sudo pacman -Runs hsuite

**Debugging and updating**

The package will get updates together with the system on Ubuntu/Debian.

On Arch run the installation commands again when there's a new release to update.

To debug the program, open the terminal and type:

    hsuite

You will see the logs in the terminal then.

# Why is the Beta better than the alpha, and why got the program a new name?

**1)** The application is now completely rewritten in Python3 and it has a standalone GUI using GTK3+ and CSS. It has/will have got a lots of new features and tools included.

**2)** The name change is because it's now more than an extra big Bash script. Now, it's an independent program with more and more features coming. It's now something like a "tool center" or a "Swiss-army". **NOTE:** The name is HSuite, **not** HiSuite (which is the property of Huawei™).

# Development process

Here are some small demos of the beta versions. Lots of work in progress...

**v0.3**

https://streamable.com/9vryf

**v0.4**

https://streamable.com/bx8jp

**v0.5**

https://streamable.com/ki5zd

# What is HSuite?

*Be SSU (Simple, Small, Useful)*

HSuite (previously Helen) is the SSU (Simple, Small, Useful) Swiss army for the Linux operating system. Features include powerful built-in custom tools, easy installation of the best quality programs, choosing Linux distribution, helping in everyday tasks and more features are coming. **ATTENTION!** This program is currently in Beta stage (v0.5). **NOTE:** Currently works on Debian/Ubuntu and Arch based distros.
