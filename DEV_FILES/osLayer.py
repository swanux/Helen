#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
alive = False
user = ''
# waitState = False
# havPass = False

#________________________________________________________________ BEGIN OF THREADS ___________________________________________________________________#

# This class and function is the core of every background process in the program

def asroot(asr):            # The function to display prompt for root acces.
        # global havPass
        # global waitState
        print(asr)
        # waitState = True
        retCode = os.system('pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY bash -c "%s"' % asr)
        # if retCode == 0:
        #     havPass = True
        #     print('Gut')
        # else:
        #     havPass = False
        #     print('Nein...')
        # waitState = False


# Search deps
def aurer(fold, extra, runDep, buildDep):                                    # The builder for AUR
    asroot('pacman -Sq --noconfirm %s %s' % (runDep, buildDep))
    if extra == '':
        print('no extras')
        exe = False
    else:
        extra = list(extra.split(" "))
        exLen = len(extra)
        print('len of ex: %s' % exLen)
    if exe:
        for i in range(exLen):
            fold = extra[i]
            cmd = 'mkdir .tmp_hsuite && echo $USER && cd /home/%s/.tmp_hsuite && git clone https://aur.archlinux.org/%s.git && cd %s && makepkg -rc' % (user, fold, fold)
            os.system('runuser -l %s -c "%s"' % (user, cmd) )
            asroot('pacman -U --noconfirm /home/%s/.tmp_hsuite/%s/*.pkg.tar.xz ; rm -rf /home/%s/.tmp_hsuite/ && pacman -Runs --noconfirm %s' % (user, fold, user, buildDep))
    cmd = 'mkdir .tmp_hsuite && echo $USER && cd /home/%s/.tmp_hsuite && git clone https://aur.archlinux.org/%s.git && cd %s && makepkg -rc' % (user, fold, fold)
    os.system('runuser -l %s -c "%s"' % (user, cmd) )
    asroot('pacman -U --noconfirm /home/%s/.tmp_hsuite/%s/*.pkg.tar.xz ; rm -rf /home/%s/.tmp_hsuite/ && pacman -Runs --noconfirm %s' % (user, fold, user, buildDep))


def fusConfs():
    os.system('mkdir -p /home/$USER/.config/autostart && mkdir -p /home/$USER/.config/fusuma && cp /usr/share/hsuite/config.yml /home/$USER/.config/fusuma/ && cp /usr/share/hsuite/fusuma.desktop /home/$USER/.config/autostart/')


def my_thread(status, distro, comm1, comm2, faur, extra, runDep, buildDep):
    print(status+' '+distro)
    print('faur: %s' % faur)
    global alive
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
                asroot('DEBIAN_FRONTEND=noninteractive apt install %s %s -y' % (comm1, extra))
        elif distro == 'Arch':
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
                    os.system('mkdir /home/%s/.tmp_tw && cd /home/%s/.tmp_tw && wget https://download.teamviewer.com/download/linux/teamviewer_amd64.tar.xz' % (user, user))
                    ver = os.popen('cd /home/%s/.tmp_tw && ls' % user).read()
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
                    os.system('tar -xJf /home/%s/.tmp_tw/%s && rm -rf /home/%s/.tmp_tw/%s' % (user, ver, user, ver))
                    asroot('cd /home/%s/.tmp_tw/teamviewer && ./tv-setup install force')
                elif comm2 == 'virtualbox':
                    asroot('pacman -Sq --noconfirm %s %s && /sbin/rcvboxdrv setup' % (comm2, extra))
                else:
                    asroot('pacman -Sq --noconfirm %s %s' % (comm2, extra))
        else:
            print('E: Bad name in os_layer!!')
    elif status == 'remove':
        if distro == 'Ubuntu' or distro == 'Debian':
            if extra == 'popsicle-cli-git':
                extra = 'popsicle-gtk'
            if comm1 == 'fusuma':
                asroot('yes | gem uninstall fusuma-plugin-wmctrl fusuma && apt purge xdotool libinput-tools -y && apt autoremove -y && gpasswd -d $USER input && rm -rf /home/$USER/.config/fusuma && rm /home/$USER/.config/autostart/fusuma.desktop')
            else:
                asroot('DEBIAN_FRONTEND=noninteractive apt purge %s %s -y ; apt autoremove -y' % (comm1, extra))
        elif distro == 'Arch':
            if comm2 == 'fusuma':
                asroot('pacman -Runs --noconfirm xdotool libinput && yes | gem uninstall fusuma-plugin-wmctrl fusuma && gpasswd -d $USER input && && rm -rf /home/$USER/.config/fusuma && rm /home/$USER/.config/autostart/fusuma.desktop')
            elif comm2 == 'TeamViewer':
                asroot('cd /home/%s/.tmp_tw/teamviewer && ./tv-setup uninstall force && rm -rf teamviewer && rm -rf /opt/teamviewer' % user)
            else:
                asroot('pacman -Runs --noconfirm  %s %s %s' % (comm2, extra, runDep))
        else:
            print('E: Bad name in os_layer!!')
    else:
        print('E: Bad status!')
    print('end of func')
    alive = False

#__________________________________________________________________ END OF THREADS _____________________________________________________________________#
