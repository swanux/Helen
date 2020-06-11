#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#________________________________________________________________________________ BEGINNING OF INIT ____________________________________________________________#

# Version of the program
version = 'HSuite v0.7 | Sinara'
v = ''

### Import modules ###

# Set program root location
import os, subprocess, gettext, locale, gi, re, webbrowser, time, notify2, platform
if os.path.exists('/home/daniel/GitRepos/hsuite'):
    fdir = "/home/daniel/GitRepos/hsuite/DEV_FILES/"
    print(fdir)
    os.chdir(fdir)
    print('Running in development mode.')
else:
    fdir = "/usr/share/hsuite/"
    print(fdir)
    os.chdir(fdir)
    print('Running in production mode.')
# Translation
APP = "hsuite"
WHERE_AM_I = os.path.abspath(os.path.dirname(__file__))
LOCALE_DIR = os.path.join(WHERE_AM_I, 'translations/mo')
locale.setlocale(locale.LC_ALL, locale.getlocale())
locale.bindtextdomain(APP, LOCALE_DIR)
gettext.bindtextdomain(APP, LOCALE_DIR)
gettext.textdomain(APP)
_ = gettext.gettext
# Import GUI modules
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk, GLib, Gdk, GObject, Gio
from github import Github
from cron_descriptor import get_description
from crontab import CronTab
token = '82a201fb7ce03647870@37a6b5f7beb4eeb68f201'
token = token.replace('@', '')
g = Github(token)
# Config
from configparser import ConfigParser
# Running background processes
from threading import Thread
from concurrent import futures
# Using time
from datetime import date
# URL handling
from urllib.request import urlopen
from decimal import Decimal
# Own module for descriptions
import details as d
import htransfer
import apt
from aptdaemon import client, enums
from aptdaemon.gtk3widgets import AptProgressBar

### Declare global variables ###

# Date
today = date.today()
month = today.strftime("%m")
day = today.strftime("%d")
year = today.strftime("%Y")

# Getting the name of the non-root user
user = os.popen("who|awk '{print $1}'r").read()
dplenv = int(os.popen("echo $DISPLAY").read().rstrip().replace(':', ''))
# Edit to only contain the name itself
user = user.rstrip()
user = user.split('\n')[0]

# Used with Distro Boutique
# It's declared because of some functions which ones are called from concurrent future
fn = 'sth'
# The name of the currently in progress download
shDict = {'downl_mint': 'True', 'downl_ubuntu': 'True', 'downl_solus': 'True', 'downl_deepin': 'True', 'downl_steamos': 'True', 'downl_deb': 'True',
          'downl_fedora': 'True', 'downl_suse': 'True', 'downl_gentoo': 'True', 'downl_arch': 'True', 'downl_lfs': 'True', }  # Dictionary for current state of download buttons (clickable or not)
dlist = ['downl_mint', 'downl_ubuntu', 'downl_solus', 'downl_deepin', 'downl_steamos',
         'downl_fedora', 'downl_suse', 'downl_deb', 'downl_arch', 'downl_gentoo', 'downl_lfs']
namDict = {'downl_mint' : 'Linux Mint', 'downl_ubuntu' : 'Ubuntu', 'downl_solus' : 'Solus Linux', 'downl_deepin' : 'Deepin Linux', 'downl_steamos' : 'SteamOS',
         'downl_fedora' : 'Fedora', 'downl_suse' : 'openSUSE', 'downl_deb' : 'Debian', 'downl_arch' : 'Arch', 'downl_gentoo' : 'Gentoo', 'downl_lfs' : 'Linux from Scratch (LFS)'}
# List of distros
dlistLen = len(dlist)                   # The number of distros
toChoseDir = {
    'mint_choser' : {'Cinnamon (Default)' : 'cinnamon', 'MATE' : 'mate', 'XFCE' : 'xfce', 'Debian Edition' : 'lmde'},

    'ubuntu_choser' : {'Gnome (Default)' : 'ubuntu', 'Kubuntu (KDE)' : 'kubuntu', 'Lubuntu (LXQt)' : 'lubuntu', 'Budgie' : 'ubuntu-budgie', 'Kylin' : 'ubuntukylin', 'MATE' : 'ubuntu-mate', 'Studio' : 'ubuntustudio', 'Xubuntu (XFCE)' : 'xubuntu'},

    'solus_chose' : {'Budgie (Default)' : 'Budgie', 'Gnome' : 'GNOME', 'MATE' : 'MATE', 'KDE' : 'Plasma'},

    'deb_chose' : {'Cinnamon' : 'cinnamon', 'Gnome' : 'gnome', 'KDE' : 'kde', 'LXDE' : 'lxde', 'LXQt' : 'lxqt', 'MATE' : 'mate', 'XFCE' : 'xfce'},

    'fedora_chose' : {'Gnome (Default)' : 'default', 'KDE' : 'KDE', 'XFCE' : 'Xfce', 'LXQt' : 'LXQt', 'LXDE' : 'LXDE', 'MATE' : 'MATE_Compiz', 'Cinnamon' : 'Cinnamon', 'SOAS' : 'SoaS'},

    'suse_chose' : {'Tumbeweed (Rolling)' : 'roll', 'Leap (Standard)' : 'stay'}
    }

# Used with App Spotlight
# Check if PKG cache is already in memory or not
appList = ['opera-stable', 'barrier', 'google-chrome-stable', 'epiphany-browser', 'firefox', 'vivaldi-stable', 'wps-office', 'libreoffice', 'onlyoffice-desktopeditors', 'softmaker-freeoffice-2018', 'gedit', 'emacs', 'code', 'atom', 'sublime-text', 'geany', 'skypeforlinux', 'discord', 'telegram-desktop', 'signal-desktop', 'hexchat',
           'franz', '0ad', 'supertux', 'lutris', 'playonlinux', 'steam', 'minecraft-launcher', 'popsicle', 'woeusb', 'winehq-stable', 'virtualbox-6.1', 'gparted', 'fusuma', 'audacity', 'deja-dup', 'timeshift', 'teamviewer', 'gnome-boxes', 'supertuxkart']                                                                        # The list with the debian app names
butDict = {'opera-stable': 'opera', 'barrier': 'barr', 'google-chrome-stable': 'chrome', 'epiphany-browser': 'web', 'firefox': 'firefox', 'vivaldi-stable': 'vivaldi', 'wps-office': 'woffice', 'libreoffice': 'loffice', 'onlyoffice-desktopeditors': 'ooffice', 'softmaker-freeoffice-2018': 'foffice', 'gedit': 'gedit', 'emacs': 'gnu', 'code': 'vscode', 'atom': 'atom', 'sublime-text': 'stedit', 'geany': 'geany', 'skypeforlinux': 'skype', 'discord': 'discord', 'telegram-desktop': 'telegram',
           'signal-desktop': 'signal', 'hexchat': 'hex', 'franz': 'franz', '0ad': 'ad', 'supertux': 'tux', 'lutris': 'lutris', 'playonlinux': 'pol', 'steam': 'steam', 'minecraft-launcher': 'mc', 'popsicle': 'pops', 'woeusb': 'woe', 'winehq-stable': 'wine', 'virtualbox-6.1': 'vbox', 'gparted': 'gparted', 'fusuma': 'gest', 'audacity': 'auda', 'deja-dup': 'deja', 'timeshift': 'tims', 'teamviewer': 'tw', 'gnome-boxes': 'box', 'supertuxkart': 'skart'}                                # Dictionary with the context of debname:humanName
appListLen = len(appList)                           # Number of apps
statDict = {'Opera': '', 'Chrome': '', 'Web': '', 'Firefox': '', 'Vivaldi': '', 'Edge': '', 'WPS Office': '', 'Libreoffice': '', 'Only Office': '', 'Free Office': '', 'Gedit': '', 'GNU Emacs': '', 'VS Code': '', 'Atom Editor': '', 'Sublime Text Editor': '', 'Geany': '', 'Skype': '', 'Discord': '', 'Telegram': '', 'Signal': '', 'HexChat': '', 'Franz': '',
            '0 A.D.': '', 'SuperTuxKart': '', 'SuperTux': '', 'Lutris': '', 'Barrier': '', 'Play On Linux': '', 'Steam': '', 'Minecraft': '', 'Popsicle': '', 'WoeUSB': '', 'Wine': '', 'Virtualbox-6.1': '', 'GParted': '', 'fusuma': '', 'Audacity': '', 'Déja-Dup': '', 'Timeshift': '', 'TeamViewer': '', 'Gnome Boxes': ''}  # store the status (installed or not)
layDict = {'opera-stable': 'Opera', 'google-chrome-stable': 'Chrome', 'epiphany-browser': 'Web', 'firefox': 'Firefox', 'vivaldi-stable': 'Vivaldi', 'dikk': 'Edge', 'wps-office': 'WPS Office', 'libreoffice': 'Libreoffice', 'onlyoffice-desktopeditors': 'Only Office', 'softmaker-freeoffice-2018': 'Free Office', 'gedit': 'Gedit', 'emacs': 'GNU Emacs', 'code': 'VS Code', 'atom': 'Atom Editor', 'sublime-text': 'Sublime Text Editor', 'geany': 'Geany', 'skypeforlinux': 'Skype', 'discord': 'Discord', 'telegram-desktop': 'Telegram', 'signal-desktop': 'Signal', 'hexchat': 'HexChat',
           'franz': 'Franz', '0ad': '0 A.D.', 'supertux': 'SuperTux', 'supertuxkart': 'SuperTuxKart', 'lutris': 'Lutris', 'barrier': 'Barrier', 'playonlinux': 'Play On Linux', 'steam': 'Steam', 'minecraft-launcher': 'Minecraft', 'popsicle': 'Popsicle', 'woeusb': 'WoeUSB', 'winehq-stable': 'Wine', 'virtualbox-6.1': 'Virtualbox', 'gparted': 'GParted', 'fusuma': 'fusuma', 'audacity': 'Audacity', 'deja-dup': 'Déja-Dup', 'timeshift': 'Timeshift', 'teamviewer': 'TeamViewer', 'gnome-boxes': 'Gnome Boxes'}                                          # debname:displayName
aurList = ['google-chrome', 'vivaldi', 'wps-office', 'onlyoffice-bin', 'freeoffice', 'signal-desktop', 'franz', 'minecraft-launcher', 'popsicle-git', 'woeusb', 'timeshift', 'skypeforlinux-stable-bin', 'barrier']
specDList = ['']
liLi = {
    'opera_but' : ['Opera', 'opera-stable', 'opera-ffmpeg-codecs', '', '', 0],
    'chrome_but' : ['Chrome', 'google-chrome-stable', '', 'alsa-lib gtk3 libcups libxss libxtst nss', '', 1],
    'web_but' : ['Web', 'epiphany-browser', '', '', '', 2],
    'firefox_but' : ['Firefox', 'firefox', '', '', '', 3],
    'vivaldi_but' : ['Vivaldi', 'vivaldi-stable', '', 'alsa-lib desktop-file-utils gtk3 hicolor-icon-theme libcups libxss nss shared-mime-info libnotify pepper-flash', 'w3m', 4],
    'edge_but' : ['', '', '', '', '', 5],
    'woffice_but' : ['WPS Office', 'wps-office', 'ttf-wps-fonts', 'fontconfig xorg-font-utils desktop-file-utils glu gtk2 hicolor-icon-theme libpulse libxrender libxss openssl-1.0 sdl2 shared-mime-info sqlite xdg-utils xorg-mkfontdir', '', 6],
    'loffice_but' : ['Libreoffice', 'libreoffice', '', '', '', 7],
    'ooffice_but' : ['Only Office', 'onlyoffice-desktopeditors', '', 'alsa-lib atk cairo curl desktop-file-utils fontconfig freetype2 gcc-libs gconf gdk-pixbuf2 gst-plugins-base-libs gstreamer gtk2 gtk3 gtkglext hicolor-icon-theme libcups libdrm libglvnd libice libpulse libsm libx11 libxcb libxcomposite libxcursor libxdamage libxext libxfixes libxi libxrandr libxrender libxss libxtst nspr nss pango qt5-declarative qt5-multimedia qt5-svg ttf-carlito ttf-dejavu ttf-liberation wget xdg-utils gtkglext libcurl-gnutls qt5-svg qt5-multimedia', '', 8],
    'foffice_but' : ['Free Office', 'softmaker-freeoffice-2018', '', 'curl desktop-file-utils gtk-update-icon-cache libxrandr xdg-utils libgl', 'chrpath', 11],
    'gedit_but' : ['Gedit', 'gedit', 'gedit-plugins', '', '', 12],
    'gnu_but' : ['GNU Emacs', 'emacs', '', '', '', 13],
    'vscode_but' : ['VS Code', 'code', '', '', '', 14],
    'atom_but' : ['Atom Editor', 'atom', '', '', '', 15],
    'stedit_but' : ['Sublime Text Editor', 'sublime-text', '', '', '', 16],
    'geany_but' : ['Geany', 'geany', '', '', '', 17],
    'skype_but' : ['Skype', 'skypeforlinux', '', 'alsa-lib gtk3 libsecret libxss libxtst nss glibc', 'asar', 18],
    'discord_but' : ['Discord', 'discord', '', '', '', 19],
    'telegram_but' : ['Telegram', 'telegram-desktop', '', '', '', 20],
    'signal_but' : ['Signal', 'signal-desktop', '', 'electron git npm', 'yarn nodejs', 21],
    'hex_but' : ['HexChat', 'hexchat', '', '', '', 22],
    'franz_but' : ['Franz', 'franz', '', 'electron npm git', 'expac', 23],
    '0ad_but' : ['0 A.D.', '0ad', '', '', '', 24],
    'skart_but' : ['SuperTuxKart', 'supertuxkart', '', '', '', 30],
    'tux_but' : ['SuperTux', 'supertux', '', '', '', 25],
    'lutris_but' : ['Lutris', 'lutris', '', '', '', 26],
    'barr_but' : ['Barrier', 'barrier', '', 'hicolor-icon-theme qt5-base avahi curl libice libsm libx11 libxext libxi libxinerama libxrandr libxtst openssl xorgproto', 'cmake', 42],
    'pol_but' : ['Play On Linux', 'playonlinux', '', '', '', 27],
    'steam_but' : ['Steam', 'steam', '', '', '', 28],
    'mc_but' : ['Minecraft', 'minecraft-launcher', '', 'alsa-lib gconf gtk2 gtk3 java-runtime libx11 libxcb libxss libxtst nss xorg-xrandr', '', 29],
    'pops_but' : ['Popsicle', 'popsicle', 'popsicle-gtk', 'git gtk3', 'cargo help2man rust xorgproto', 31],
    'woe_but' : ['WoeUSB', 'woeusb', '', 'dosfstools grub ntfs-3g parted wget wxgtk2', '', 32],
    'wine_but' : ['Wine', 'winehq-stable', '', '', '', 33],
    'vbox_but' : ['Virtualbox', 'virtualbox-6.1', '', '', '', 34],
    'gparted_but' : ['GParted', 'gparted', 'gpart', '', '', 35],
    'gest_but' : ['fusuma', 'fusuma', 'wmctrl libinput-tools xdotool', '', '', 36],
    'auda_but' : ['Audacity', 'audacity', '', '', '', 37],
    'deja_but' : ['Déja-Dup', 'deja-dup', '', '', '', 38],
    'tims_but' : ['Timeshift', 'timeshift', '', 'cronie desktop-file-utils gtk3 json-glib libsoup rsync vte3 xapps libgee', 'coreutils diffutils vala vte3', 39],
    'tw_but' : ['TeamViewer', 'teamviewer', '', '', '', 40],
    'box_but' : ['Gnome Boxes', 'gnome-boxes', '', '', '', 41]
    }
loLa = {
    'mint' : ['', 43],
    'ubuntu' : ['', 44],
    'solus' : ['', 45],
    'deepin' : ['', 46],
    'elementary' : ['', 47],
    'steamos' : ['', 48],
    'deb' : ['', 49],
    'fedora' : ['', 50],
    'opsu' : ['', 51],
    'arch' : ['', 52],
    'gentoo' : ['', 53],
    'lfs' : ['', 54]
    }

extDat = [
    ['dash-to-dock@micxgx.gmail.com', 'appindicatorsupport@rgcjonas.gmail.com', 'Move_Clock@rmy.pobox.com', 'user-theme@gnome-shell-extensions.gcampax.github.com'],
    ['appindicatorsupport@rgcjonas.gmail.com', 'user-theme@gnome-shell-extensions.gcampax.github.com', 'dash-to-panel@jderose9.github.com', 'arc-menu@linxgem33.com', 'remove-dropdown-arrows@mpdeimos.com', 'TopIcons@phocean.net'],
    ['dash-to-dock@micxgx.gmail.com', 'user-theme@gnome-shell-extensions.gcampax.github.com', 'Move_Clock@rmy.pobox.com', 'appindicatorsupport@rgcjonas.gmail.com', 'unite@hardpixel.eu'],
    ['user-theme@gnome-shell-extensions.gcampax.github.com']
]

themDat = {
    'Desktop theme' : 
    [
        'cd ~/ && wget https://github.com/swanux/hsuite/raw/master/DEV_FILES/themes_src/Mojave-dark-20200519113011.tar.xz && tar -xf Mojave-dark-20200519113011.tar.xz && rm -rf ~/.themes/Mojave-dark && mv Mojave-dark ~/.themes/ && gsettings set org.gnome.shell.extensions.user-theme name "Mojave-dark" && gsettings set org.gnome.desktop.interface gtk-theme "Mojave-dark"',
        'cd ~/ && wget https://github.com/swanux/hsuite/raw/master/DEV_FILES/themes_src/Windows-10-Dark-3.2-dark.tar.gz && tar -xf Windows-10-Dark-3.2-dark.tar.gz && rm -rf ~/.themes/Windows-10-Dark-3.2-dark && mv Windows-10-Dark-3.2-dark ~/.themes/ && gsettings set org.gnome.shell.extensions.user-theme name "Windows-10-Dark-3.2-dark" && gsettings set org.gnome.desktop.interface gtk-theme "Windows-10-Dark-3.2-dark"',
        'cd ~/ && wget https://github.com/swanux/hsuite/raw/master/DEV_FILES/themes_src/Unity-8-2.0.tar.gz && tar -xf Unity-8-2.0.tar.gz && rm -rf ~/.themes/Unity-8-2.0 && mv Unity-8-2.0 ~/.themes/ && gsettings set org.gnome.shell.extensions.user-theme name "Unity-8-2.0" && gsettings set org.gnome.desktop.interface gtk-theme "Unity-8-2.0"',
        'gsettings set org.gnome.desktop.interface gtk-theme "Adwaita" && gsettings set org.gnome.shell.extensions.user-theme name "Vanilla"'
    ],
    'Layout' : 
    [
        'gsettings set org.gnome.shell enabled-extensions "%s" && gsettings set org.gnome.shell.extensions.dash-to-dock dock-position "BOTTOM" && gsettings set org.gnome.shell.extensions.dash-to-dock intellihide "true" && gsettings set org.gnome.shell.extensions.dash-to-dock autohide true && gsettings set org.gnome.shell.extensions.dash-to-dock extend-height "false" && gsettings set org.gnome.shell.extensions.dash-to-dock background-opacity "0.4" && gsettings set org.gnome.shell.extensions.dash-to-dock dock-fixed "false" && gsettings set org.gnome.shell.extensions.dash-to-dock click-action "minimize" && gsettings set org.gnome.shell.extensions.dash-to-dock show-apps-at-top "true" && gsettings set org.gnome.shell.extensions.dash-to-dock show-running "true" && gsettings set org.gnome.shell.extensions.dash-to-dock apply-custom-theme "false" && gsettings set org.gnome.desktop.wm.preferences button-layout "close,minimize,maximize:"' % extDat[0],
        'gsettings set org.gnome.shell enabled-extensions "%s" && gsettings set org.gnome.shell.extensions.topicons tray-pos "Center" && gsettings set org.gnome.shell.extensions.topicons tray-order "2" && gsettings set org.gnome.shell.extensions.dash-to-panel panel-position "BOTTOM" && gsettings set org.gnome.shell.extensions.dash-to-panel location-clock "STATUSRIGHT" && gsettings set org.gnome.desktop.wm.preferences button-layout ":minimize,maximize,close" && gsettings set org.gnome.shell.extensions.arc-menu menu-button-icon "Custom_Icon" && gsettings set org.gnome.shell.extensions.arc-menu menu-button-active-color "rgb(45,138,217)" && gsettings set org.gnome.shell.extensions.arc-menu menu-hotkey "Super_L" && gsettings set org.gnome.shell.extensions.arc-menu manu-layout "Windows" && gsettings set org.gnome.shell.extensions.arc-menu multi-monitor "true" && gsettings set org.gnome.shell.extensions.dash-to-panel show-show-apps-button "false"' % extDat[1],
        'gsettings set org.gnome.shell enabled-extensions "%s" && gsettings set org.gnome.shell.extensions.dash-to-dock dock-position "LEFT" && gsettings set org.gnome.shell.extensions.dash-to-dock intellihide "false" && gsettings set org.gnome.shell.extensions.dash-to-dock autohide false && gsettings set org.gnome.shell.extensions.dash-to-dock background-opacity "0.7" && gsettings set org.gnome.shell.extensions.dash-to-dock background-color "#2C001E" && gsettings set org.gnome.shell.extensions.dash-to-dock dock-fixed "true" && gsettings set org.gnome.shell.extensions.dash-to-dock extend-height "true" && gsettings set org.gnome.shell.extensions.dash-to-dock show-running true && gsettings set org.gnome.shell.extensions.dash-to-dock show-apps-at-top true && gsettings set org.gnome.desktop.wm.preferences button-layout "close,minimize,maximize:"' % extDat[2],
        'gsettings set org.gnome.shell enabled-extensions "%s"' % extDat[3]
    ],
    'Icons' : 
    [
        'cd ~/ && wget https://github.com/swanux/hsuite/raw/master/DEV_FILES/themes_src/01-McMojave-circle.tar.xz && tar -xf 01-McMojave-circle.tar.xz && rm -rf ~/.icons/McMojave-circle-dark && mv McMojave-circle-dark ~/.icons/ && rm -rf ~/.icons/McMojave-circle && mv McMojave-circle ~/.icons/ && gsettings set org.gnome.desktop.interface icon-theme "McMojave-circle-dark"',
        'cd ~/ && wget https://github.com/swanux/hsuite/raw/master/DEV_FILES/themes_src/Windows-10-1.0.tar.gz && tar -xf Windows-10-1.0.tar.gz && rm -rf ~/.icons/Windows-10-1.0 && mv Windows-10-1.0 ~/.icons/ && gsettings set org.gnome.desktop.interface icon-theme "Windows-10-1.0"',
        'cd ~/ && wget https://github.com/swanux/hsuite/raw/master/DEV_FILES/themes_src/Suru.tar.xz && tar -xf Suru.tar.xz && rm -rf ~/.icons/Suru && mv Suru ~/.icons/ && gsettings set org.gnome.desktop.interface icon-theme "Suru"',
        'gsettings set org.gnome.desktop.interface icon-theme "Adwaita"'
    ],
    'Cursor' : 
    [
        'cd ~/ && wget https://github.com/swanux/hsuite/raw/master/DEV_FILES/themes_src/capitaine-cursors-r3.tar.xz && tar -xf capitaine-cursors-r3.tar.xz && rm -rf ~/.icons/capitaine-cursors && mv capitaine-cursors ~/.icons/ && gsettings set org.gnome.desktop.interface cursor-theme capitaine-cursors',
        'cd ~/ && wget https://github.com/swanux/hsuite/raw/master/DEV_FILES/themes_src/Win-8.1-S.tar.xz && tar -xf Win-8.1-S.tar.xz && rm -rf ~/.icons/Win-8.1-S && mv Win-8.1-S ~/.icons/ && gsettings set org.gnome.desktop.interface cursor-theme Win-8.1-S',
        'gsettings set org.gnome.desktop.interface cursor-theme DMZ-White',
        'gsettings set org.gnome.desktop.interface cursor-theme "Adwaita"'
    ],
}

# Used generally
# The glade file
UI_FILE = "hsuite.glade"
# Get current session type
xorw = os.popen('echo $XDG_SESSION_TYPE').read()
# It's Xorg, so it wokrs with gestures'
if "x" in xorw:
    lehete = _("""You need to reboot after the install has been completed
to apply all changes. You can configure the tool
through the ~/.config/fusuma/config.yml file.""")
# It is Wayland, so it won't work
else:
    lehete = _("""You need to reboot after the install has been completed
to apply all changes. However note that support for Wayland
is experimental. You can configure the tool
through the ~/.config/fusuma/config.yml file.""")
# Discover the current working dir
wer = os.popen('ls').read()

#________________________________________________________________________ END OF INIT ____________________________________________________________#

#___________________________________________________________________ BEGIN OF GUI ___________________________________________________________________#

# This class handles everything releated to the GUI and some background tasks connected to the program
class myThread (Thread):
    def __init__(self, threadID, name, ds=0, extra=0, post=0):
        Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.extra = extra
        self.ds = ds
        self.post = post
        self._stop_event = False

    def run(self):
        print("Starting " + self.name)
        # Calls the function
        if self.name == "Data":
            c = htransfer.Transser()
            lists = ""
            t = 0
            for i in self.extra:
                if t == 0:
                    lists = lists + '/home/%s/%s' % (user, i)
                else:
                    lists = lists + ', /home/%s/%s' % (user, i)
                t = t+1
            print('Lets do this')
            c.modPre(lists, '/home/%s/hswitcher/BUILD/restore-1.0/backups/' % user)
        else:
            os.system("mkdir -p /home/%s/hswitcher/BUILD/restore-1.0/" % user)
            os.system("cd /home/%s/hswitcher/BUILD/restore-1.0/ && dh_make -s -n -y && cd debian/ && rm -fr *.ex *.EX docs source RE* *.docs copyright" % user)
            changelog = "restore (1.0-1) unstable; urgency=medium\n\n  * Initial Release\n\n -- %s <%s@%s>  %s" % (user, user, platform.uname().node, time.strftime("%a, %d %b %Y %H:%M:%S +0200"))
            change_file = open("/home/%s/hswitcher/BUILD/restore-1.0/debian/changelog" % user, "w")
            change_file.write(changelog)
            change_file.close()
            compat_file = open("/home/%s/hswitcher/BUILD/restore-1.0/debian/compat" % user, "w")
            compat_file.write("11")
            compat_file.close()
            bds = "debhelper (>= 11)"
            print('DS_HERE')
            control = "Source: restore\nSection: metapackages\nPriority: optional\nMaintainer: %s <%s@%s>\nBuild-Depends: %s\nStandards-Version: 1.0-1\n\nPackage: restore\nArchitecture: amd64\nDepends: tar, %s\nDescription: Backup by HSwitcher\n Backup by HSwitcher. Just install it to use, then remove." % (user, user, platform.uname().node, bds, self.ds)
            print('Mem control')
            control_file = open("/home/%s/hswitcher/BUILD/restore-1.0/debian/control" % user, "w")
            control_file.write(control)
            control_file.close()
            install = "backups /usr/share/\n"
            install_file = open("/home/%s/hswitcher/BUILD/restore-1.0/debian/install" % user, "w")
            install_file.write(install)
            install_file.close()
            print('MAN')
            print("SUP")
            postins_file = open("/home/%s/hswitcher/BUILD/restore-1.0/debian/postinst" % user, "w")
            postins_file.write("#!/bin/bash +e\n\n"+self.post+"\n\n#DEBHELPER#")
            postins_file.close()
            os.system("chmod +x /home/%s/hswitcher/BUILD/restore-1.0/debian/postinst" % user)
            os.system("cd /home/%s/hswitcher/BUILD/restore-1.0/ && debuild -i -us -uc -b && cd .. && cd .. && cd ..&& cp hswitcher/BUILD/*.deb restore.deb && rm -rf hswitcher/" % user)
        print("Exiting " + self.name)

    def stop(self):
        self._stop_event = True
        print("stop func")

class GUI:
    count = 0
    def __init__(self):
        # if distro == 'Ubuntu' or distro == 'Debian':
        self.GNOME_SITE = "https://extensions.gnome.org"
        self.GNOME_VERSION = os.popen("DISPLAY=':0' gnome-shell --version | tr -cd '0-9.' | cut -d'.' -f1,2").read().rstrip()
        self.EXTENSION_PATH = "/home/%s/.local/share/gnome-shell/extensions" % user
        self.DIRS = os.popen("find /usr/share/gnome-shell/extensions $HOME/.local/share/gnome-shell/extensions -maxdepth 1 -type d -printf '%P\n'").read().replace('\n\n', '\n').split('\n')
        self.scanner = True
        self.them_conf = []
        self.hardCron = ""
        self.cPkg = ''
        self.runE = False
        self.tC2 = futures.ThreadPoolExecutor(max_workers=2)
        self.cache = {}
        self.stop = False
        self.Tdownl = ""
        self.quit = True
        self.b_cron = False
        self.b_progs = False
        self.b_settings = False
        self.b_theme = False
        self.b_data = False
        self.b_desk = False
        self.b_dl = False
        self.b_doc = False
        self.b_ms = False
        self.b_pic = False
        self.b_vid = False
        self.hsdir = '/home/%s/hswitcher/BUILD/restore-1.0/backups' % user
        # Prepare to use builder
        self.builder = Gtk.Builder()
        self.builder.set_translation_domain(APP)
        # Import the glade file
        self.builder.add_from_file(UI_FILE)
        # Connect all signals
        self.builder.connect_signals(self)
        self.switch_stack = self.builder.get_object('switch_stack')
        # Get the main stack object
        self.stack = self.builder.get_object('stack')
        self.window = self.builder.get_object(
            'window')                  # Get the main window
        # window.connect('check-resize', self.on_resize)

        if os.geteuid() == 0:
            # Indicate if runnung as root or not
            self.window.set_title(version+' (as superuser)')
        else:
            self.window.set_title(version)
        # Display the program
        self.progBox = self.builder.get_object('progBox')
        if distro == 'Ubuntu' or distro == 'Debian':
            self.dia = AptProgressBar()
        else:
            self.dia = Gtk.ProgressBar()
        self.progBox.pack_start(self.dia, True, True, 0)
        self.window.show_all()
        GLib.idle_add(self.dia.hide)
    
    # def on_resize(self, e):
    #     time.sleep(0.01)
    #     sx, sy = self.window.get_size()
    #     num = sy/4
    #     ssig = "%"
    #     num2 = "%s%s" % (num, ssig)
    #     css = """
    #     window {
    #         font-size: %s
    #     }
    #     button {
    #         border-radius: 15px;
    #         color:whitesmoke;
    #         background-color: dimgray;
    #         background-image:none;
    #         border-right-width: 3px; 
    #         border-left-width: 3px;
    #     }
    #     notebook > header.top > tabs > tab {
    #         color: whitesmoke;
    #     }
    #     notebook > header.bottom > tabs > tab {
    #         color: whitesmoke;
    #     }
    #     notebook > header > tabs > tab:hover {
    #         background: rgb(0, 153, 255);
    #         color: whitesmoke;
    #         border-image: none;
    #     }
    #     notebook > header > tabs > tab:checked {
    #         background: rgb(0, 91, 175);
    #         color: whitesmoke;
    #         border-image: none;
    #     }
    #     button:hover {
    #         background-color: rgb(0, 153, 255);
    #         color:whitesmoke;
    #     }
    #     button:disabled {
    #         background-color: rgb(54, 54, 54);
    #         color:whitesmoke;
    #     }
    #     button:hover:active {
    #         background-color: lightblue;
    #         color: darkgreen;
    #     }
    #     .red-background{
    #         background-image: none;
    #         background-color: red;
    #         color: white;
    #     }
    #     .green-background{
    #         background-image: none;
    #         background-color: green;
    #         color: white;
    #     }
    #     """
    #     css = css % num2
    #     css = str.encode(css)
    #     provider.load_from_data(css)
        # GLib.idle_add(provider.load_from_data, css)

    # This happens when close button is clicked
    def on_window_delete_event(self, window, e):
        self.construct_dialog(Gtk.MessageType.QUESTION, Gtk.ButtonsType.YES_NO, _('Do you really would like to exit now?'), _("Prompt"), 'exit')
        return True

###################################################################################

    # Set the button colors
    def colorer(self, gbut, name, insList):
        # Call function to check if apps are installed or not
        status = self.OnCheck(name, insList)
        # set the button label depending on this
        GLib.idle_add(gbut.set_label, status)
        gbut.get_style_context().remove_class("red-background")
        gbut.get_style_context().remove_class("green-background")
        if _("Remove") in status:
            gbut.get_style_context().add_class('red-background')
        else:
            gbut.get_style_context().add_class('green-background')
        return status

    def scannerf(self):                                         # Scans the OS for programs
        insList = apt.Cache()
        # Check for every program in the list
        for i in range(appListLen):
            if distro == 'Ubuntu' or distro == 'Debian':
                # the name to check for
                name = appList[i]
            else:
                print('ERROR IN NAME')
            # importing the button
            gbut = self.builder.get_object("%s_but" % butDict[appList[i]])
            # Call function for setting label and color
            status = self.colorer(gbut, name, insList)
            # value refers to the state: Install/Remove
            tempNam = layDict[appList[i]]
            statDict[tempNam] = status

        # It indicates that the state of every program is now loaded into the memory
        self.scanner = False

    # check if program is installed or not
    def OnCheck(self, name, insList):
        if 'fusuma' in name:
            vane = os.popen('gem list --local').read()
            vfil = os.popen('ls /usr/lib/ruby/gems/2.6.0/cache/').read()
            if name in vane or name in vfil:
                status = _('Remove')
            else:
                status = _('Install')
        elif 'TeamViewer' in name:
            vane = os.path.exists("/opt/teamviewer")
            print('tw check = %s' % vane)
            if vane:
                status = _('Remove')
            else:
                status = _('Install')
        else:
            if distro == 'Debian' or distro == 'Ubuntu':
                try:
                    if insList[name].is_installed:
                        print('Found %s' % name)
                        status = _('Remove')
                    else:
                        print('Not found %s' % name)
                        status = _('Install')
                except:
                    print('Auto error handling --> Falling back to default (Not found)')
                    status = _('Install')
        if self.spece(name):
            status = '%s (AUR)' % status
        return status

    def construct_dialog(self, typed, typeb, txt, title, name, mode=''):
        # Getting the window position
        x, y = self.window.get_position()
        # Get the size of the window
        sx, sy = self.window.get_size()
        dialogWindow = Gtk.MessageDialog(parent=self.window, modal=True, destroy_with_parent=True, message_type=typed, buttons=typeb, text=txt)
        # set the title
        dialogWindow.set_title(title)
        dsx, dsy = dialogWindow.get_size()                          # get the dialogs size
        # Move it to the center of the main window
        dialogWindow.move(x+((sx-dsx)/2), y+((sy-dsy)/2))
        dx, dy = dialogWindow.get_position()                        # set the position
        print(dx, dy)
        if name == 'custom':
            dialogWindow.add_button("What's new", 55)
            dialogWindow.show_all()
            res = dialogWindow.run()
            print(res)
            if res == 55:
                print('Want visit')
                webbrowser.open_new("https://swanux.github.io/hsuite/")
            else:
                print('just ok')
            dialogWindow.destroy()
        else:
            dialogWindow.show_all()
            res = dialogWindow.run()
            if name != 'general':
                if res == Gtk.ResponseType.YES:                             # if yes ...
                    print('OK pressed')
                    dialogWindow.destroy()
                    if name == 'exit':
                        self.noMean = True
                        code = 'force'
                        if osLayer.alive:
                            code = self.construct_dialog(Gtk.MessageType.WARNING, Gtk.ButtonsType.YES_NO, _("Do you really would like to abort now? It could end up with a broken program. If you decide to abort, then you may need to remove %s manually.") % self.cPkg, _("Attention!"), 'abort', 'install')
                        if self.quit == False:
                            code = self.construct_dialog(Gtk.MessageType.WARNING, Gtk.ButtonsType.YES_NO, _("Do you really would like to abort now? Download is currently in progress for %s.") % namDict[self.Tdownl], _("Attention!"), 'abort', 'download')
                        if code == 'force':
                            self.stop = True
                            try:
                                self.tS.shutdown()
                            except:
                                pass
                            raise SystemExit
                        else:
                            dialogWindow.destroy()
                            return True
                    elif name == 'switcher':
                        if res == Gtk.ResponseType.YES:
                            print('OK pressed')
                            dialogWindow.destroy()
                            return True
                        elif res == Gtk.ResponseType.NO:
                            print('No pressed')
                            dialogWindow.destroy()
                            return False
                        else:
                            return False
                    elif name == 'abort':
                        if res == Gtk.ResponseType.YES:
                            if mode == 'download':
                                self.quit = True
                                self.rmE = True
                                print(self.quit)
                            elif mode == 'install':
                                print('Installation already running')
                                if distro == 'Ubuntu' or distro == 'Debian':
                                    try:
                                        print(self.trans.cancellable)
                                        self.trans.cancel()
                                    except:
                                        print('Cant cancel')
                                        self.construct_dialog(Gtk.MessageType.ERROR, Gtk.ButtonsType.OK, _("You can't cancel installation, as it's in a critical state."), _("Safety first!"), 'general')
                                else:
                                    print('ERROR IN DIST AB')
                            print('OK pressed')
                            dialogWindow.destroy()
                            return 'force'
                        elif res == Gtk.ResponseType.NO:
                            print('No pressed')
                            dialogWindow.destroy()
                            return True
                elif res == Gtk.ResponseType.NO:                            # if no ...
                    print('No pressed')
                    dialogWindow.destroy()                                  # destroy dialog
                    return True                                             # end function
                else:
                    dialogWindow.destroy()                                  # destroy dialog
                    return True                                             # end function
            else:
                dialogWindow.destroy()
                return True

    def on_fin(self, transaction, exit_state):
        GLib.idle_add(self.dia.hide)
        osLayer.alive = False
        print('Trans : %s' % transaction)
        print('Code : %s' % exit_state)
        print("FIN")
    
    def on_done(self, sth):
        osLayer.alive = False

    # This is executed when an app is being installed/removed
    def OnNeed(self, cInB, name, status, comm1, comm2, faur, extra, runDep, buildDep, tempInd=''):
        # removes scan cache from memory because it needs to rescan because one app changed
        sTxt = cInB
        # Current pkg name
        self.cPkg = name
        if distro == 'Ubuntu' or distro == 'Debian':
            progr, self.trans = osLayer.my_thread(status, distro, comm1, comm2, faur, extra, runDep, buildDep)
            if progr == True:
                self.dia.set_transaction(self.trans)
                GLib.idle_add(self.dia.show)
                self.trans.connect("finished", self.on_fin)
                self.trans.run()
            else:
                print('E: osLayer error')
        wt = False
        print(self, wt)
        for i in range(appListLen):
            print("Toggle %s" % i)
            if appList[i] != tempInd:
                print(appList[i], butDict[appList[i]], tempInd)
                cBut = self.builder.get_object('%s_but' % butDict[appList[i]])
                GLib.idle_add(cBut.set_sensitive, wt)
        # function for counting time
        def counter(timer, m):
            # seconds incraseing
            s = timer.count+1
            # counter is equal to s
            timer.count = s
            sTxt.set_label(_('Processing ')+name+' '+str(m) +
                           ':'+str(s))
            if s == 59:                                                             # add one to min and reset sec
                timer.count = -1
                m = m+1
            if osLayer.alive:                                                        # if thread is still running repeat
                return True
            else:                                                                   # on exit
                # reset counter
                timer.count = 0
                # declare button variable (don't know why)
                button = 0
                # imitate reopening of app spotlight
                wt = True
                print(self, wt)
                for i in range(appListLen):
                    cBut = self.builder.get_object('%s_but' % butDict[appList[i]])
                    GLib.idle_add(cBut.set_sensitive, wt)
                self.scanner = True
                self.button_clicked(button)
                if not self.window.is_active():
                    notify2.init('HSuite')
                    n = notify2.Notification('HSuite', _('Finished processing %s!') % self.cPkg)
                    n.show()
                self.cPkg = ''
                return False                                                      # end
        self.source_id = GLib.timeout_add(1000, counter, self, 0)

    def spece(self, name):
        if distro == 'Ubuntu' or distro == 'Debian':
            if name in specDList:
                return True
            else:
                return False
        else:
            print('SpecERROR!')

    def lilFunc(self, name, comm1, extra, runDep, buildDep):
        if osLayer.alive:
            print('Operation already running, which is %s' % self.cPkg)
        if name == self.cPkg:
            self.construct_dialog(Gtk.MessageType.WARNING, Gtk.ButtonsType.YES_NO, _("Do you really would like to abort now?"), _("Attention!"), 'abort', 'install')
        else:
            comm2 = ''
            cInB = self.builder.get_object("%s_but" % butDict[comm1])
            tempInd = comm1
            if _('Install') in statDict[name]:
                if name == 'fusuma':
                    self.construct_dialog(Gtk.MessageType.WARNING, Gtk.ButtonsType.OK, lehete, _("Note!"), 'general')
                print(name)
                self.OnNeed(cInB, name, 'install', comm1, comm2, self.spece(comm2), extra, runDep, buildDep, tempInd)
            elif _('Remove') in statDict[name]:
                print(name)
                self.OnNeed(cInB, name, 'remove', comm1, comm2, self.spece(comm2), extra, runDep, buildDep)

# Download methods

    # Disable or enable buttons based on a pattern
    def toggle(self, fn):
        print(self, fn, self.state)
        for i in range(dlistLen):
            if dlist[i] != self.Tdownl and shDict[dlist[i]] != "PFalse":
                cBut = self.builder.get_object(dlist[i])
                t = cBut.get_label()
                if t == _("Server error"):
                    print('Skipping due to server error')
                else:
                    GLib.idle_add(cBut.set_sensitive, self.state)
                    shDict[dlist[i]] = "%s" % self.state
        if self.state:
            self.scanningUrl = False

    # Starting download in a background thread BUT inside the GUI class, not the thread. This is because of the nature of GTK (and other GUI toolkits) that can't handle GUI changes from outside of the main thread (gui class)
    def ex_target(self, block_sz, downl, file_size, file_name, file_size_dl, u, f):
        print("DLthread...")
        # This variable shows if the thread needs to exit
        self.quit = False
        while not self.quit:
            # Reads the downloaded bytes in blocks
            buffer = u.read(block_sz)
            if not buffer:
                # break if error occures
                break
            # Set the downloaded file size to buffer
            file_size_dl += len(buffer)
            # write this block to the downloaded file
            f.write(buffer)
            status = r"Cancel  [%3.2f%%]" % (
                file_size_dl * 100 / file_size)  # Calculate precentage
            # Place on waiting list to change the label to the actual status
            GLib.idle_add(downl.set_label, status)
        print("DLend!!")
        # Shows that no downloads are running
        self.runE = False
        # Set back the button label to the original
        GLib.idle_add(downl.set_label, self.orig)
        print('quit: %s' % self.quit)
        print(self.orig)
        print("Label restore")
        # If the download is aborted by the user, remove the already downloaded file
        if self.rmE:
            print('Cleaning up...')
            os.system('rm /home/%s/Downloads/%s' % (user, file_name))
        else:
            # Set label to ready
            GLib.idle_add(downl.set_label, _("Ready in ~/Downloads/"))
            # Disable button
            GLib.idle_add(downl.set_sensitive, False)
            # Set the state to permanent false
            shDict[self.Tdownl] = "PFalse"
            print("done with it")
            if not self.window.is_active():
                notify2.init('HSuite')
                n = notify2.Notification('HSuite', _('Finished downloading %s!') % namDict[self.Tdownl])
                n.show()
        self.quit = True

    def on_downl_begin(self, url, downl):
        # Open the url
        u = urlopen(url)
        if self.runE == True:                                                  # If download is already running
            # set remove flag to true
            self.rmE = True
            # tell the thread to stop
            self.quit = True
            print("TruTogle")
            # set button state to enabled
            self.state = True
            # enable every button
            self.toggle(fn)
            return
        elif self.runE == False:                                               # If no downloads are running
            # toggle that now one is running
            self.runE = True
            # we don't need to remove the downloaded file, because it's ready
            self.rmE = False
            # save the original label of the button
            self.orig = downl.get_label()
        file_name = url.split('/')[-1]
        f = open('/home/%s/Downloads/%s' %
                 (user, file_name), 'wb')  # set download location
        print('Downloading %s' % file_name)
        print("FalsTogle")
        # disable buttons
        self.state = False
        # run function to do this
        self.toggle(fn)
        t1 = futures.ThreadPoolExecutor(
            max_workers=4)                    # init thread
        # start it
        fa = t1.submit(self.ex_target, 8192, downl, int(
            u.getheader('Content-Length')), file_name, 0, u, f)
        # set buttons to active
        self.state = True
        # after done run this function
        fa.add_done_callback(self.toggle)

    def generalSizer(self, di, url):
        print(self.uriDict[di])
        print('Updated linklist!!')
        print("Getting size...")
        cBut = self.builder.get_object(di)
        try:
            u = urlopen(url)
            time.sleep(0.1)
            file_size = int(u.getheader('Content-Length'))
            # convert to MB
            file_size = Decimal(int(file_size) / 1024 / 1024)
            GLib.idle_add(cBut.set_label, "Download (%s MB)" %
                        round(file_size, 1))  # set download label
            # store value in cache
            self.cache[di] = round(file_size, 1)
        except:
            print('URL ERROR!')
            GLib.idle_add(cBut.set_label, _("Server error"))
            self.cache[di] = round(0, 1)

    def getSizeOnce(self, forDl, distrol, flav):
        print('Getting Link...')
        if 'mint' in distrol:
            print('mint now')
            if 'lmde' in forDl:
                vers, misc = self.findNew("http://mirrors.evowise.com/linuxmint/debian/", r'-+[\d]+-', r'[\d]')
                url = 'http://mirrors.evowise.com/linuxmint/debian/lmde-%s-cinnamon-64bit.iso' % vers[0]
            else:
                vers, misc = self.findNew("http://mirrors.evowise.com/linuxmint/stable/", r'"+[\d]+.[\d]+/', r'[\d]+[\d]+[\d]')
                url = 'http://mirrors.evowise.com/linuxmint/stable/%s%s.%s/linuxmint-%s%s.%s-%s-64bit.iso' % (vers[0], vers[1], vers[2], vers[0], vers[1], vers[2], forDl)
            self.uriDict['downl_mint'] = url
            self.generalSizer('downl_mint', url)
        elif 'ubuntu' in distrol:
            print('ubuntu now')
            vers, misc = self.findNew("http://cdimage.ubuntu.com/%s/releases/" % forDl, r'"+[\d]+.[\d]+/', r'[\d]+[\d]+[\d]+[\d]')
            url = 'http://cdimage.ubuntu.com/%s/releases/%s%s.%s%s/release/%s-%s%s.%s%s-desktop-amd64.iso' % (forDl, vers[0], vers[1], vers[2], vers[3], forDl, vers[0], vers[1], vers[2], vers[3])
            self.uriDict['downl_ubuntu'] = url
            self.generalSizer('downl_ubuntu', url)
        elif 'solus' in distrol:
            print('solus now')
            vers, misc = self.findNew("https://solus.veatnet.de/iso/images", r'"+[\d]+.[\d]+/', r'[\d]+[\d]')
            url = 'https://solus.veatnet.de/iso/images/%s.%s/Solus-%s.%s-%s.iso' % (vers[0], vers[1], vers[0], vers[1], forDl)
            self.uriDict['downl_solus'] = url
            self.generalSizer('downl_solus', url)
        elif 'deb' in distrol:
            print('debian now')
            vers, misc = self.findNew("https://cdimage.debian.org/images/unofficial/non-free/images-including-firmware/current-live/amd64/iso-hybrid/", r'debian-live-+[\d]+[\d]+.[\d]+.[\d]', r'[\d]+[\d]+[\d]')
            url = 'https://cdimage.debian.org/images/unofficial/non-free/images-including-firmware/current-live/amd64/iso-hybrid/debian-live-%s%s.%s.%s-amd64-%s+nonfree.iso' % (vers[0], vers[1], vers[2], vers[3], forDl)
            self.uriDict['downl_deb'] = url
            self.generalSizer('downl_deb', url)
        elif 'fedora' in distrol:
            print('fedora now')
            if 'default' in forDl:
                vers, misc = self.findNew("http://fedora.inode.at/releases/", r'"+[\d]+/', r'[\d]+[\d]')
                versf, misc = self.findNew('http://fedora.inode.at/releases/%s%s/Workstation/x86_64/iso' % (vers[0], vers[1]), r'-+[\d]+.+[\d]+.', r'-+[\d]+[\d]+-x')
                url = 'http://fedora.inode.at/releases/%s%s/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-%s%s-%s.%s.iso' % (vers[0], vers[1], vers[0], vers[1], versf[0], versf[2])
            else:
                vers, misc = self.findNew("http://fedora.inode.at/releases/", r'"+[\d]+/', r'[\d]+[\d]')
                versf, misc = self.findNew('http://fedora.inode.at/releases/%s%s/Spins/x86_64/iso' % (vers[0], vers[1]), r'-+[\d]+.+[\d]+.', r'-+[\d]+[\d]+-x')
                url = 'http://fedora.inode.at/releases/%s%s/Spins/x86_64/iso/Fedora-%s-Live-x86_64-%s%s-%s.%s.iso' % (vers[0], vers[1],forDl , vers[0], vers[1], versf[0], versf[2])
            self.uriDict['downl_fedora'] = url
            self.generalSizer('downl_fedora', url)
        elif 'suse' in distrol:
            print('opensuse now')
            if 'roll' in forDl:
                url = 'https://download.opensuse.org/tumbleweed/iso/openSUSE-Tumbleweed-DVD-x86_64-Current.iso'
            else:
                reponse = urlopen("https://download.opensuse.org/distribution/openSUSE-stable/iso")
                dat = reponse.read()
                text = dat.decode('utf-8')
                pattern = re.findall(r'openSUSE-Leap-+[\d]+[\d]+.+[\d]+-DVD-x86_64.iso"><', text)
                vers = pattern[0].replace('"', '').replace('><', '')
                url = "https://download.opensuse.org/distribution/openSUSE-stable/iso/%s" % vers
            self.uriDict['downl_suse'] = url
            self.generalSizer('downl_suse', url)
            

    def on_choose(self, widget):
        distrol = Gtk.Buildable.get_name(widget)
        flav = widget.get_active_text()
        linkForIso = toChoseDir[distrol][flav]
        self.tS = futures.ThreadPoolExecutor(max_workers=2)
        self.tS.submit(self.getSizeOnce, forDl=linkForIso, distrol=distrol, flav=flav)

    def general_download(self, button):
        self.Tdownl = Gtk.Buildable.get_name(button)
        self.on_downl_begin(self.uriDict[self.Tdownl], self.builder.get_object(self.Tdownl))

# End of download section

    # Button is the name of the app spotlight button
    def button_clicked(self, button):
        # If already in memory don't waste resources
        if self.scanner == False:
            print('VALUE_FOUND')
            # notebook box is the name of the app spotlight page
            notebook_box = self.builder.get_object('notebook_box')
            # set it visible
            self.stack.set_visible_child(notebook_box)
        # if not in memory, then scan it now
        elif self.scanner:
            notebook_box = self.builder.get_object('notebook_box')
            self.stack.set_visible_child(notebook_box)
            print('NO_VALUE')
            # start scanning
            aS = futures.ThreadPoolExecutor(max_workers=2)
            s = aS.submit(self.scannerf)
            print('SCANN START')
            print(s)
        else:
            print('ERROR')

    # feedback button
    def on_fb_but_clicked(self, button):
        web_box = self.builder.get_object('web_box')
        texV = self.builder.get_object('txt_long')
        titE = self.builder.get_object('tit_entry')
        text = texV.get_buffer()
        text = text.set_text('')
        titE.set_text('')
        self.stack.set_visible_child(web_box)
        tC = futures.ThreadPoolExecutor(max_workers=2)
        f = tC.submit(self.check)
        self.where = 'fb'
        f.add_done_callback(self.chk_again)

    def check(self):
        try:
            urlopen('http://216.58.192.142', timeout=5)
            print('yes, net')
            self.net = True
        except:
            print('no internet')
            self.net = False
    def chk_again(self, arg):
        if not self.net:
            button = 0
            self.construct_dialog(Gtk.MessageType.WARNING, Gtk.ButtonsType.OK, _("You have no internet connection!"), _("Attention!"), 'general')
            if self.where == 'fb':
                self.home_clicked(button)
            else:
                self.tC2 = futures.ThreadPoolExecutor(max_workers=2)
                for i in range(dlistLen):
                    # dlist is distro list (contains all distro names), cbut is current button
                    cBut = self.builder.get_object(dlist[i])
                    cBut.set_label(_('No internet'))
        else:
            if self.where == 'gs':
                self.tS = futures.ThreadPoolExecutor(max_workers=2)
                f = self.tS.submit(self.getSize)
                # toggle everything back when ready
                self.state = True
                f.add_done_callback(self.toggle)

    def on_send(self, button):
        titE = self.builder.get_object('tit_entry')
        emE = self.builder.get_object('email_entry')
        texV = self.builder.get_object('txt_long')
        cat = self.builder.get_object('typ_comb')
        title = titE.get_text()
        email = emE.get_text()
        text = texV.get_buffer()
        start = text.get_start_iter()
        end = text.get_end_iter()
        text = text.get_text(start, end, True)
        category = cat.get_active_text()
        print(title, text, category, email)
        if '@' not in email or '.' not in email:
            if email == '' or email == None:
                print('Optional, of course')
                email = 'Not provided'
            else:
                print('invalid email!!')
                self.construct_dialog(Gtk.MessageType.WARNING, Gtk.ButtonsType.OK, _('Invalid email address!'), _("Attention!"), 'general')
                return
        elif text == '' or title == '':
            self.construct_dialog(Gtk.MessageType.WARNING, Gtk.ButtonsType.OK, _('You need to fill out all the fields!'), _("Attention!"), 'general')
            return
        text = text+"\n\n---------------------------------\n\nEmail: %s\nUsername: %s\nComputer name: %s\nOS: %s\nCPU: %s" % (email, user, platform.uname().node, platform.platform(), platform.processor())
        repo = g.get_repo('swanux/hsuite_feedbacks')
        if category == _('Enhancement'):
            lab = ['enhancement']
        elif category == _('Question'):
            lab = ['question']
        elif category == _('Bug'):
            lab = ['bug']
        else:
            print('Feedback Error')
            lab = ['invalid']
        repo.create_issue(title=title, body=text, labels=lab)
        print('Uploaded')
        self.construct_dialog(Gtk.MessageType.INFO, Gtk.ButtonsType.OK, _('Feedback submitted succesfully!'), _("Information"), 'general')
        self.home_clicked(button)

    # information button in about section
    def on_git_link_clicked(self, button):
        # open project page in browser
        webbrowser.open_new("https://swanux.github.io/hsuite/")

#######################################################################################

    def appl_but_clicked(self, button):
        os.system('mkdir -p ~/.themes && mkdir -p ~/.icons && mkdir -p ~/.local/share/glib-2.0/schemas/ && export XDG_DATA_DIRS=~/.local/share:/usr/share && find ~/.local/share/gnome-shell/extensions/ -name *gschema.xml -exec ln {} -sfn ~/.local/share/glib-2.0/schemas/ \; && glib-compile-schemas ~/.local/share/glib-2.0/schemas/')
        for i in self.them_conf:
            command = themDat[i][self.themNum]
            if i == 'Layout':
                os.system('gsettings set org.gnome.shell enabled-extensions []')
                for ext in extDat[self.themNum]:
                    if ext in self.DIRS:
                        print('%s is already installed.' % ext)
                    else:
                        print('Installing %s...' % ext)
                        if 'remove-dropdown-arrows' in ext and float(self.GNOME_VERSION) >= 3.36:
                            JSON = "%s/extension-info/?uuid=%s&shell_version=3.34" % (self.GNOME_SITE, ext)
                        else:
                            JSON = "%s/extension-info/?uuid=%s&shell_version=%s" % (self.GNOME_SITE, ext, self.GNOME_VERSION)
                        tmp = os.popen("curl -s '%s'" % JSON).read().split(' ')
                        EXTENSION_URL = self.GNOME_SITE + tmp[-1].replace('"', '').replace('}', '')
                        os.system("wget --header='Accept-Encoding:none' -O '~/tmp.zip' '%s'" % EXTENSION_URL)
                        os.system("mkdir -p %s/%s && unzip -oq ~/tmp.zip -d %s/%s && chmod +r %s/%s/* && rm -f ~/tmp.zip" % (self.EXTENSION_PATH, ext, self.EXTENSION_PATH, ext, self.EXTENSION_PATH, ext))
            os.system(command)
        os.system('cd ~/ && rm -rf 01-McMojave-circle.tar.xz capitaine-cursors-r3.tar.xz Mojave-dark-20200519113011.tar.xz Win-8.1-S.tar.xz Windows-10-1.0.tar.gz Windows-10-Dark-3.2-dark.tar.gz Suru.tar.xz Unity-8-2.0.tar.gz')

    def del_themer(self, twindow, e):
        twindow.hide()
        return True

    def all_toggle(self, widget):
        if widget.get_active():
            print('Active')
            self.builder.get_object('desk_them_chk').set_active(True)
            self.builder.get_object('lay_chk').set_active(True)
            self.builder.get_object('ico_chk').set_active(True)
            self.builder.get_object('cur_chk').set_active(True)
        else:
            print('Inactive')
            self.builder.get_object('desk_them_chk').set_active(False)
            self.builder.get_object('lay_chk').set_active(False)
            self.builder.get_object('ico_chk').set_active(False)
            self.builder.get_object('cur_chk').set_active(False)
        print(self.them_conf)

    def them_conf_ch(self, widget):
        name = widget.get_label()
        if widget.get_active():
            print('Active')
            self.them_conf.append(name)
        else:
            print('Inactive')
            self.them_conf.remove(name)
        print(self.them_conf)

    def general_theme_click(self, button):
        name = button.get_label()
        if 'MacOS' in name:
            self.themNum = 0
        elif 'Windows' in name:
            self.themNum = 1
        else:
            self.themNum = 2
        win = self.builder.get_object('themer_win')
        win.show_all()

#######################################################################################

    def on_general_chk(self, widget):
        which = Gtk.Buildable.get_name(widget)
        status = widget.get_active()
        if 'prog' in which:
            self.b_progs = status
        elif 'usr' in which:
            self.b_data = status
        elif 'cron' in which:
            self.b_cron = status
        elif 'them' in which:
            self.b_theme = status
            self.b_settings = status
    
    def on_prog_tog(self, widget, name):
        if widget.get_active():
            print('Active')
            self.appsToSave.append(name)
        else:
            print('Inactive')
            self.appsToSave.remove(name)
        print(self.appsToSave)

    def on_dat_toggle(self, widget):
        name = widget.get_label()
        if widget.get_active():
            print('Active')
            self.datToSave.append(name)
        else:
            print('Inactive')
            self.datToSave.remove(name)
        print(self.datToSave)

    def on_dat_proc_but_clicked(self, button):
        barcur = self.builder.get_object('current')
        bartot = self.builder.get_object('total')
        barcur.set_fraction(0.00)
        bartot.set_fraction(0.00)
        self.builder.get_object('back_button1').set_sensitive(False)
        GLib.idle_add(self.switch_stack.set_visible_child, self.builder.get_object('data_box'))
        self.datT = myThread(3, "Data", extra=self.datToSave)
        self.datT.start()
        def counter(timer):
            if self.datT.isAlive():
                GLib.idle_add(barcur.set_fraction, htransfer.filePer/100)
                GLib.idle_add(barcur.set_text, htransfer.yetFil)
                GLib.idle_add(bartot.set_fraction, htransfer.currPer/100)
                return True
            else:
                # self.b_data = False
                # self.on_prog_proc_but_clicked(0)
                self.crTask()
                return False
        self.source_id = GLib.timeout_add(200, counter, None)

    def crTask(self):
        self.builder.get_object('back_button1').set_sensitive(False)
        spinner = self.builder.get_object('create_spin')
        spinner.start()
        self.switch_stack.set_visible_child(self.builder.get_object('create_box'))
        postinst = ""
        if self.b_data:
            for i in self.datToSave:
                postinst = postinst + "cp -R /usr/share/backups/%s/* /home/%s/%s/\nchown -R %s /home/%s/%s\n" % (i, user, i, user, user, i)
        ds = ""
        if self.b_progs:
            l = 0
            for i in self.appsToSave:
                if l == 0:
                    ds = ds+"%s" % i
                else:
                    ds = ds+", %s" % i
                l = l+1
            for i in self.appsToSave:
                postinst = postinst + "apt-mark manual %s\n" % i
        if self.b_theme:
            postinst = postinst + 'cp /usr/share/backups/background/* /usr/share/backgrounds/\n'
            postinst = postinst + 'cp /usr/share/backups/screensaver/* /usr/share/backgrounds/\n'
            postinst = postinst + 'tar -pxvzf /usr/share/backups/shellTheme.tar.gz -C /usr/share/themes/\n'
            postinst = postinst + 'tar -pxvzf /usr/share/backups/deskTheme.tar.gz -C /usr/share/themes/\n'
            postinst = postinst + 'tar -pxvzf /usr/share/backups/cursorTheme.tar.gz -C /usr/share/themes/\n'
            postinst = postinst + 'tar -pxvzf /usr/share/backups/iconTheme.tar.gz -C /usr/share/icons/\n'
            postinst = postinst + "user=$(who|awk '{print $1}'r)\n"
            postinst = postinst + 'tar -pxvzf /usr/share/backups/extensions.tar.gz -C /home/$user/.local/share/gnome-shell/\n'
            postinst = postinst + "runuser -l $user -c 'dconf load /org/gnome/ < /usr/share/backups/gnome'\n"
        if self.b_cron:
            postinst = postinst + "user=$(who|awk '{print $1}'r)\n"
            postinst = postinst + 'crontab -u $user /usr/share/backups/crontab\n'
        postinst += 'chown -R %s /home/%s/\n' % (user, user)
        # print('DS: %s' % ds)
        t1 = myThread(5, "Builder", ds=ds, post=postinst)
        t1.start()
        def counter(timer):
            if t1.isAlive():
                return True
            else:
                spinner.stop()
                self.builder.get_object('back_button1').set_sensitive(True)
                self.switch_stack.set_visible_child(self.builder.get_object('done_txt'))
                return False
        self.source_id = GLib.timeout_add(1000, counter, None)

    def on_prog_proc_but_clicked(self, button):
        if self.b_data:
            self.switch_stack.set_visible_child(self.builder.get_object('scroll_dat'))
        else:
            self.crTask()

    def on_proc_but_clicked(self, button):
        os.system("mkdir -p %s/" % self.hsdir)
        self.appsToSave = []
        self.datToSave = []
        if self.b_settings and self.b_theme:
            os.system("mkdir -p %s/background" % self.hsdir)
            os.system("mkdir -p %s/screensaver" % self.hsdir)
            print('Desktop True')
            os.system('dconf dump /org/gnome/ > %s/gnome' % self.hsdir)
            os.system('cd /home/%s/.local/share/gnome-shell/ && tar -pcvzf %s/extensions.tar.gz extensions' % (user, self.hsdir))
            locparse = ConfigParser()
            locparse.read('%s/gnome' % self.hsdir)
            screensaver = locparse.get('desktop/screensaver', 'picture-uri').replace('file://', '')
            sname = screensaver.split('/')[-1].replace("'", '')
            os.system('cp %s %s/screensaver/%s' % (screensaver, self.hsdir, sname))
            print(sname)
            background = locparse.get('desktop/background', 'picture-uri').replace('file://', '')
            fname = background.split('/')[-1].replace("'", '')
            os.system('cp %s %s/background/%s' % (background, self.hsdir, fname))
            print(fname)
            locparse.set('desktop/screensaver', 'picture-uri', "'file:///usr/share/backgrounds/%s'" % sname)
            locparse.set('desktop/background', 'picture-uri', "'file:///usr/share/backgrounds/%s'" % fname)
            shellTheme = locparse.get('shell/extensions/user-theme', 'name')
            if os.path.exists('/home/%s/.themes/%s' % (user, shellTheme.replace("'", ""))):
                os.system('cd /home/%s/.themes/ && tar -pcvzf %s/shellTheme.tar.gz %s' % (user, self.hsdir, shellTheme))
            else:
                os.system('cd /usr/share/themes/ && tar -pcvzf %s/shellTheme.tar.gz %s' % (self.hsdir, shellTheme))
            deskTheme = locparse.get('desktop/interface', 'gtk-theme')
            iconTheme = locparse.get('desktop/interface', 'icon-theme')
            cursorTheme = locparse.get('desktop/interface', 'cursor-theme')
            if os.path.exists('/home/%s/.themes/%s' % (user, deskTheme)):
                os.system('cd /home/%s/.themes/ && tar -pcvzf %s/deskTheme.tar.gz %s' % (user, self.hsdir, deskTheme))
            else:
                os.system('cd /usr/share/themes/ && tar -pcvzf %s/deskTheme.tar.gz %s' % (self.hsdir, deskTheme))
            if os.path.exists('/home/%s/.themes/%s' % (user, cursorTheme)):
                os.system('cd /home/%s/.icons/ && tar -pcvzf %s/cursorTheme.tar.gz %s' % (user, self.hsdir, cursorTheme))
            else:
                os.system('cd /usr/share/icons/ && tar -pcvzf %s/cursorTheme.tar.gz %s' % (self.hsdir, cursorTheme))
            if os.path.exists('/home/%s/.icons/%s' % (user, iconTheme)):
                os.system('cd /home/%s/.icons/ && tar -pcvzf %s/iconTheme.tar.gz %s' % (user, self.hsdir, iconTheme))
            else:
                os.system('cd /usr/share/icons/ && tar -pcvzf %s/iconTheme.tar.gz %s' % (self.hsdir, iconTheme))
            tconf = open('%s/gnome' % self.hsdir, 'w+')
            locparse.write(tconf)
            tconf.close()
        if self.b_progs:
            b_simple = self.construct_dialog(Gtk.MessageType.QUESTION, Gtk.ButtonsType.YES_NO, _('Would you like to view a simplified list of applications? (some less common programs may miss from the list)'), _("Ask"), 'switcher')
            print('Programs true')
            extendedApps = subprocess.check_output('apt-mark showmanual', shell=True, executable='/bin/bash')
            extendedApps = extendedApps.decode()
            extendedApps = extendedApps.split('\n')
            if b_simple:
                minimalApps = []
                for i in extendedApps:
                    if "acpi" in i or "avahi" in i or "alsa" in i or "bluez" in i or "cups" in i or "theme" in i or "fonts" in i or "gdm" in i or "gir1" in i or "grub" in i or "gstreamer" in i or "ubuntu" in i or "ibus" in i or "kernel" in i or "linux-headers-generic" in i or "linux-signed-generic" in i or "network-manager" in i:
                        pass
                    else:
                        minimalApps.append(i)
            self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
            self.builder.get_object('progs_box').pack_start(self.box, True, True, 0)
            if b_simple:
                for program in minimalApps:
                    if program == "" or program == None:
                        break
                    chker = Gtk.CheckButton(program)
                    chker.connect("toggled", self.on_prog_tog, program)
                    self.box.pack_start(chker, True, True, 0)
            else:
                for program in extendedApps:
                    if program == "" or program == None:
                        break
                    chker = Gtk.CheckButton(program)
                    chker.connect("toggled", self.on_prog_tog, program)
                    self.box.pack_start(chker, True, True, 0)
            self.box.show_all()
        if self.b_cron:
            print('Cron true')
            os.system('crontab -l > %s/crontab' % self.hsdir)
        if self.b_progs:
            if self.b_data == False:
                self.builder.get_object('prog_proc_but').set_label('Start backup')
            else:
                self.builder.get_object('prog_proc_but').set_label('Continue')
            self.switch_stack.set_visible_child(self.builder.get_object('scroll_progs'))
        elif self.b_data:
            self.switch_stack.set_visible_child(self.builder.get_object('scroll_dat'))
        else:
            self.crTask()

    # hswitcher clicked
    def on_ac_but_clicked(self, button):
        self.switch_stack.set_visible_child(self.builder.get_object('r_box'))
        self.stack.set_visible_child(self.builder.get_object('scroll_switcher'))

######################################################################################################################

    # hcontrol
    def row_activated(self, widget, row, col):
        relPos = self.tree.get_selection().get_selected_rows()[1][0][0]
        print(relPos)

    def mouse_click(self, widget, event):
        if event.button == 3:
            try:
                pthinfo = self.tree.get_path_at_pos(event.x, event.y)
                path,col,cellx,celly = pthinfo
                self.tree.grab_focus()
                self.tree.set_cursor(path,col,0)
                menu = Gtk.Menu()
                menu_item = Gtk.MenuItem.new_with_label('Delete job')
                menu_item.connect("activate", self.del_cur)
                menu.add(menu_item)
                menu.show_all()
                menu.popup_at_pointer()
            except:
                print('Not the best place to right-click bro!')
    
    def del_cur(self, action):
        cron  = CronTab(user=True)
        this = self.tree.get_selection().get_selected_rows()[1][0][0]
        print(this)
        print(cron[this])
        cron.remove(cron[this])
        cron.write()
        self.on_htools_but_clicked('button')

    def new_but_clicked(self, button):
        self.page = 0
        self.noMean = False
        self.builder.get_object('au_stack').set_visible_child(self.builder.get_object('cron_box'))
        self.on_cron_book_change_current_page('widget', 'box', self.page)
    
    def cancel_but_clicked(self, button):
        self.noMean = True
        self.builder.get_object('au_stack').set_visible_child(self.builder.get_object('au_box'))
    
    def cron_entr_changed(self, widget):
        print('man')
        atx = self.builder.get_object('cron_entr').get_text().split(' ')
        self.minu = atx[0]
        self.hour = atx[1]
        self.daym = atx[2]
        self.cmonth = atx[3]
        self.dayw = atx[4]

    def min_entr_changed(self, widget):
        self.minu = self.builder.get_object('min_entr').get_text()
    
    def hour_entr_changed(self, widget):
        self.hour = self.builder.get_object('hour_entr').get_text()
    
    def day_entr_changed(self, widget):
        self.daym = self.builder.get_object('day_entr').get_text()
    
    def month_choose_changed(self, widget):
        self.cmonth = self.builder.get_object('month_choose').get_active_text()

    def exec_choose_changed(self, widget):
        self.hardCron = self.builder.get_object('exec_choose').get_active_text()

    def on_cron_book_change_current_page(self, widget, box, page):
        print('Changed mode %s' % page)
        self.page = page
        self.noMean = True
        self.hardCron, self.minu, self.hour, self.daym, self.cmonth, self.dayw = "", "", "", "", "", ""
        if page == 0:
            print('simple')
            self.hardCron = self.builder.get_object('exec_choose').get_active_text()
        elif page == 1:
            print('adv')
            self.dayw = '*'
            self.minu = self.builder.get_object('min_entr').get_text()
            self.hour = self.builder.get_object('hour_entr').get_text()
            self.daym = self.builder.get_object('day_entr').get_text()
            self.cmonth = self.builder.get_object('month_choose').get_active_text()
        elif page == 2:
            print('man')
            atx = self.builder.get_object('cron_entr').get_text()
            if '@' not in atx:
                atx = atx.split(' ')
                self.minu = atx[0]
                self.hour = atx[1]
                self.daym = atx[2]
                self.cmonth = atx[3]
                self.dayw = atx[4]
            else:
                self.hardCron = atx
        self.noMean = False
        tC = futures.ThreadPoolExecutor(max_workers=2)
        tC.submit(self.getMeaning)
    
    def getMeaning(self):
        print('Getting meaning')
        while self.noMean == False:
            try:
                if self.cronCommand != "" and self.cronJob != "":
                    self.builder.get_object('done_but').set_sensitive(True)
                else:
                    self.builder.get_object('done_but').set_sensitive(False)
            except:
                self.builder.get_object('done_but').set_sensitive(False)
            time.sleep(0.1)
            if self.minu != "" and self.hour != "" and self.daym != "" and self.cmonth != "" and self.dayw != "":
                print('first if')
                cronMean = get_description(f"{self.minu} {self.hour} {self.daym} {self.cmonth} {self.dayw}")
                self.cronJob = f"{self.minu} {self.hour} {self.daym} {self.cmonth} {self.dayw}"
            elif self.hardCron != "":
                print('sec if')
                print(self.hardCron)
                if self.hardCron == "reboot" or self.hardCron == "yearly" or self.hardCron == "monthly" or self.hardCron == "weekly" or self.hardCron == "daily" or self.hardCron == "hourly":
                    print('sir if')
                    if self.hardCron == 'reboot':
                        cronMean = 'After reboot.'
                    else:
                        cronMean = f"Repeat {self.hardCron}."
                    self.cronJob = f"@{self.hardCron}"
                else:
                    print('xs else')
                    cronMean = "Invalid syntax!"
                    self.cronJob = ""
            else:
                print('xl else')
                cronMean = "Invalid syntax!"
                self.cronJob = ""
            self.cronCommand = self.builder.get_object('comm_entr').get_text()
            GLib.idle_add(self.builder.get_object('tx_lab').set_label, cronMean)
        print(cronMean)
        print(self.cronJob)
        print(self.cronCommand)
        print('stopmean')

    def on_done_but_clicked(self, button):
        print('Saving...')
        cron  = CronTab(user=True)
        job = cron.new(command=f"DISPLAY={dplenv} && {self.cronCommand}")
        job.setall(self.cronJob)
        cron.write()
        self.builder.get_object('au_stack').set_visible_child(self.builder.get_object('au_box'))
        self.on_htools_but_clicked('button')

    def on_htools_but_clicked(self, button):
        self.noMean = True
        cron  = CronTab(user=True)
        box = self.builder.get_object('au_box')
        try:
            box.remove(self.scrollable_treelist)
        except:
            pass
        storeCron = Gtk.ListStore(str, int)
        self.tree = Gtk.TreeView.new_with_model(storeCron)
        self.tree.connect("row-activated", self.row_activated)
        self.tree.connect("button_press_event", self.mouse_click)
        self.tree.set_reorderable(False)
        self.scrollable_treelist = Gtk.ScrolledWindow()
        self.scrollable_treelist.set_vexpand(True)
        self.scrollable_treelist.add(self.tree)
        box.pack_start(self.scrollable_treelist, True, True, 0)
        l = 0
        for job in cron:
            storeCron.append([str(job), l])
            l += 1
        print("First time")
        for i, column_title in enumerate(["Job", "ID"]):
            renderer = Gtk.CellRendererText(xalign=0)
            renderer.set_property("ellipsize", True)
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            if column_title == "Job":
                column.set_fixed_width(700)
                column.set_resizable(True)
            else:
                column.set_max_width(50)
                column.set_resizable(False)
            column.set_sort_column_id(i)
            self.tree.append_column(column)
        self.builder.get_object('control_box').show_all()
        self.stack.set_visible_child(self.builder.get_object('control_box'))

##################################################################################

    def findNew(self, urii, perPat, perVer):
        if self.stop:
            print('Aborted by user.')
            raise SystemExit
        reponse = urlopen(urii)
        dat = reponse.read()
        text = dat.decode('utf-8')
        pattern = re.findall(perPat, text)
        gentoo = pattern[0]
        pattern = ''.join(pattern)
        pattern = pattern.replace(".", "")
        pattern = re.findall(perVer, pattern)
        if 'fedora' in urii and 'iso' in urii:
            pattern = ''.join(pattern)
            pattern = pattern.replace('-', '').replace('x', '')
        pattern = list(map(int, pattern))
        try:
            pattern.remove(710)
            pattern.remove(710)
        except:
            pass
        pattern.sort()
        vers = pattern[-1]
        vers = [int(i) for i in str(vers)]
        if 'fedora' in urii and 'iso' in urii:
            vers = [str(i) for i in pattern]
            vers = int("".join(vers))
            vers = [int(d) for d in str(vers)]
        return vers, gentoo

    # fetch download sizes
    def getSize(self):
        print('Getting Links...')
        reponse = urlopen("http://mirrors.evowise.com/archlinux/iso/latest")
        dat = reponse.read()
        text = dat.decode('utf-8')
        pattern = re.findall(r'archlinux-+[\d]+[\d]+[\d]+[\d]+.+[\d]+[\d]+.+[\d]+[\d]+-x86_64.iso">', text)
        print(pattern)
        vers = pattern[0].replace('"', '').replace('>', '')
        archLink = 'http://mirrors.evowise.com/archlinux/iso/latest/%s' % vers

        vers, misc = self.findNew("http://releases.ubuntu.com",
                r'"+[\d]+.[\d]+/', r'[\d]+[\d]+[\d]+[\d]')
        # global ubuntuLink
        ubuntuLink = 'http://releases.ubuntu.com/%s%s.%s%s/ubuntu-%s%s.%s%s-desktop-amd64.iso' % (
            vers[0], vers[1], vers[2], vers[3], vers[0], vers[1], vers[2], vers[3])

        vers, misc = self.findNew("http://mirrors.evowise.com/linuxmint/stable/",
                r'"+[\d]+.[\d]+/', r'[\d]+[\d]+[\d]')
        # global mintLink
        mintLink = 'http://mirrors.evowise.com/linuxmint/stable/%s%s.%s/linuxmint-%s%s.%s-cinnamon-64bit.iso' % (
            vers[0], vers[1], vers[2], vers[0], vers[1], vers[2])

        vers, misc = self.findNew("http://mirror.inode.at/data/deepin-cd/",
                r'"+[\d]+.[\d]+/', r'[\d]+[\d]+[\d]')
        # global deepinLink
        deepinLink = 'http://mirror.inode.at/data/deepin-cd/%s%s.%s%s/deepin-%s%s.%s%s-amd64.iso' % (
            vers[0], vers[1], vers[2], vers[3], vers[0], vers[1], vers[2], vers[3])

        vers, misc = self.findNew("https://cdimage.debian.org/images/unofficial/non-free/images-including-firmware/current-live/amd64/iso-hybrid/",
                r'debian-live-+[\d]+[\d]+.[\d]+.[\d]', r'[\d]+[\d]+[\d]')
        # global debianLink
        debianLink = 'https://cdimage.debian.org/images/unofficial/non-free/images-including-firmware/current-live/amd64/iso-hybrid/debian-live-%s%s.%s.%s-amd64-cinnamon+nonfree.iso' % (
            vers[0], vers[1], vers[2], vers[3])

        # global steamosLink
        steamosLink = 'http://repo.steampowered.com/download/SteamOSDVD.iso'

        vers, misc = self.findNew("http://fedora.inode.at/releases/", r'"+[\d]+/', r'[\d]+[\d]')
        versf, misc = self.findNew('http://fedora.inode.at/releases/%s%s/Workstation/x86_64/iso' % (vers[0], vers[1]), r'-+[\d]+.+[\d]+.', r'-+[\d]+[\d]+-x')
        # global fedoraLink
        fedoraLink = 'http://fedora.inode.at/releases/%s%s/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-%s%s-%s.%s.iso' % (
            vers[0], vers[1], vers[0], vers[1], versf[0], versf[2])

        # global opensuseLink
        opensuseLink = 'https://download.opensuse.org/tumbleweed/iso/openSUSE-Tumbleweed-DVD-x86_64-Current.iso'

        vers, misc = self.findNew("https://solus.veatnet.de/iso/images", r'"+[\d]+.[\d]+/', r'[\d]+[\d]')
        # global solusLink
        solusLink = 'https://solus.veatnet.de/iso/images/%s.%s/Solus-%s.%s-Budgie.iso' % (vers[0], vers[1], vers[0], vers[1])

        vers, misc = self.findNew("http://distfiles.gentoo.org/releases/amd64/autobuilds/current-install-amd64-minimal/",
                r'[\d]+[\d]+[\w]+[\d][\w]', r'[\d]+[\d]')
        # global gentooLink
        gentooLink = 'http://distfiles.gentoo.org/releases/amd64/autobuilds/current-install-amd64-minimal/install-amd64-minimal-%s.iso' % misc

        vers, misc = self.findNew("http://www.linuxfromscratch.org/lfs/downloads/",
                r'[\d]+.[\d]+-systemd/', r'[\d]+[\d]')
        # global lfsLink
        lfsLink = 'http://www.linuxfromscratch.org/lfs/downloads/%s.%s-systemd/LFS-BOOK-%s.%s-systemd.pdf' % (
            vers[0], vers[1], vers[0], vers[1])

        self.uriDict = {'downl_mint': mintLink, 'downl_ubuntu': ubuntuLink, 'downl_solus': solusLink, 'downl_deepin': deepinLink, 'downl_steamos': steamosLink,
                'downl_deb': debianLink, 'downl_fedora': fedoraLink, 'downl_suse': opensuseLink, 'downl_gentoo': gentooLink, 'downl_arch': archLink, 'downl_lfs': lfsLink}
        print('Updated linklist!!')
        print("Getting size...")
        # dlistlen is the length of dlist
        for i in range(dlistLen):
            if self.stop:
                print('Aborted by user.')
                raise SystemExit
            # dlist is distro list (contains all distro names), cbut is current button
            cBut = self.builder.get_object(dlist[i])
            # get url from dictionary
            url = self.uriDict[dlist[i]]
            try:
                u = urlopen(url)
                time.sleep(0.1)
                file_size = int(u.getheader('Content-Length'))
                # convert to MB
                file_size = Decimal(int(file_size) / 1024 / 1024)
                GLib.idle_add(cBut.set_label, "Download (%s MB)" %
                            round(file_size, 1))  # set download label
                # store value in cache
                self.cache[dlist[i]] = round(file_size, 1)
            except:
                print('URL ERROR!')
                GLib.idle_add(cBut.set_label, _("Server error"))
                self.cache[dlist[i]] = round(0, 1)

    def on_db_but_clicked(self, button):
        distro_box = self.builder.get_object('distro_box')
        thss = len(self.tC2._threads)
        print(thss)
        if not self.cache and thss == 0:                                                             # if not fetched already
            # disable
            self.scanningUrl = True
            self.state = False
            self.toggle(fn)  # all buttons
            # init non-normal thread (getting sizes)
            f = self.tC2.submit(self.check)
            self.where = 'gs'
            f.add_done_callback(self.chk_again)
        elif not self.scanningUrl:
            r = 0
            for i in dlist:
                cBut = self.builder.get_object(dlist[r])        # if loaded
                # load from cache
                cBut.set_label(_("Download (%s MB)") % self.cache[i])
                r += 1
        self.stack.set_visible_child(distro_box)

    # on about ...
    def on_about_but_clicked(self, button):
        scroll_about = self.builder.get_object('scroll_about')
        self.stack.set_visible_child(scroll_about)

    def home_clicked(self, button):  # back button
        self.noMean = True
        scroll_home = self.builder.get_object('scroll_home')
        self.stack.set_visible_child(scroll_home)

    def on_page(self, button):                                      # general descrition page
        text = self.builder.get_object('page_txt')
        page = self.builder.get_object('scroll_desc')
        back_button = self.builder.get_object(
            'back_button')        # back but not to home
        # hide rew link and web link when not in distro boutique
        rew_link = self.builder.get_object('rew_link')
        rew_link.hide()
        web_link = self.builder.get_object('web_link')
        web_link.hide()
        # if yes, show. bp indicates the current page, regarding its meaning I have no idea
        if self.bp == _("Distro Boutique"):
            rew_link.show()
            web_link.show()
        text.set_text(self.label)
        back_button.set_label(self.bp)
        self.stack.set_visible_child(page)

    # when going back but not to home
    def on_back_button_clicked(self, button):
        if self.bp == _("App Spotlight"):                                 # go back to app spotlight or distro boutique
            self.button_clicked(button)
        elif self.bp == _("Distro Boutique"):
            distro_box = self.builder.get_object('distro_box')
            self.stack.set_visible_child(distro_box)
        else:
            print('ERROR')

    def on_rew_link_clicked(self, button):
        webbrowser.open_new(self.rew)

    def on_web_link_clicked(self, button):
        webbrowser.open_new(self.web)

# What to do on button clicks
    def general_clicks(self, button):
        btn = Gtk.Buildable.get_name(button)
        self.lilFunc(name=liLi[btn][0], comm1=liLi[btn][1], extra=liLi[btn][2], runDep=liLi[btn][3], buildDep=liLi[btn][4])

    def on_msoffice_but_clicked(self, button):
        webbrowser.open_new("https://office.com")

    def on_goffice_but_clicked(self, button):
        webbrowser.open_new("https://docs.google.com")

# End of button clicks

# Descriptions

    def displayDesc(self, x, button):
        self.label = d.descList[x]
        self.bp = d.descDict[self.label]
        if self.bp == _('Distro Boutique'):
            self.web = d.webDict[self.label]
            self.rew = d.vidDict[self.label]
        self.on_page(button)
    
    def applay(self, button):
        fLili = Gtk.Buildable.get_name(button)
        self.displayDesc(liLi['%s_but' % fLili][5], button)

    def on_msoffice_clicked(self, button):
        self.displayDesc(9, button)

    def on_goffice_clicked(self, button):
        self.displayDesc(10, button)
    
    def dissplay(self, button):
        fLola = Gtk.Buildable.get_name(button)
        self.displayDesc(loLa[fLola][1], button)

# End of descriptions
# _____________________________________________________________________ END OF GUI ____________________________________________________________________#

if __name__ == "__main__":
    ## Config section ##
    parser = ConfigParser()
    confP = '/home/%s/.config/hsuite.conf' % user
    if os.path.exists(confP):
        print('Configured already')
        parser.read(confP)
        distro = parser.get('system', 'distro')
        v = parser.get('hsuite', 'v')
        dist = parser.get('system', 'dist')
        app = GUI()  # variable to call GUI class
    else:
        print('Config not found')
        # Detect distro
        dist = os.popen('uname -a').read()          # Get distro name
        if 'Ubuntu' in dist:
            distro = 'Ubuntu'
        elif 'solus' in dist:
            distro = 'Solus'
        elif 'Debian' in dist:
            distro = 'Debian'
        elif 'deepin' in dist:
            distro = 'Debian'
            print('W: Not fully compatible with Deepin!')
            app = GUI()
            app.construct_dialog(Gtk.MessageType.WARNING, Gtk.ButtonsType.OK, _("Your distro is detected as Deepin. This distro is not fully tested, you may encounter some problems with the program. Currently tested on distros: Ubuntu (bionic, eoan), Debian (buster)."), _("Attention!"), 'general')
        else:
            distro = ''
            app = GUI()
            print('E: Complete incompatibility!')
            app.construct_dialog(Gtk.MessageType.ERROR, Gtk.ButtonsType.OK, _("Can not detect your distro. Currently compatible with distros: Ubuntu (bionic, eoan), Debian (buster) and everything based on them. Aborting now."), _("Attention!"), 'general')
            raise SystemExit
        app = GUI()
        parser.add_section('system')
        parser.add_section('hsuite')
        parser.set('system', 'distro',  distro)
        parser.set('hsuite', 'v', version)
        parser.set('system', 'dist', dist)
        file = open(confP, "w+")
        parser.write(file)
        file.close()
    # Own module for root prompt and background installation
    import osLayer
    osLayer.init(distro)
    osLayer.user = user
    ## Colors (button)
    provider = Gtk.CssProvider()
    colors = Gio.File.new_for_path('colors.css')
    provider.load_from_file(colors)
    Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
    if v != version and v != '':
        app.construct_dialog(Gtk.MessageType.INFO, Gtk.ButtonsType.OK, _("HSuite has been updated to %s. For changelog click the button below." % version), _("Information"), 'custom')
        os.system('rm %s' % confP)
    # Print info to debug
    print("Current date: %s" % today)
    print("Current day: %s" % day)
    print("Current month: %s" % month)
    print("Current year: %s" % year)
    print("Name of non-root user: %s" % user)
    print('---BEGIN---')
    print("Content of working directory: %s" % str(wer))
    print("---END---")
    print("Output of $uname -a$ : %s" % dist)
    print("Detected distro: %s" % distro)
    print('Updated? : %s' % v)
    Gtk.main()  # execute main GTK window