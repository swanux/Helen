#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import gi
import gettext
import locale
APP = "hsuite"
WHERE_AM_I = os.path.abspath(os.path.dirname(__file__))
LOCALE_DIR = os.path.join(WHERE_AM_I, 'translations/mo')
locale.setlocale(locale.LC_ALL, locale.getlocale())
locale.bindtextdomain(APP, LOCALE_DIR)
gettext.bindtextdomain(APP, LOCALE_DIR)
gettext.textdomain(APP)
_ = gettext.gettext
alive = False
user = ''
scanner = True

def init(distro):
    global apt_client
    if distro == 'Ubuntu' or distro == 'Debian':
        from aptdaemon import client
        apt_client = client.AptClient()

#________________________________________________________________ BEGIN OF THREADS ___________________________________________________________________#

# This class and function is the core of every background process in the program

def asroot(asr):            # The function to display prompt for root acces.
        print(asr)
        os.system('pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY bash -c "%s"' % asr)


def fusConfs():
    os.system('mkdir -p /home/$USER/.config/autostart && mkdir -p /home/$USER/.config/fusuma && cp /usr/share/hsuite/config.yml /home/$USER/.config/fusuma/ && cp /usr/share/hsuite/fusuma.desktop /home/$USER/.config/autostart/')

def my_thread(status, distro, comm1, comm2, extra):
    print(status+' '+distro)
    global alive
    global trans
    trans = ""
    alive = True
    if status == 'install':
        if distro == 'Ubuntu' or distro == 'Debian':
            if comm1 == 'firefox' and distro == 'Debian':
                comm1 = 'firefox-esr'
            if extra == 'popsicle-cli-git':
                extra = 'popsicle-gtk'
            if comm1 == 'fusuma':
                try:
                    os.system('gsettings set org.gnome.desktop.peripherals.touchpad send-events enabled')
                except:
                    print('no gnome found')
                asroot('DEBIAN_FRONTEND=noninteractive apt install %s -y && gem install %s fusuma-plugin-wmctrl && gpasswd -a $USER input' % (extra, comm1))
                fusConfs()
            else:
                if extra == "":
                    pkgs = [comm1]
                    print(*pkgs)
                else:
                    pkgs = [comm1, extra]
                    print(*pkgs)
                trans = apt_client.install_packages(pkgs)
                return True, trans
        else:
            print('E: Bad name in os_layer!!')
    elif status == 'remove':
        if distro == 'Ubuntu' or distro == 'Debian':
            if comm1 == 'firefox' and distro == 'Debian':
                comm1 = 'firefox-esr'
            if comm1 == 'fusuma':
                asroot('yes | gem uninstall fusuma-plugin-wmctrl fusuma && apt purge xdotool libinput-tools -y && apt autoremove -y && gpasswd -d $USER input && rm -rf /home/$USER/.config/fusuma && rm /home/$USER/.config/autostart/fusuma.desktop')
            else:
                if extra == "":
                    pkgs = [comm1]
                    print(*pkgs)
                else:
                    pkgs = [comm1, extra]
                    print(*pkgs)
                trans = apt_client.remove_packages(pkgs)
                return True, trans
        else:
            print('E: Bad name in os_layer!!')
    else:
        print('E: Bad status!')
    print('end of func')

#__________________________________________________________________ END OF THREADS _____________________________________________________________________#
