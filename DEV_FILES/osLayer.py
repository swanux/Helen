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
    if CA == 'Opera':                                                             # CA is a global variable which is declared before calling this function. Its main role is to indicate the name of the program which is being changed/used. It tells the function what to do. CA means "Current Action"
        if distro == 'Ubuntu' or distro == 'Debian':                            # We need to check the current distro for some distro specific commands
            asr = 'DEBIAN_FRONTEND=noninteractive apt install opera-stable pepperflashplugin-nonfree -y' # asr is a global parameter, it means "as root". If something is given to asr, it'll run it with pkexec prompt
            app.asroot()                                                            # It calls the function itself
        elif distro == 'Arch':
            asr = 'pacman -Sq --noconfirm opera opera-ffmpeg-codecs flashplugin'
            app.asroot()
    elif CA == 'OperaR':                                                          # The R means this is for the removal of the program.
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge opera-stable pepperflashplugin-nonfree -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm  opera opera-ffmpeg-codecs flashplugin'
            app.asroot()
    elif CA == 'Lutris':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt install lutris -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Sq --noconfirm lutris'
            app.asroot()
    elif CA == 'LutrisR':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge lutris -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm  lutris'
            app.asroot()
    elif CA == 'Chrome':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt install google-chrome-stable -y'
            app.asroot()
        elif distro == 'Arch':
            fold = 'google-chrome' # The name of the folder (AUR)
            num = 2 # The position inside the folder (AUR)
            app.aurer() # Calling the builder function
    elif CA == 'ChromeR':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge google-chrome-stable -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm google-chrome'
            app.asroot()
    elif CA == 'Web':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt install epiphany-browser -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Sq --noconfirm epiphany'
            app.asroot()
    elif CA == 'WebR':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge epiphany-browser -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm epiphany'
            app.asroot()
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
    elif CA == 'Vivaldi':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt install vivaldi-stable -y'
            app.asroot()
        elif distro == 'Arch':
            fold = 'vivaldi'
            num = 2
            app.aurer()
    elif CA == 'VivaldiR':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge vivaldi-stable -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm vivaldi'
            app.asroot()
    elif CA == 'Only Office':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt install onlyoffice-desktopeditors -y'
            app.asroot()
        elif distro == 'Arch':
            fold = 'onlyoffice-bin'
            num = 1
            app.aurer()
    elif CA == 'Only OfficeR':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge onlyoffice-desktopeditors -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm onlyoffice-bin'
            app.asroot()
    elif CA == 'Free Office':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt install softmaker-freeoffice-2018 -y'
            app.asroot()
        elif distro == 'Arch':
            fold = 'freeoffice'
            num = 1
            app.aurer()
    elif CA == 'Free OfficeR':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge softmaker-freeoffice-2018 -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --nocnonfirm freeoffice'
            app.asroot()
    elif CA == 'Gedit':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt install gedit gedit-plugins -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Sq --noconfirm gedit gedit-plugins'
            app.asroot()
    elif CA == 'GeditR':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge gedit gedit-plugins -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm gedit gedit-plugins'
            app.asroot()
    elif CA == 'GNU Emacs':
        if distro == 'Ubuntu'or distro == 'Debian':
            asr = 'apt install emacs26 -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Sq --noconfirm emacs'
            app.asroot()
    elif CA == 'GNU EmacsR':
        if distro == 'Ubuntu':
            asr = 'apt purge emacs26 -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm emacs'
            app.asroot()
        elif distro == 'Debian':
            asr = 'apt purge emacs -y ; apt autoremove -y'
            app.asroot()
    elif CA == 'Visual Studio Code':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt install code -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Sq --noconfirm code'
            app.asroot()
    elif CA == 'Visual Studio CodeR':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge code -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm code'
            app.asroot()
    elif CA == 'Atom Editor':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt install atom -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Sq --noconfirm atom'
            app.asroot()
    elif CA == 'Atom EditorR':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge atom -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm atom'
            app.asroot()
    elif CA == 'Sublime Text Editor':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt install sublime-text -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Sq --noconfirm sublime-text'
            app.asroot()
    elif CA == 'Sublime Text EditorR':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge sublime-text -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm sublime-text'
            app.asroot()
    elif CA == 'Geany':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt install geany -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Sq --noconfirm geany'
            app.asroot()
    elif CA == 'GeanyR':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge geany -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm geany'
            app.asroot()
    elif CA == 'Discord':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt install discord -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Sq --noconfirm discord'
            app.asroot()
    elif CA == 'DiscordR':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge discord -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm discord'
            app.asroot()
    elif CA == 'Telegram':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt install telegram-desktop -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Sq --noconfirm telegram-desktop'
            app.asroot()
    elif CA == 'TelegramR':
        if distro == 'Ubuntu'or distro == 'Debian':
            asr = 'apt purge telegram-desktop -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm telegram-desktop'
            app.asroot()
    elif CA == 'Signal':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt install signal-desktop -y'
            app.asroot()
        elif distro == 'Arch':
            fold = 'signal'
            num = 2
            app.aurer()
    elif CA == 'SignalR':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge signal-desktop -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm signal'
            app.asroot()
    elif CA == 'HexChat':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt install hexchat -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Sq --noconfirm hexchat'
            app.asroot()
    elif CA == 'HexChatR':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge hexchat -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm hexchat'
            app.asroot()
    elif CA == 'SuperTux':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt install supertux -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Sq --noconfirm supertux'
            app.asroot()
    elif CA == 'SuperTuxR':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge supertux -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm supertux'
            app.asroot()
    elif CA == 'Play On Linux':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt install playonlinux -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Sq --noconfirm playonlinux'
            app.asroot()
    elif CA == 'Play On LinuxR':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge playonlinux -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm playonlinux'
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
    elif CA == 'Gnome Boxes':
        if distro == 'Ubuntu'or distro == 'Debian':
            asr = 'apt install gnome-boxes -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Sq --noconfirm gnome-boxes'
            app.asroot()
    elif CA == 'Gnome BoxesR':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge gnome-boxes -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm gnome-boxes'
            app.asroot()
    elif CA == 'Franz':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt install franz -y'
            app.asroot()
        elif distro == 'Arch':
            num = 2
            fold = 'franz'
            app.aurer()
    elif CA == 'FranzR':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge franz -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm franz'
            app.asroot()
    elif CA == 'Libreoffice':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt install libreoffice libreoffice-gtk -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Sq --noconfirm libreoffice-fresh'
            app.asroot()
    elif CA == 'LibreofficeR':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge libreoffice-* -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm libreoffice-fresh'
            app.asroot()
    elif CA == 'WPS Office':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'DEBIAN_FRONTEND=noninteractive apt install wps-office ttf-wps-fonts -y'
            app.asroot()
        elif distro == 'Arch':
            num = 2
            fold = 'wps-office'
            app.aurer()
            num = 2
            fold = 'ttf-wps-fonts'
            app.aurer()
    elif CA == 'WPS OfficeR':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge ttf-wps-fonts wps-office -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm wps-office ttf-wps-fonts'
            app.asroot()
    elif CA == 'Popsicle':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt install popsicle* -y'
            app.asroot()
        elif distro == 'Arch':
            fold = 'popsicle-git'
            num = 3
            app.aurer()
    elif CA == 'PopsicleR':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge popsicle* -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm popsicle-gtk-git'
            app.asroot()
    elif CA == 'Wine':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt install wine wine32 wine64 -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Sq --noconfirm wine'
            app.asroot()
    elif CA == 'WineR':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge wine* -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm wine'
            app.asroot()
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
    elif CA == 'WoeUSB':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt install woeusb -y'
            app.asroot()
        elif distro == 'Arch':
            num = 2
            fold = 'woeusb'
            app.aurer()
    elif CA == 'WoeUSBR':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge woeusb -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm woeusb'
            app.asroot()
    elif CA == 'GParted':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt install gparted gpart -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Sq --noconfirm gparted gpart'
            app.asroot()
    elif CA == 'GPartedR':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge gpart* -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm gparted'
            app.asroot()
    elif CA == 'Audacity':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt install audacity -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Sq --noconfirm audacity'
            app.asroot()
    elif CA == 'AudacityR':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge audacity* -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm audacity'
            app.asroot()
    elif CA == 'Déja-Dup':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt install deja-dup* -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Sq --noconfirm deja-dup'
            app.asroot()
    elif CA == 'Déja-DupR':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge deja-dup* -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm deja-dup'
            app.asroot()
    elif CA == 'Timeshift':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt install timeshift -y'
            app.asroot()
        elif distro == 'Arch':
            num = 1
            fold = 'timeshift'
            app.aurer()
    elif CA == 'TimeshiftR':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge timeshift -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm timeshift'
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
    elif CA == 'Skype':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt install skypeforlinux -y'
            app.asroot()
        elif distro == 'Arch':
            num = 3
            fold = 'skypeforlinux-stable-bin'
            app.aurer()
    elif CA == 'SkypeR':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge skypeforlinux -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm skypeforlinux-stable-bin'
            app.asroot()
    elif CA == 'Barrier by debauchee':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt install barrier -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Sq --noconfirm barrier'
            app.asroot()
    elif CA == 'Barrier by debaucheeR':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge barrier -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm barrier'
            app.asroot()
    elif CA == '0 A.D.':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt install 0ad -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Sq --noconfirm 0ad'
            app.asroot()
    elif CA == '0 A.D.R':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge 0ad -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm 0ad'
            app.asroot()
    elif CA == 'SuperTuxKart':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt install supertuxkart -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Sq --noconfirm supertuxkart'
            app.asroot()
    elif CA == 'SuperTuxKartR':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge supertuxkart -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm supertuxkart'
            app.asroot()
    elif CA == 'Steam':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt install steam-launcher -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Sq --noconfirm steam steam-native-runtime'
            app.asroot()
    elif CA == 'SteamR':
        if distro == 'Ubuntu' or distro == 'Debian':
            asr = 'apt purge steam* -y ; apt autoremove -y'
            app.asroot()
        elif distro == 'Arch':
            asr = 'pacman -Runs --noconfirm steam steam-native-runtime'
            app.asroot()
    else:
        print('Error 3')

#___________________________________________________________________________________________ END OF THREADS ______________________________________________________________________________________#
