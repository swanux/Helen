#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from concurrent import futures
asr = ''
bp = ''
alive = False

#_________________________________________________________________________________________ BEGIN OF THREADS _______________________________________________________________________________#

# This class and function is the core of every background process in the program

def asroot():                                               # The function to display prompt for root acces.
        print(asr)
        os.system('pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY bash -c "%s"' % asr)


myT = futures.ThreadPoolExecutor(max_workers=4)                    # init thread
# f = myT.submit(asroot())                                     # start it
# f.add_done_callback(done)                                    # after done run this function


def done (x):
    global alive
    alive = False


def my_thread():
    print(status+' '+distro)
    global alive
    global asr
    alive = True
    if status == 'install':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'DEBIAN_FRONTEND=noninteractive apt install %s -y' % comm1
            os.system('pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY bash -c "%s"' % asr)
        elif distro == 'Arch':
            asr = 'pacman -Sq --noconfirm %s' % comm2
            os.system('pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY bash -c "%s"' % asr)
        else:
            print('E: Bad name in os_layer!!')
    elif status == 'remove':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge %s -y ; apt autoremove -y' % comm1
            os.system('pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY bash -c "%s"' % asr)
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm  %s' % comm2
            os.system('pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY bash -c "%s"' % asr)
        else:
            print('E: Bad name in os_layer!!')
    else:
        print('E: Bad status!')
    print('end of func')
    alive = False






def my2_thread(dist, comm1, comm2):
    elif CA == 'Firefox':
        if distro == 'Ubuntu':
            asr = 'apt install firefox -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Sq --noconfirm firefox'
            app.asroot()
        elif distro == 'Debian':
            asr = 'apt install firefox-esr -y'
            app.asroot()
    elif CA == 'FirefoxR':
        if distro == 'Ubuntu':
            asr = 'apt purge firefox -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm firefox'
            app.asroot()
        elif distro == 'Debian':
            asr = 'apt purge firefox-esr -y ; apt autoremove -y'
            app.asroot()
    elif CA == 'Minecraft':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'wget ~/Minecraft.deb https://launcher.mojancom/download/Minecraft.deb ; dpkg -i --force-all Minecraft.deb ; apt install -f -y ; rm Minecraft.deb'
            app.asroot()
        elif distro == 'Arch':
            fold = 'minecraft-launcher'
            num = 1
            app.aurer()
    elif CA == 'MinecraftR':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge minecraft-launcher -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm minecraft-launcher'
            app.asroot()
    elif CA == 'TeamViewer':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'DEBIAN_FRONTEND=noninteractive apt install teamviewer -y ; teamviewer --daemon enable'
            app.asroot()
        elif distro == 'Arch':
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
            asr = 'cd teamviewer ; ./tv-setup install force'
            app.asroot()
    elif CA == 'TeamViewerR':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge teamviewer -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'cd teamviewer ; ./tv-setup uninstall force'
            app.asroot()
            os.system('rm -rf teamviewer && rm -rf /opt/teamviewer')
    elif CA == 'Virtualbox':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt install virtualbox -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Sq --noconfirm virtualbox ; /sbin/rcvboxdrv setup'
            app.asroot()
    elif CA == 'VirtualboxR':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge virtualbox* -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm virtualbox'
            app.asroot()
    elif CA == 'Touchpad Gestures':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt install libinput-tools libinput-bin wmctrl python3 xdotool python3-setuptools -y ; gpasswd -a %s input ; cd %s ; git clone https://github.com/bulletmark/libinput-gestures.git ; git clone https://gitlab.com/cunidev/gestures ; cd libinput-gestures ; ./libinput-gestures-setup install ; cd .. ; cd gestures ; python3 setup.py install ; cd .. ; rm -rf libinput-gestures ; rm -rf gestures' % (user, dire)
            app.asroot()
            os.system('cp /usr/share/hsuite/confs/libinput-gestures.conf ~/.config')
        elif distro == 'Arch':
            num = 3
            fold = 'libinput-gestures'
            app.aurer()
            num = 1
            fold = 'gestures'
            app.aurer()
            os.system('cp /usr/share/hsuite/confs/libinput-gestures.conf ~/.config')
    elif CA == 'Touchpad GesturesR':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge libinput-tools xdotool libinput-bin python3-setuptools -y ; apt autoremove -y ; rm -rf /usr/local/bin/gestures ; rm -rf /usr/bin/libinput-gestures ; rm -rf /usr/share/applications/libinput-gestures.desktop ; rm -rf /usr/share/applications/orcunidev.gestures.desktop'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm libinput-gestures gestures'
            app.asroot()
    else:
        print('Error 3')

#___________________________________________________________________________________________ END OF THREADS ______________________________________________________________________________________#
