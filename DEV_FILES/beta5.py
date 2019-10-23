#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
import os
import webbrowser
import threading
dire = '/home/sources/HSUITE/DEV_FILES'
os.chdir(dire)
import common as g
xorw = os.popen('echo $XDG_SESSION_TYPE').read()
if "x" in xorw:
    g.lehete = "You need to reboot or log in and out again after the install has been completed to apply all changes."
else:
    g.lehete = "You can currently only use this feature with x11 based desktop. It does not support Wayland."
g.dir = dire
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk, GLib, WebKit2


UI_FILE = "hsuite.glade"

pkg = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]
print(pkg)

g.user = os.popen("logname").read()
g.user = g.user.rstrip()
print(g.user)
g.spinning = False
g.scanner = True
g.doIt = False

wer = os.popen('ls').read()
print(str(wer))

dist = os.popen('uname -a').read()
print(dist)
if  'Ubuntu' in dist:
    g.distro = 'Ubuntu'
    vane = os.path.exists("/etc/apt/sources.list.d/hsources.list")
    print(vane)
    if vane:
        print('not first run')
    else:
        g.doIt = True
        print('first run')
elif 'archlinux' in dist or 'MANJARO' in dist:
    g.distro = 'Arch'
    vane = os.path.exists("/etc/hsuite.conf")
    print(vane)
    if vane:
        print('not first run')
    else:
        g.doIt = True
        print('first run')
elif 'Debian' in dist:
    g.distro = 'Debian'
    vane = os.path.exists("/etc/apt/sources.list.d/hsources.list")
    print(vane)
    if vane:
        print('not first run')
    else:
        g.doIt = True
        print('first run')
else:
    g.distro = 'Error 4'
print(g.distro)

class myThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print ("Starting " + self.name)
        my_thread()
        print ("Exiting " + self.name)

#######################################################################################

def my_thread():
    if g.CA == 'Opera':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'DEBIAN_FRONTEND=noninteractive apt install opera-stable pepperflashplugin-nonfree -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Sq --noconfirm opera opera-ffmpeg-codecs flashplugin'
            app.asroot()
    elif g.CA == 'OperaR':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt purge opera-stable pepperflashplugin-nonfree -y ; apt autoremove -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.asr = 'pacman -Runs --noconfirm  opera opera-ffmpeg-codecs flashplugin'
            app.asroot()
    elif g.CA == 'Chrome':
        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.asr = 'apt install google-chrome-stable -y'
            app.asroot()
        elif g.distro == 'Arch':
            g.fold = 'google-chrome'
            g.num = 2
            app.aurer()
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
            g.asr = 'pacman -S --noconfirm epiphany'
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
            g.asr = 'pacman -S --noconfirm firefox'
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
            g.asr = 'pacman -S --noconfirm gedit gedit-plugins'
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
            g.asr = 'pacman -S --noconfirm emacs'
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
            g.asr = 'pacman -S --noconfirm code'
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
            g.asr = 'pacman -S --noconfirm atom'
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
            g.asr = 'pacman -S --noconfirm sublime-text'
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
            g.asr = 'pacman -S --noconfirm geany'
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
            g.asr = 'pacman -S --noconfirm discord'
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
            g.asr = 'pacman -S --noconfirm telegram-desktop'
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
            g.asr = 'pacman -S --noconfirm hexchat'
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
            g.asr = 'pacman -S --noconfirm supertux'
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
            g.asr = 'pacman -S --noconfirm playonlinux'
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
            g.asr = 'DEBIAN_FRONTEND=noninteractive apt install teamviewer -y'
            app.asroot()
        elif g.distro == 'Arch':
            os.system('wget https://download.teamviewer.com/download/linux/teamviewer_amd64.tar.xz')
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
            g.asr = 'pacman -S --noconfirm gnome-boxes'
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
            g.asr = 'apt install libinput-tools libinput-bin wmctrl python3 xdotool python3-setuptools -y ; gpasswd -a %s input ; git clone https://github.com/bulletmark/libinput-gestures.git ; git clone https://gitlab.com/cunidev/gestures ; cd %s ; cd libinput-gestures ; ./libinput-gestures-setup install ; cd .. ; cd gestures ; python3 setup.py install ; cd .. ; rm -rf libinput-gestures ; rm -rf gestures ; cp /usr/share/hsuite/confs/libinput-gestures.conf ~/.config' % (g.user, g.dir)
            app.asroot()
        elif g.distro == 'Arch':
            g.num = 3
            g.fold = 'libinput-gestures'
            app.aurer()
            g.num = 1
            g.fold = 'gestures'
            app.aurer()
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
#    elif g.CA == 'powertop':
#        if g.distro == 'Ubuntu':
#            os.system('apt install powertop -y')
#        elif g.distro == 'Arch':
#            os.system('pacman -Sq --noconfirm powertop')
#        dial = wx.MessageDialog(None, 'Would you like to configure powertop now??', 'Attention', wx.YES_NO | wx.YES_DEFAULT | wx.ICON_QUESTION | wx.STAY_ON_TOP)
#        result = dial.ShowModal()
#        if result == wx.ID_YES:
#            wx.MessageBox('Configuring powertop. This will take a while... Do not let your PC to go to sleep!' , 'Attention', wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)
#            os.system('powertop -c')
#            os.system('powertop --auto-tune')
#        else:
#            print("No pressed")
#    elif g.CA == 'powertopR':
#        if g.distro == 'Ubuntu':
#            os.system('apt purge powertop -y && apt autoremove -y')
#        elif g.distro == 'Arch':
#            os.system('pacman -Runs --noconfirm powertop')
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
#    elif g.CA == 'aptORaur':
#        if g.distro == 'Ubuntu':
#            os.system('add-apt-repository -y ppa:apt-fast/stable && apt update && echo debconf apt-fast/maxdownloads string 16 | debconf-set-selections && echo debconf apt-fast/dlflag boolean true | debconf-set-selections && echo debconf apt-fast/aptmanager string apt | debconf-set-selections && apt install apt-fast -y')
#        elif g.distro == 'Arch':
#            with open("logname.sh") as f:
#                lines = f.readlines()
#            lines[4] = 'runuser -l $persist -c "echo $USER && cd && git clone https://aur.archlinux.org/pakku.git && cd pakku && makepkg -rc"'
#            with open("logname.sh", "w") as f:
#                f.writelines(lines)
#            os.system('./logname.sh')
#            pkg = os.popen('ls /home/%s/pakku/' % g.user).read()
#            pkg = pkg.split()
#            pkg = pkg[1]
#            print(pkg)
#            os.system('pacman -U --noconfirm /home/%s/pakku/%s && rm -rf /home/%s/pakku' % (g.user, pkg, g.user))
#            os.system('pakku -S --noconfirm pamac-classic pamac-aur pamac-tray-appindicator')
#    elif g.CA == 'aptORaurR':
#        if g.distro == 'Ubuntu':
#            os.system('apt purge apt-fast -y && apt autoremove -y')
#        elif g.distro == 'Arch':
#            os.system('pacman -Runs --noconfirm pakku pamac-classic pamac-aur pamac-tray-appindicator')
    else:
        print('Error 3')


#######################################################################################

class GUI:

    def asroot(self):
        with open("bashLayer.sh") as f:
            lines = f.readlines()
        lines[2] = 'CMD="%s"\n' % g.asr
        with open("bashLayer.sh", "w") as f:
            f.writelines(lines)
        os.system('bash bashLayer.sh')

    def aurer(self):
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

    count = 0
    def __init__(self):

        self.builder = Gtk.Builder()
        self.win = Gtk.Window()
        self.builder.add_from_file(UI_FILE)
        g.browserholder = WebKit2.WebView()
        g.browserholder.set_editable(False)
        self.builder.connect_signals(self)
        g.stack = self.builder.get_object('stack')

        g.window = self.builder.get_object('window')
        if os.geteuid() == 0:
           g.window.set_title(g.version+' (as superuser)')
        else:
            g.window.set_title(g.version)
        g.window.show_all()

    def on_window_delete_event(self, window, e):
        x, y = g.window.get_position()
        sx, sy = g.window.get_size()
        dialogWindow = Gtk.MessageDialog(None,
                              Gtk.DialogFlags.MODAL | Gtk.DialogFlags.DESTROY_WITH_PARENT,
                              Gtk.MessageType.QUESTION,
                              Gtk.ButtonsType.YES_NO,
                              "Do you really would like to exit now?")
        dialogWindow.set_title("Prompt")
        dsx, dsy = dialogWindow.get_size()
        dialogWindow.move(x+((sx-dsx)/2), y+((sy-dsy)/2))
        dx, dy = dialogWindow.get_position()
        dialogWindow.show_all()
        res = dialogWindow.run()
        if res == Gtk.ResponseType.YES:
            print('OK pressed')
            dialogWindow.destroy()
            Gtk.main_quit()
        elif res == Gtk.ResponseType.NO:
            print('No pressed')
            dialogWindow.destroy()
            return True

###################################################################################

    def stamp(self):
        if g.distro == 'Arch':
            g.status2 = g.status+' (AUR)'
        elif g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.status2 = g.status

    def scanner(self):

        if g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.insList = os.popen('apt list --installed').read()
        elif g.distro == 'Arch':
            g.insList = os.popen('pacman -Q').read()
        else:
            print('PACK ERROR')

        #g.insList = g.insList.split()

        opera_but = self.builder.get_object("opera_but")
        chrome_but = self.builder.get_object("chrome_but")
        web_but = self.builder.get_object("web_but")
        firefox_but = self.builder.get_object("firefox_but")
        vivaldi_but = self.builder.get_object("vivaldi_but")
        edge_but = self.builder.get_object("edge_but")
        woffice_but = self.builder.get_object("woffice_but")
        loffice_but = self.builder.get_object("loffice_but")
        ooffice_but = self.builder.get_object("ooffice_but")
        msoffice_but = self.builder.get_object("msoffice_but")
        goffice_but = self.builder.get_object("goffice_but")
        foffice_but = self.builder.get_object("foffice_but")
        gedit_but = self.builder.get_object("gedit_but")
        gnu_but = self.builder.get_object("gnu_but")
        vscode_but = self.builder.get_object("vscode_but")
        atom_but = self.builder.get_object("atom_but")
        stedit_but = self.builder.get_object("stedit_but")
        geany_but = self.builder.get_object("geany_but")

        skype_but = self.builder.get_object("skype_but")
        discord_but = self.builder.get_object("discord_but")
        telegram_but = self.builder.get_object("telegram_but")
        signal_but = self.builder.get_object("signal_but")
        hex_but = self.builder.get_object("hex_but")
        franz_but = self.builder.get_object("franz_but")

        ad_but = self.builder.get_object("0ad_but")
        tux_but = self.builder.get_object("tux_but")
        wot_but = self.builder.get_object("wot_but")
        pol_but = self.builder.get_object("pol_but")
        steam_but = self.builder.get_object("steam_but")
        mc_but = self.builder.get_object("mc_but")

        pops_but = self.builder.get_object("pops_but")
        woe_but = self.builder.get_object("woe_but")
        wine_but = self.builder.get_object("wine_but")
        vbox_but = self.builder.get_object("vbox_but")
        gparted_but = self.builder.get_object("gparted_but")
        gest_but = self.builder.get_object("gest_but")
        auda_but = self.builder.get_object("auda_but")
        deja_but = self.builder.get_object("deja_but")
        tims_but = self.builder.get_object("tims_but")
        tw_but = self.builder.get_object("tw_but")
        box_but = self.builder.get_object("box_but")


        if g.distro == 'Arch':
            g.name = 'opera'
        elif g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.name = 'opera-stable'
        else:
            print('ERROR IN NAME')
        self.OnCheck()
        opera_but.set_label(g.status)
        g.opera_value = g.status

        if g.distro == 'Arch':
            g.name = 'google-chrome'
        elif g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.name = 'google-chrome-stable'
        else:
            print('ERROR IN NAME')
        self.OnCheck()
        self.stamp()
        chrome_but.set_label(g.status2)
        g.chrome_value = g.status

        if g.distro == 'Arch':
            g.name = 'epiphany'
        elif g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.name = 'epiphany-browser'
        else:
            print('ERROR IN NAME')
        self.OnCheck()
        web_but.set_label(g.status)
        g.web_value = g.status

        g.name = 'firefox'
        self.OnCheck()
        firefox_but.set_label(g.status)
        g.firefox_value = g.status

        if g.distro == 'Arch':
            g.name = 'vivaldi'
        elif g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.name = 'vivaldi-stable'
        else:
            print('ERROR IN NAME')
        self.OnCheck()
        self.stamp()
        vivaldi_but.set_label(g.status2)
        g.vivaldi_value = g.status

        edge_but.set_label("Coming soon")

        g.name = 'wps-office'
        self.OnCheck()
        self.stamp()
        woffice_but.set_label(g.status2)
        g.woffice_value = g.status

        if g.distro == 'Arch':
            g.name = 'libreoffice-fresh'
        elif g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.name = 'libreoffice'
        else:
            print('ERROR IN NAME')
        self.OnCheck()
        loffice_but.set_label(g.status)
        g.loffice_value = g.status

        if g.distro == 'Arch':
            g.name = 'onlyoffice-bin'
        elif g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.name = 'onlyoffice-desktopeditors'
        else:
            print('ERROR IN NAME')
        self.OnCheck()
        self.stamp()
        ooffice_but.set_label(g.status2)
        g.ooffice_value = g.status

        msoffice_but.set_label('Open in browser')

        goffice_but.set_label('Open in browser')

        if g.distro == 'Arch':
            g.name = 'freeoffice'
        elif g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.name = 'softmaker-freeoffice'
        else:
            print('EROOR IN NAME')
        self.OnCheck()
        self.stamp()
        foffice_but.set_label(g.status2)
        g.foffice_value = g.status

        g.name = 'gedit'
        self.OnCheck()
        gedit_but.set_label(g.status)
        g.gedit_value = g.status

        if g.distro == 'Arch' or g.distro == 'Debian':
            g.name = 'emacs/'
        elif g.distro == 'Ubuntu':
            g.name = 'emacs26'
        else:
            print('ERROR IN NAME')
        self.OnCheck()
        gnu_but.set_label(g.status)
        g.gnu_value = g.status

        g.name = 'code/s'
        self.OnCheck()
        vscode_but.set_label(g.status)
        g.vscode_value = g.status

        g.name = 'atom/'
        self.OnCheck()
        atom_but.set_label(g.status)
        g.atom_value = g.status

        g.name = 'sublime-text'
        self.OnCheck()
        stedit_but.set_label(g.status)
        g.stedit_value = g.status

        g.name = 'geany'
        self.OnCheck()
        geany_but.set_label(g.status)
        g.geany_value = g.status

        if g.distro == 'Arch':
            g.name = 'skypeforlinux-stable-bin'
        elif g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.name = 'skypeforlinux'
        else:
            print('ERROR IN NAME')
        self.OnCheck()
        skype_but.set_label(g.status)
        g.skype_value = g.status

        g.name = 'discord'
        self.OnCheck()
        discord_but.set_label(g.status)
        g.discord_value = g.status

        g.name = 'telegram-desktop'
        self.OnCheck()
        telegram_but.set_label(g.status)
        g.telegram_value = g.status

        if g.distro == 'Arch':
            g.name = 'signal'
        elif g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.name = 'signal-desktop'
        else:
            print('ERROR IN NAME')
        self.OnCheck()
        self.stamp()
        signal_but.set_label(g.status2)
        g.signal_value = g.status

        g.name = 'hexchat'
        self.OnCheck()
        hex_but.set_label(g.status)
        g.hex_value = g.status

        g.name = 'franz/'
        self.OnCheck()
        self.stamp()
        franz_but.set_label(g.status2)
        g.franz_value = g.status

        g.name = '0ad'
        self.OnCheck()
        ad_but.set_label(g.status)
        g.ad_value = g.status

        g.name = 'supertux'
        self.OnCheck()
        tux_but.set_label(g.status)
        g.tux_value = g.status

        wot_but.set_label("Working on it (with Wine)")

        g.name = 'playonlinux'
        self.OnCheck()
        pol_but.set_label(g.status)
        g.pol_value = g.status

        g.name = 'steam-launcher'
        self.OnCheck()
        steam_but.set_label(g.status)
        g.steam_value = g.status

        g.name = 'minecraft-launcher'
        self.OnCheck()
        self.stamp()
        mc_but.set_label(g.status2)
        g.mc_value = g.status

        if g.distro == 'Arch':
            g.name = 'popsicle-gtk-git'
        elif g.distro == 'Ubuntu' or g.distro == 'Debian':
            g.name = 'popsicle'
        else:
            print('ERROR IN NAME')
        self.OnCheck()
        self.stamp()
        pops_but.set_label(g.status2)
        g.pops_value = g.status

        g.name = 'woeusb'
        self.OnCheck()
        self.stamp()
        woe_but.set_label(g.status2)
        g.woe_value = g.status

        g.name = 'wine'
        self.OnCheck()
        wine_but.set_label(g.status)
        g.wine_value = g.status

        g.name = 'virtualbox'
        self.OnCheck()
        vbox_but.set_label(g.status)
        g.vbox_value = g.status

        g.name = 'gparted'
        self.OnCheck()
        gparted_but.set_label(g.status)
        g.gparted_value = g.status

        g.name = 'Touchpad'
        self.OnCheck()
        self.stamp()
        gest_but.set_label(g.status2)
        g.gest_value = g.status

        g.name = 'audacity'
        self.OnCheck()
        auda_but.set_label(g.status)
        g.auda_value = g.status

        g.name = 'deja-dup'
        self.OnCheck()
        deja_but.set_label(g.status)
        g.deja_value = g.status

        g.name = 'timeshift'
        self.OnCheck()
        self.stamp()
        tims_but.set_label(g.status2)
        g.tims_value = g.status

        g.name = 'TeamViewer'
        self.OnCheck()
        tw_but.set_label(g.status)
        g.tw_value = g.status

        g.name = 'gnome-boxes'
        self.OnCheck()
        box_but.set_label(g.status)
        g.box_value = g.status

        g.scanner = False
#################################################################################

    def button_clicked (self, button):

        if g.scanner == False:
            print('VALUE_FOUND')
            notebook_box = self.builder.get_object('notebook_box')
            g.stack.set_visible_child(notebook_box)
        elif g.scanner:
            notebook_box = self.builder.get_object('notebook_box')
            g.stack.set_visible_child(notebook_box)
            print('NO_VALUE')
            app.scanner()
        else:
            print('ERROR')

    def OnNeed(self):
        g.scanner = True
        g.spinning = True
        sTxt = self.builder.get_object('spinner_txt')
        sTxt.set_label('Loading...')
        spinner = self.builder.get_object('spinner')
        t1 = myThread(1, "Thread-1")
        t1.start()
        spinner_box = self.builder.get_object('spinner_box')
        g.stack.set_visible_child(spinner_box)
        g.m = 0
        self.win.set_decorated(False)
        spinner.start()
        def counter(timer):
            s=timer.count+1
            #print(s)
            timer.count = s
            if g.name+'R' == g.CA:
                sTxt.set_label(g.rmMsg+'         Elapsed time : '+str(g.m)+':'+str(s))
            else:
                sTxt.set_label(g.inMsg+'         Elapsed time : '+str(g.m)+':'+str(s)+'        It will take around %d minute(s).' % g.kbTime)
            if s == 59:
                timer.count = -1
                g.m = g.m+1
            if t1.isAlive():
                return True
            else:
                timer.count = 0
                spinner.stop()
                button = 0 # WTF??! Why does it work?!
                self.button_clicked(button)
                self.win.set_decorated(True)
                g.spinning = False
                return False
        self.source_id = GLib.timeout_add(1000, counter, self)

    def on_fb_but_clicked(self, button):
        view_fb = self.builder.get_object('view_fb')
        web_box = self.builder.get_object('web_box')
        g.browserholder.load_uri("https://docs.google.com/forms/d/e/1FAIpQLSec6abGuF3c-zTyLt1NUes2kifOlAAhrc5FOLPUIPUHhA9cmA/viewform?hl=en")
        view_fb.add(g.browserholder)
        g.browserholder.show()
        g.stack.set_visible_child(web_box)

    def on_git_link_clicked(self, button):
        webbrowser.open_new("https://swanux.github.io/hsuite/")

    def on_htools_but_clicked(self, button):
        x, y = g.window.get_position()
        sx, sy = g.window.get_size()
        dialogWindow = Gtk.MessageDialog(None,
                              Gtk.DialogFlags.MODAL | Gtk.DialogFlags.DESTROY_WITH_PARENT,
                              Gtk.MessageType.INFO,
                              Gtk.ButtonsType.OK,
                              g.txt1)

        dialogWindow.set_title("Coming soon")
        dsx, dsy = dialogWindow.get_size()
        dialogWindow.move(x+((sx-dsx)/2), y+((sy-dsy)/2))
        dialogWindow.show_all()
        res = dialogWindow.run()
        dialogWindow.destroy()

    def on_ac_but_clicked(self, button):
        self.on_htools_but_clicked(button)

    def on_db_but_clicked(self, button):
        distro_box = self.builder.get_object('distro_box')
        g.stack.set_visible_child(distro_box)

    def on_about_but_clicked(self, button):
        scroll_about = self.builder.get_object('scroll_about')
        g.stack.set_visible_child(scroll_about)

    def OnCheck(self):
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

    def home_clicked (self, button):
        scroll_home = self.builder.get_object('scroll_home')
        g.stack.set_visible_child(scroll_home)

    def on_page(self, button):
        g.text = self.builder.get_object('page_txt')
        page = self.builder.get_object('scroll_desc')
        g.text.set_text(g.label)
        g.stack.set_visible_child(page)
############################################################################
    def on_opera_clicked (self, button):
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
        g.label = """Google Chrome

Google Chrome is the most popular browser nowadays for Android and PC also. 
It's reliable, stable and fast, however, you know, Google doesn't respect your privacy sometimes... 

But at the end of the day, Chrome is still one of the best choices
if you'd like to use a well-known, cross platform browser.
        """
        self.on_page(button)

    def on_web_clicked (self, button):
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
        g.label = """WPS Office

WPS Office is the complete free office suite, integrates all office word processor functions: Word, Presentation, Spreadsheet, PDF, and fully compatible with Microsoft Word, Excel, PowerPoint, Google Doc and Adobe PDF format. If you need to use advanced features(e.g.: PDF2WORD, more cloud storage space), you can subscribe Preminum.

The aim of WPS Office is to provide you one-stop working solution since 1989. Various of office tools and unique and intuitive UI design ensures you enjoy the best office experience. You could easy to do all office documents processing on-the-go on Windows PC. WPS Office suite allows you can create, view, edit and share office documents.

It's the best free MS Office alternative for Linux in my opinion.
        """
        self.on_page(button)

    def on_loffice_clicked (self, button):
        g.label = """Libreoffice

LibreOffice is developed by users who, just like you, believe in the principles of Free Software and in sharing their work with the world in non-restrictive ways. At the core of these principles are the four essential freedoms and the tenets of The Document Foundation's Next Decade Manifesto.

We believe that users should have the freedom to run, copy, distribute, study, change and improve the software that we distribute. While we do offer no-cost downloads of the LibreOffice suite of programs, Free Software is first and foremost a matter of liberty, not price. We campaign for these freedoms because we believe that everyone deserves them.
        """
        self.on_page(button)

    def on_ooffice_clicked (self, button):
        g.label = """Only Office

ONLYOFFICE Desktop Editors is a free open source office suite that combines text, spreadsheet and presentation editors allowing to create, view and edit documents stored on your Windows/Linux PC or Mac without an Internet connection. It is fully compatible with Office Open XML formats: .docx, .xlsx, .pptx.

The ONLYOFFICE desktop suite pack allows extending the functionality with the pre-installed plugins, e.g. you can insert special symbols and ClipArts, edit pictures, translate text, send documents as mail attachments right from the editors, etc.

The suite also provides quick access to broad collaborative capabilities. Users are able to switch to the online mode by connecting to the cloud (ONLYOFFICE cloud, Nextcloud, ownCloud) and collaborate on documents with the team in real time.
        """
        self.on_page(button)

    def on_msoffice_clicked (self, button):
        g.label = """Microsoft Office Online

Microsoft Office Online can serve as a free Microsoft Office alternative, as it lets you edit and share files created in a word processor, spreadsheet, and presentation program, as well access MS Outlook and OneNote.

Everything done through Microsoft Office Online is performed through a web browser and saved online so you can access the files from anywhere.
        """
        self.on_page(button)

    def on_goffice_clicked (self, button):
        g.label = """Google G Suite

G Suite—formerly known as Google Apps for Work—is a Software as a Service (SaaS) product that groups all the cloud-based productivity and collaboration tools developed by Google for businesses, institutes, and nonprofits. Included with every subscription you get access to custom Gmail addresses, Docs, Sheets, Slides, Calendar, Drive, Sites, and so much more.
        """
        self.on_page(button)

    def on_foffice_clicked (self, button):
        g.label = """Softmaker Free Office

SoftMaker Office is an office suite developed since 1987 by the German company SoftMaker Software GmbH, Nuremberg. SoftMaker is available as a one-time purchase option, in Standard and Professional editions, as well as a subscription-based version known as SoftMaker Office NX (available as Home and Universal editions).

A freeware version is released as well, under the name of SoftMaker FreeOffice. FreeOffice supersedes SoftMaker Office 2006 and 2008, which were released as freeware after originally being available for purchase.
        """
        self.on_page(button)

    def on_gedit_clicked (self, button):
        g.label = """Gedit

It is is the default text editor of the GNOME desktop environment and part of the GNOME Core Applications. Designed as a general-purpose text editor, gedit emphasizes simplicity and ease of use, with a clean and simple GUI, according to the philosophy of the GNOME project. It includes tools for editing source code and structured text such as markup languages.

It is free and open-source software subject to the requirements of the GNU General Public License version 2 or later.

gedit is also available for Mac OS X and Microsoft Windows.

Personally, I use gedit with extensions for programming, HSuite is also written in gedit.
        """
        self.on_page(button)

    def on_gnu_clicked (self, button):
        g.label = """GNU Emacs

EMACS (Editor MACroS) is a family of text editors that are characterized by their extensibility. The manual for the most widely used variant, GNU Emacs, describes it as "the extensible, customizable, self-documenting, real-time display editor". Development of the first Emacs began in the mid-1970s, and work on its direct descendant, GNU Emacs, continues actively as of 2019.

Emacs has over 10,000 built-in commands and its user interface allows the user to combine these commands into macros to automate work. Implementations of Emacs typically feature a dialect of the Lisp programming language that provides a deep extension capability, allowing users and developers to write new commands and applications for the editor. Extensions have been written to manage email, files, outlines, and RSS feeds, as well as clones of ELIZA, Pong, Conway's Life, Snake and Tetris.
        """
        self.on_page(button)

    def on_vscode_clicked (self, button):
        g.label = """Visual Studio Code

Visual Studio Code is a source-code editor developed by Microsoft for Windows, Linux and macOS. It includes support for debugging, embedded Git control and GitHub, syntax highlighting, intelligent code completion, snippets, and code refactoring. It is highly customizable, allowing users to change the theme, keyboard shortcuts, preferences, and install extensions that add additional functionality. The source code is free and open source and released under the permissive MIT License. The compiled binaries are freeware and free for private or commercial use.
        """
        self.on_page(button)

    def on_atom_clicked (self, button):
        g.label = """Atom Editor

Atom is a free and open-source text and source code editor for macOS, Linux, and Microsoft Windows with support for plug-ins written in Node.js, and embedded Git Control, developed by GitHub. Atom is a desktop application built using web technologies. Most of the extending packages have free software licenses and are community-built and maintained. Atom is based on Electron (formerly known as Atom Shell), a framework that enables cross-platform desktop applications using Chromium and Node.js. It is written in CoffeeScript and Less.
        """
        self.on_page(button)

    def on_stedit_clicked (self, button):
        g.label = """Sublime Text Editor

Sublime Text is a proprietary cross-platform source code editor with a Python application programming interface (API). It natively supports many programming languages and markup languages, and functions can be added by users with plugins, typically community-built and maintained under free-software licenses.
        """
        self.on_page(button)

    def on_geany_clicked (self, button):
        g.label = """Geany

Geany is a lightweight GUI text editor using Scintilla and GTK+, including basic IDE features. It is designed to have short load times, with limited dependency on separate packages or external libraries on Linux. It has been ported to a wide range of operating systems, such as BSD, Linux, macOS, Solaris and Windows. The Windows port lacks an embedded terminal window; also missing from the Windows version are the external development tools present under Unix, unless installed separately by the user. Among the supported programming languages and markup languages are C, C++, C#, Java, JavaScript, PHP, HTML, LaTeX, CSS, Python, Perl, Ruby, Pascal, Haskell, Erlang, Vala and many others.
        """
        self.on_page(button)

    def on_skype_clicked (self, button):
        g.label = """Skype

Skype is for connecting with the people that matter most in your life and work. It's built for both one-on-one and group conversations and works wherever you are – via mobile, PC, Xbox and Alexa. Skype messaging and HD voice and video calling will help you share experiences and get things done with others.

With Skype, you can have meetings and create great things with your workgroup, share a story or celebrate a birthday with friends and family, and learn a new skill or hobby with a teacher. It’s free to use Skype – to send messages and have audio and video calls with groups of up to 50 people!

If you pay a little, you can do more things, in more ways, with more people – like call phones or SMS messages. You can pay as you go or buy a subscription, whatever works for you.

Try Skype out today and start adding your friends, family and colleagues. They won’t be hard to find; hundreds of millions of people are already using Skype to do all sorts of things together.
        """
        self.on_page(button)

    def on_discord_clicked (self, button):
        g.label = """Discord

Discord is a proprietary freeware VoIP application and digital distribution platform—designed initially for the video gaming community—that specializes in text, image, video and audio communication between users in a chat channel. Discord runs on Windows, macOS, Android, iOS, Linux, and in web browsers. As of 21 July 2019, there are over 250 million unique users of the software.
        """
        self.on_page(button)

    def on_telegram_clicked (self, button):
        g.label = """Telegram

Telegram is a cloud-based instant messaging and voice over IP service. Telegram client apps are available for Android, iOS, Windows Phone, Windows NT, macOS and Linux. Users can send messages and exchange photos, videos, stickers, audio and files of any type.

Telegram's client-side code is open-source software but the source code for recent versions is not always immediately published, whereas its server-side code is closed-source and proprietary. The service also provides APIs to independent developers. In March 2018, Telegram stated that it had 200 million monthly active users.
        """
        self.on_page(button)

    def on_signal_clicked (self, button):
        g.label = """Signal

Signal is a cross-platform encrypted messaging service developed by the Signal Foundation and Signal Messenger LLC. It uses the Internet to send one-to-one and group messages, which can include files, voice notes, images and videos. Its mobile apps can also make one-to-one voice and video calls, and the Android version can optionally function as an SMS app.

Signal uses standard cellular telephone numbers as identifiers and uses end-to-end encryption to secure all communications to other Signal users. The apps include mechanisms by which users can independently verify the identity of their contacts and the integrity of the data channel.

All Signal software are free and open-source. The clients are published under the GPLv3 license, while the server code is published under the AGPLv3 license. The non-profit Signal Foundation was launched in February 2018 with an initial funding of $50 million.
        """
        self.on_page(button)

    def on_hex_clicked (self, button):
        g.label = """HexChat

HexChat is an Internet Relay Chat client (IRC), forked from XChat. It has a choice of a tabbed document interface or tree interface, support for multiple servers, and numerous configuration options. Both command-line and graphical versions were available.
        """
        self.on_page(button)

    def on_franz_clicked (self, button):
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
        g.label = """0 A.D.

The best strategic game for Linux (in my opinion)

0 A.D. (pronounced "zero ey-dee") is a free, open-source, cross-platform real-time strategy (RTS) game of ancient warfare. In short, it is a historically-based war/economy game that allows players to relive or rewrite the history of Western civilizations, focusing on the years between 500 B.C. and 500 A.D. The project is highly ambitious, involving state-of-the-art 3D graphics, detailed artwork, sound, and a flexible and powerful custom-built game engine.

It also supports online and LAN multiplayer, custom map creation, adding mods to the game and if you would like to take part in the development you can do that also.
        """
        self.on_page(button)

    def on_tux_clicked (self, button):
        g.label = """SuperTux

The game, that every hardcore Linux users should play out.

SuperTux is a free and open-source two-dimensional platform video game published under the GNU General Public License (GPL).[1] The game was inspired by Nintendo's Super Mario Bros. series; instead of Mario, the hero in the game is Tux, the official mascot of the Linux kernel.
        """
        self.on_page(button)

    def on_wot_clicked (self, button):
        g.label = """World Of Tanks (Unofficial)

World of Tanks (WoT) is a massively multiplayer online game developed by Belarusian company Wargaming, featuring mid-20th century (1930s–1960s) era combat vehicles. It is built upon a freemium business model where the game is free-to-play, but participants also have the option of paying a fee for use of "premium" features. The focus is on player vs. player gameplay with each player controlling an armored vehicle.

World of Tanks has been ported to multiple gaming consoles. The PlayStation 4, Xbox 360 and Xbox Ones version was developed by Wargaming West studio. World of Tanks has also recently expanded to mobile platforms under the title World of Tanks Blitz, in addition to a board game titled World of Tanks Rush and a collectable card game titled World of Tanks: Generals. World of Tanks was followed by World of Warplanes and World of Warships.
        """
        self.on_page(button)

    def on_pol_clicked (self, button):
        g.label = """Play On Linux

One of the best ways to play Windows games on Linux.

PlayOnLinux is a piece of software which allows you to easily install and use numerous games and apps designed to run with Microsoft® Windows®.
Few games are compatible with GNU/Linux at the moment and it certainly is a factor preventing the migration to this system. PlayOnLinux brings a cost-free, accessible and efficient solution to this problem.
        """
        self.on_page(button)

    def on_steam_clicked (self, button):
        g.label = """Steam

The overall best when it comes to gaming on every platform.

Steam is the ultimate game platform, also for Linux. It offers Steam Play feature. Steam Play allows you to purchase your games once and play anywhere. Whether you have purchased your Steam Play enabled game on a Mac or PC (both Windows and Linux), you will be able to play on the other platform free of charge. So a lots of Windows only games can be played on Linux without problems.
        """
        self.on_page(button)

    def on_mc_clicked (self, button):
        g.label = """Minecraft

Everyone knows this game... But if you don't, here's a short descriptio.

Minecraft is a sandbox video game created by Swedish game developer Markus Persson and released by Mojang in 2011. The game allows players to build with a variety of different blocks in a 3D procedurally generated world, requiring creativity from players. Other activities in the game include exploration, resource gathering, crafting, and combat. Multiple game modes that change gameplay are available, including—but not limited to—a survival mode, in which players must acquire resources to build the world and maintain health, and a creative mode, where players have unlimited resources to build with. The Java Edition of the game allows players to modify the game with mods to create new gameplay mechanics, items, textures and assets. In September 2014, Microsoft announced a deal to buy Mojang and the Minecraft intellectual property for US$2.5 billion, with the acquisition completed two months later.'
        """
        self.on_page(button)

    def on_pops_clicked (self, button):
        g.label = """Popsicle

Popsicle is a lightweight open source USB image writer tool written in Rust by System76, the company behind a lots of outsandingly great Linux Desktops/Laptops and the heavy customized Ubuntu based distro, Pop!_OS.
        """
        self.on_page(button)

    def on_woe_clicked (self, button):
        g.label = """WoeUSB

Write Windows ISO to removable storage.

WoeUSB is Linux tool for creating Windows USB stick installer from a real Windows DVD or an image. It contains two programs, woeusb and woeusbgui. It’s a fork of Congelli501’s WinUSB software which received its last update in 2012.

woeusb is a CLI utility that does the actual creation of a bootable Windows installation USB storage device from either an existing Windows installation or a disk image. woeusbgui (as the name suggests,) is a woeusb GUI wrapper based on WxWidgets.
        """
        self.on_page(button)

    def on_wine_clicked (self, button):
        g.label = """Wine

Run Windows programs on Linux

Wine (originally an acronym for "Wine Is Not an Emulator") is a compatibility layer capable of running Windows applications on several POSIX-compliant operating systems, such as Linux, macOS, & BSD. Instead of simulating internal Windows logic like a virtual machine or emulator, Wine translates Windows API calls into POSIX calls on-the-fly, eliminating the performance and memory penalties of other methods and allowing you to cleanly integrate Windows applications into your desktop.
        """
        self.on_page(button)

    def on_vbox_clicked (self, button):
        g.label = """Oracle Virtualbox

Run virtual machines on your PC

A VirtualBox or VB is a software virtualization package that installs on an operating system as an application. VirtualBox allows additional operating systems to be installed on it, as a Guest OS, and run in a virtual environment. In 2010, VirtualBox was the most popular virtualization software application. Supported operating systems include Windows XP, Windows Vista, Windows 7, macOS X, Linux, Solaris, and OpenSolaris.

VirtualBox was originally developed by Innotek GmbH and released in 2007 as an open-source software package. The company was later purchased by Sun Microsystems. Oracle Corporation now develops the software package and titles it Oracle VM VirtualBox.
        """
        self.on_page(button)

    def on_gparted_clicked (self, button):
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
        g.label = """Touchpad Gestures

The app is called ‘Gestures’ and is described by its developer as being a “minimal Gtk+ GUI app for libinput-gestures”.

Windows and macOS both come with a variety of useful touchpad gestures pre-configured out of the box, and offer easy-to-access settings for adjusting or changing gesture behaviour to your liking.

Alas Ubuntu, like many Linux distributions, is a little lacking in this regard. Only a handful of basic gestures for scrolling and right-click available out of the box on Ubuntu 18.04 LTS, for instance.

But by using the “Gestures” app you can quickly effect a set of custom trackpad gestures that are on par with other operating systems, and in some cases, far more useful!
        """
        self.on_page(button)

    def on_auda_clicked (self, button):
        g.label = """Audacity

The free and open-source audio tool

Audacity is the name of a popular open source multilingual audio editor and recorder software that is used to record and edit sounds. It is free and works on Windows, Mac OS X, GNU/Linux and other operating systems.

Audacity can be used to perform a number of audio editing and recording tasks such as making ringtones, mixing stero tracks, transferring tapes and records to computer or CD, splitting recordings into separate tracks and more. The Audacity Wiki provides indepth tutorials on how to do these types of tasks in Audacity. Vendors can also freely bundle Audacity with their products or sell or distribute copies of Audacity under the GNU General Public License (GPL). 
        """
        self.on_page(button)

    def on_deja_clicked (self, button):
        g.label = """Déja-Dup

One of the most powerful backup solutions for Linux

Deja-dup: is a simple yet powerful backup tool included with Ubuntu. It offers the power of resync with incremental backups, encryption, scheduling, and support for remote services. With Deja-dup, you can quickly revert files to previous versions or restore missing files from a file manager window. 

You can do full system backups, Home folder backup or even settings backup in Ubuntu. You can backup to your GDrive storage also.
        """
        self.on_page(button)

    def on_tims_clicked (self, button):
        g.label = """Timeshift

The best backup solution (in my opinion) for Linux

Timeshift for Linux is an application that provides functionality similar to the System Restore feature in Windows and the Time Machine tool in Mac OS. Timeshift protects your system by taking incremental snapshots of the file system at regular intervals. These snapshots can be restored at a later date to undo all changes to the system.

In RSYNC mode, snapshots are taken using rsync and hard-links. Common files are shared between snapshots which saves disk space. Each snapshot is a full system backup that can be browsed with a file manager.

In BTRFS mode, snapshots are taken using the in-built features of the BTRFS filesystem. BTRFS snapshots are supported only on BTRFS systems having an Ubuntu-type subvolume layout (with @ and @home subvolumes).

Timeshift is similar to applications like rsnapshot, BackInTime and TimeVault but with different goals. It is designed to protect only system files and settings. User files such as documents, pictures and music are excluded. This ensures that your files remains unchanged when you restore your system to an earlier date.
        """
        self.on_page(button)

    def on_tw_clicked (self, button):
        g.label = """TeamViewer

TeamViewer (TeamViewer 6) is a popular piece of  software used for Internet-based remote access and support. TeamViewer software can connect to any PC or server, so you can remote control your partner's PC as if you were sitting right in front of it. For the remote session to work the partner has to start a small application, which does not require installation or administrative rights.

TeamViewer 6 is the latest version of the software and works with Windows, Mac, Linux operating systems and Mobile (Android, Apple iPad, Apple iPhone) devices. TeamViewer 6 is free for all non-commercial users.
        """
        self.on_page(button)

    def on_box_clicked (self, button):
        g.label = """Gnome Boxes

The simpliest way to run virtual machines as a normal, non-expert user.

GNOME Boxes is an application of the GNOME Desktop Environment, used to access remote or virtual systems. Boxes uses the QEMU, KVM, and libvirt virtualisation technologies.

GNOME Boxes requires the CPU to support some kind of Hardware-assisted virtualization (Intel VT-x, for example).
        """
        self.on_page(button)



    def onIns(self):
        g.CA = g.name
        g.inMsg = 'Installing '+g.name+':'
        g.indMsg = g.name+' installed sucsesfully!'
        if g.name == 'Timeshift' and g.distro == 'Arch':
            g.inMsg = 'Installing '+g.name+'''. NOTE: The AUR package is currently 
broken because vala incompatibility. If it does not work correctly 
run sudo rm -rf /home/$USER/.tmp_hsuite/ to remove trash files after broken install.'''

    def onRem(self):
        g.CA = g.name+'R'
        g.rmMsg = 'Removing '+g.name+':'
        g.rmdMsg = g.name+' removed sucsesfully.'
############################################################################
    def on_opera_but_clicked(self, button):
        g.name = 'Opera'
        if g.opera_value == 'Install':
            if g.distro == 'Arch':
                g.kbTime = 1
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.kbTime = 1
            self.onIns()
        elif g.opera_value == 'Remove':
            self.onRem()
        print(g.CA)
        self.OnNeed()

    def on_chrome_but_clicked(self, button):
        g.name = 'Chrome'
        if g.chrome_value == 'Install':
            if g.distro == 'Arch':
                g.kbTime = 4
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.kbTime = 1
            self.onIns()
        elif g.chrome_value == 'Remove':
            self.onRem()
        print(g.CA)
        self.OnNeed()

    def on_web_but_clicked(self, button):
        g.name = 'Web'
        if g.web_value == 'Install':
            if g.distro == 'Arch':
                g.kbTime = 1
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.kbTime = 1
            self.onIns()
        elif g.web_value == 'Remove':
            self.onRem()
        print(g.CA)
        self.OnNeed()

    def on_firefox_but_clicked(self, button):
        g.name = 'Firefox'
        if g.firefox_value == 'Install':
            if g.distro == 'Arch':
                g.kbTime = 1
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.kbTime = 2
            self.onIns()
        elif g.firefox_value == 'Remove':
            self.onRem()
        print(g.CA)
        self.OnNeed()

    def on_vivaldi_but_clicked(self, button):
        g.name = 'Vivaldi'
        if g.vivaldi_value == 'Install':
            if g.distro == 'Arch':
                g.kbTime = 4
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.kbTime = 1
            self.onIns()
        elif g.vivaldi_value == 'Remove':
            self.onRem()
        print(g.CA)
        self.OnNeed()

    def on_edge_but_clicked(self, button):
        g.name = 'Edge'

    def on_woffice_but_clicked(self, button):
        g.name = 'WPS Office'
        if g.woffice_value == 'Install':
            if g.distro == 'Arch':
                g.kbTime = 15
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.kbTime = 3
            self.onIns()
        elif g.woffice_value == 'Remove':
            self.onRem()
        print(g.CA)
        self.OnNeed()

    def on_loffice_but_clicked(self, button):
        g.name = 'Libreoffice'
        if g.loffice_value == 'Install':
            if g.distro == 'Arch':
                g.kbTime = 2
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.kbTime = 3
            self.onIns()
        elif g.loffice_value == 'Remove':
            self.onRem()
        print(g.CA)
        self.OnNeed()

    def on_ooffice_but_clicked(self, button):
        g.name = 'Only Office'
        if g.ooffice_value == 'Install':
            if g.distro == 'Arch':
                g.kbTime = 9
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.kbTime = 2
            self.onIns()
        elif g.ooffice_value == 'Remove':
            self.onRem()
        print(g.CA)
        self.OnNeed()

    def on_msoffice_but_clicked(self, button):
        webbrowser.open_new("https://office.com")

    def on_goffice_but_clicked(self, button):
        webbrowser.open_new("https://docs.google.com")

    def on_foffice_but_clicked(self, button):
        g.name = 'Free Office'
        if g.foffice_value == 'Install':
            if g.distro == 'Arch':
                g.kbTime = 7
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.kbTime = 5
            self.onIns()
        elif g.foffice_value == 'Remove':
            self.onRem()
        print(g.CA)
        self.OnNeed()

    def on_gedit_but_clicked(self, button):
        g.name = 'Gedit'
        if g.gedit_value == 'Install':
            if g.distro == 'Arch':
                g.kbTime = 1
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.kbTime = 1
            self.onIns()
        elif g.gedit_value == 'Remove':
            self.onRem()
        print(g.CA)
        self.OnNeed()

    def on_gnu_but_clicked(self, button):
        g.name = 'GNU Emacs'
        if g.gnu_value == 'Install':
            if g.distro == 'Arch':
                g.kbTime = 1
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.kbTime = 1
            self.onIns()
        elif g.gnu_value == 'Remove':
            self.onRem()
        print(g.CA)
        self.OnNeed()

    def on_vscode_but_clicked(self, button):
        g.name = 'Visual Studio Code'
        if g.vscode_value == 'Install':
            if g.distro == 'Arch':
                g.kbTime = 1
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.kbTime = 1
            self.onIns()
        elif g.vscode_value == 'Remove':
            self.onRem()
        print(g.CA)
        self.OnNeed()

    def on_atom_but_clicked(self, button):
        g.name = 'Atom Editor'
        if g.atom_value == 'Install':
            if g.distro == 'Arch':
                g.kbTime = 1
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.kbTime = 4
            self.onIns()
        elif g.atom_value == 'Remove':
            self.onRem()
        print(g.CA)
        self.OnNeed()

    def on_stedit_but_clicked(self, button):
        g.name = 'Sublime Text Editor'
        if g.stedit_value == 'Install':
            if g.distro == 'Arch':
                g.kbTime = 1
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.kbTime = 1
            self.onIns()
        elif g.stedit_value == 'Remove':
            self.onRem()
        print(g.CA)
        self.OnNeed()

    def on_geany_but_clicked(self, button):
        g.name = 'Geany'
        if g.geany_value == 'Install':
            if g.distro == 'Arch':
                g.kbTime = 1
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.kbTime = 1
            self.onIns()
        elif g.geany_value == 'Remove':
            self.onRem()
        print(g.CA)
        self.OnNeed()

    def on_skype_but_clicked(self, button):
        g.name = 'Skype'
        if g.skype_value == 'Install':
            if g.distro == 'Arch':
                g.kbTime = 5
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.kbTime = 1
            self.onIns()
        elif g.skype_value == 'Remove':
            self.onRem()
        print(g.CA)
        self.OnNeed()

    def on_discord_but_clicked(self, button):
        g.name = 'Discord'
        if g.discord_value == 'Install':
            if g.distro == 'Arch':
                g.kbTime = 1
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.kbTime = 1
            self.onIns()
        elif g.discord_value == 'Remove':
            self.onRem()
        print(g.CA)
        self.OnNeed()

    def on_telegram_but_clicked(self, button):
        g.name = 'Telegram'
        if g.telegram_value == 'Install':
            if g.distro == 'Arch':
                g.kbTime = 1
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.kbTime = 1
            self.onIns()
        elif g.telegram_value == 'Remove':
            self.onRem()
        print(g.CA)
        self.OnNeed()

    def on_signal_but_clicked(self, button):
        g.name = 'Signal'
        if g.signal_value == 'Install':
            if g.distro == 'Arch':
                g.kbTime = 8
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.kbTime = 1
            self.onIns()
        elif g.signal_value == 'Remove':
            self.onRem()
        print(g.CA)
        self.OnNeed()

    def on_hex_but_clicked(self, button):
        g.name = 'HexChat'
        if g.hex_value == 'Install':
            if g.distro == 'Arch':
                g.kbTime = 1
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.kbTime = 1
            self.onIns()
        elif g.hex_value == 'Remove':
            self.onRem()
        print(g.CA)
        self.OnNeed()

    def on_franz_but_clicked(self, button):
        g.name = 'Franz'
        if g.franz_value == 'Install':
            if g.distro == 'Arch':
                g.kbTime = 8
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.kbTime = 1
            self.onIns()
        elif g.franz_value == 'Remove':
            self.onRem()
        print(g.CA)
        self.OnNeed()

    def on_0ad_but_clicked(self, button):
        g.name = '0 A.D.'
        if g.ad_value == 'Install':
            if g.distro == 'Arch':
                g.kbTime = 2
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.kbTime = 5
            self.onIns()
        elif g.ad_value == 'Remove':
            self.onRem()
        print(g.CA)
        self.OnNeed()

    def on_tux_but_clicked(self, button):
        g.name = 'SuperTux'
        if g.tux_value == 'Install':
            if g.distro == 'Arch':
                g.kbTime = 1
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.kbTime = 2
            self.onIns()
        elif g.tux_value == 'Remove':
            self.onRem()
        print(g.CA)
        self.OnNeed()

    def on_wot_but_clicked(self, button):
        g.name = 'World Of Tanks (Unofficial)'

    def on_pol_but_clicked(self, button):
        g.name = 'Play On Linux'
        if g.pol_value == 'Install':
            if g.distro == 'Arch':
                g.kbTime = 1
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.kbTime = 2
            self.onIns()
        elif g.pol_value == 'Remove':
            self.onRem()
        print(g.CA)
        self.OnNeed()

    def on_steam_but_clicked(self, button):
        g.name = 'Steam'
        if g.steam_value == 'Install':
            if g.distro == 'Arch':
                g.kbTime = 1
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.kbTime = 1
            self.onIns()
        elif g.steam_value == 'Remove':
            self.onRem()
        print(g.CA)
        self.OnNeed()

    def on_mc_but_clicked(self, button):
        g.name = 'Minecraft'
        if g.mc_value == 'Install':
            if g.distro == 'Arch':
                g.kbTime = 3
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.kbTime = 1
            self.onIns()
        elif g.mc_value == 'Remove':
            self.onRem()
        print(g.CA)
        self.OnNeed()

    def on_pops_but_clicked(self, button):
        g.name = 'Popsicle'
        if g.pops_value == 'Install':
            if g.distro == 'Arch':
                g.kbTime = 5
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.kbTime = 1
            self.onIns()
        elif g.pops_value == 'Remove':
            self.onRem()
        print(g.CA)
        self.OnNeed()

    def on_woe_but_clicked(self, button):
        g.name = 'WoeUSB'
        if g.woe_value == 'Install':
            if g.distro == 'Arch':
                g.kbTime = 2
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.kbTime = 1
            self.onIns()
        elif g.woe_value == 'Remove':
            self.onRem()
        print(g.CA)
        self.OnNeed()

    def on_wine_but_clicked(self, button):
        g.name = 'Wine'
        if g.wine_value == 'Install':
            if g.distro == 'Arch':
                g.kbTime = 1
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.kbTime = 1
            self.onIns()
        elif g.wine_value == 'Remove':
            self.onRem()
        print(g.CA)
        self.OnNeed()

    def on_vbox_but_clicked(self, button):
        g.name = 'Virtualbox'
        if g.vbox_value == 'Install':
            if g.distro == 'Arch':
                g.kbTime = 2
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.kbTime = 1
            self.onIns()
        elif g.vbox_value == 'Remove':
            self.onRem()
        print(g.CA)
        self.OnNeed()

    def on_gparted_but_clicked(self, button):
        g.name = 'GParted'
        if g.gparted_value == 'Install':
            if g.distro == 'Arch':
                g.kbTime = 1
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.kbTime = 1
            self.onIns()
        elif g.gparted_value == 'Remove':
            self.onRem()
        print(g.CA)
        self.OnNeed()

    def on_gest_but_clicked(self, button):
        g.name = 'Touchpad Gestures'
        if g.gest_value == 'Install':
            if g.distro == 'Arch':
                g.kbTime = 1
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.kbTime = 1
            self.onIns()
            x, y = g.window.get_position()
            sx, sy = g.window.get_size()
            dialogWindow = Gtk.MessageDialog(None,
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
            self.OnNeed()
            t1.join()
        elif g.gest_value == 'Remove':
            self.onRem()
        print(g.CA)
        self.OnNeed()
        t1.join()

    def on_auda_but_clicked(self, button):
        g.name = 'Audacity'
        if g.auda_value == 'Install':
            if g.distro == 'Arch':
                g.kbTime = 1
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.kbTime = 1
            self.onIns()
        elif g.auda_value == 'Remove':
            self.onRem()
        print(g.CA)
        self.OnNeed()

    def on_deja_but_clicked(self, button):
        g.name = 'Déja-Dup'
        if g.deja_value == 'Install':
            if g.distro == 'Arch':
                g.kbTime = 1
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.kbTime = 1
            self.onIns()
        elif g.deja_value == 'Remove':
            self.onRem()
        print(g.CA)
        self.OnNeed()

    def on_tims_but_clicked(self, button):
        g.name = 'Timeshift'
        if g.tims_value == 'Install':
            if g.distro == 'Arch':
                g.kbTime = 2
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.kbTime = 1
            self.onIns()
        elif g.tims_value == 'Remove':
            self.onRem()
        print(g.CA)
        self.OnNeed()

    def on_tw_but_clicked(self, button):
        g.name = 'TeamViewer'
        if g.tw_value == 'Install':
            if g.distro == 'Arch':
                g.kbTime = 1
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.kbTime = 1
            self.onIns()
        elif g.tw_value == 'Remove':
            self.onRem()
        print(g.CA)
        self.OnNeed()

    def on_box_but_clicked(self, button):
        g.name = 'Gnome Boxes'
        if g.box_value == 'Install':
            if g.distro == 'Arch':
                g.kbTime = 1
            elif g.distro == 'Ubuntu' or g.distro == 'Debian':
                g.kbTime = 1
            self.onIns()
        elif g.box_value == 'Remove':
            self.onRem()
        print(g.CA)
        self.OnNeed()
############################################################################x
    def on_back_button_clicked (self, button):
        if g.spinning:
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
        self.button_clicked(button)

app = GUI()
Gtk.main()
