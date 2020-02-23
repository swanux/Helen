#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from aptdaemon import client
alive = False
user = ''
scanner = True
apt_client = client.AptClient()
trans = ""
# apt_trans = client.AptTransaction()
# waitState = False
# havPass = False

#________________________________________________________________ BEGIN OF THREADS ___________________________________________________________________#

# This class and function is the core of every background process in the program

def asroot(asr):            # The function to display prompt for root acces.
        # global havPass
        # global waitState
        print(asr)
        # waitState = True
        os.system('pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY bash -c "%s"' % asr)
        # if retCode == 0:
        #     havPass = True
        #     print('Gut')
        # else:
        #     havPass = False
        #     print('Nein...')
        # waitState = False


# Search deps
def aurer(fold, extra, runDep, buildDep):                                    # The builder for AUR
    os.system('zenity --info --text="Note, that installing from AUR can require\npassword up to 3 times and can last longer (~5-10 mins).\nAlso note, that these packages may fail to build\ndue to problems in the PKGBUILD file from AUR." --ellipsize')
    asroot('pacman -Sq --noconfirm %s %s' % (runDep, buildDep))
    if extra == '':
        print('no extras')
        exe = False
    else:
        exe = True
        extra = list(extra.split(" "))
        exLen = len(extra)
        print('len of ex: %s' % exLen)
    if exe:
        for i in range(exLen):
            os.system('mkdir /home/$USER/.tmp_hsuite && echo $USER && cd /home/%s/.tmp_hsuite && git clone https://aur.archlinux.org/%s.git && cd %s && makepkg -rc' % (user, extra[i], extra[i]))
            asroot('pacman -U --noconfirm /home/%s/.tmp_hsuite/%s/*.pkg.tar.xz ; rm -rf /home/%s/.tmp_hsuite/ && pacman -Runs --noconfirm %s' % (user, extra[i], user, buildDep))
    if 'popsicle' in fold:
        os.system('mkdir /home/$USER/.tmp_hsuite && echo $USER && cd /home/%s/.tmp_hsuite && git clone https://github.com/swanux/popsicle-git.git && cd %s && makepkg -rc' % (user, fold))
    else:
        os.system('mkdir /home/$USER/.tmp_hsuite && echo $USER && cd /home/%s/.tmp_hsuite && git clone https://aur.archlinux.org/%s.git && cd %s && makepkg -rc' % (user, fold, fold))
    asroot('pacman -U --noconfirm /home/%s/.tmp_hsuite/%s/*.pkg.tar.xz ; rm -rf /home/%s/.tmp_hsuite/ && pacman -Runs --noconfirm %s' % (user, fold, user, buildDep))


def fusConfs():
    os.system('mkdir -p /home/$USER/.config/autostart && mkdir -p /home/$USER/.config/fusuma && cp /usr/share/hsuite/config.yml /home/$USER/.config/fusuma/ && cp /usr/share/hsuite/fusuma.desktop /home/$USER/.config/autostart/')

def on_fin(transaction, exit_state):
    global alive
    alive = False
    print('Trans : %s' % transaction)
    print('Code : %s' % exit_state)
    print("FIN")

# def on_fin2(transaction, exit_state):
#     print('REMOVEING OBSOLETED DEPS...')
#     transaction = apt_trans.remove_obsoleted_depends
#     transaction.connect("finished", on_fin)
#     transaction.run()
#     print('Trans : %s' % transaction)
#     print('Code : %s' % exit_state)
#     print("FIN")

def my_thread(status, distro, comm1, comm2, faur, extra, runDep, buildDep):
    print(status+' '+distro)
    print('faur: %s' % faur)
    global alive
    global trans
    alive = True
    if status == 'install':
        if distro == 'Ubuntu' or distro == 'Debian':
            # if faur:
            #     asroot('wget -o ~/Minecraft.deb https://launcher.mojang.com/download/Minecraft.deb && dpkg -i --force-all Minecraft.deb && apt install -f -y && rm Minecraft.deb')
            # else:
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
                # asroot('DEBIAN_FRONTEND=noninteractive apt install %s %s -y' % (comm1, extra))
                if extra == "":
                    pkgs = [comm1]
                    print(*pkgs)
                else:
                    pkgs = [comm1, extra]
                    print(*pkgs)
                trans = apt_client.install_packages(pkgs)
                trans.connect("finished", on_fin)
                trans.run()
        elif distro == 'Arch':
            if extra == 'popsicle-gtk':
                extra = ''
            if faur:
                aurer(comm2, extra, runDep, buildDep)
            else:
                if comm2 == 'fusuma':
                    try:
                        os.system('gsettings set org.gnome.desktop.peripherals.touchpad send-events enabled')
                    except:
                        print('no gnome found')
                    asroot('pacman -Sq --noconfirm wmctrl libinput xdotool && gem install %s fusuma-plugin-wmctrl && gpasswd -a $USER input' % comm2)
                    fusConfs()
                elif comm2 == 'TeamViewer':
                    os.system('mkdir /home/%s/.tmp_tw' % user)
                    os.system('cd /home/%s/.tmp_tw && wget https://download.teamviewer.com/download/linux/teamviewer_amd64.tar.xz' % user)
                    os.system('cd /home/%s/.tmp_tw && tar -xJf /home/%s/.tmp_tw/teamviewer_amd64.tar.xz && rm /home/%s/.tmp_tw/teamviewer_amd64.tar.xz' % (user, user, user))
                    asroot('cd /home/%s/.tmp_tw/teamviewer && pacman -S --noconfirm qt5-quickcontrols qt5-webkit qt5-x11extras && ./tv-setup install force' % user)
                elif comm2 == 'virtualbox':
                    asroot('pacman -Sq --noconfirm %s %s && /sbin/rcvboxdrv setup' % (comm2, extra))
                    print('Applying patch for VBox on Arch')
                else:
                    asroot('pacman -Sq --noconfirm %s %s' % (comm2, extra))
                alive = False
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
                trans.connect("finished", on_fin)
                trans.run()
                # asroot('DEBIAN_FRONTEND=noninteractive apt purge %s %s -y ; apt autoremove -y' % (comm1, extra))
        elif distro == 'Arch':
            if extra == 'popsicle-gtk':
                extra = ''
            if comm2 == 'fusuma':
                asroot('pacman -Runs --noconfirm xdotool libinput && yes | gem uninstall fusuma-plugin-wmctrl fusuma && gpasswd -d $USER input && && rm -rf /home/$USER/.config/fusuma && rm /home/$USER/.config/autostart/fusuma.desktop')
            elif comm2 == 'TeamViewer':
                asroot('cd /home/%s/.tmp_tw/teamviewer && ./tv-setup uninstall force && rm -rf /home/%s/.tmp_tw/ && rm -rf /opt/teamviewer' % (user, user))
            else:
                asroot('pacman -Runs --noconfirm  %s %s %s' % (comm2, extra, runDep))
            alive = False
        else:
            print('E: Bad name in os_layer!!')
    else:
        print('E: Bad status!')
    print('end of func')

#__________________________________________________________________ END OF THREADS _____________________________________________________________________#
