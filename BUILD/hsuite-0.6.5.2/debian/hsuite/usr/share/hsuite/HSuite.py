#! /usr/bin/python3
# -*- coding: utf-8 -*-

#________________________________________________________________________________ BEGINNING OF INIT ____________________________________________________________#


# Version of the program
version = 'HSuite v0.6.5 | Emerald'
v = ''

### Import modules ###

# Set program root location
import os, subprocess, gettext, locale, gi, re, webbrowser, time, notify2
pathCheck = os.popen('ls /usr/share/hsuite/').read()
if 'hsuite' in pathCheck:
    fdir = "/usr/share/hsuite/"
    print(fdir)
    os.chdir(fdir)
    print('Running in production mode.')
else:
    fdir = "/home/daniel/GitRepos/hsuite/DEV_FILES/"
    print(fdir)
    os.chdir(fdir)
    print('Running in development mode.')
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
token = '82a201fb7ce03647870@37a6b5f7beb4eeb68f201'
token = token.replace('@', '')
g = Github(token)
# Config
from configparser import ConfigParser
# Module for opening webbrowser
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


### Declare global variables ###


# Date
today = date.today()
month = today.strftime("%m")
day = today.strftime("%d")
year = today.strftime("%Y")

# Getting the name of the non-root user
user = os.popen("who|awk '{print $1}'r").read()
machine = os.popen("hostname").read()
# Edit to only contain the name itself
user = user.rstrip()
user = user.split('\n')[0]
machine = machine.rstrip()
machine = machine.split('\n')[0]

## Config section ##

parser = ConfigParser()

confP = '/home/%s/.config/hsuite.conf' % user
if os.path.exists(confP):
    print('Configured already')
    parser.read(confP)
    distro = parser.get('system', 'distro')
    v = parser.get('hsuite', 'v')
    dist = parser.get('system', 'dist')
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
    # elif 'MANJARO' in dist:
    #     distro = 'Arch'
    #     print('W: Not fully compatible with Manjaro!')
    #     mantxt = _("Your distro is detected as Manjaro.\nThis distro is not fully tested,\nyou may encounter some problems\nwith the program. Currently tested\non distros: Arch, Ubuntu (bionic, eoan), Debian (buster).")
    #     os.system('zenity --warning --text=%s --ellipsize' % mantxt)
    elif 'deepin' in dist:
        distro = 'Debian'
        print('W: Not fully compatible with Deepin!')
        deptxt = _("Your distro is detected as Deepin.\nThis distro is not fully\ntested, you may encounter some\nproblems with the program. Currently tested\non distros: Ubuntu (bionic, eoan), Debian (buster).")
        os.system('zenity --warning --text=%s --ellipsize' % deptxt)
    else:
        print('E: Complete incompatibility!')
        kiltxt = _("Can not detect your distro.\nCurrently compatible with distros:\nUbuntu (bionic, eoan), Debian (buster)\n and everything based on them. Aborting now.")
        os.system('zenity --error --text=%s --ellipsize' % kiltxt)
        raise SystemExit
    parser.add_section('system')
    parser.add_section('hsuite')
    parser.set('system', 'distro',  distro)
    parser.set('hsuite', 'v', version)
    parser.set('system', 'dist', dist)
    file = open(confP, "w+")
    parser.write(file)
    file.close()

if distro == 'Ubuntu' or distro == 'Debian':
    import apt
    from aptdaemon import client, enums
    from aptdaemon.gtk3widgets import AptProgressBar

# Own module for root prompt and background installation
import osLayer
osLayer.init(distro)
osLayer.user = user

## Colors (button)
provider = Gtk.CssProvider()
colors = Gio.File.new_for_path('colors.css')
provider.load_from_file(colors)
Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)


# Used with Distro Boutique
# To check if a download is already in progress or not
runE = False
# It's declared because of some functions which ones are called from concurrent future
fn = 'sth'
# The name of the currently in progress download
Tdownl = ''
# Array that contains the fetched sizes of the ISOs
cache = []
shDict = {'downl_mint': 'True', 'downl_ubuntu': 'True', 'downl_solus': 'True', 'downl_zorin': 'True', 'downl_deepin': 'True', 'downl_steamos': 'True', 'downl_deb': 'True',
          'downl_fedora': 'True', 'downl_suse': 'True', 'downl_gentoo': 'True', 'downl_arch': 'True', 'downl_lfs': 'True', }  # Dictionary for current state of download buttons (clickable or not)
dlist = ['downl_mint', 'downl_ubuntu', 'downl_zorin', 'downl_solus', 'downl_deepin', 'downl_steamos',
         'downl_fedora', 'downl_suse', 'downl_deb', 'downl_arch', 'downl_gentoo', 'downl_lfs']
namDict = {'downl_mint' : 'Linux Mint', 'downl_ubuntu' : 'Ubuntu', 'downl_zorin' : 'Zorin OS', 'downl_solus' : 'Solus Linux', 'downl_deepin' : 'Deepin Linux', 'downl_steamos' : 'SteamOS',
         'downl_fedora' : 'Fedora', 'downl_suse' : 'openSUSE', 'downl_deb' : 'Debian', 'downl_arch' : 'Arch', 'downl_gentoo' : 'Gentoo', 'downl_lfs' : 'Linux from Scratch (LFS)'}
# List of distros
dlistLen = len(dlist)                   # The number of distros

# Used with App Spotlight
pkg = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
       "o", "p"]          # For AUR builds (this will be depracted in the future)
# Check if PKG cache is already in memory or not
scanner = True
appList = ['opera-stable', 'barrier', 'google-chrome-stable', 'epiphany-browser', 'firefox', 'vivaldi-stable', 'wps-office', 'libreoffice', 'onlyoffice-desktopeditors', 'softmaker-freeoffice-2018', 'gedit', 'emacs', 'code', 'atom', 'sublime-text', 'geany', 'skypeforlinux', 'discord', 'telegram-desktop', 'signal-desktop', 'hexchat',
           'franz', '0ad', 'supertux', 'lutris', 'playonlinux', 'steam', 'minecraft-launcher', 'popsicle', 'woeusb', 'winehq-stable', 'virtualbox-6.1', 'gparted', 'fusuma', 'audacity', 'deja-dup', 'timeshift', 'teamviewer', 'gnome-boxes', 'supertuxkart']                                                                        # The list with the debian app names
# archDict = {'opera-stable': 'opera', 'barrier': 'barrier', 'google-chrome-stable': 'google-chrome', 'epiphany-browser': 'epiphany ', 'firefox': 'firefox', 'vivaldi-stable': 'vivaldi', 'wps-office': 'wps-office', 'libreoffice': 'libreoffice-fresh', 'onlyoffice-desktopeditors': 'onlyoffice-bin', 'softmaker-freeoffice-2018': 'freeoffice', 'gedit': 'gedit', 'emacs': 'emacs ', 'code': 'code 1', 'atom': 'atom ', 'sublime-text': 'sublime-text', 'geany': 'geany', 'skypeforlinux': 'skypeforlinux-stable-bin', 'discord': 'discord', 'telegram-desktop': 'telegram-desktop', 'signal-desktop': 'signal-desktop',
#             'hexchat': 'hexchat', 'franz': 'franz', '0ad': '0ad', 'supertux': 'supertux', 'lutris': 'lutris', 'playonlinux': 'playonlinux', 'steam': 'steam', 'minecraft-launcher': 'minecraft-launcher', 'popsicle': 'popsicle-git', 'woeusb': 'woeusb', 'winehq-stable': 'wine', 'virtualbox-6.1': 'virtualbox', 'gparted': 'gparted', 'fusuma': 'fusuma', 'audacity': 'audacity', 'deja-dup': 'deja-dup', 'timeshift': 'timeshift', 'teamviewer': 'TeamViewer', 'gnome-boxes': 'gnome-boxes', 'supertuxkart': 'supertuxkart'}                             # The dictionary with the context of debname:archname
butDict = {'opera-stable': 'opera', 'barrier': 'barr', 'google-chrome-stable': 'chrome', 'epiphany-browser': 'web', 'firefox': 'firefox', 'vivaldi-stable': 'vivaldi', 'wps-office': 'woffice', 'libreoffice': 'loffice', 'onlyoffice-desktopeditors': 'ooffice', 'softmaker-freeoffice-2018': 'foffice', 'gedit': 'gedit', 'emacs': 'gnu', 'code': 'vscode', 'atom': 'atom', 'sublime-text': 'stedit', 'geany': 'geany', 'skypeforlinux': 'skype', 'discord': 'discord', 'telegram-desktop': 'telegram',
           'signal-desktop': 'signal', 'hexchat': 'hex', 'franz': 'franz', '0ad': 'ad', 'supertux': 'tux', 'lutris': 'lutris', 'playonlinux': 'pol', 'steam': 'steam', 'minecraft-launcher': 'mc', 'popsicle': 'pops', 'woeusb': 'woe', 'winehq-stable': 'wine', 'virtualbox-6.1': 'vbox', 'gparted': 'gparted', 'fusuma': 'gest', 'audacity': 'auda', 'deja-dup': 'deja', 'timeshift': 'tims', 'teamviewer': 'tw', 'gnome-boxes': 'box', 'supertuxkart': 'skart'}                                # Dictionary with the context of debname:humanName
appListLen = len(appList)                           # Number of apps
statDict = {'Opera': '', 'Chrome': '', 'Web': '', 'Firefox': '', 'Vivaldi': '', 'Edge': '', 'WPS Office': '', 'Libreoffice': '', 'Only Office': '', 'Free Office': '', 'Gedit': '', 'GNU Emacs': '', 'VS Code': '', 'Atom Editor': '', 'Sublime Text Editor': '', 'Geany': '', 'Skype': '', 'Discord': '', 'Telegram': '', 'Signal': '', 'HexChat': '', 'Franz': '',
            '0 A.D.': '', 'SuperTuxKart': '', 'SuperTux': '', 'Lutris': '', 'Barrier': '', 'Play On Linux': '', 'Steam': '', 'Minecraft': '', 'Popsicle': '', 'WoeUSB': '', 'Wine': '', 'Virtualbox-6.1': '', 'GParted': '', 'fusuma': '', 'Audacity': '', 'Déja-Dup': '', 'Timeshift': '', 'TeamViewer': '', 'Gnome Boxes': ''}  # store the status (installed or not)
layDict = {'opera-stable': 'Opera', 'google-chrome-stable': 'Chrome', 'epiphany-browser': 'Web', 'firefox': 'Firefox', 'vivaldi-stable': 'Vivaldi', 'dikk': 'Edge', 'wps-office': 'WPS Office', 'libreoffice': 'Libreoffice', 'onlyoffice-desktopeditors': 'Only Office', 'softmaker-freeoffice-2018': 'Free Office', 'gedit': 'Gedit', 'emacs': 'GNU Emacs', 'code': 'VS Code', 'atom': 'Atom Editor', 'sublime-text': 'Sublime Text Editor', 'geany': 'Geany', 'skypeforlinux': 'Skype', 'discord': 'Discord', 'telegram-desktop': 'Telegram', 'signal-desktop': 'Signal', 'hexchat': 'HexChat',
           'franz': 'Franz', '0ad': '0 A.D.', 'supertux': 'SuperTux', 'supertuxkart': 'SuperTuxKart', 'lutris': 'Lutris', 'barrier': 'Barrier', 'playonlinux': 'Play On Linux', 'steam': 'Steam', 'minecraft-launcher': 'Minecraft', 'popsicle': 'Popsicle', 'woeusb': 'WoeUSB', 'winehq-stable': 'Wine', 'virtualbox-6.1': 'Virtualbox', 'gparted': 'GParted', 'fusuma': 'fusuma', 'audacity': 'Audacity', 'deja-dup': 'Déja-Dup', 'timeshift': 'Timeshift', 'teamviewer': 'TeamViewer', 'gnome-boxes': 'Gnome Boxes'}                                          # debname:displayName
aurList = ['google-chrome', 'vivaldi', 'wps-office', 'onlyoffice-bin', 'freeoffice', 'signal-desktop', 'franz', 'minecraft-launcher', 'popsicle-git', 'woeusb', 'timeshift', 'skypeforlinux-stable-bin', 'barrier']
specDList = ['']

# Used generally
tC2 = futures.ThreadPoolExecutor(max_workers=2)
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
scanningUrl = False
cPkg = ''
where = ''
net = ''
insList = ''
label = ''
bp = ''
web = ''
rew = ''
uriDict = {}
state = ''
vers = ''
gentoo = ''
rmE = ''
quit = ''
stop = False
orig = ''
m = ''
tempInd = ''
_stop_event = ''
browserholder = ''
stack = ''
window = ''

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

if v != version and v != '':
    uptxt = _("HSuite has been updated to %s.\nFor changelog visit https://swanux.github.io/hsuite/" % version)
    os.system('zenity --info --text=%s --ellipsize' % uptxt)
    os.system('rm %s' % confP)


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
        global _stop_event
        _stop_event = False

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
            changelog = "restore (1.0-1) unstable; urgency=medium\n\n  * Initial Release\n\n -- %s <%s@%s>  %s" % (user, user, machine, time.strftime("%a, %d %b %Y %H:%M:%S +0200"))
            change_file = open("/home/%s/hswitcher/BUILD/restore-1.0/debian/changelog" % user, "w")
            change_file.write(changelog)
            change_file.close()
            compat_file = open("/home/%s/hswitcher/BUILD/restore-1.0/debian/compat" % user, "w")
            compat_file.write("11")
            compat_file.close()
            bds = "debhelper (>= 11)"
            print('DS_HERE')
            control = "Source: restore\nSection: metapackages\nPriority: optional\nMaintainer: %s <%s@%s>\nBuild-Depends: %s\nStandards-Version: 1.0-1\n\nPackage: restore\nArchitecture: amd64\nDepends: tar, %s\nDescription: Backup by HSwitcher\n Backup by HSwitcher. Just install it to use, then remove." % (user, user, machine, bds, self.ds)
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
        global _stop_event
        _stop_event = True
        print("stop func")


class GUI:
    count = 0
    def __init__(self):                                             # Init the main gui
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
        global stack
        stack = self.builder.get_object('stack')
        global window
        window = self.builder.get_object(
            'window')                  # Get the main window
        # window.connect('check-resize', self.on_resize)

        if os.geteuid() == 0:
            # Indicate if runnung as root or not
            window.set_title(version+' (as superuser)')
        else:
            window.set_title(version)
        # Display the program
        self.progBox = self.builder.get_object('progBox')
        if distro == 'Ubuntu' or distro == 'Debian':
            self.dia = AptProgressBar()
        else:
            self.dia = Gtk.ProgressBar()
        self.progBox.pack_start(self.dia, True, True, 0)
        window.show_all()
        GLib.idle_add(self.dia.hide)
    
    # def on_resize(self, e):
    #     time.sleep(0.01)
    #     sx, sy = window.get_size()
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
        global stop
        global tS
        # Getting the window position
        x, y = window.get_position()
        # Get the size of the window
        sx, sy = window.get_size()
        dialogWindow = Gtk.MessageDialog(parent=window, modal=True, destroy_with_parent=True, message_type=Gtk.MessageType.QUESTION, buttons=Gtk.ButtonsType.YES_NO, text=_('Do you really would like to exit now?'))
        # set the title
        dialogWindow.set_title(_("Prompt"))
        dsx, dsy = dialogWindow.get_size()                          # get the dialogs size
        # Move it to the center of the main window
        dialogWindow.move(x+((sx-dsx)/2), y+((sy-dsy)/2))
        dx, dy = dialogWindow.get_position()                        # set the position
        print(dx, dy)
        dialogWindow.show_all()
        res = dialogWindow.run()                                    # save the response
        if res == Gtk.ResponseType.YES:                             # if yes ...
            print('OK pressed')
            dialogWindow.destroy()
            code = 'force'
            if osLayer.alive:
                text = _("Do you really would like to abort now? It could end up with a broken program. If you decide to abort, then it is recommended to remove %s manually.") % cPkg
                code = self.abort('install', text)
            if quit == False:
                text = _("Do you really would like to abort now? Download is currently in progress for %s.") % namDict[Tdownl]
                code = self.abort('download', text)
            if code == 'force':
                stop = True
                try:
                    tS.shutdown()
                except:
                    pass
                raise SystemExit
            else:
                dialogWindow.destroy()
                return True
        elif res == Gtk.ResponseType.NO:                            # if no ...
            print('No pressed')
            dialogWindow.destroy()                                  # destroy dialog
            return True                                             # end function
        else:
            dialogWindow.destroy()                                  # destroy dialog
            return True                                             # end function

###################################################################################

    # Set the button colors
    def colorer(self, gbut, name):
        # Call function to check if apps are installed or not
        status = self.OnCheck(name)
        # set the button label depending on this
        GLib.idle_add(gbut.set_label, status)
        gbut.get_style_context().remove_class("red-background")
        gbut.get_style_context().remove_class("green-background")
        if _("Remove") in status:
            gbut.get_style_context().add_class('red-background')
        else:
            gbut.get_style_context().add_class('green-background')
        return status

    def scanner(self):                                         # Scans the OS for programs
        global scanner
        global insList
        # if distro == 'Arch':
            # insList = os.popen('pacman -Q').read()
        # else:
        insList = apt.Cache()
        # Check for every program in the list
        for i in range(appListLen):
            # if distro == 'Arch':
            #     name = archDict[appList[i]]
            if distro == 'Ubuntu' or distro == 'Debian':
                # the name to check for
                name = appList[i]
            else:
                print('ERROR IN NAME')
            # importing the button
            gbut = self.builder.get_object("%s_but" % butDict[appList[i]])
            # Call function for setting label and color
            status = self.colorer(gbut, name)
            # value refers to the state: Install/Remove
            tempNam = layDict[appList[i]]
            statDict[tempNam] = status

        # It indicates that the state of every program is now loaded into the memory
        scanner = False

    # check if program is installed or not
    def OnCheck(self, name):
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
            # if distro == 'Arch':
            #     if name in insList:
            #         print('Found %s' % name)
            #         status = _('Remove')
            #     else:
            #         print('Not found %s' % name)
            #         status = _('Install')
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

    def abort(self, mode, text):
        global quit
        global rmE
        x, y = window.get_position()
        sx, sy = window.get_size()
        dialogWindow = Gtk.MessageDialog(parent=window, modal=True, destroy_with_parent=True, message_type=Gtk.MessageType.QUESTION, buttons=Gtk.ButtonsType.YES_NO, text=text)
        dialogWindow.set_title(_("Attention!"))
        dsx, dsy = dialogWindow.get_size()
        dialogWindow.move(x+((sx-dsx)/2), y+((sy-dsy)/2))
        dx, dy = dialogWindow.get_position()
        print(dx, dy)
        dialogWindow.show_all()
        res = dialogWindow.run()
        if res == Gtk.ResponseType.YES:
            if mode == 'download':
                quit = True
                rmE = True
                print(quit)
            elif mode == 'install':
                print('Installation already running')
                if distro == 'Ubuntu' or distro == 'Debian':
                    try:
                        osLayer.trans.cancel()
                    except:
                        print('Cant cancel')
                # elif distro == 'Arch':
                #     osLayer.asroot('rm /var/lib/pacman/db.lck ; killall pacman ; pacman -R $(pacman -Qdtq) ; rm -rf /home/%s/.tmp_hsuite' % user)
                else:
                    print('ERROR IN DIST AB')
            print('OK pressed')
            dialogWindow.destroy()
            return 'force'
        elif res == Gtk.ResponseType.NO:
            print('No pressed')
            dialogWindow.destroy()
            return True

    def on_fin(self, transaction, exit_state):
        GLib.idle_add(self.dia.hide)
        osLayer.alive = False
        print('Trans : %s' % transaction)
        print('Code : %s' % exit_state)
        print("FIN")
        # return trans.exit == enums.EXIT_SUCCESS
    
    def on_done(self, sth):
        osLayer.alive = False

    # This is executed when an app is being installed/removed
    def OnNeed(self, cInB, name, status, comm1, comm2, faur, extra, runDep, buildDep):
        global cPkg
        global m
        # removes scan cache from memory because it needs to rescan because one app changed
        sTxt = cInB
        # Current pkg name
        cPkg = name
        if distro == 'Ubuntu' or distro == 'Debian':
            progr, trans = osLayer.my_thread(status, distro, comm1, comm2, faur, extra, runDep, buildDep)
            if progr == True:
                self.dia.set_transaction(trans)
                GLib.idle_add(self.dia.show)
                trans.connect("finished", self.on_fin)
                trans.run()
            else:
                print('E: osLayer error')
        # else:
        #     print('Future')
        #     osLayer.my_thread(status, distro, comm1, comm2, faur, extra, runDep, buildDep)
        m = 0
        
        wt = False
        print(self, wt)
        for i in range(appListLen):
            print("Toggle %s" % i)
            if appList[i] != tempInd:
                print(appList[i], butDict[appList[i]], tempInd)
                cBut = self.builder.get_object('%s_but' % butDict[appList[i]])
                GLib.idle_add(cBut.set_sensitive, wt)
        # function for counting time
        def counter(timer):
            global m
            global cPkg
            global scanner
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
                scanner = True
                self.button_clicked(button)
                if not window.is_active():
                    notify2.init('HSuite')
                    n = notify2.Notification('HSuite', _('Finished processing %s!') % cPkg)
                    n.show()
                cPkg = ''
                return False                                                      # end
        self.source_id = GLib.timeout_add(1000, counter, self)

    def spece(self, name):
        if distro == 'Ubuntu' or distro == 'Debian':
            if name in specDList:
                return True
            else:
                return False
        # elif distro == 'Arch':
        #     if name in aurList:
        #         return True
        #     else:
        #         return False
        else:
            print('SpecERROR!')

    def lilFunc(self, name, comm1, extra, runDep, buildDep):
        global tempInd
        if osLayer.alive:
            print('Operation already running, which is %s' % cPkg)
        if name == cPkg:
            text = _("Do you really would like to abort now? It could end up with a broken program. If you decide to abort, then you may need to remove %s manually.") % cPkg
            self.abort('install', text)
        else:
            # comm2 = archDict[comm1]
            comm2 = ''
            cInB = self.builder.get_object("%s_but" % butDict[comm1])
            tempInd = comm1
            # origCom2 = comm2
            # if ' ' in comm2:
            #     comm2 = comm2.replace(' ', '')
            # elif 'e 1' in comm2:
            #     comm2 = comm2.replace('e 1', 'e')
            if _('Install') in statDict[name]:
                if name == 'fusuma':
                    x, y = window.get_position()
                    sx, sy = window.get_size()
                    dialogWindow = Gtk.MessageDialog(parent=window, modal=True, destroy_with_parent=True, message_type=Gtk.MessageType.WARNING, buttons=Gtk.ButtonsType.OK, text=lehete)
                    dialogWindow.set_title(_("Note!"))
                    dsx, dsy = dialogWindow.get_size()
                    dialogWindow.move(x+((sx-dsx)/2), y+((sy-dsy)/2))
                    dialogWindow.show_all()
                    res = dialogWindow.run()
                    print(res)
                    dialogWindow.destroy()
                    print('OK pressed')
                    dialogWindow.destroy()
                print(name)
                self.OnNeed(cInB, name, 'install', comm1, comm2, self.spece(comm2), extra, runDep, buildDep)
            elif _('Remove') in statDict[name]:
                print(name)
                self.OnNeed(cInB, name, 'remove', comm1, comm2, self.spece(comm2), extra, runDep, buildDep)

# Download methods

    # Disable or enable buttons based on a pattern
    def toggle(self, fn):
        print(self, fn, state)
        for i in range(dlistLen):
            if dlist[i] != Tdownl and shDict[dlist[i]] != "PFalse":
                cBut = self.builder.get_object(dlist[i])
                t = cBut.get_label()
                if t == _("Server error"):
                    print('Skipping due to server error')
                else:
                    GLib.idle_add(cBut.set_sensitive, state)
                    shDict[dlist[i]] = "%s" % state
        global scanningUrl
        if state:
            scanningUrl = False

    # Starting download in a background thread BUT inside the GUI class, not the thread. This is because of the nature of GTK (and other GUI toolkits) that can't handle GUI changes from outside of the main thread (gui class)
    def ex_target(self, block_sz, downl, file_size, file_name, file_size_dl, u, f):
        print("DLthread...")
        # This variable shows if the thread needs to exit
        global quit
        quit = False
        while not quit:
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
        global runE
        runE = False
        # Set back the button label to the original
        GLib.idle_add(downl.set_label, orig)
        print('quit: %s' % quit)
        print(orig)
        print("Label restore")
        # If the download is aborted by the user, remove the already downloaded file
        if rmE:
            print('Cleaning up...')
            os.system('rm /home/%s/Downloads/%s' % (user, file_name))
        else:
            # Set label to ready
            GLib.idle_add(downl.set_label, _("Ready in ~/Downloads/"))
            # Disable button
            GLib.idle_add(downl.set_sensitive, False)
            # Set the state to permanent false
            shDict[Tdownl] = "PFalse"
            print("done with it")
            if not window.is_active():
                notify2.init('HSuite')
                n = notify2.Notification('HSuite', _('Finished downloading %s!') % namDict[Tdownl])
                n.show()
        quit = True

    def on_downl_begin(self, url, downl):
        # Open the url
        global runE
        global state
        u = urlopen(url)
        if runE == True:                                                  # If download is already running
            # set remove flag to true
            global rmE
            rmE = True
            # tell the thread to stop
            global quit
            quit = True
            print("TruTogle")
            # set button state to enabled
            state = True
            # enable every button
            self.toggle(fn)
            return
        elif runE == False:                                               # If no downloads are running
            # toggle that now one is running
            runE = True
            # we don't need to remove the downloaded file, because it's ready
            rmE = False
            # save the original label of the button
            global orig
            orig = downl.get_label()
        file_name = url.split('/')[-1]
        f = open('/home/%s/Downloads/%s' %
                 (user, file_name), 'wb')  # set download location
        print('Downloading %s' % file_name)
        print("FalsTogle")
        # disable buttons
        state = False
        # run function to do this
        self.toggle(fn)
        t1 = futures.ThreadPoolExecutor(
            max_workers=4)                    # init thread
        # start it
        f = t1.submit(self.ex_target, 8192, downl, int(
            u.getheader('Content-Length')), file_name, 0, u, f)
        # set buttons to active
        state = True
        # after done run this function
        f.add_done_callback(self.toggle)

    def on_downl_mint_clicked(self, button):
        print("mint")
        # this download
        global Tdownl
        Tdownl = 'downl_mint'
        self.on_downl_begin(uriDict["downl_mint"],
                            self.builder.get_object('downl_mint'))

    def on_downl_ubuntu_clicked(self, button):
        print("ubuntu")
        global Tdownl
        Tdownl = 'downl_ubuntu'
        self.on_downl_begin(uriDict["downl_ubuntu"],
                            self.builder.get_object('downl_ubuntu'))

    def on_downl_solus_clicked(self, button):
        print("solus")
        global Tdownl
        Tdownl = 'downl_solus'
        self.on_downl_begin(uriDict["downl_solus"],
                            self.builder.get_object('downl_solus'))

    def on_downl_deepin_clicked(self, button):
        print("deepin")
        global Tdownl
        Tdownl = 'downl_deepin'
        self.on_downl_begin(uriDict["downl_deepin"],
                            self.builder.get_object('downl_deepin'))

    def on_downl_zorin_clicked(self, button):
        print("zorin")
        global Tdownl
        Tdownl = 'downl_zorin'
        self.on_downl_begin(uriDict["downl_zorin"],
                            self.builder.get_object('downl_zorin'))

    def on_downl_steamos_clicked(self, button):
        print("steamos")
        global Tdownl
        Tdownl = 'downl_steamos'
        self.on_downl_begin(uriDict["downl_steamos"],
                            self.builder.get_object('downl_steamos'))

    def on_downl_deb_clicked(self, button):
        print("deb")
        global Tdownl
        Tdownl = 'downl_deb'
        self.on_downl_begin(uriDict["downl_deb"],
                            self.builder.get_object('downl_deb'))

    def on_downl_fedora_clicked(self, button):
        print("fedora")
        global Tdownl
        Tdownl = 'downl_fedora'
        self.on_downl_begin(uriDict["downl_fedora"],
                            self.builder.get_object('downl_fedora'))

    def on_downl_suse_clicked(self, button):
        print("suse")
        global Tdownl
        Tdownl = 'downl_suse'
        self.on_downl_begin(uriDict["downl_suse"],
                            self.builder.get_object('downl_suse'))

    def on_downl_arch_clicked(self, button):
        print("arch")
        global Tdownl
        Tdownl = 'downl_arch'
        self.on_downl_begin(uriDict["downl_arch"],
                            self.builder.get_object('downl_arch'))

    def on_downl_gentoo_clicked(self, button):
        print("gentoo")
        global Tdownl
        Tdownl = 'downl_gentoo'
        self.on_downl_begin(uriDict["downl_gentoo"],
                            self.builder.get_object('downl_gentoo'))

    def on_downl_lfs_clicked(self, button):
        print("lfs")
        global Tdownl
        Tdownl = 'downl_lfs'
        self.on_downl_begin(uriDict["downl_lfs"],
                            self.builder.get_object('downl_lfs'))

# End of download section

    # Button is the name of the app spotlight button
    def button_clicked(self, button):
        # If already in memory don't waste resources
        if scanner == False:
            print('VALUE_FOUND')
            # notebook box is the name of the app spotlight page
            notebook_box = self.builder.get_object('notebook_box')
            # set it visible
            stack.set_visible_child(notebook_box)
        # if not in memory, then scan it now
        elif scanner:
            notebook_box = self.builder.get_object('notebook_box')
            stack.set_visible_child(notebook_box)
            print('NO_VALUE')
            # start scanning
            aS = futures.ThreadPoolExecutor(max_workers=2)
            s = aS.submit(app.scanner)
            print('SCANN START')
            print(s)
        else:
            print('ERROR')

    # feedback button
    def on_fb_but_clicked(self, button):
        global where
        web_box = self.builder.get_object('web_box')
        texV = self.builder.get_object('txt_long')
        titE = self.builder.get_object('tit_entry')
        text = texV.get_buffer()
        text = text.set_text('')
        titE.set_text('')
        stack.set_visible_child(web_box)
        tC = futures.ThreadPoolExecutor(max_workers=2)
        f = tC.submit(self.check)
        where = 'fb'
        f.add_done_callback(self.chk_again)

    def check(self):
        global net
        try:
            urlopen('http://216.58.192.142', timeout=5)
            print('yes, net')
            net = True
        except:
            print('no internet')
            net = False
    def chk_again(self, arg):
        global where
        global net
        global state
        global tC2
        global tS
        if not net:
            button = 0
            offtxt = _("You have no internet connection!")
            os.system('zenity --warning --text=%s --ellipsize' % offtxt)
            if where == 'fb':
                self.home_clicked(button)
            else:
                tC2 = futures.ThreadPoolExecutor(max_workers=2)
                for i in range(dlistLen):
                    # dlist is distro list (contains all distro names), cbut is current button
                    cBut = self.builder.get_object(dlist[i])
                    cBut.set_label(_('No internet'))
        else:
            if where == 'gs':
                tS = futures.ThreadPoolExecutor(max_workers=2)
                f = tS.submit(self.getSize)
                # toggle everything back when ready
                state = True
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
            print('invalid email!!')
            x, y = window.get_position()
            sx, sy = window.get_size()
            dialogWindow = Gtk.MessageDialog(parent=window, modal=True, destroy_with_parent=True, message_type=Gtk.MessageType.WARNING, buttons=Gtk.ButtonsType.OK, text=_('Invalid email address!'))
            dialogWindow.set_title(_("Attention!"))
            dsx, dsy = dialogWindow.get_size()
            dialogWindow.move(x+((sx-dsx)/2), y+((sy-dsy)/2))
            dialogWindow.show_all()
            res = dialogWindow.run()
            print(res)
            dialogWindow.destroy()
            return
        elif text == '' or title == '':
            x, y = window.get_position()
            sx, sy = window.get_size()
            dialogWindow = Gtk.MessageDialog(parent=window, modal=True, destroy_with_parent=True, message_type=Gtk.MessageType.WARNING, buttons=Gtk.ButtonsType.OK, text=_('You need to fill out all the fields!'))
            dialogWindow.set_title(_("Attention!"))
            dsx, dsy = dialogWindow.get_size()
            dialogWindow.move(x+((sx-dsx)/2), y+((sy-dsy)/2))
            dialogWindow.show_all()
            res = dialogWindow.run()
            print(res)
            dialogWindow.destroy()
            return
        text = text+"\n\n---------------------------------\n\nEmail: %s" % email
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
        x, y = window.get_position()
        sx, sy = window.get_size()
        dialogWindow = Gtk.MessageDialog(parent=window, modal=True, destroy_with_parent=True, message_type=Gtk.MessageType.INFO, buttons=Gtk.ButtonsType.OK, text=_('Feedback submitted succesfully!'))
        dialogWindow.set_title(_("Information"))
        dsx, dsy = dialogWindow.get_size()
        dialogWindow.move(x+((sx-dsx)/2), y+((sy-dsy)/2))
        dialogWindow.show_all()
        res = dialogWindow.run()
        print(res)
        dialogWindow.destroy()
        self.home_clicked(button)

    # information button in about section
    def on_git_link_clicked(self, button):
        # open project page in browser
        webbrowser.open_new("https://swanux.github.io/hsuite/")

######################################################################################################################

    def on_prog_chk_toggled(self, widget):
        if widget.get_active():
            print('Active')
            self.b_progs = True
        else:
            print('Inactive')
            self.b_progs = False

    def on_usr_chk_toggled(self, widget):
        if widget.get_active():
            print('Active')
            self.b_data = True
        else:
            print('Inactive')
            self.b_data = False
    
    def on_cron_chk_toggled(self, widget):
        if widget.get_active():
            print('Active')
            self.b_cron = True
        else:
            print('Inactive')
            self.b_cron = False
    
    def on_them_chk_toggled(self, widget):
        if widget.get_active():
            print('Active')
            self.b_theme = True
            self.b_settings = True
        else:
            print('Inactive')
            self.b_theme = False
            self.b_settings = False
    
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
            x, y = window.get_position()
            sx, sy = window.get_size()
            dialogWindow = Gtk.MessageDialog(parent=window, modal=True, destroy_with_parent=True, message_type=Gtk.MessageType.QUESTION, buttons=Gtk.ButtonsType.YES_NO, text=_('Would you like to view a simplified list of applications? (some less common programs may miss from the list)'))
            dialogWindow.set_title(_("Ask"))
            dsx, dsy = dialogWindow.get_size()
            dialogWindow.move(x+((sx-dsx)/2), y+((sy-dsy)/2))
            dx, dy = dialogWindow.get_position()
            print(dx, dy)
            dialogWindow.show_all()
            res = dialogWindow.run()
            if res == Gtk.ResponseType.YES:
                b_simple = True
                print('OK pressed')
                dialogWindow.destroy()
            elif res == Gtk.ResponseType.NO:
                print('No pressed')
                dialogWindow.destroy()
                b_simple = False
            else:
                b_simple = False
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
        stack.set_visible_child(self.builder.get_object('scroll_switcher'))










######################################################################################################################


    # foss collection (?)
    def on_htools_but_clicked(self, button):
        x, y = window.get_position()
        sx, sy = window.get_size()
        dialogWindow = Gtk.MessageDialog(parent=window, modal=True, destroy_with_parent=True, message_type=Gtk.MessageType.INFO, buttons=Gtk.ButtonsType.OK, text=_('Coming in future Beta releases...'))
        dialogWindow.set_title(_("Coming Soon"))
        dsx, dsy = dialogWindow.get_size()
        dialogWindow.move(x+((sx-dsx)/2), y+((sy-dsy)/2))
        dialogWindow.show_all()
        res = dialogWindow.run()
        print(res)
        dialogWindow.destroy()

    # fetch download sizes
    def getSize(self):
        global stop
        print('Getting Links...')

        def findNew(urii, perPat, perVer):
            if stop:
                print('Aborted by user.')
                raise SystemExit
            global vers
            global gentoo
            reponse = urlopen(urii)
            dat = reponse.read()
            text = dat.decode('utf-8')
            pattern = re.findall(perPat, text)
            gentoo = pattern[0]
            pattern = ''.join(pattern)
            pattern = pattern.replace(".", "")
            pattern = re.findall(perVer, pattern)
            pattern = list(map(int, pattern))
            try:
                pattern.remove(710)
                pattern.remove(710)
            except:
                # print("no lfs")
                pass
            pattern.sort()
            vers = pattern[-1]
            vers = [int(i) for i in str(vers)]

        if day == "01":
            if month == "01":
                aMonth = 12
                aYear = int(year) - 1
            else:
                aMonth = int(month) - 1
                aYear = year
        else:
            aMonth = month
            aYear = year
        archLink = 'http://mirrors.evowise.com/archlinux/iso/%s.%s.01/archlinux-%s.%s.01-x86_64.iso' % (
            aYear, aMonth, aYear, aMonth)

        findNew("http://releases.ubuntu.com",
                r'"+[\d]+.[\d]+/', r'[\d]+[\d]+[\d]+[\d]')
        # global ubuntuLink
        ubuntuLink = 'http://releases.ubuntu.com/%s%s.%s%s/ubuntu-%s%s.%s%s-desktop-amd64.iso' % (
            vers[0], vers[1], vers[2], vers[3], vers[0], vers[1], vers[2], vers[3])

        findNew("http://mirrors.evowise.com/linuxmint/stable/",
                r'"+[\d]+.[\d]+/', r'[\d]+[\d]+[\d]')
        # global mintLink
        mintLink = 'http://mirrors.evowise.com/linuxmint/stable/%s%s.%s/linuxmint-%s%s.%s-cinnamon-64bit.iso' % (
            vers[0], vers[1], vers[2], vers[0], vers[1], vers[2])

        findNew("http://mirror.inode.at/data/deepin-cd/",
                r'"+[\d]+.[\d]+/', r'[\d]+[\d]+[\d]')
        # global deepinLink
        deepinLink = 'http://mirror.inode.at/data/deepin-cd/%s%s.%s%s/deepin-%s%s.%s%s-amd64.iso' % (
            vers[0], vers[1], vers[2], vers[3], vers[0], vers[1], vers[2], vers[3])

        findNew("https://cdimage.debian.org/images/unofficial/non-free/images-including-firmware/current-live/amd64/iso-hybrid/",
                r'debian-live-+[\d]+[\d]+.[\d]+.[\d]', r'[\d]+[\d]+[\d]')
        # global debianLink
        debianLink = 'https://cdimage.debian.org/images/unofficial/non-free/images-including-firmware/current-live/amd64/iso-hybrid/debian-live-%s%s.%s.%s-amd64-cinnamon+nonfree.iso' % (
            vers[0], vers[1], vers[2], vers[3])

        # global steamosLink
        steamosLink = 'http://repo.steampowered.com/download/SteamOSDVD.iso'

        findNew("https://sourceforge.net/projects/zorin-os/files/",
                r'files/+[\d]+/download', r'[\d]+[\d]')
        # global zorinosLink
        zorinosLink = 'https://netcologne.dl.sourceforge.net/project/zorin-os/%s%s/Zorin-OS-%s%s-Core-64-bit-r1.iso' % (
            vers[0], vers[1], vers[0], vers[1])

        findNew("http://fedora.inode.at/releases/", r'"+[\d]+/', r'[\d]+[\d]')
        # global fedoraLink
        fedoraLink = 'http://fedora.inode.at/releases/%s%s/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-%s%s-1.9.iso' % (
            vers[0], vers[1], vers[0], vers[1])

        # global opensuseLink
        opensuseLink = 'https://download.opensuse.org/tumbleweed/iso/openSUSE-Tumbleweed-DVD-x86_64-Current.iso'

        # global solusLink
        solusLink = 'http://solus.veatnet.de/iso/images/4.0/Solus-4.0-Budgie.iso'

        findNew("http://distfiles.gentoo.org/releases/amd64/autobuilds/current-install-amd64-minimal/",
                r'[\d]+[\d]+[\w]+[\d][\w]', r'[\d]+[\d]')
        # global gentooLink
        gentooLink = 'http://distfiles.gentoo.org/releases/amd64/autobuilds/current-install-amd64-minimal/install-amd64-minimal-%s.iso' % gentoo

        findNew("http://www.linuxfromscratch.org/lfs/downloads/",
                r'[\d]+.[\d]+-systemd/', r'[\d]+[\d]')
        # global lfsLink
        lfsLink = 'http://www.linuxfromscratch.org/lfs/downloads/%s.%s-systemd/LFS-BOOK-%s.%s-systemd.pdf' % (
            vers[0], vers[1], vers[0], vers[1])

        global uriDict
        global cache
        uriDict = {'downl_mint': mintLink, 'downl_ubuntu': ubuntuLink, 'downl_solus': solusLink, 'downl_zorin': zorinosLink, 'downl_deepin': deepinLink, 'downl_steamos': steamosLink,
                'downl_deb': debianLink, 'downl_fedora': fedoraLink, 'downl_suse': opensuseLink, 'downl_gentoo': gentooLink, 'downl_arch': archLink, 'downl_lfs': lfsLink}
        print('Updated linklist!!')
        print("Getting size...")
        # dlistlen is the length of dlist
        for i in range(dlistLen):
            # dlist is distro list (contains all distro names), cbut is current button
            cBut = self.builder.get_object(dlist[i])
            # get url from dictionary
            url = uriDict[dlist[i]]
            try:
                u = urlopen(url)
                time.sleep(0.1)
                file_size = int(u.getheader('Content-Length'))
                # convert to MB
                file_size = Decimal(int(file_size) / 1024 / 1024)
                GLib.idle_add(cBut.set_label, "Download (%s MB)" %
                            round(file_size, 1))  # set download label
                # store value in cache
                cache.append(round(file_size, 1))
            except:
                print('URL ERROR!')
                GLib.idle_add(cBut.set_label, _("Server error"))
                cache.append(round(0, 1))
            stop = True

    def on_db_but_clicked(self, button):
        distro_box = self.builder.get_object('distro_box')
        global cache
        global tC2
        global scanningUrl
        thss = len(tC2._threads)
        print(thss)
        if not cache and thss == 0:                                                             # if not fetched already
            # disable
            global where
            global state
            scanningUrl = True
            state = False
            self.toggle(fn)  # all buttons
            # init non-normal thread (getting sizes)
            f = tC2.submit(self.check)
            where = 'gs'
            f.add_done_callback(self.chk_again)
        elif not scanningUrl:
            i = 0
            for i in range(dlistLen):
                cBut = self.builder.get_object(dlist[i])        # if loaded
                # load from cache
                cBut.set_label(_("Download (%s MB)") % cache[i])
        stack.set_visible_child(distro_box)

    # on about ...
    def on_about_but_clicked(self, button):
        scroll_about = self.builder.get_object('scroll_about')
        stack.set_visible_child(scroll_about)

    def home_clicked(self, button):  # back button
        scroll_home = self.builder.get_object('scroll_home')
        stack.set_visible_child(scroll_home)

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
        if bp == _("Distro Boutique"):
            rew_link.show()
            web_link.show()
        text.set_text(label)
        back_button.set_label(bp)
        stack.set_visible_child(page)

    # when going back but not to home
    def on_back_button_clicked(self, button):
        if bp == _("App Spotlight"):                                 # go back to app spotlight or distro boutique
            self.button_clicked(button)
        elif bp == _("Distro Boutique"):
            distro_box = self.builder.get_object('distro_box')
            stack.set_visible_child(distro_box)
        else:
            print('ERROR')

    def on_rew_link_clicked(self, button):
        webbrowser.open_new(rew)

    def on_web_link_clicked(self, button):
        webbrowser.open_new(web)

# What to do on button clicks
    def on_opera_but_clicked(self, button):
        self.lilFunc('Opera', 'opera-stable', 'opera-ffmpeg-codecs', '', '')

    def on_chrome_but_clicked(self, button):
        self.lilFunc('Chrome', 'google-chrome-stable', '', 'alsa-lib gtk3 libcups libxss libxtst nss', '')

    def on_web_but_clicked(self, button):
        self.lilFunc('Web', 'epiphany-browser', '', '', '')

    def on_firefox_but_clicked(self, button):
        self.lilFunc('Firefox', 'firefox', '', '', '')

    def on_vivaldi_but_clicked(self, button):
        self.lilFunc('Vivaldi', 'vivaldi-stable', '', 'alsa-lib desktop-file-utils gtk3 hicolor-icon-theme libcups libxss nss shared-mime-info libnotify pepper-flash', 'w3m')

    def on_edge_but_clicked(self, button):
        name = 'Edge'
        print(name)

    def on_woffice_but_clicked(self, button):
        self.lilFunc('WPS Office', 'wps-office', 'ttf-wps-fonts', 'fontconfig xorg-font-utils desktop-file-utils glu gtk2 hicolor-icon-theme libpulse libxrender libxss openssl-1.0 sdl2 shared-mime-info sqlite xdg-utils xorg-mkfontdir', '')

    def on_loffice_but_clicked(self, button):
        self.lilFunc('Libreoffice', 'libreoffice', '', '', '')

    def on_ooffice_but_clicked(self, button):
        self.lilFunc('Only Office', 'onlyoffice-desktopeditors', '', 'alsa-lib atk cairo curl desktop-file-utils fontconfig freetype2 gcc-libs gconf gdk-pixbuf2 gst-plugins-base-libs gstreamer gtk2 gtk3 gtkglext hicolor-icon-theme libcups libdrm libglvnd libice libpulse libsm libx11 libxcb libxcomposite libxcursor libxdamage libxext libxfixes libxi libxrandr libxrender libxss libxtst nspr nss pango qt5-declarative qt5-multimedia qt5-svg ttf-carlito ttf-dejavu ttf-liberation wget xdg-utils gtkglext libcurl-gnutls qt5-svg qt5-multimedia', '')

    def on_msoffice_but_clicked(self, button):
        webbrowser.open_new("https://office.com")

    def on_goffice_but_clicked(self, button):
        webbrowser.open_new("https://docs.google.com")

    def on_foffice_but_clicked(self, button):
        self.lilFunc('Free Office', 'softmaker-freeoffice-2018', '', 'curl desktop-file-utils gtk-update-icon-cache libxrandr xdg-utils libgl', 'chrpath')

    def on_gedit_but_clicked(self, button):
        self.lilFunc('Gedit', 'gedit', 'gedit-plugins', '', '')

    def on_gnu_but_clicked(self, button):
        self.lilFunc('GNU Emacs', 'emacs', '', '', '')

    def on_vscode_but_clicked(self, button):
        self.lilFunc('VS Code', 'code', '', '', '')

    def on_atom_but_clicked(self, button):
        self.lilFunc('Atom Editor', 'atom', '', '', '')

    def on_stedit_but_clicked(self, button):
        self.lilFunc('Sublime Text Editor', 'sublime-text', '', '', '')

    def on_geany_but_clicked(self, button):
        self.lilFunc('Geany', 'geany', '', '', '')

    def on_skype_but_clicked(self, button):
        self.lilFunc('Skype', 'skypeforlinux', '', 'alsa-lib gtk3 libsecret libxss libxtst nss glibc', 'asar')

    def on_discord_but_clicked(self, button):
        self.lilFunc('Discord', 'discord', '', '', '')

    def on_telegram_but_clicked(self, button):
        self.lilFunc('Telegram', 'telegram-desktop', '', '', '')

    def on_signal_but_clicked(self, button):
        self.lilFunc('Signal', 'signal-desktop', '', 'electron git npm', 'yarn nodejs')

    def on_hex_but_clicked(self, button):
        self.lilFunc('HexChat', 'hexchat', '', '', '')

    def on_franz_but_clicked(self, button):
        self.lilFunc('Franz', 'franz', '', 'electron npm git', 'expac')

    def on_0ad_but_clicked(self, button):
        self.lilFunc('0 A.D.', '0ad', '', '', '')

    def on_skart_but_clicked(self, button):
        self.lilFunc('SuperTuxKart', 'supertuxkart', '', '', '')

    def on_tux_but_clicked(self, button):
        self.lilFunc('SuperTux', 'supertux', '', '', '')

    def on_lutris_but_clicked(self, button):
        self.lilFunc('Lutris', 'lutris', '', '', '')

    def on_barr_but_clicked(self, button):
        self.lilFunc('Barrier', 'barrier', '', 'hicolor-icon-theme qt5-base avahi curl libice libsm libx11 libxext libxi libxinerama libxrandr libxtst openssl xorgproto', 'cmake ')

    def on_pol_but_clicked(self, button):
        self.lilFunc('Play On Linux', 'playonlinux', '', '', '')

    def on_steam_but_clicked(self, button):
        self.lilFunc('Steam', 'steam', '', '', '')

    def on_mc_but_clicked(self, button):
        self.lilFunc('Minecraft', 'minecraft-launcher', '', 'alsa-lib gconf gtk2 gtk3 java-runtime libx11 libxcb libxss libxtst nss xorg-xrandr', '')

    def on_pops_but_clicked(self, button):
        self.lilFunc('Popsicle', 'popsicle', 'popsicle-gtk', 'git gtk3', 'cargo help2man rust xorgproto')

    def on_woe_but_clicked(self, button):
        self.lilFunc('WoeUSB', 'woeusb', '', 'dosfstools grub ntfs-3g parted wget wxgtk2', '')

    def on_wine_but_clicked(self, button):
        self.lilFunc('Wine', 'winehq-stable', '', '', '')

    def on_vbox_but_clicked(self, button):
        self.lilFunc('Virtualbox', 'virtualbox-6.1', '', '', '')

    def on_gparted_but_clicked(self, button):
        self.lilFunc('GParted', 'gparted', 'gpart', '', '')

    def on_gest_but_clicked(self, button):
        self.lilFunc('fusuma', 'fusuma', 'wmctrl libinput-tools xdotool', '', '')

    def on_auda_but_clicked(self, button):
        self.lilFunc('Audacity', 'audacity', '', '', '')

    def on_deja_but_clicked(self, button):
        self.lilFunc('Déja-Dup', 'deja-dup', '', '', '')

    def on_tims_but_clicked(self, button):
        self.lilFunc('Timeshift', 'timeshift', '', 'cronie desktop-file-utils gtk3 json-glib libsoup rsync vte3 xapps libgee', 'coreutils diffutils vala vte3')

    def on_tw_but_clicked(self, button):
        self.lilFunc('TeamViewer', 'teamviewer', '', '', '')

    def on_box_but_clicked(self, button):
        self.lilFunc('Gnome Boxes', 'gnome-boxes', '', '', '')

# End of button clicks


# Descriptions


    def displayDesc(self, x, button):
        global label
        global bp
        label = d.descList[x]
        bp = d.descDict[label]
        if bp == _('Distro Boutique'):
            global web
            global rew
            web = d.webDict[label]
            rew = d.vidDict[label]
        self.on_page(button)

    def on_opera_clicked(self, button):
        self.displayDesc(0, button)

    def on_chrome_clicked(self, button):
        self.displayDesc(1, button)

    def on_skart_clicked(self, button):
        self.displayDesc(30, button)

    def on_web_clicked(self, button):
        self.displayDesc(2, button)

    def on_firefox_clicked(self, button):
        self.displayDesc(3, button)

    def on_vivaldi_clicked(self, button):
        self.displayDesc(4, button)

    def on_edge_clicked(self, button):
        self.displayDesc(5, button)

    def on_woffice_clicked(self, button):
        self.displayDesc(6, button)

    def on_loffice_clicked(self, button):
        self.displayDesc(7, button)

    def on_ooffice_clicked(self, button):
        self.displayDesc(8, button)

    def on_msoffice_clicked(self, button):
        self.displayDesc(9, button)

    def on_goffice_clicked(self, button):
        self.displayDesc(10, button)

    def on_foffice_clicked(self, button):
        self.displayDesc(11, button)

    def on_gedit_clicked(self, button):
        self.displayDesc(12, button)

    def on_gnu_clicked(self, button):
        self.displayDesc(13, button)

    def on_vscode_clicked(self, button):
        self.displayDesc(14, button)

    def on_atom_clicked(self, button):
        self.displayDesc(15, button)

    def on_stedit_clicked(self, button):
        self.displayDesc(16, button)

    def on_geany_clicked(self, button):
        self.displayDesc(17, button)

    def on_skype_clicked(self, button):
        self.displayDesc(18, button)

    def on_discord_clicked(self, button):
        self.displayDesc(19, button)

    def on_telegram_clicked(self, button):
        self.displayDesc(20, button)

    def on_signal_clicked(self, button):
        self.displayDesc(21, button)

    def on_hex_clicked(self, button):
        self.displayDesc(22, button)

    def on_franz_clicked(self, button):
        self.displayDesc(23, button)

    def on_0ad_clicked(self, button):
        self.displayDesc(24, button)

    def on_tux_clicked(self, button):
        self.displayDesc(25, button)

    def on_lutris_clicked(self, button):
        self.displayDesc(26, button)

    def on_barr_clicked(self, button):
        self.displayDesc(42, button)

    def on_pol_clicked(self, button):
        self.displayDesc(27, button)

    def on_steam_clicked(self, button):
        self.displayDesc(28, button)

    def on_mc_clicked(self, button):
        self.displayDesc(29, button)

    def on_pops_clicked(self, button):
        self.displayDesc(31, button)

    def on_woe_clicked(self, button):
        self.displayDesc(32, button)

    def on_wine_clicked(self, button):
        self.displayDesc(33, button)

    def on_vbox_clicked(self, button):
        self.displayDesc(34, button)

    def on_gparted_clicked(self, button):
        self.displayDesc(35, button)

    def on_gest_clicked(self, button):
        self.displayDesc(36, button)

    def on_auda_clicked(self, button):
        self.displayDesc(37, button)

    def on_deja_clicked(self, button):
        self.displayDesc(38, button)

    def on_tims_clicked(self, button):
        self.displayDesc(39, button)

    def on_tw_clicked(self, button):
        self.displayDesc(40, button)

    def on_box_clicked(self, button):
        self.displayDesc(41, button)

    def on_mint_clicked(self, button):
        self.displayDesc(43, button)

    def on_ubuntu_clicked(self, button):
        self.displayDesc(44, button)

    def on_solus_clicked(self, button):
        self.displayDesc(45, button)

    def on_deepin_clicked(self, button):
        self.displayDesc(46, button)

    def on_elementary_clicked(self, button):
        self.displayDesc(47, button)

    def on_zorin_clicked(self, button):
        self.displayDesc(48, button)

    def on_steamos_clicked(self, button):
        self.displayDesc(49, button)

    def on_deb_clicked(self, button):
        self.displayDesc(50, button)

    def on_fedora_clicked(self, button):
        self.displayDesc(51, button)

    def on_opsu_clicked(self, button):
        self.displayDesc(52, button)

    def on_arch_clicked(self, button):
        self.displayDesc(53, button)

    def on_gentoo_clicked(self, button):
        self.displayDesc(54, button)

    def on_lfs_clicked(self, button):
        self.displayDesc(55, button)

# End of descriptions
# _____________________________________________________________________ END OF GUI ____________________________________________________________________#

if __name__ == "__main__":
    app = GUI()  # variable to call GUI class
    Gtk.main()  # execute main GTK window
