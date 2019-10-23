# Changelog
Here is the changelog of every update. For further details you can always check https://github.com/swanux/hsuite/releases

**v0.4 | Aphrodite**
*Note: This version is foucuses on new techniques rather than overall stability.*

    * Rewritten the complete program in GTK3
    * Beautiful new logos by Seh
    * Complete redesign of App Spotlight
    * Better UX and GUI
    * Fixed a lots of bugs
    * Added more bugs to fix later...
    * New feedback form for GitHub Issues

# Get things working

**For Ubuntu/Debian:**

To install run:

    sudo apt install software-properties-common && sudo add-apt-repository ppa:swanux/hsuite && sudo apt update && sudo apt install hsuite
    
And to remove, execute:

    sudo apt purge hsuite && sudo apt autoremove
    
**For Arch:**

To install:

    wget https://github.com/swanux/hsuite/raw/master/PKGS/hsuite-0.4.1-1-any.pkg.tar.xz && sudo pacman -U hsuite-0.4.1-1-any.pkg.tar.xz && rm hsuite-0.4.1-1-any.pkg.tar.xz && sudo pacman -Sy
    
And to remove:

    sudo pacman -Runs hsuite
    
**Debugging and updating**

The package will get updates automatically on Ubuntu/Debian.

On Arch run the installation commands when there's a new release to update.

To debug the program, open the terminal and type:

    hsuite
    
You will see the logs in the terminal then.

# Why is the Beta better than the alpha, and why got the program a new name?

**1)** The application is now completely rewritten in Python3 and it has a standalone GUI using wxPython Phoenix. It's got a lots of new features and useful tools included.

**2)** The name change is because it's now more than an extra big Bash script. Now, it's an independent program with more and more features coming. It's now something like a "tool center" or a "Swiss-army". **NOTE:** The name is HSuite, **not** HiSuite (which is the property of Huawei™).

# Demo

Here are some small demos of the beta versions. Lots of work in progress...

**v0.3**

https://streamable.com/9vryf

**v0.4**

https://streamable.com/bx8jp

# What is HSuite?

*Be SSU (Simple, Small, Useful)*

HSuite (previously Helen) is a small program written in Python. Its main goal is to be the Linux "Swiss-army". It's simple and helpful for the new users who want to experience Linux as a daily OS, or for those who are switching distros often. ATTENTION! This program is currently in Beta stage (v0.4). **NOTE:** Currently works on Debian/Ubuntu and Arch based distros.

# Also checkout

HelenArch (Help enter arch) is a CLI installer ISO for Arch Linux. **Installation made easy.**
You can download it from here: https://sourceforge.net/projects/helenarch/
