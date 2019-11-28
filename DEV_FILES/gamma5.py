#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#______________________________________________________________________________________________ BEGINNING OF INIT _________________________________________________________________________#


### Import modules ###


## Set minimum required versions
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')

from gi.repository import Gtk, GLib, WebKit2, Gdk, GObject
import os
import re
import webbrowser
from threading import Thread
import time
from datetime import date
from urllib.request import urlopen
from decimal import Decimal
from concurrent import futures

## Set program root location
dire = '/home/daniel/GitRepos/hsuite/DEV_FILES/'
os.chdir(dire)

import common as g                          # For global values


### Declare global variables ###


## Date
g.today = date.today()
g.month = g.today.strftime("%m")
g.day = g.today.strftime("%d")
g.year = g.today.strftime("%Y")

## Detect distro
dist = os.popen('uname -a').read()          # Get distro name
if  'Ubuntu' in dist:
    g.distro = 'Ubuntu'
elif 'archlinux' in dist or 'MANJARO' in dist:
    g.distro = 'Arch'
elif 'Debian' in dist:
    g.distro = 'Debian'
else:
    g.distro = 'Automatic distro detection failed!'

## Colors (button)
colorR = Gdk.color_parse('red')
rgbaR = Gdk.RGBA.from_color(colorR)
colorG = Gdk.color_parse('green')
rgbaG = Gdk.RGBA.from_color(colorG)

## Used with Distro Boutique
g.runE = False                              # To check if a download is already in progress or not
fn = 'sth'                                  # It's declared because of some functions which ones are called from concurrent future
g.Tdownl = ''                               # The name of the currently in progress download
g.cache = []                                # Array that contains the fetched sizes of the ISOs
g.shDict = {'downl_mint' : 'True', 'downl_ubuntu' : 'True', 'downl_solus' : 'True', 'downl_zorin' : 'True', 'downl_deepin' : 'True', 'downl_steamos' : 'True', 'downl_deb' : 'True', 'downl_fedora' : 'True', 'downl_suse' : 'True', 'downl_gentoo' : 'True', 'downl_arch' : 'True', 'downl_lfs' : 'True',} # Dictionary for current state of download buttons (clickable or not)
g.dlist = ['downl_mint', 'downl_ubuntu', 'downl_zorin', 'downl_solus', 'downl_deepin', 'downl_steamos', 'downl_fedora', 'downl_suse', 'downl_deb', 'downl_arch', 'downl_gentoo', 'downl_lfs'] # List of distros
g.dlistLen = len(g.dlist)                   # The number of distros

## Used with App Spotlight
pkg = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]          # For AUR builds (this will be depracted in the future)
g.spinning = False                                                                              # Check if the spinner is spinning or not
g.scanner = True                                                                                # Check if PKG cache is already in memory or not
g.appList = ['opera-stable/', 'barrier/', 'google-chrome-stable/', 'epiphany-browser/', 'firefox', 'vivaldi-stable/', 'wps-office/', 'libreoffice', 'onlyoffice-desktopeditors/', 'softmaker-freeoffice', 'gedit', 'emacs26/', 'code/s', 'atom/', 'sublime-text/', 'geany/', 'skypeforlinux/', 'discord/', 'telegram-desktop/', 'signal-desktop/', 'hexchat/', 'franz/', '0ad/', 'supertux/', 'lutris/', 'playonlinux/', 'steam/', 'minecraft-launcher/', 'popsicle/', 'woeusb/', 'wine/', 'virtualbox/', 'gparted/', 'Touchpad', 'audacity/', 'deja-dup/', 'timeshift/', 'TeamViewer', 'gnome-boxes/', 'supertuxkart/']                                                                        # The list with the debian app names
g.archDict = {'opera-stable/' : 'opera', 'barrier/' : 'barrier/', 'google-chrome-stable/' : 'google-chrome', 'epiphany-browser/' : 'epiphany', 'firefox' : 'firefox', 'vivaldi-stable/' : 'vivaldi', 'wps-office/' : 'wps-office/', 'libreoffice' : 'libreoffice-fresh', 'onlyoffice-desktopeditors/' : 'onlyoffice-bin', 'softmaker-freeoffice' : 'freeoffice', 'gedit' : 'gedit', 'emacs26/' : 'emacs/', 'code/s' : 'code/s', 'atom/' : 'atom/', 'sublime-text/' : 'sublime-text/', 'geany/' : 'geany/', 'skypeforlinux/' : 'skypeforlinux-stable-bin', 'discord/' : 'discord/', 'telegram-desktop/' : 'telegram-desktop/', 'signal-desktop/' : 'signal', 'hexchat/' : 'hexchat/', 'franz/' : 'franz/', '0ad/' : '0ad/', 'supertux/' : 'supertux/', 'lutris/' : 'lutris/', 'playonlinux/' : 'playonlinux/', 'steam/' : 'steam-launcher', 'minecraft-launcher/' : 'minecraft-launcher/', 'popsicle/' : 'popsicle-gtk-git', 'woeusb/' : 'woeusb/', 'wine/' : 'wine/', 'virtualbox/' : 'virtualbox/', 'gparted/' : 'gparted/', 'Touchpad' : 'Touchpad', 'audacity/' : 'audacity/', 'deja-dup/' : 'deja-dup/', 'timeshift/' : 'timeshift/', 'TeamViewer' : 'TeamViewer', 'gnome-boxes/' : 'gnome-boxes/', 'supertuxkart/' : 'supertuxkart/'}                             # The dictionary woth the context of debname:archname
g.humAppsList = ['opera', 'chrome', 'web', 'firefox', 'vivaldi', 'edge', 'woffice', 'loffice', 'ooffice', 'msoffice', 'goffice', 'foffice', 'gedit', 'gnu', 'vscode', 'atom', 'stedit', 'geany', 'skype', 'discord', 'telegram', 'signal', 'hex', 'franz', 'ad', 'skart', 'tux', 'lutris', 'barr', 'pol', 'steam', 'mc', 'pops', 'woe', 'wine', 'vbox', 'gparted', 'gest', 'auda', 'deja', 'tims', 'tw', 'box']
g.butDict = {'opera-stable/' : 'opera', 'barrier/' : 'barr', 'google-chrome-stable/' : 'chrome', 'epiphany-browser/' : 'web', 'firefox' : 'firefox', 'vivaldi-stable/' : 'vivaldi', 'wps-office/' : 'woffice', 'libreoffice' : 'loffice', 'onlyoffice-desktopeditors/' : 'ooffice', 'softmaker-freeoffice' : 'foffice', 'gedit' : 'gedit', 'emacs26/' : 'gnu', 'code/s' : 'vscode', 'atom/' : 'atom', 'sublime-text/' : 'stedit', 'geany/' : 'geany', 'skypeforlinux/' : 'skype', 'discord/' : 'discord', 'telegram-desktop/' : 'telegram', 'signal-desktop/' : 'signal', 'hexchat/' : 'hex', 'franz/' : 'franz', '0ad/' : 'ad', 'supertux/' : 'tux', 'lutris/' : 'lutris', 'playonlinux/' : 'pol', 'steam/' : 'steam', 'minecraft-launcher/' : 'mc', 'popsicle/' : 'pops', 'woeusb/' : 'woe', 'wine/' : 'wine', 'virtualbox/' : 'vbox', 'gparted/' : 'gparted', 'Touchpad' : 'gest', 'audacity/' : 'auda', 'deja-dup/' : 'deja', 'timeshift/' : 'tims', 'TeamViewer' : 'tw', 'gnome-boxes/' : 'box', 'supertuxkart/' : 'skart'}
g.appListLen = len(g.appList)
g.statDict = {'Opera' : '', 'Chrome' : '', 'Web' : '', 'Firefox' : '', 'Vivaldi' : '', 'Edge' : '', 'WPS Office' : '', 'Libreoffice' : '', 'Only Office' : '', 'Free Office' : '', 'Gedit' : '', 'GNU Emacs' : '', 'Visual Studio Code' : '', 'Atom Editor' : '', 'Sublime Text Editor' : '', 'Geany' : '', 'Skype' : '', 'Discord' : '', 'Telegram' : '', 'Signal' : '', 'HexChat' : '', 'Franz' : '', '0 A.D.' : '', 'SuperTuxKart' : '', 'SuperTux' : '', 'Lutris' : '', 'Barrier by debauchee' : '', 'Play On Linux' : '', 'Steam' : '', 'Minecraft' : '', 'Popsicle' : '', 'WoeUSB' : '', 'Wine' : '', 'Virtualbox' : '', 'GParted' : '', 'Touchpad Gestures' : '', 'Audacity' : '', 'Déja-Dup' : '', 'Timeshift' : '', 'TeamViewer' : '', 'Gnome Boxes' : ''}
g.layDict = {'opera-stable/' : 'Opera', 'google-chrome-stable/' : 'Chrome', 'epiphany-browser/' : 'Web', 'firefox' : 'Firefox', 'vivaldi-stable/' : 'Vivaldi', 'dikk' : 'Edge', 'wps-office/' : 'WPS Office', 'libreoffice' : 'Libreoffice', 'onlyoffice-desktopeditors/' : 'Only Office', 'softmaker-freeoffice' : 'Free Office', 'gedit' : 'Gedit', 'emacs26/' : 'GNU Emacs', 'code/s' : 'Visual Studio Code', 'atom/' : 'Atom Editor', 'sublime-text/' : 'Sublime Text Editor', 'geany/' : 'Geany', 'skypeforlinux/' : 'Skype', 'discord/' : 'Discord', 'telegram-desktop/' : 'Telegram', 'signal-desktop/' : 'Signal', 'hexchat/' : 'HexChat', 'franz/' : 'Franz', '0ad/' : '0 A.D.', 'supertux/' : 'SuperTuxKart', 'supertuxkart/' : 'SuperTux', 'lutris/' : 'Lutris', 'barrier/' : 'Barrier by debauchee', 'playonlinux/' : 'Play On Linux', 'steam/' : 'Steam', 'minecraft-launcher/' : 'Minecraft', 'popsicle/' : 'Popsicle', 'woeusb/' : 'WoeUSB', 'wine/' : 'Wine', 'virtualbox/' : 'Virtualbox', 'gparted/' : 'GParted', 'Touchpad' : 'Touchpad Gestures', 'audacity/' : 'Audacity', 'deja-dup/' : 'Déja-Dup', 'timeshift/' : 'Timeshift', 'TeamViewer' : 'TeamViewer', 'gnome-boxes/' : 'Gnome Boxes'}

## Used generally
UI_FILE = "hsuite.glade"                                                                        # The glade file
g.user = os.popen("who|awk '{print $1}'r").read()                                               # Getting the name of the non-root user
g.user = g.user.rstrip()                                                                        # Edit to only contain the name itself
xorw = os.popen('echo $XDG_SESSION_TYPE').read()                                                # Get current session type
if "x" in xorw:                                                                                 # It's Xorg, so it wokrs with gestures'
    g.lehete = "You need to reboot or log in and out again after the install has been completed to apply all changes."
else:                                                                                           # It is Wayland, so it won't work
    g.lehete = "You can currently only use this feature with x11 based desktop. It does not support Wayland."
wer = os.popen('ls').read()                                                                     # Discover the current working dir

## Print info to debug
print("Current date: %s" % g.today)
print("Current day: %s" % g.day)
print("Current month: %s" % g.month)
print("Current year: %s" % g.year)
print("Name of non-root user: %s" % g.user)
print("Content of working directory: %s" % str(wer))
print("Output of $uname -a$ : %s" % dist)
print("Detected distro: %s" % g.distro)


#______________________________________________________________________________________________ END OF INIT ______________________________________________________________________________________#

#_________________________________________________________________________________________ BEGIN OF THREADS _____________________________________________________________________________________#

# This class and function is the core of every background process in the program

class myThread (Thread):
    def __init__(self, threadID, name):
        Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        g._stop_event = False
    def run(self):
        print ("Starting " + self.name)
        my_thread()                                                                 # Calls the function
        print ("Exiting " + self.name)
    def stop(self):
        g._stop_event = True
        print("stop func")

def my_thread():
    if g.CA == 'Opera':                                                             # g.CA is a global variable which is declared before calling this function. Its main role is to indicate the name of the program which is being changed/used. It tells the function what to do. CA means "Current Action"
        if g.distro == 'Ubuntu' or g.distro == 'Debian':                            # We need to check the current distro for some distro specific commands
            g.asr = 'DEBIAN_FRONTEND=noninteractive apt install opera-stable pepperflashplugin-nonfree -y' # g.asr is a global parameter, it means "as root". If something is given to asr, it'll run it with pkexec prompt
            app.asroot()                                                            # It calls the function itself
        elif g.distro == 'Arch':
            g.asr = 'pacman -Sq --noconfirm opera opera-ffmpeg-codecs flashplugin'
            app.asroot()
    elif g.CA == 'OperaR':                                                          # The R means this is for the removal of the program.
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge opera-stable pepperflashplugin-nonfree -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm  opera opera-ffmpeg-codecs flashplugin'
            app.asroot()
    elif g.CA == 'Lutris':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt install lutris -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Sq --noconfirm lutris'
            app.asroot()
    elif g.CA == 'LutrisR':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge lutris -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm  lutris'
            app.asroot()
    elif g.CA == 'Chrome':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt install google-chrome-stable -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.fold = 'google-chrome' # The name of the folder (AUR)
            g.num = 2 # The position inside the folder (AUR)
            app.aurer() # Calling the builder function
    elif g.CA == 'ChromeR':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge google-chrome-stable -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm google-chrome'
            app.asroot()
    elif g.CA == 'Web':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt install epiphany-browser -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Sq --noconfirm epiphany'
            app.asroot()
    elif g.CA == 'WebR':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge epiphany-browser -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm epiphany'
            app.asroot()
    elif g.CA == 'Firefox':
        if g.distro == 'Ubuntu':
            g.asr = 'apt install firefox -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Sq --noconfirm firefox'
            app.asroot()
        elif g.distro == 'Debian':
            g.asr = 'apt install firefox-esr -y'
            app.asroot()
    elif g.CA == 'FirefoxR':
        if g.distro == 'Ubuntu':
            g.asr = 'apt purge firefox -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm firefox'
            app.asroot()
        elif g.distro == 'Debian':
            g.asr = 'apt purge firefox-esr -y ; apt autoremove -y'
            app.asroot()
    elif g.CA == 'Vivaldi':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt install vivaldi-stable -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.fold = 'vivaldi'
            g.num = 2
            app.aurer()
    elif g.CA == 'VivaldiR':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge vivaldi-stable -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm vivaldi'
            app.asroot()
    elif g.CA == 'Only Office':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt install onlyoffice-desktopeditors -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.fold = 'onlyoffice-bin'
            g.num = 1
            app.aurer()
    elif g.CA == 'Only OfficeR':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge onlyoffice-desktopeditors -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm onlyoffice-bin'
            app.asroot()
    elif g.CA == 'Free Office':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt install softmaker-freeoffice-2018 -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.fold = 'freeoffice'
            g.num = 1
            app.aurer()
    elif g.CA == 'Free OfficeR':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge softmaker-freeoffice-2018 -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --nocnonfirm freeoffice'
            app.asroot()
    elif g.CA == 'Gedit':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt install gedit gedit-plugins -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Sq --noconfirm gedit gedit-plugins'
            app.asroot()
    elif g.CA == 'GeditR':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge gedit gedit-plugins -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm gedit gedit-plugins'
            app.asroot()
    elif g.CA == 'GNU Emacs':
        if g.distro == 'Ubuntu':
            g.asr = 'apt install emacs26 -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Sq --noconfirm emacs'
            app.asroot()
        elif g.distro == 'Debian':
            g.asr = 'apt install emacs -y'
            app.asroot()
    elif g.CA == 'GNU EmacsR':
        if g.distro == 'Ubuntu':
            g.asr = 'apt purge emacs26 -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm emacs'
            app.asroot()
        elif g.distro == 'Debian':
            g.asr = 'apt purge emacs -y ; apt autoremove -y'
            app.asroot()
    elif g.CA == 'Visual Studio Code':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt install code -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Sq --noconfirm code'
            app.asroot()
    elif g.CA == 'Visual Studio CodeR':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge code -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm code'
            app.asroot()
    elif g.CA == 'Atom Editor':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt install atom -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Sq --noconfirm atom'
            app.asroot()
    elif g.CA == 'Atom EditorR':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge atom -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm atom'
            app.asroot()
    elif g.CA == 'Sublime Text Editor':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt install sublime-text -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Sq --noconfirm sublime-text'
            app.asroot()
    elif g.CA == 'Sublime Text EditorR':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge sublime-text -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm sublime-text'
            app.asroot()
    elif g.CA == 'Geany':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt install geany -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Sq --noconfirm geany'
            app.asroot()
    elif g.CA == 'GeanyR':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge geany -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm geany'
            app.asroot()
    elif g.CA == 'Discord':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt install discord -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Sq --noconfirm discord'
            app.asroot()
    elif g.CA == 'DiscordR':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge discord -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm discord'
            app.asroot()
    elif g.CA == 'Telegram':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt install telegram-desktop -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Sq --noconfirm telegram-desktop'
            app.asroot()
    elif g.CA == 'TelegramR':
        if g.distro == 'Ubuntu'or g.distro == 'Debian':
            g.asr = 'apt purge telegram-desktop -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm telegram-desktop'
            app.asroot()
    elif g.CA == 'Signal':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt install signal-desktop -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.fold = 'signal'
            g.num = 2
            app.aurer()
    elif g.CA == 'SignalR':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge signal-desktop -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm signal'
            app.asroot()
    elif g.CA == 'HexChat':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt install hexchat -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Sq --noconfirm hexchat'
            app.asroot()
    elif g.CA == 'HexChatR':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge hexchat -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm hexchat'
            app.asroot()
    elif g.CA == 'SuperTux':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt install supertux -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Sq --noconfirm supertux'
            app.asroot()
    elif g.CA == 'SuperTuxR':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge supertux -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm supertux'
            app.asroot()
    elif g.CA == 'Play On Linux':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt install playonlinux -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Sq --noconfirm playonlinux'
            app.asroot()
    elif g.CA == 'Play On LinuxR':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge playonlinux -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm playonlinux'
            app.asroot()
    elif g.CA == 'Minecraft':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'wget ~/Minecraft.deb https://launcher.mojang.com/download/Minecraft.deb ; dpkg -i --force-all Minecraft.deb ; apt install -f -y ; rm Minecraft.deb'
            app.asroot()
        elif g.distro == 'Arch':
            g.fold = 'minecraft-launcher'
            g.num = 1
            app.aurer()
    elif g.CA == 'MinecraftR':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge minecraft-launcher -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm minecraft-launcher'
            app.asroot()
    elif g.CA == 'TeamViewer':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'DEBIAN_FRONTEND=noninteractive apt install teamviewer -y ; teamviewer --daemon enable'
            app.asroot()
        elif g.distro == 'Arch':
            os.system('wget https://download.teamviewer.com/download/linux/teamviewer_amd64.tar.xz') # It's special, because it grabs the sources directly from the developers page and builds the most up to date version
            ver = os.popen('ls').read()
            ver = ver.split()
            hos = len(ver)
            print(hos)
            i = 0
            print(ver)
            while i < hos:
                if 'teamviewer' in ver[i]:
                    ver = ver[i]
                else:
                    i += 1
            os.system('tar -xJf %s && rm -rf %s' % (ver, ver))
            g.asr = 'cd teamviewer ; ./tv-setup install force'
            app.asroot()
    elif g.CA == 'TeamViewerR':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge teamviewer -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'cd teamviewer ; ./tv-setup uninstall force'
            app.asroot()
            os.system('rm -rf teamviewer && rm -rf /opt/teamviewer')
    elif g.CA == 'Gnome Boxes':
        if g.distro == 'Ubuntu'or g.distro == 'Debian':
            g.asr = 'apt install gnome-boxes -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Sq --noconfirm gnome-boxes'
            app.asroot()
    elif g.CA == 'Gnome BoxesR':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge gnome-boxes -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm gnome-boxes'
            app.asroot()
    elif g.CA == 'Franz':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt install franz -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.num = 2
            g.fold = 'franz'
            app.aurer()
    elif g.CA == 'FranzR':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge franz -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm franz'
            app.asroot()
    elif g.CA == 'Libreoffice':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt install libreoffice libreoffice-gtk -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Sq --noconfirm libreoffice-fresh'
            app.asroot()
    elif g.CA == 'LibreofficeR':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge libreoffice-* -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm libreoffice-fresh'
            app.asroot()
    elif g.CA == 'WPS Office':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'DEBIAN_FRONTEND=noninteractive apt install wps-office ttf-wps-fonts -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.num = 2
            g.fold = 'wps-office'
            app.aurer()
            g.num = 2
            g.fold = 'ttf-wps-fonts'
            app.aurer()
    elif g.CA == 'WPS OfficeR':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge ttf-wps-fonts wps-office -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm wps-office ttf-wps-fonts'
            app.asroot()
    elif g.CA == 'Popsicle':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt install popsicle* -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.fold = 'popsicle-git'
            g.num = 3
            app.aurer()
    elif g.CA == 'PopsicleR':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge popsicle* -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm popsicle-gtk-git'
            app.asroot()
    elif g.CA == 'Wine':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt install wine wine32 wine64 -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Sq --noconfirm wine'
            app.asroot()
    elif g.CA == 'WineR':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge wine* -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm wine'
            app.asroot()
    elif g.CA == 'Virtualbox':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt install virtualbox-6.0 -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Sq --noconfirm virtualbox ; /sbin/rcvboxdrv setup'
            app.asroot()
    elif g.CA == 'VirtualboxR':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge virtualbox* -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm virtualbox'
            app.asroot()
    elif g.CA == 'WoeUSB':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt install woeusb -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.num = 2
            g.fold = 'woeusb'
            app.aurer()
    elif g.CA == 'WoeUSBR':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge woeusb -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm woeusb'
            app.asroot()
    elif g.CA == 'GParted':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt install gparted gpart -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Sq --noconfirm gparted gpart'
            app.asroot()
    elif g.CA == 'GPartedR':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge gpart* -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm gparted'
            app.asroot()
    elif g.CA == 'Audacity':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt install audacity -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Sq --noconfirm audacity'
            app.asroot()
    elif g.CA == 'AudacityR':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge audacity* -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm audacity'
            app.asroot()
    elif g.CA == 'Déja-Dup':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt install deja-dup* -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Sq --noconfirm deja-dup'
            app.asroot()
    elif g.CA == 'Déja-DupR':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge deja-dup* -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm deja-dup'
            app.asroot()
    elif g.CA == 'Timeshift':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt install timeshift -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.num = 1
            g.fold = 'timeshift'
            app.aurer()
    elif g.CA == 'TimeshiftR':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge timeshift -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm timeshift'
            app.asroot()
    elif g.CA == 'Touchpad Gestures':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt install libinput-tools libinput-bin wmctrl python3 xdotool python3-setuptools -y ; gpasswd -a %s input ; cd %s ; git clone https://github.com/bulletmark/libinput-gestures.git ; git clone https://gitlab.com/cunidev/gestures ; cd libinput-gestures ; ./libinput-gestures-setup install ; cd .. ; cd gestures ; python3 setup.py install ; cd .. ; rm -rf libinput-gestures ; rm -rf gestures' % (g.user, dire)
            app.asroot()
            os.system('cp /usr/share/hsuite/confs/libinput-gestures.conf ~/.config')
        elif g.distro == 'Arch':
            g.num = 3
            g.fold = 'libinput-gestures'
            app.aurer()
            g.num = 1
            g.fold = 'gestures'
            app.aurer()
            os.system('cp /usr/share/hsuite/confs/libinput-gestures.conf ~/.config')
    elif g.CA == 'Touchpad GesturesR':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge libinput-tools xdotool libinput-bin python3-setuptools -y ; apt autoremove -y ; rm -rf /usr/local/bin/gestures ; rm -rf /usr/bin/libinput-gestures ; rm -rf /usr/share/applications/libinput-gestures.desktop ; rm -rf /usr/share/applications/org.cunidev.gestures.desktop'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm libinput-gestures gestures'
            app.asroot()
    elif g.CA == 'Skype':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt install skypeforlinux -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.num = 3
            g.fold = 'skypeforlinux-stable-bin'
            app.aurer()
    elif g.CA == 'SkypeR':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge skypeforlinux -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm skypeforlinux-stable-bin'
            app.asroot()
    elif g.CA == 'Barrier by debauchee':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt install barrier -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Sq --noconfirm barrier'
            app.asroot()
    elif g.CA == 'Barrier by debaucheeR':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge barrier -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm barrier'
            app.asroot()
    elif g.CA == '0 A.D.':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt install 0ad -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Sq --noconfirm 0ad'
            app.asroot()
    elif g.CA == '0 A.D.R':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge 0ad -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm 0ad'
            app.asroot()
    elif g.CA == 'SuperTuxKart':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt install supertuxkart -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Sq --noconfirm supertuxkart'
            app.asroot()
    elif g.CA == 'SuperTuxKartR':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge supertuxkart -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm supertuxkart'
            app.asroot()
    elif g.CA == 'Steam':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt install steam-launcher -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Sq --noconfirm steam steam-native-runtime'
            app.asroot()
    elif g.CA == 'SteamR':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge steam* -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm steam steam-native-runtime'
            app.asroot()
    else:
        print('Error 3')

#___________________________________________________________________________________________ END OF THREADS ______________________________________________________________________________________#

#______________________________________________________________________________________________ BEGIN OF GUI ______________________________________________________________________________________#

# This class handles everything releated to the GUI and some background tasks connected to the program

class GUI:

    def asroot(self):                                               # The function to display prompt for root acces.
        with open("bashLayer.sh") as f:
            lines = f.readlines()
        lines[2] = 'CMD="%s"\n' % g.asr
        with open("bashLayer.sh", "w") as f:
            f.writelines(lines)
        os.system('bash bashLayer.sh')                              # bashLayer.sh is a small bash script which runs predefined programs. It's like a module.

    def aurer(self):                                                # The builder for AUR
        with open("logname.sh") as f:
            lines = f.readlines()
        cmd = 'echo $USER && cd /home/%s/.tmp_hsuite && git clone https://aur.archlinux.org/%s.git && cd %s && makepkg -rc' % (g.user, g.fold, g.fold)
        lines[4] = 'mkdir .tmp_hsuite && %s' % cmd
        with open("logname.sh", "w") as f:
            f.writelines(lines)
        os.system('./logname.sh')
        pkg = os.popen('ls /home/%s/.tmp_hsuite/%s' % (g.user, g.fold)).read()
        pkg = pkg.split()
        pkg = pkg[g.num]
        print(pkg)
        g.asr = 'pacman -U --noconfirm /home/%s/.tmp_hsuite/%s/%s ; rm -rf /home/%s/.tmp_hsuite/' % (g.user, g.fold, pkg, g.user)
        app.asroot()

    count = 0                                                       # It'll be used later when displaying the time during program install
    def __init__(self):                                             # Init the main gui

        self.builder = Gtk.Builder()                                # Prepare to use builder
        self.win = Gtk.Window()                                     # The main window
        self.builder.add_from_file(UI_FILE)                         # Import the glade file
        g.browserholder = WebKit2.WebView()                         # Prepare webview
        g.browserholder.set_editable(False)                         # Disable user interraction
        self.builder.connect_signals(self)                          # Connect all signals
        g.stack = self.builder.get_object('stack')                  # Get the main stack object

        g.window = self.builder.get_object('window')                # Get the main window
        if os.geteuid() == 0:
           g.window.set_title(g.version+' (as superuser)')          # Indicate if runnung as root or not
        else:
            g.window.set_title(g.version)
        g.window.show_all()                                         # Display the program

    def on_window_delete_event(self, window, e):                    # This happens when close button is clicked
        x, y = g.window.get_position()                              # Getting the window position
        sx, sy = g.window.get_size()                                # Get the size of the window
        dialogWindow = Gtk.MessageDialog(None,                      # Make a popup window without parent
                              Gtk.DialogFlags.MODAL | Gtk.DialogFlags.DESTROY_WITH_PARENT, # make it modal (always on top) and destroy together with main window (for example on force quit)
                              Gtk.MessageType.QUESTION,             # message type is question
                              Gtk.ButtonsType.YES_NO,               # add yes and no buttons
                              "Do you really would like to exit now?") # set the label
        dialogWindow.set_title("Prompt")                            # set the title
        dsx, dsy = dialogWindow.get_size()                          # get the dialogs size
        dialogWindow.move(x+((sx-dsx)/2), y+((sy-dsy)/2))           # Move it to the center of the main window
        dx, dy = dialogWindow.get_position()                        # set the position
        dialogWindow.show_all()                                     # display the dialog
        res = dialogWindow.run()                                    # save the response
        if res == Gtk.ResponseType.YES:                             # if yes ...
            print('OK pressed')
            dialogWindow.destroy()
            Gtk.main_quit()                                         # quit program
        elif res == Gtk.ResponseType.NO:                            # if no ...
            print('No pressed')
            dialogWindow.destroy()                                  # sestroy dialog
            return True                                             # end function

###################################################################################

    def colorer(self):                                          # Set the button colors
        self.OnCheck()                                          # Call function to check if apps are installed or not
        g.gbut.set_label(g.status)                              # set the button label depending on this
        if g.status == "Remove":
            g.gbut.override_background_color(0,rgbaR)           # red for remove
        else:
            g.gbut.override_background_color(0,rgbaG)           # green for install

    def scanner(self):                                          # Scans the OS for programs

        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.insList = os.popen('apt list --installed').read() # list of installed apps on debian based OS
        elif g.distro == 'Arch':
            g.insList = os.popen('pacman -Q').read()            # same on arch
        else:
            print('PACK ERROR')

### Check for every program in the list

        for i in range(g.appListLen):
            if g.distro == 'Arch':
                g.name = g.archDict[g.appList[i]]
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.name = g.appList[i]                                               # the name to check for
            else:
                print('ERROR IN NAME')
            g.gbut = self.builder.get_object("%s_but" % g.butDict[g.appList[i]])    # importing the button to a general global variable
            self.colorer()                                                          # Call function for setting label and color
            g.current_value = g.status                                              # value refers to the state: Install/Remove DING
            g.tempNam = g.layDict[g.appList[i]]
            g.statDict[g.tempNam] = g.status

        g.scanner = False                                                   # It indicates that the state of every program is now loaded into the memory

### Download methods

    def toggle(self, fn):                                                   # Disable or enable buttons based on a pattern
        print(self, fn, g.state)
        for i in range(g.dlistLen):
            print("Toggle %s" % i)
            if g.dlist[i] != g.Tdownl and g.shDict[g.dlist[i]] != "PFalse":
                print(g.dlist[i], g.shDict[g.dlist[i]], g.Tdownl)
                g.cBut = self.builder.get_object(g.dlist[i])
                GLib.idle_add(g.cBut.set_sensitive, g.state)
                g.shDict[g.dlist[i]] = "%s" % g.state

    def ex_target(self):                                                    # Starting download in a background thread BUT inside the GUI class, not the thread. This is because of the nature of GTK (and other GUI toolkits) that can't handle GUI changes from outside of the main thread (gui class)
        print("DLthread...")
        g.quit = False                                                      # This variable shows if the thread needs to exit
        while not g.quit:
            buffer = g.u.read(g.block_sz)                                   # Reads the downloaded bytes in blocks
            if not buffer:
               break                                                        # break if error occures
            g.file_size_dl += len(buffer)                                   # Set the downloaded file size to buffer
            g.f.write(buffer)                                               # write this block to the downloaded file
            g.status = r"Cancel  [%3.2f%%]" % (g.file_size_dl * 100 / g.file_size) # Calculate precentage
            GLib.idle_add(g.downl.set_label, g.status)                      # Place on waiting list to change the label to the actual status
        print("DLend!!")
        g.runE = False                                                      # Shows that no downloads are running
        GLib.idle_add(g.downl.set_label, g.orig)                            # Set back the button label to the original
        print(g.orig)
        print("Label restore")
        if g.rmE:                                                           # If the download is aborted by the user, remove the already downloaded file
            os.system('rm /home/%s/Downloads/%s' % (g.user, g.file_name) )
        else:
            GLib.idle_add(g.downl.set_label, "Ready in ~/Downloads/")       # Set label to ready
            GLib.idle_add(g.downl.set_sensitive, False)                     # Disable button
            g.shDict[g.Tdownl] = "PFalse"                                   # Set the state to permanent false
            print("done with it")

    def on_downl_begin(self):
        g.u = urlopen(g.url)                                                # Open the url
        g.file_size = int(g.u.getheader('Content-Length'))                  # Get the size of the file
        if g.runE == True:                                                  # If download is already running
            g.rmE = True                                                    # set remove flag to true
            g.quit = True                                                   # tell the thread to stop
            print("TruTogle")
            g.state = True                                                  # set button state to enabled
            self.toggle(fn)                                                 # enable every button
            return                                                          # end
        elif g.runE == False:                                               # If no downloads are running
            g.runE = True                                                   # toggle that now one is running
            g.rmE = False                                                   # we don't need to remove the downloaded file, because it's ready
            g.orig = g.downl.get_label()                                    # save the original label of the button
        g.file_name = g.url.split('/')[-1]                                  # get the filename
        g.f = open('/home/%s/Downloads/%s' % (g.user, g.file_name) , 'wb')  # set download location
        print("Downloading: %s Bytes: %s" % (g.file_name, g.file_size))
        g.file_size_dl = 0                                                  # set downloaded size to 0
        g.block_sz = 8192                                                   # set block size
        print("FalsTogle")
        g.state = False                                                     # disable buttons
        self.toggle(fn)                                                     # run function to do this

        g.t1 = futures.ThreadPoolExecutor(max_workers=2)                    # init thread
        f = g.t1.submit(self.ex_target)                                     # start it
        g.state = True                                                      # set buttons to active
        f.add_done_callback(self.toggle)                                    # after done run this function

    def on_downl_mint_clicked(self, button):
        print("mint")
        g.downl = self.builder.get_object('downl_mint')
        g.Tdownl = 'downl_mint'                                             # this download
        g.url = g.uriDict["downl_mint"]
        self.on_downl_begin()

    def on_downl_ubuntu_clicked(self, button):
        print("ubuntu")
        g.downl = self.builder.get_object('downl_ubuntu')
        g.Tdownl = 'downl_ubuntu'
        g.url = g.uriDict["downl_ubuntu"]
        self.on_downl_begin()

    def on_downl_solus_clicked(self, button):
        print("solus")
        g.downl = self.builder.get_object('downl_solus')
        g.Tdownl = 'downl_solus'
        g.url = g.uriDict["downl_solus"]
        self.on_downl_begin()

    def on_downl_deepin_clicked(self, button):
        print("deepin")
        g.downl = self.builder.get_object('downl_deepin')
        g.Tdownl = 'downl_deepin'
        g.url = g.uriDict["downl_deepin"]
        self.on_downl_begin()

    def on_downl_zorin_clicked(self, button):
        print("zorin")
        g.downl = self.builder.get_object('downl_zorin')
        g.Tdownl = 'downl_zorin'
        g.url = g.uriDict["downl_zorin"]
        self.on_downl_begin()

    def on_downl_steamos_clicked(self, button):
        print("steamos")
        g.downl = self.builder.get_object('downl_steamos')
        g.Tdownl = 'downl_steamos'
        g.url = g.uriDict["downl_steamos"]
        self.on_downl_begin()

    def on_downl_deb_clicked(self, button):
        print("deb")
        g.downl = self.builder.get_object('downl_deb')
        g.Tdownl = 'downl_deb'
        g.url = g.uriDict["downl_deb"]
        self.on_downl_begin()

    def on_downl_fedora_clicked(self, button):
        print("fedora")
        g.downl = self.builder.get_object('downl_fedora')
        g.Tdownl = 'downl_fedora'
        g.url = g.uriDict["downl_fedora"]
        self.on_downl_begin()

    def on_downl_suse_clicked(self, button):
        print("suse")
        g.downl = self.builder.get_object('downl_suse')
        g.Tdownl = 'downl_suse'
        g.url = g.uriDict["downl_suse"]
        self.on_downl_begin()

    def on_downl_arch_clicked(self, button):
        print("arch")
        g.downl = self.builder.get_object('downl_arch')
        g.Tdownl = 'downl_arch'
        g.url = g.uriDict["downl_arch"]
        self.on_downl_begin()

    def on_downl_gentoo_clicked(self, button):
        print("gentoo")
        g.downl = self.builder.get_object('downl_gentoo')
        g.Tdownl = 'downl_gentoo'
        g.url = g.uriDict["downl_gentoo"]
        self.on_downl_begin()

    def on_downl_lfs_clicked(self, button):
        print("lfs")
        g.downl = self.builder.get_object('downl_lfs')
        g.Tdownl = 'downl_lfs'
        g.url = g.uriDict["downl_lfs"]
        self.on_downl_begin()

######## End of download section

    def button_clicked (self, button):                                              # Button is the name of the app spotlight button

        if g.scanner == False:                                                      # If already in memory don't waste resources
            print('VALUE_FOUND')
            notebook_box = self.builder.get_object('notebook_box')                  # notebook box is the name of the app spotlight page
            g.stack.set_visible_child(notebook_box)                                 # set it visible
        elif g.scanner:                                                             # if not in memory, then scan it now
            notebook_box = self.builder.get_object('notebook_box')
            g.stack.set_visible_child(notebook_box)
            print('NO_VALUE')
            app.scanner()                                                           # start scanning
        else:
            print('ERROR')

    def OnNeed(self):                                                               # This is executed when an app is being installed/removed
        g.scanner = True                                                            # removes scan cache from memory because it needs to rescan because one app changed
        g.spinning = True                                                           # indicates that the spinner is running
        sTxt = self.builder.get_object('spinner_txt')                               # get the label of the spinner
        sTxt.set_label('Loading...')                                                # set to loading
        spinner = self.builder.get_object('spinner')                                # get spinner itself
        t1 = myThread(1, "Thread-1")                                                # init thread with thread function
        t1.start()                                                                  # start it
        spinner_box = self.builder.get_object('spinner_box')                        # get the box with the spinner
        g.stack.set_visible_child(spinner_box)                                      # make it visible
        g.m = 0                                                                     # set minutes to 0
        spinner.start()                                                             # start spinner
        def counter(timer):                                                         # function for counting time
            s=timer.count+1                                                         # seconds incraseing
            timer.count = s                                                         # counter is equal to s
            sTxt.set_label('Processing '+g.name+'         Elapsed time : '+str(g.m)+':'+str(s))  # set spin label
            if s == 59:                                                             # add one to min and reset sec
                timer.count = -1
                g.m = g.m+1
            if t1.isAlive():                                                        # if thread is still running repeat
                return True
            else:                                                                   # on exit
                timer.count = 0                                                     # reset counter
                spinner.stop()                                                      # stop spinner
                button = 0                                                          # declare button variable (don't know why)
                self.button_clicked(button)                                         # imitate reopening of app spotlight
                g.spinning = False                                                  # indicate that spinner stopped
                return False                                                        # end
        self.source_id = GLib.timeout_add(1000, counter, self)                      # DING

    def on_fb_but_clicked(self, button):                                            # feedback button
        view_fb = self.builder.get_object('view_fb')
        web_box = self.builder.get_object('web_box')
        g.browserholder.load_uri("https://docs.google.com/forms/d/e/1FAIpQLSec6abGuF3c-zTyLt1NUes2kifOlAAhrc5FOLPUIPUHhA9cmA/viewform?hl=en") # load google from
        view_fb.add(g.browserholder)
        g.browserholder.show()
        g.stack.set_visible_child(web_box)

    def on_git_link_clicked(self, button):                                          # information button in about section
        webbrowser.open_new("https://swanux.github.io/hsuite/")                     # open project page in browser

    def on_htools_but_clicked(self, button):                                        # htools clicked
        x, y = g.window.get_position()
        sx, sy = g.window.get_size()
        dialogWindow = Gtk.MessageDialog(None,
                              Gtk.DialogFlags.MODAL | Gtk.DialogFlags.DESTROY_WITH_PARENT,
                              Gtk.MessageType.INFO,
                              Gtk.ButtonsType.OK,
                              g.txt1)                                               # dialog for prompting that this feature isn't ready yet

        dialogWindow.set_title("Coming soon")
        dsx, dsy = dialogWindow.get_size()
        dialogWindow.move(x+((sx-dsx)/2), y+((sy-dsy)/2))
        dialogWindow.show_all()
        res = dialogWindow.run()
        dialogWindow.destroy()

    def on_ac_but_clicked(self, button):                                            # previously android corner (ac) is same as htools
        self.on_htools_but_clicked(button)

    def getSize (self):                                                             # fetch download sizes
        print('Getting Links...')
        def findNew():
            reponse = urlopen(urii)
            dat = reponse.read()
            text = dat.decode('utf-8')
            pattern = re.findall(r'%s' % perPat, text)
            g.gentoo = pattern[0]
            pattern = ''.join(pattern)
            pattern = pattern.replace(".", "")
            pattern = re.findall(r'%s' % perVer, pattern)
            pattern = list(map(int, pattern))
            try:
                pattern.remove(710)
                pattern.remove(710)
            except:
                print("no lfs")
            pattern.sort()
            g.vers = pattern[-1]
            g.vers = [int(i) for i in str(g.vers)]

        if g.day == "01":
            aMonth = int(g.month, button) - 1
        else:
            aMonth = g.month
        archLink = 'http://mirrors.evowise.com/archlinux/iso/%s.%s.01/archlinux-%s.%s.01-x86_64.iso' % (g.year, aMonth, g.year, aMonth)

        urii = "http://releases.ubuntu.com" # The URL
        perPat = '"+[\d]+.[\d]+/'           # Personal pattern
        perVer = '[\d]+[\d]+[\d]+[\d]'      # Personal version syntax
        findNew()                           # Call function
        ubuntuLink = 'http://releases.ubuntu.com/%s%s.%s%s/ubuntu-%s%s.%s%s-desktop-amd64.iso' % (g.vers[0], g.vers[1], g.vers[2], g.vers[3], g.vers[0], g.vers[1], g.vers[2], g.vers[3])

        urii = "http://mirrors.evowise.com/linuxmint/stable/"
        perPat = '"+[\d]+.[\d]+/'
        perVer = '[\d]+[\d]+[\d]'
        findNew()
        mintLink = 'http://mirrors.evowise.com/linuxmint/stable/%s%s.%s/linuxmint-%s%s.%s-cinnamon-64bit.iso' % (g.vers[0], g.vers[1], g.vers[2], g.vers[0], g.vers[1], g.vers[2])

        urii = "http://mirror.inode.at/data/deepin-cd/"
        perPat = '"+[\d]+.[\d]+/'
        perVer = '[\d]+[\d]+[\d]'
        findNew()
        deepinLink = 'http://mirror.inode.at/data/deepin-cd/%s%s.%s%s/deepin-%s%s.%s%s-amd64.iso' % (g.vers[0], g.vers[1], g.vers[2], g.vers[3], g.vers[0], g.vers[1], g.vers[2], g.vers[3])

        urii = "https://cdimage.debian.org/images/unofficial/non-free/images-including-firmware/current-live/amd64/iso-hybrid/"
        perPat = 'debian-live-+[\d]+[\d]+.[\d]+.[\d]'
        perVer = '[\d]+[\d]+[\d]'
        findNew()
        debianLink = 'https://cdimage.debian.org/images/unofficial/non-free/images-including-firmware/current-live/amd64/iso-hybrid/debian-live-%s%s.%s.%s-amd64-cinnamon+nonfree.iso' % (g.vers[0], g.vers[1], g.vers[2], g.vers[3])

        steamosLink = 'http://repo.steampowered.com/download/SteamOSDVD.iso'

        urii = "https://sourceforge.net/projects/zorin-os/files/"
        perPat = 'files/+[\d]+/download'
        perVer = '[\d]+[\d]'
        findNew()
        zorinosLink = 'https://netcologne.dl.sourceforge.net/project/zorin-os/%s%s/Zorin-OS-%s%s-Core-64-bit-r1.iso' % (g.vers[0], g.vers[1], g.vers[0], g.vers[1])

        urii = "http://fedora.inode.at/releases/"
        perPat = '"+[\d]+/'
        perVer = '[\d]+[\d]'
        findNew()
        fedoraLink = 'http://fedora.inode.at/releases/%s%s/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-%s%s-1.9.iso' % (g.vers[0], g.vers[1], g.vers[0], g.vers[1])

        opensuseLink = 'https://download.opensuse.org/tumbleweed/iso/openSUSE-Tumbleweed-DVD-x86_64-Current.iso'

        solusLink = 'http://solus.veatnet.de/iso/images/4.0/Solus-4.0-Budgie.iso'

        urii = "http://distfiles.gentoo.org/releases/amd64/autobuilds/current-install-amd64-minimal/"
        perPat = '[\d]+[\d]+[\w]+[\d][\w]'
        perVer = '[\d]+[\d]'
        findNew()
        gentooLink = 'http://distfiles.gentoo.org/releases/amd64/autobuilds/current-install-amd64-minimal/install-amd64-minimal-%s.iso' % g.gentoo

        urii = "http://www.linuxfromscratch.org/lfs/downloads/"
        perPat = '[\d]+.[\d]+-systemd/'
        perVer = '[\d]+[\d]'
        findNew()
        lfsLink = 'http://www.linuxfromscratch.org/lfs/downloads/%s.%s-systemd/LFS-BOOK-%s.%s-systemd.pdf' % (g.vers[0], g.vers[1], g.vers[0], g.vers[1])

        g.uriDict = {'downl_mint' : mintLink, 'downl_ubuntu' : ubuntuLink, 'downl_solus' : solusLink, 'downl_zorin' : zorinosLink, 'downl_deepin' : deepinLink, 'downl_steamos' : steamosLink, 'downl_deb' : debianLink, 'downl_fedora' : fedoraLink, 'downl_suse' : opensuseLink, 'downl_gentoo' : gentooLink, 'downl_arch' : archLink, 'downl_lfs' : lfsLink}
        print('Updated linklist!!')
        print("Getting size...")
        for i in range(g.dlistLen):                                                 # dlistlen is the length of dlist
            cBut = self.builder.get_object(g.dlist[i])                              # dlist is distro list (contains all distro names), cbut is current button
            print("rundownl")
            print(g.dlist[i])
            g.url = g.uriDict[g.dlist[i]]                                           # get url from dictionary
            g.u = urlopen(g.url)
            time.sleep(0.1)
            g.file_size = int(g.u.getheader('Content-Length'))
            print("runned")
            g.file_size = Decimal(int(g.file_size) / 1024 / 1024)                   # convert to MB
            GLib.idle_add(cBut.set_label, "Download (%s MB)" % round(g.file_size,1)) # set download label
            g.cache.append(round(g.file_size,1))                                    # store value in cache

    def on_db_but_clicked(self, button):
        distro_box = self.builder.get_object('distro_box')
        if not g.cache:                                                             # if not fetched already
            g.state = False                                                         # disable
            self.toggle(fn)                                                         #         all buttons
            g.tS = futures.ThreadPoolExecutor(max_workers=2)                        # init non-normal thread (getting sizes)
            f = g.tS.submit(self.getSize)
            g.state = True                                                          # toggle everything back when ready
            f.add_done_callback(self.toggle)
        else:                                                                       # if loaded
            for i in range(g.dlistLen):
                cBut = self.builder.get_object(g.dlist[i])
                cBut.set_label("Download (%s MB)" % g.cache[i])                     # load from cache
        g.stack.set_visible_child(distro_box)

    def on_about_but_clicked(self, button):                                         # on about ...
        scroll_about = self.builder.get_object('scroll_about')
        g.stack.set_visible_child(scroll_about)

    def OnCheck(self):                                                              # check if program is installed or not
        if 'Touchpad' in g.name:
            vane = os.path.exists("/usr/share/applications/org.cunidev.gestures.desktop")
            print(vane)
            if vane:
                g.status = 'Remove'
            else:
                g.status = 'Install'
        elif 'TeamViewer' in g.name:
            vane = os.path.exists("/opt/teamviewer")
            print(vane)
            if vane:
                g.status = 'Remove'
            else:
                g.status = 'Install'
        else:
            if g.name in g.insList:
                print('Found %s' % g.name)
                g.status = 'Remove'
            else:
                print('Not found %s' % g.name)
                g.status = 'Install'

    def home_clicked (self, button): # back button
        scroll_home = self.builder.get_object('scroll_home')
        g.stack.set_visible_child(scroll_home)

    def on_page(self, button):                                      # general descrition page
        g.text = self.builder.get_object('page_txt')
        page = self.builder.get_object('scroll_desc')
        back_button = self.builder.get_object('back_button')        # back but not to home
        page_box = self.builder.get_object('page_box')
        rew_link = self.builder.get_object('rew_link')              # hide rew link and web link when not in distro boutique
        rew_link.hide()
        web_link = self.builder.get_object('web_link')
        web_link.hide()
        if g.bp == "Distro Boutique":                               # if yes, show. g.bp indicates the current page, regarding its meaning I have no idea
            rew_link.show()
            web_link.show()
        g.text.set_text(g.label)
        back_button.set_label(g.bp)
        g.stack.set_visible_child(page)

    def on_back_button_clicked (self, button):                      # when going back but not to home
        if g.spinning:                                              # if installation in progress
            x, y = g.window.get_position()
            sx, sy = g.window.get_size()
            dialogWindow = Gtk.MessageDialog(None,
                                  Gtk.DialogFlags.MODAL | Gtk.DialogFlags.DESTROY_WITH_PARENT,
                                  Gtk.MessageType.QUESTION,
                                  Gtk.ButtonsType.YES_NO,
                                  "Do you really would like to abort now? It could end up with a broken program. If you decide to abort, then it is recommended to remove %s manually." % g.CA)
            dialogWindow.set_title("Attention!")
            dsx, dsy = dialogWindow.get_size()
            dialogWindow.move(x+((sx-dsx)/2), y+((sy-dsy)/2))
            dx, dy = dialogWindow.get_position()
            dialogWindow.show_all()
            res = dialogWindow.run()
            if res == Gtk.ResponseType.YES:
                print('OK pressed')
                dialogWindow.destroy()
                print('Spinning')
                if g.distro == 'Ubuntu' or g.distro == 'Debian':
                    g.asr = 'killall apt apt-get ; dpkg --configure -a ; apt autoremove -y ; apt autoclean -y'
                elif g.distro == 'Arch':
                    g.asr = 'rm /var/lib/pacman/db.lck ; killal pacman ; pacman -R $(pacman -Qdtq)'
                else:
                    print('ERROR IN DIST AB')
                app.asroot()
            elif res == Gtk.ResponseType.NO:
                print('No pressed')
                dialogWindow.destroy()
                return True
        elif g.spinning == False:
            print('Standing')
        if g.bp == "App Spotlight": # go back to app spotlight or distro boutique
            self.button_clicked(button)
        elif g.bp == "Distro Boutique":
            distro_box = self.builder.get_object('distro_box')
            g.stack.set_visible_child(distro_box)
        else:
            print('ERROR')

    def on_rew_link_clicked(self, button):
        webbrowser.open_new(g.rew)

    def on_web_link_clicked(self, button):
        webbrowser.open_new(g.web)

### What to do on button clicks

    def lilFunc (self):
        if g.statDict[g.name] == 'Install':
            g.CA = g.name
            if g.name == 'Touchpad Gestures':
                x, y = g.window.get_position()
                sx, sy = g.window.get_size()
                dialogWindow = Gtk.MessageDialog(None, # some prompts
                                      Gtk.DialogFlags.MODAL | Gtk.DialogFlags.DESTROY_WITH_PARENT,
                                      Gtk.MessageType.WARNING,
                                      Gtk.ButtonsType.OK,
                                      g.lehete)

                dialogWindow.set_title("Attention!")
                dsx, dsy = dialogWindow.get_size()
                dialogWindow.move(x+((sx-dsx)/2), y+((sy-dsy)/2))
                dialogWindow.show_all()
                res = dialogWindow.run()
                dialogWindow.destroy()
                print('OK pressed')
                dialogWindow.destroy()
            print(g.CA)
            self.OnNeed()
        elif g.statDict[g.name] == 'Remove':
            g.CA = g.name+'R'
            print(g.CA)
            self.OnNeed()                               # begin operation

    def on_opera_but_clicked(self, button):
        g.name = 'Opera'
        self.lilFunc()

    def on_chrome_but_clicked(self, button):
        g.name = 'Chrome'
        self.lilFunc()

    def on_web_but_clicked(self, button):
        g.name = 'Web'
        self.lilFunc()

    def on_firefox_but_clicked(self, button):
        g.name = 'Firefox'
        self.lilFunc()

    def on_vivaldi_but_clicked(self, button):
        g.name = 'Vivaldi'
        self.lilFunc()

    def on_edge_but_clicked(self, button):
        g.name = 'Edge'

    def on_woffice_but_clicked(self, button):
        g.name = 'WPS Office'
        self.lilFunc()

    def on_loffice_but_clicked(self, button):
        g.name = 'Libreoffice'
        self.lilFunc()

    def on_ooffice_but_clicked(self, button):
        g.name = 'Only Office'
        self.lilFunc()

    def on_msoffice_but_clicked(self, button):
        webbrowser.open_new("https://office.com")

    def on_goffice_but_clicked(self, button):
        webbrowser.open_new("https://docs.google.com")

    def on_foffice_but_clicked(self, button):
        g.name = 'Free Office'
        self.lilFunc()

    def on_gedit_but_clicked(self, button):
        g.name = 'Gedit'
        self.lilFunc()

    def on_gnu_but_clicked(self, button):
        g.name = 'GNU Emacs'
        self.lilFunc()

    def on_vscode_but_clicked(self, button):
        g.name = 'Visual Studio Code'
        self.lilFunc()

    def on_atom_but_clicked(self, button):
        g.name = 'Atom Editor'
        self.lilFunc()

    def on_stedit_but_clicked(self, button):
        g.name = 'Sublime Text Editor'
        self.lilFunc()

    def on_geany_but_clicked(self, button):
        g.name = 'Geany'
        self.lilFunc()

    def on_skype_but_clicked(self, button):
        g.name = 'Skype'
        self.lilFunc()

    def on_discord_but_clicked(self, button):
        g.name = 'Discord'
        self.lilFunc()

    def on_telegram_but_clicked(self, button):
        g.name = 'Telegram'
        self.lilFunc()

    def on_signal_but_clicked(self, button):
        g.name = 'Signal'
        self.lilFunc()

    def on_hex_but_clicked(self, button):
        g.name = 'HexChat'
        self.lilFunc()

    def on_franz_but_clicked(self, button):
        g.name = 'Franz'
        self.lilFunc()

    def on_0ad_but_clicked(self, button):
        g.name = '0 A.D.'
        self.lilFunc()

    def on_skart_but_clicked(self, button):
        g.name = 'SuperTuxKart'
        self.lilFunc()

    def on_tux_but_clicked(self, button):
        g.name = 'SuperTux'
        self.lilFunc()

    def on_lutris_but_clicked(self, button):
        g.name = 'Lutris'
        self.lilFunc()

    def on_barr_but_clicked(self, button):
        g.name = 'Barrier by debauchee'
        self.lilFunc()

    def on_pol_but_clicked(self, button):
        g.name = 'Play On Linux'
        self.lilFunc()

    def on_steam_but_clicked(self, button):
        g.name = 'Steam'
        self.lilFunc()

    def on_mc_but_clicked(self, button):
        g.name = 'Minecraft'
        self.lilFunc()

    def on_pops_but_clicked(self, button):
        g.name = 'Popsicle'
        self.lilFunc()

    def on_woe_but_clicked(self, button):
        g.name = 'WoeUSB'
        self.lilFunc()

    def on_wine_but_clicked(self, button):
        g.name = 'Wine'
        self.lilFunc()

    def on_vbox_but_clicked(self, button):
        g.name = 'Virtualbox'
        self.lilFunc()

    def on_gparted_but_clicked(self, button):
        g.name = 'GParted'
        self.lilFunc()

    def on_gest_but_clicked(self, button):
        g.name = 'Touchpad Gestures'
        self.lilFunc()

    def on_auda_but_clicked(self, button):
        g.name = 'Audacity'
        self.lilFunc()

    def on_deja_but_clicked(self, button):
        g.name = 'Déja-Dup'
        self.lilFunc()

    def on_tims_but_clicked(self, button):
        g.name = 'Timeshift'
        self.lilFunc()

    def on_tw_but_clicked(self, button):
        g.name = 'TeamViewer'
        self.lilFunc()

    def on_box_but_clicked(self, button):
        g.name = 'Gnome Boxes'
        self.lilFunc()

#### End of button clicks

#### Descriptions

    def on_opera_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """Opera

Fast, secure, easy-to-use browser
Try the Opera browser - now with a built-in ad blocker, battery saver and free VPN.

Opera is one of the most underrated browsers out yet. However, it's one of the bests, if not the best.
It's based on Chromium, so it's basicly Chrome on steroids. It's faster, lighter, more secure and more productive.
The Opera Sync is the best on the market, and the sidebar with integrated messengers is really productive.

Give the web browser of the future a try!
        """
        self.on_page(button)

    def on_chrome_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """Google Chrome

Google Chrome is the most popular browser nowadays for Android and PC also.
It's reliable, stable and fast, however, you know, Google doesn't respect your privacy sometimes...

But at the end of the day, Chrome is still one of the best choices
if you'd like to use a well-known, cross platform browser.
        """
        self.on_page(button)

    def on_skart_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """SuperTuxKart

Karts. Nitro. Action! SuperTuxKart is a 3D open-source arcade racer with a variety characters, tracks, and modes to play. Our aim is to create a game that is more fun than realistic, and provide an enjoyable experience for all ages.

In Story mode, you must face the evil Nolok, and defeat him in order to make the Mascot Kingdom safe once again! You can race by yourself against the computer, compete in several Grand Prix cups, or try to beat your fastest time in Time Trial mode. You can also race or battle with up to eight friends on a single computer, play on a local network or play online with other players all over the world.
        """
        self.on_page(button)

    def on_web_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """Gnome Web

Gnome Web is a simple and lightweight yet powerful browser.
It only supports Linux, so it isn't the best for you
if you would like to have your settings and pages synced on the go.
It is the best for old hardware and laptops (bacause it is very battery friendly).
It could be a good choice if you are coming from mac, because its user interface is similar to Safari.

Note: It also the only browser that supports touchpad gestures for Linux out of the box.
        """
        self.on_page(button)

    def on_firefox_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """Mozilla Firefox

Meet Firefox Quantum. Fast for good.

Features:

    - A powerful, new engine that’s built for rapidfire performance.
    - Better, faster page loading that uses less computer memory.
    - Gorgeous design and smart features for intelligent browsing.

Firefox is made by Mozilla, the non-profit champions of a healthy internet.
Mozilla also tackles issues like privacy, misinformation and trolling
by investing in fellowships, campaigns and new technologies designed to make
the internet healthier.
        """
        self.on_page(button)

    def on_vivaldi_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """Vivaldi

A browser should adapt to you, not the other way around.

We believe that many people want to customize
and tweak every square inch of their browser to make it their own.
They want access to advanced tools without sacrificing performance or security.
And they want to be heard.

"We’re building a browser that is powerful, personal and flexible.
A browser that adapts to you, not the other way around."

This is the philosophy of the Vivaldi team. The CEO is the ex-founder of Opera.

I recommend you to try this browser out. (Android version is also on the way)
        """
        self.on_page(button)

    def on_edge_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """Microsoft Edge

Microsoft Edge was originally announced as a replacement for Internet Explorer,
which had been the default browser in Windows operating systems since 1995.
However, both Edge and Internet Explorer are included with Windows 10,
with Edge simply acting as the default browser.

Microsoft Edge requires at least 1 gigabyte of memory.
The browser offers better security and better organization than Internet Explorer
as well as a reading list which is similar to (but separate from) bookmarks.

Now Chromium based Edge browser is on the way,
and hopefully it is arriving to Linux between 2020 and 2021.
        """
        self.on_page(button)

    def on_woffice_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """WPS Office

WPS Office is the complete free office suite, integrates all office word processor functions: Word, Presentation, Spreadsheet, PDF, and fully compatible with Microsoft Word, Excel, PowerPoint, Google Doc and Adobe PDF format. If you need to use advanced features(e.g.: PDF2WORD, more cloud storage space), you can subscribe Preminum.

The aim of WPS Office is to provide you one-stop working solution since 1989. Various of office tools and unique and intuitive UI design ensures you enjoy the best office experience. You could easy to do all office documents processing on-the-go on Windows PC. WPS Office suite allows you can create, view, edit and share office documents.

It's the best free MS Office alternative for Linux in my opinion.
        """
        self.on_page(button)

    def on_loffice_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """Libreoffice

LibreOffice is developed by users who, just like you, believe in the principles of Free Software and in sharing their work with the world in non-restrictive ways. At the core of these principles are the four essential freedoms and the tenets of The Document Foundation's Next Decade Manifesto.

We believe that users should have the freedom to run, copy, distribute, study, change and improve the software that we distribute. While we do offer no-cost downloads of the LibreOffice suite of programs, Free Software is first and foremost a matter of liberty, not price. We campaign for these freedoms because we believe that everyone deserves them.
        """
        self.on_page(button)

    def on_ooffice_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """Only Office

ONLYOFFICE Desktop Editors is a free open source office suite that combines text, spreadsheet and presentation editors allowing to create, view and edit documents stored on your Windows/Linux PC or Mac without an Internet connection. It is fully compatible with Office Open XML formats: .docx, .xlsx, .pptx.

The ONLYOFFICE desktop suite pack allows extending the functionality with the pre-installed plugins, e.g. you can insert special symbols and ClipArts, edit pictures, translate text, send documents as mail attachments right from the editors, etc.

The suite also provides quick access to broad collaborative capabilities. Users are able to switch to the online mode by connecting to the cloud (ONLYOFFICE cloud, Nextcloud, ownCloud) and collaborate on documents with the team in real time.
        """
        self.on_page(button)

    def on_msoffice_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """Microsoft Office Online

Microsoft Office Online can serve as a free Microsoft Office alternative, as it lets you edit and share files created in a word processor, spreadsheet, and presentation program, as well access MS Outlook and OneNote.

Everything done through Microsoft Office Online is performed through a web browser and saved online so you can access the files from anywhere.
        """
        self.on_page(button)

    def on_goffice_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """Google G Suite

G Suite—formerly known as Google Apps for Work—is a Software as a Service (SaaS) product that groups all the cloud-based productivity and collaboration tools developed by Google for businesses, institutes, and nonprofits. Included with every subscription you get access to custom Gmail addresses, Docs, Sheets, Slides, Calendar, Drive, Sites, and so much more.
        """
        self.on_page(button)

    def on_foffice_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """Softmaker Free Office

SoftMaker Office is an office suite developed since 1987 by the German company SoftMaker Software GmbH, Nuremberg. SoftMaker is available as a one-time purchase option, in Standard and Professional editions, as well as a subscription-based version known as SoftMaker Office NX (available as Home and Universal editions).

A freeware version is released as well, under the name of SoftMaker FreeOffice. FreeOffice supersedes SoftMaker Office 2006 and 2008, which were released as freeware after originally being available for purchase.
        """
        self.on_page(button)

    def on_gedit_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """Gedit

It is is the default text editor of the GNOME desktop environment and part of the GNOME Core Applications. Designed as a general-purpose text editor, gedit emphasizes simplicity and ease of use, with a clean and simple GUI, according to the philosophy of the GNOME project. It includes tools for editing source code and structured text such as markup languages.

It is free and open-source software subject to the requirements of the GNU General Public License version 2 or later.

gedit is also available for Mac OS X and Microsoft Windows.

Personally, I use gedit with extensions for programming, HSuite is also written in gedit.
        """
        self.on_page(button)

    def on_gnu_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """GNU Emacs

EMACS (Editor MACroS) is a family of text editors that are characterized by their extensibility. The manual for the most widely used variant, GNU Emacs, describes it as "the extensible, customizable, self-documenting, real-time display editor". Development of the first Emacs began in the mid-1970s, and work on its direct descendant, GNU Emacs, continues actively as of 2019.

Emacs has over 10,000 built-in commands and its user interface allows the user to combine these commands into macros to automate work. Implementations of Emacs typically feature a dialect of the Lisp programming language that provides a deep extension capability, allowing users and developers to write new commands and applications for the editor. Extensions have been written to manage email, files, outlines, and RSS feeds, as well as clones of ELIZA, Pong, Conway's Life, Snake and Tetris.
        """
        self.on_page(button)

    def on_vscode_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """Visual Studio Code

Visual Studio Code is a source-code editor developed by Microsoft for Windows, Linux and macOS. It includes support for debugging, embedded Git control and GitHub, syntax highlighting, intelligent code completion, snippets, and code refactoring. It is highly customizable, allowing users to change the theme, keyboard shortcuts, preferences, and install extensions that add additional functionality. The source code is free and open source and released under the permissive MIT License. The compiled binaries are freeware and free for private or commercial use.
        """
        self.on_page(button)

    def on_atom_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """Atom Editor

Atom is a free and open-source text and source code editor for macOS, Linux, and Microsoft Windows with support for plug-ins written in Node.js, and embedded Git Control, developed by GitHub. Atom is a desktop application built using web technologies. Most of the extending packages have free software licenses and are community-built and maintained. Atom is based on Electron (formerly known as Atom Shell), a framework that enables cross-platform desktop applications using Chromium and Node.js. It is written in CoffeeScript and Less.
        """
        self.on_page(button)

    def on_stedit_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """Sublime Text Editor

Sublime Text is a proprietary cross-platform source code editor with a Python application programming interface (API). It natively supports many programming languages and markup languages, and functions can be added by users with plugins, typically community-built and maintained under free-software licenses.
        """
        self.on_page(button)

    def on_geany_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """Geany

Geany is a lightweight GUI text editor using Scintilla and GTK+, including basic IDE features. It is designed to have short load times, with limited dependency on separate packages or external libraries on Linux. It has been ported to a wide range of operating systems, such as BSD, Linux, macOS, Solaris and Windows. The Windows port lacks an embedded terminal window; also missing from the Windows version are the external development tools present under Unix, unless installed separately by the user. Among the supported programming languages and markup languages are C, C++, C#, Java, JavaScript, PHP, HTML, LaTeX, CSS, Python, Perl, Ruby, Pascal, Haskell, Erlang, Vala and many others.
        """
        self.on_page(button)

    def on_skype_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """Skype

Skype is for connecting with the people that matter most in your life and work. It's built for both one-on-one and group conversations and works wherever you are – via mobile, PC, Xbox and Alexa. Skype messaging and HD voice and video calling will help you share experiences and get things done with others.

With Skype, you can have meetings and create great things with your workgroup, share a story or celebrate a birthday with friends and family, and learn a new skill or hobby with a teacher. It’s free to use Skype – to send messages and have audio and video calls with groups of up to 50 people!

If you pay a little, you can do more things, in more ways, with more people – like call phones or SMS messages. You can pay as you go or buy a subscription, whatever works for you.

Try Skype out today and start adding your friends, family and colleagues. They won’t be hard to find; hundreds of millions of people are already using Skype to do all sorts of things together.
        """
        self.on_page(button)

    def on_discord_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """Discord

Discord is a proprietary freeware VoIP application and digital distribution platform—designed initially for the video gaming community—that specializes in text, image, video and audio communication between users in a chat channel. Discord runs on Windows, macOS, Android, iOS, Linux, and in web browsers. As of 21 July 2019, there are over 250 million unique users of the software.
        """
        self.on_page(button)

    def on_telegram_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """Telegram

Telegram is a cloud-based instant messaging and voice over IP service. Telegram client apps are available for Android, iOS, Windows Phone, Windows NT, macOS and Linux. Users can send messages and exchange photos, videos, stickers, audio and files of any type.

Telegram's client-side code is open-source software but the source code for recent versions is not always immediately published, whereas its server-side code is closed-source and proprietary. The service also provides APIs to independent developers. In March 2018, Telegram stated that it had 200 million monthly active users.
        """
        self.on_page(button)

    def on_signal_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """Signal

Signal is a cross-platform encrypted messaging service developed by the Signal Foundation and Signal Messenger LLC. It uses the Internet to send one-to-one and group messages, which can include files, voice notes, images and videos. Its mobile apps can also make one-to-one voice and video calls, and the Android version can optionally function as an SMS app.

Signal uses standard cellular telephone numbers as identifiers and uses end-to-end encryption to secure all communications to other Signal users. The apps include mechanisms by which users can independently verify the identity of their contacts and the integrity of the data channel.

All Signal software are free and open-source. The clients are published under the GPLv3 license, while the server code is published under the AGPLv3 license. The non-profit Signal Foundation was launched in February 2018 with an initial funding of $50 million.
        """
        self.on_page(button)

    def on_hex_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """HexChat

HexChat is an Internet Relay Chat client (IRC), forked from XChat. It has a choice of a tabbed document interface or tree interface, support for multiple servers, and numerous configuration options. Both command-line and graphical versions were available.
        """
        self.on_page(button)

    def on_franz_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """Franz

Franz Messaging app is one of my top best messaging apps for linux platform. It’s a free, simple to use chat app that combines all the various chat & messaging services features into one promising application.

Currently it supports
    ~ Slack
    ~ WhatsApp
    ~ WeChat
    ~ HipChat
    ~ Facebook Messenger
    ~ Telegram
    ~ Google Hangouts
    ~ GroupMe
    ~ Skype
    ~ Gmail
    ~ Google Messages
    ~ Google Calendar
    ~ Discord
    ~ Linkedin
    ~ Outlook
    ~ and many more.

At the moment, you are only able to install and run the app on the following operating systems “Mac, Windows & Linux”.

If you have multiple business and private accounts, then Franz Messaging app will allow you to add all your accounts so its easy to manage them from a single dashboard. What this means is, you could add / manage five different Facebook Messenger accounts all at once.
        """
        self.on_page(button)

    def on_0ad_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """0 A.D.

The best strategic game for Linux (in my opinion)

0 A.D. (pronounced "zero ey-dee") is a free, open-source, cross-platform real-time strategy (RTS) game of ancient warfare. In short, it is a historically-based war/economy game that allows players to relive or rewrite the history of Western civilizations, focusing on the years between 500 B.C. and 500 A.D. The project is highly ambitious, involving state-of-the-art 3D graphics, detailed artwork, sound, and a flexible and powerful custom-built game engine.

It also supports online and LAN multiplayer, custom map creation, adding mods to the game and if you would like to take part in the development you can do that also.
        """
        self.on_page(button)

    def on_tux_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """SuperTux

The game, that every hardcore Linux users should play out.

SuperTux is a free and open-source two-dimensional platform video game published under the GNU General Public License (GPL).[1] The game was inspired by Nintendo's Super Mario Bros. series; instead of Mario, the hero in the game is Tux, the official mascot of the Linux kernel.
        """
        self.on_page(button)

    def on_lutris_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """Lutris

Lutris is an Open Source gaming platform for Linux. It installs and launches games so you can start playing without the hassle of setting up your games. Get your games from GOG, Steam, Battle.net, Origin, Uplay and many other sources running on any Linux powered gaming machine.
        """
        self.on_page(button)

    def on_barr_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """Barrier by debauchee

Barrier is KVM software forked from Symless's synergy 1.9 codebase. Synergy was a commercialized reimplementation of the original CosmoSynergy written by Chris Schoeneman.

Whereas synergy has moved beyond its goals from the 1.x era, Barrier aims to maintain that simplicity. Barrier will let you use your keyboard and mouse from machine A to control machine B (or more). It's that simple.
        """
        self.on_page(button)

    def on_pol_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """Play On Linux

One of the best ways to play Windows games on Linux.

PlayOnLinux is a piece of software which allows you to easily install and use numerous games and apps designed to run with Microsoft® Windows®.
Few games are compatible with GNU/Linux at the moment and it certainly is a factor preventing the migration to this system. PlayOnLinux brings a cost-free, accessible and efficient solution to this problem.
        """
        self.on_page(button)

    def on_steam_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """Steam

The overall best when it comes to gaming on every platform.

Steam is the ultimate game platform, also for Linux. It offers Steam Play feature. Steam Play allows you to purchase your games once and play anywhere. Whether you have purchased your Steam Play enabled game on a Mac or PC (both Windows and Linux), you will be able to play on the other platform free of charge. So a lots of Windows only games can be played on Linux without problems.
        """
        self.on_page(button)

    def on_mc_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """Minecraft

Everyone knows this game... But if you don't, here's a short descriptio.

Minecraft is a sandbox video game created by Swedish game developer Markus Persson and released by Mojang in 2011. The game allows players to build with a variety of different blocks in a 3D procedurally generated world, requiring creativity from players. Other activities in the game include exploration, resource gathering, crafting, and combat. Multiple game modes that change gameplay are available, including—but not limited to—a survival mode, in which players must acquire resources to build the world and maintain health, and a creative mode, where players have unlimited resources to build with. The Java Edition of the game allows players to modify the game with mods to create new gameplay mechanics, items, textures and assets. In September 2014, Microsoft announced a deal to buy Mojang and the Minecraft intellectual property for US$2.5 billion, with the acquisition completed two months later.'
        """
        self.on_page(button)

    def on_pops_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """Popsicle

Popsicle is a lightweight open source USB image writer tool written in Rust by System76, the company behind a lots of outsandingly great Linux Desktops/Laptops and the heavy customized Ubuntu based distro, Pop!_OS.
        """
        self.on_page(button)

    def on_woe_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """WoeUSB

Write Windows ISO to removable storage.

WoeUSB is Linux tool for creating Windows USB stick installer from a real Windows DVD or an image. It contains two programs, woeusb and woeusbgui. It’s a fork of Congelli501’s WinUSB software which received its last update in 2012.

woeusb is a CLI utility that does the actual creation of a bootable Windows installation USB storage device from either an existing Windows installation or a disk image. woeusbgui (as the name suggests,) is a woeusb GUI wrapper based on WxWidgets.
        """
        self.on_page(button)

    def on_wine_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """Wine

Run Windows programs on Linux

Wine (originally an acronym for "Wine Is Not an Emulator") is a compatibility layer capable of running Windows applications on several POSIX-compliant operating systems, such as Linux, macOS, & BSD. Instead of simulating internal Windows logic like a virtual machine or emulator, Wine translates Windows API calls into POSIX calls on-the-fly, eliminating the performance and memory penalties of other methods and allowing you to cleanly integrate Windows applications into your desktop.
        """
        self.on_page(button)

    def on_vbox_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """Oracle Virtualbox

Run virtual machines on your PC

A VirtualBox or VB is a software virtualization package that installs on an operating system as an application. VirtualBox allows additional operating systems to be installed on it, as a Guest OS, and run in a virtual environment. In 2010, VirtualBox was the most popular virtualization software application. Supported operating systems include Windows XP, Windows Vista, Windows 7, macOS X, Linux, Solaris, and OpenSolaris.

VirtualBox was originally developed by Innotek GmbH and released in 2007 as an open-source software package. The company was later purchased by Sun Microsystems. Oracle Corporation now develops the software package and titles it Oracle VM VirtualBox.
        """
        self.on_page(button)

    def on_gparted_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """GParted

The ultimate partition manager for Linux

The gparted application is the GNOME partition editor for creating, reorganizing, and deleting disk partitions.
A disk device can be subdivided into one or more partitions. The gparted application enables you to change the partition organization on a disk device while preserving the contents of the partition.

With gparted you can accomplish the following tasks:
- Create a partition table on a disk device.
- Enable and disable partition flags such as boot and hidden.
- Perform actions with partitions such as create, delete, resize, move, check, label, copy, and paste.

More documentation can be found in the application help manual, and online at:
http://gparted.org
        """
        self.on_page(button)

    def on_gest_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """Touchpad Gestures

The app is called ‘Gestures’ and is described by its developer as being a “minimal Gtk+ GUI app for libinput-gestures”.

Windows and macOS both come with a variety of useful touchpad gestures pre-configured out of the box, and offer easy-to-access settings for adjusting or changing gesture behaviour to your liking.

Alas Ubuntu, like many Linux distributions, is a little lacking in this regard. Only a handful of basic gestures for scrolling and right-click available out of the box on Ubuntu 18.04 LTS, for instance.

But by using the “Gestures” app you can quickly effect a set of custom trackpad gestures that are on par with other operating systems, and in some cases, far more useful!
        """
        self.on_page(button)

    def on_auda_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """Audacity

The free and open-source audio tool

Audacity is the name of a popular open source multilingual audio editor and recorder software that is used to record and edit sounds. It is free and works on Windows, Mac OS X, GNU/Linux and other operating systems.

Audacity can be used to perform a number of audio editing and recording tasks such as making ringtones, mixing stero tracks, transferring tapes and records to computer or CD, splitting recordings into separate tracks and more. The Audacity Wiki provides indepth tutorials on how to do these types of tasks in Audacity. Vendors can also freely bundle Audacity with their products or sell or distribute copies of Audacity under the GNU General Public License (GPL).
        """
        self.on_page(button)

    def on_deja_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """Déja-Dup

One of the most powerful backup solutions for Linux

Deja-dup: is a simple yet powerful backup tool included with Ubuntu. It offers the power of resync with incremental backups, encryption, scheduling, and support for remote services. With Deja-dup, you can quickly revert files to previous versions or restore missing files from a file manager window.

You can do full system backups, Home folder backup or even settings backup in Ubuntu. You can backup to your GDrive storage also.
        """
        self.on_page(button)

    def on_tims_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """Timeshift

The best backup solution (in my opinion) for Linux

Timeshift for Linux is an application that provides functionality similar to the System Restore feature in Windows and the Time Machine tool in Mac OS. Timeshift protects your system by taking incremental snapshots of the file system at regular intervals. These snapshots can be restored at a later date to undo all changes to the system.

In RSYNC mode, snapshots are taken using rsync and hard-links. Common files are shared between snapshots which saves disk space. Each snapshot is a full system backup that can be browsed with a file manager.

In BTRFS mode, snapshots are taken using the in-built features of the BTRFS filesystem. BTRFS snapshots are supported only on BTRFS systems having an Ubuntu-type subvolume layout (with @ and @home subvolumes).

Timeshift is similar to applications like rsnapshot, BackInTime and TimeVault but with different goals. It is designed to protect only system files and settings. User files such as documents, pictures and music are excluded. This ensures that your files remains unchanged when you restore your system to an earlier date.
        """
        self.on_page(button)

    def on_tw_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """TeamViewer

TeamViewer (TeamViewer 6) is a popular piece of  software used for Internet-based remote access and support. TeamViewer software can connect to any PC or server, so you can remote control your partner's PC as if you were sitting right in front of it. For the remote session to work the partner has to start a small application, which does not require installation or administrative rights.

TeamViewer 6 is the latest version of the software and works with Windows, Mac, Linux operating systems and Mobile (Android, Apple iPad, Apple iPhone) devices. TeamViewer 6 is free for all non-commercial users.
        """
        self.on_page(button)

    def on_box_clicked (self, button):
        g.bp = "App Spotlight"
        g.label = """Gnome Boxes

The simpliest way to run virtual machines as a normal, non-expert user.

GNOME Boxes is an application of the GNOME Desktop Environment, used to access remote or virtual systems. Boxes uses the QEMU, KVM, and libvirt virtualisation technologies.

GNOME Boxes requires the CPU to support some kind of Hardware-assisted virtualization (Intel VT-x, for example).
        """
        self.on_page(button)

    def on_mint_clicked (self, button):
        g.bp = "Distro Boutique"
        g.web = "https://www.linuxmint.com"
        g.rew = "https://youtu.be/fm7d2mM0cqQ"
        g.label = """Linux Mint

Linux Mint was my first distro, and now I am a hardcore Linux user, so it was really beginner friendly :)
First of all, the DE (Cinnamon) looks nearly exactly like Windows, so it is easy to get used to it. It is also pretty lightweight and stable for the everydays. It also supports deskletts and plugins. It has all the codecs and drivers that you will need out of the box, and it has a driver manager also. Regarding the OS itself, it is based on Ubuntu LTS version so it is compatible with everything and it is also reliable. The community is excellent! If you have some questions or problems, just ask, and probably within a few days you will get a solution. I recommend it to every beginner.
        """
        self.on_page(button)

    def on_ubuntu_clicked (self, button):
        g.bp = "Distro Boutique"
        g.web = "https://ubuntu.com"
        g.rew = "https://youtu.be/lzFcjW70xZ4"
        g.label = """Ubuntu

Ubuntu is one of the oldest and most popular consumer Linux distos. Because of this, the support is outstanding. It has a lots of flavours (Kubuntu with KDE, Xubuntu with XFCE, Lubuntu with LXQT and so on...), the main version uses GNOME as its DE with some tweaks. It is stable and up to date enough for daily usage, and it has lots of programs in its repos. If you still can not find something there are lots of PPAs out there. It runs on nearly everything without problems, and the installation process is extremely easy and straightforward.
        """
        self.on_page(button)

    def on_solus_clicked (self, button):
        g.bp = "Distro Boutique"
        g.web = "https://getsol.us/home/"
        g.rew = "https://youtu.be/ZJE28tnPkRE"
        g.label = """Solus Linux

Solus is a pretty fresh Linux distro built from scratch by a small (but growing) group of talented developers and users. The story behind the project is also very special. The community is rather small, but very helpful. The OS is extremely stable and well optimized, and its own DE, Budgie is also very modern and useful. The only drawback is that because of it is based on nothing, not every package is avilable. However, probablyy you will find everything right in the official repos without the need of any 3rd party repo. If not, then you can request new packages on the official site. I recommend it for those who are not afraid of a littlebit of learning to make everything work.
        """
        self.on_page(button)

    def on_deepin_clicked (self, button):
        g.bp = "Distro Boutique"
        g.web = "https://www.deepin.org/en/"
        g.rew = "https://youtu.be/Uq_IbFNueTE"
        g.label = """Deepin Linux

Deepin is the beautiful, minimalist, well supported, regularly updated and perfectly optimized distro from China with lots of great features and an interesting name. It is based on Debian (Unstable), it has a rolling release update method and a lots of own programs (DDE, DWM, Deepin Boot maker, Deepin Installer/Music/Movie/Backup/Clone/Recovery/Print/Connect and so on...). If you would like to use something that works out of the box (in nearly every case), and you do not want to learn anything about computers and Linux, then this is the perfect choice for you.
        """
        self.on_page(button)

    def on_elementary_clicked (self, button):
        g.bp = "Distro Boutique"
        g.web = "https://elementary.io"
        g.rew = "https://youtu.be/9qO_Ft_wRqs"
        g.label = """Elementary OS

Elementary is the macOS of the Linux world. Not because it is expensive or closed source, but because of its simplicity and user friendliness. If you are a beginner, then maybe this is the perfect distro for you. It is nothing special, no bloatware, based on Ubuntu, simple interface, stability and performance. But what else do you need? Regarding its pretty old-school look, trust me, you will get used to it after around a week, and after that you will just love it.
        """
        self.on_page(button)

    def on_zorin_clicked (self, button):
        g.bp = "Distro Boutique"
        g.web = "https://zorinos.com"
        g.rew = "https://youtu.be/30BKvLCEdkQ"
        g.label = """Zorin OS

Personally, I do not like this distro, because of its philosophy. It is a littlebit like Windows in my eyes. At the other hand it is a well constructed and complete OS that works out of the box on a PC, Laptop, or even a Tablet (Intel CPU). It has a simple UI with a start menu, a tablet UI and a Pro version (khm Windows 10...). If it is okay for you, then it is a great Ubuntu based distro.
        """
        self.on_page(button)

    def on_steamos_clicked (self, button):
        g.bp = "Distro Boutique"
        g.web = "https://store.steampowered.com/steamos/"
        g.rew = "https://youtu.be/1saebgKGLuY"
        g.label = """Steam OS

SteamOS is the primary operating system for the Steam Machine gaming platform by Valve Corporation. It is based on Debian Linux. It was released alongside the start of end-user beta testing of Steam Machines in December 2013.
        """
        self.on_page(button)

    def on_deb_clicked (self, button):
        g.bp = "Distro Boutique"
        g.web = "https://www.debian.org"
        g.rew = "https://youtu.be/fUcvL4fbtPo"
        g.label = """Debian

Debian GNU/Linux, is a Linux distribution composed of free and open-source software, developed by the community-supported Debian Project, which was established by Ian Murdock on August 16, 1993. The first version, Debian 0.01, was released on September 15, 1993, and the first stable version, 1.1, was released on June 17, 1996. The Debian Stable branch is the most popular edition for personal computers and servers, and is the basis for many other distributions.
        """
        self.on_page(button)

    def on_fedora_clicked (self, button):
        g.bp = "Distro Boutique"
        g.web = "https://getfedora.org"
        g.rew = "https://youtu.be/DO2acx2W2i8"
        g.label = """Fedora

Fedora Linux is a Linux distribution developed by the independent community-supported Fedora Project, sponsored primarily by Red Hat with substantial support by other companies. Fedora contains software distributed under various free and open-source licenses and aims to be on the leading edge of such technologies. Fedora is the upstream source of the commercial Red Hat Enterprise Linux distribution.
        """
        self.on_page(button)

    def on_opsu_clicked (self, button):
        g.bp = "Distro Boutique"
        g.web = "https://www.opensuse.org"
        g.rew = "https://youtu.be/9oonm2GCCMo"
        g.label = """openSUSE

openSUSE, formerly SUSE Linux and SuSE Linux Professional, is a Linux distribution sponsored by SUSE Linux GmbH and other companies. It is widely used throughout the world. The focus of its development is creating usable open-source tools for software developers and system administrators, while providing a user-friendly desktop and feature-rich server environment.
        """
        self.on_page(button)

    def on_arch_clicked (self, button):
        g.bp = "Distro Boutique"
        g.web = "https://www.archlinux.org"
        g.rew = "https://youtu.be/8RqFL92IEYs"
        g.label = """Arch Linux

Arch Linux is a Linux distribution for computers based on x86-64 architectures. The Arch Linux repositories contain both libre, and nonfree software, and the default Arch Linux kernel contains nonfree proprietary blobs, hence the distribution is not endorsed by the GNU project.

The design approach of the development team follows the KISS principle ("keep it simple, stupid") as the general guideline. It focuses on elegance, code correctness, minimalism, simplicity, and expects the user to be willing to make some effort to understand the system's operation. A package manager written specifically for Arch Linux, pacman, is used to install, remove and update software packages.
        """
        self.on_page(button)

    def on_gentoo_clicked (self, button):
        g.bp = "Distro Boutique"
        g.web = "https://www.gentoo.org"
        g.rew = "https://youtu.be/6D5X78XsLi8"
        g.label = """Gentoo

Gentoo Linux is a Linux distribution built using the Portage package management system. Unlike a binary software distribution, the source code is compiled locally according to the user's preferences and is often optimized for the specific type of computer. Precompiled binaries are available for some larger packages or those with no available source code.
        """
        self.on_page(button)

    def on_lfs_clicked (self, button):
        g.bp = "Distro Boutique"
        g.web = "http://www.linuxfromscratch.org"
        g.rew = "https://youtu.be/qZJzbI6ZJ34"
        g.label = """LFS

Linux From Scratch (LFS) is a project that provides you with step-by-step instructions for building your own custom Linux system, entirely from source code.
        """
        self.on_page(button)

#### End of descriptions
#______________________________________________________________________________________________ END OF GUI ______________________________________________________________________________________#

app = GUI() # variable to call GUI class
Gtk.main() # execute main GTK window
