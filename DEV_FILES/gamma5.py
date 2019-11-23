#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#______________________________________________________________________________________________ BEGINNING OF INIT _________________________________________________________________________#


### Import modules ###


## Set minimum required versions
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')

import gi
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

import common as g # For global values


### Declare global variables ###


## Date
g.today = date.today()
g.month = g.today.strftime("%m")
g.day = g.today.strftime("%d")
g.year = g.today.strftime("%y")

## Detect distro
dist = os.popen('uname -a').read() # Get distro name
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
g.runE = False # To check if a download is already in progress or not
fn = 'sth' # It's declared because of some functions which ones are called from concurrent future
g.Tdownl = '' # The name of the currently in progress download
g.cache = [] # Array that contains the fetched sizes of the ISOs
g.shDict = {'downl_mint' : 'True', 'downl_ubuntu' : 'True', 'downl_solus' : 'True', 'downl_elementary' : 'True', 'downl_zorin' : 'True', 'downl_deepin' : 'True', 'downl_steamos' : 'True', 'downl_deb' : 'True', 'downl_fedora' : 'True', 'downl_suse' : 'True', 'downl_gentoo' : 'True', 'downl_arch' : 'True', 'downl_lfs' : 'True',} # Dictionary for current state of download buttons (clickable or not)
g.dlist = ['downl_mint', 'downl_ubuntu', 'downl_zorin', 'downl_solus', 'downl_elementary', 'downl_deepin', 'downl_steamos', 'downl_fedora', 'downl_suse', 'downl_deb', 'downl_arch', 'downl_gentoo', 'downl_lfs'] # List of distros
g.dlistLen = len(g.dlist) # The number of distros

# Links

def findNew():
    reponse = urlopen(urii)
    dat = reponse.read()
    text = dat.decode('utf-8')
    pattern = re.findall(r'%s' % perPat, text)
    print(pattern)
    pattern = ''.join(pattern)
    print(pattern)
    pattern = pattern.replace(".", "")
    pattern = re.findall(r'%s' % perVer, pattern)
    print(pattern)
    pattern = list(map(int, pattern))
    print(pattern)
    pattern.sort()
    print(pattern)
    g.vers = pattern[-1]
    print(g.vers)
    g.vers = [int(i) for i in str(g.vers)]
    print(g.vers)

if g.day == "01":
    aMonth = int(g.month, button) - 1
archLink = 'http://mirrors.evowise.com/archlinux/iso/%s.%s.01/archlinux-%s.%s.01-x86_64.iso' % (g.year, aMonth, g.year, aMonth)

urii = "http://releases.ubuntu.com"
perPat = '"+[\d]+.[\d]+/'
perVer = '[\d]+[\d]+[\d]+[\d]'
verForm = '[\d]+[\d]'
findNew()
ubuntuLink = 'http://releases.ubuntu.com/%s%s.%s%s/ubuntu-%s%s.%s%s-desktop-amd64.iso' % (g.vers[0], g.vers[1], g.vers[2], g.vers[3], g.vers[0], g.vers[1], g.vers[2], g.vers[3])

urii = "http://mirrors.evowise.com/linuxmint/stable/"
perPat = '"+[\d]+.[\d]+/'
perVer = '[\d]+[\d]+[\d]'
verForm = '[\d]+[\d]'
findNew()
mintLink = 'http://mirrors.evowise.com/linuxmint/stable/%s%s.%s/linuxmint-%s%s.%s-cinnamon-64bit.iso' % (g.vers[0], g.vers[1], g.vers[2], g.vers[0], g.vers[1], g.vers[2])

urii = "http://mirror.inode.at/data/deepin-cd/"
perPat = '"+[\d]+.[\d]+/'
perVer = '[\d]+[\d]+[\d]'
verForm = '[\d]+[\d]'
findNew()
deepinLink = 'http://mirror.inode.at/data/deepin-cd/%s%s.%s%s/deepin-%s%s.%s%s-amd64.iso' % (g.vers[0], g.vers[1], g.vers[2], g.vers[3], g.vers[0], g.vers[1], g.vers[2], g.vers[3])

urii = "https://cdimage.debian.org/images/unofficial/non-free/images-including-firmware/current-live/amd64/iso-hybrid/"
perPat = 'debian-live-+[\d]+[\d]+.[\d]+.[\d]'
perVer = '[\d]+[\d]+[\d]'
verForm = '[\d]+[\d]'
findNew()
debianLink = 'https://cdimage.debian.org/images/unofficial/non-free/images-including-firmware/current-live/amd64/iso-hybrid/debian-live-%s%s.%s.%s-amd64-cinnamon+nonfree.iso' % (g.vers[0], g.vers[1], g.vers[2], g.vers[3])

steamosLink = 'http://repo.steampowered.com/download/SteamOSDVD.iso'

elementaryLink = 'https://ams3.dl.elementary.io/download/MTU3Mjk2NDY5NA==/elementaryos-5.0-stable.20181016.iso'

urii = "https://sourceforge.net/projects/zorin-os/files/"
perPat = 'files/+[\d]+/download'
perVer = '[\d]+[\d]'
verForm = '[\d]+[\d]'
findNew()
zorinosLink = 'https://netcologne.dl.sourceforge.net/project/zorin-os/%s%s/Zorin-OS-%s%s-Core-64-bit-r1.iso' % (g.vers[0], g.vers[1], g.vers[0], g.vers[1])

urii = "http://fedora.inode.at/releases/"
perPat = '"+[\d]+/'
perVer = '[\d]+[\d]'
verForm = '[\d]+[\d]'
findNew()
fedoraLink = 'http://fedora.inode.at/releases/%s%s/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-%s%s-1.9.iso' % (g.vers[0], g.vers[1], g.vers[0], g.vers[1])

opensuseLink = 'https://download.opensuse.org/tumbleweed/iso/openSUSE-Tumbleweed-DVD-x86_64-Current.iso'

urii = "http://fedora.inode.at/releases/"
perPat = '"+[\d]+/'
perVer = '[\d]+[\d]'
verForm = '[\d]+[\d]'
findNew()

solusLink = 'http://solus.veatnet.de/iso/images/4.0/Solus-4.0-Budgie.iso'

gentooLink = 'http://distfiles.gentoo.org/releases/amd64/autobuilds/20191030T214502Z/install-amd64-minimal-20191030T214502Z.iso'
lfsLink = 'http://www.linuxfromscratch.org/lfs/downloads/stable-systemd/LFS-BOOK-9.0-systemd.pdf'
g.uriDict = {'downl_mint' : mintLink, 'downl_ubuntu' : ubuntuLink, 'downl_solus' : solusLink, 'downl_elementary' : elementaryLink, 'downl_zorin' : zorinosLink, 'downl_deepin' : deepinLink, 'downl_steamos' : steamosLink, 'downl_deb' : debianLink, 'downl_fedora' : fedoraLink, 'downl_suse' : opensuseLink, 'downl_gentoo' : gentooLink, 'downl_arch' : archLink, 'downl_lfs' : lfsLink}

## Used with App Spotlight
pkg = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"] # For AUR builds (this will be depracted in the future)
g.spinning = False # Check if the spinner is spinning or not
g.scanner = True # Check if PKG cache is already in memory or not

## Used generally
UI_FILE = "hsuite.glade"
g.user = os.popen("logname").read() # Getting the name of the non-root user
g.user = g.user.rstrip() # Edit to only contain the name itself
xorw = os.popen('echo $XDG_SESSION_TYPE').read() # Get current session type
if "x" in xorw: # It's Xorg, so it wokrs with gestures'
    g.lehete = "You need to reboot or log in and out again after the install has been completed to apply all changes."
else: # It is Wayland, so it won't work
    g.lehete = "You can currently only use this feature with x11 based desktop. It does not support Wayland."
wer = os.popen('ls').read() # Discover the current working dir

## Print info to debug
print("Current date: "g.today)
print("Current day: "g.day)
print("Current month: "g.month)
print("Current year: "g.year)
print("Name of non-root user: "g.user)
print("Content of working directory: "str(wer))
print("Output of $uname -a$ : "dist)
print("Detected distro: "g.distro)


#______________________________________________________________________________________________ END OF INIT ______________________________________________________________________________________#
