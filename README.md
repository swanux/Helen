# Changelog
Here is the changelog of every update. For further details you can always check https://github.com/swanux/hsuite/releases

**v0.3 | Perseus**
*Note: In this version the ETA feature always shows 0 minutes*

    ~ Complete rewrite of the program now in Python3 using wxPython4.0.6
    ~ Published as .deb package for Debian based systems and .pkg for Arch based systems
    ~ Uploaded to PPA on launchpad, easy update management
    ~ Currently mainly for demo purposes and for learning, bigger improvements will come in beta v0.4

# Get things working

**For Ubuntu/Debian:**

To install run:

    sudo add-apt-repository ppa:swanux/hsuite && sudo apt update && sudo apt install hsuite
    
And to remove, execute:

    sudo apt purge hsuite && sudo apt autoremove
    
**For Arch:**

To install:

    wget https://github.com/swanux/hsuite/raw/master/hsuite-0.3.4-1-any.pkg.tar.xz && sudo pacman -U hsuite-0.3.4-1-any.pkg.tar.xz && rm hsuite-0.3.4-1-any.pkg.tar.xz
    
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

Here's a small demo of the beta. Lots of work in progress...

https://streamable.com/9vryf

# What is HSuite?

*Be SSU (Simple, Small, Useful)*

HSuite (previously Helen) is a small program written in Python. Its main goal is to be the Linux "Swiss-army". It's simple and helpful for the new users who want to experience Linux as a daily OS, or for those who are switching distros often. ATTENTION! This program is currently in Beta stage (v0.3). **NOTE:** The first beta will be avilable soon. 
Currently works on Debian/Ubuntu and Arch based distros.

# Also checkout

Helena (Help enter arch) is a CLI installer ISO for Arch Linux. **Installation made easy.**
You can download it from here: https://sourceforge.net/projects/helenarch/
