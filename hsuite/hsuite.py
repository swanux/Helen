#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
author: swanux
last modified: July 2019

ToDos

     - Install & Update
DONE - App Spotlight
     - Distro Boutique
 ____________________________
|                            |
|   For the future...        |
|____________________________|

- Tools (xiaomi, adb)
- onlyoffice
- Rate apps
- App categories

~~~ After the beta stage ~~~

- Windows version
- Android version
"""
#Import modules
import wx
import wx.adv
import os
import sys
import threading
import time
import re
#try:
#    if getattr(sys, 'frozen') and hasattr(sys, '_MEIPASS'):
#        print(sys._MEIPASS)
#        os.chdir(sys._MEIPASS)
#    else:
#        fdir = "/home/sources"
#        os.chdir(fdir)
#        print(fdir)
#except:
#    fdir = "/home/sources"
#    os.chdir(fdir)
#    print(fdir)

os.chdir("/usr/share/hsuite")

import common as g

g.user = os.popen("logname").read()
g.user = g.user.rstrip()
print(g.user)

wer = os.popen('ls').read()
print(str(wer))
updated = False

dist = os.popen('uname -a').read()
print(dist)
if  'Ubuntu' in dist or 'Debian' in dist:
    g.distro = 'Ubuntu'
elif 'archlinux' in dist or 'manjaro' in dist:
    g.distro = 'Arch'
    vane = os.path.exists("/etc/hsuite.conf")
    print(vane)
    if vane:
        print('not first run')
    else:
        g.doIt = True
        print('first run')
else:
    g.distro = 'Error 4'
print(g.distro)
                    
if g.distro == 'Ubuntu':
    g.distroSpec = 'Apt-fast'
elif g.distro == 'Arch':
    g.distroSpec = 'AUR support'
else:
    g.distroSpec = 'Error 1'

print(g.distroSpec)
#except:
#    dial = wx.MessageDialog(None, 'Due to permission errors regarding the Debian package management we need to apply a fix on folder /usr/share/hsuite. Do you agree to run the required command automatically?', 'Attention', wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION | wx.STAY_ON_TOP)
#    result = dial.ShowModal()
#    if result == wx.ID_YES:
#        os.system('./bashLayer.sh')
#        wx.MessageBox('Now everything is fixed and will work correctly without any further interraction.' , 'Done', wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)
#    else:
#        wx.MessageBox('You need to run manually the command "sudo chmod 777 /usr/share/hsuite" without quotes if you would like to use the program.' , 'Note', wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)
#        exit()

#Declare functions
class myThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print ("Starting " + self.name)
        my_thread()
        print ("Exiting " + self.name)

def my_thread():
    if g.CA == 'update':
        if g.distro == 'Ubuntu':
            g.p = os.popen('apt update').read()
            if 'All packages are up to date.' in g.p:
                g.p = 0
            else:
                res = [int(i) for i in g.p.split() if i.isdigit()] 
                print(res)
                try:
                    g.p = res[1]
                except:
                    g.p = res[0]
                print(g.p)
        elif g.distro == 'Arch':
            os.system('pacman -Sy')
            g.p = os.popen('echo "n" | pacman -Su').read()
            if 'there is nothing to do' in g.p:
                g.p = 0
            else:
                m = re.findall(r'\d+(?:\.\d+)?', g.p)
                print(m)
                g.p = m[0]
    elif g.CA == 'upgrade':
        if g.distro == 'Ubuntu':
            g.p = os.popen('apt full-upgrade -y').read()
        elif g.distro == 'Arch':
            g.p = os.popen('pacman -Syu --noconfirm').read()
    elif g.CA == 'opera-stable':
        if g.distro == 'Ubuntu':
            os.system('wget https://download1.operacdn.com/pub/opera/desktop/60.0.3255.170/linux/opera-stable_60.0.3255.170_amd64.deb')
            os.system('apt install -f opera-stable_60.0.3255.170_amd64.deb && apt update && apt full-upgrade -y && rm opera-stable_60.0.3255.170_amd64.deb && apt install pepperflashplugin-nonfree')
        elif g.distro == 'Arch':
            os.system('pacman -Sq --noconfirm opera opera-ffmpeg-codecs flashplugin')
    elif g.CA == 'opera-stableR':
        if g.distro == 'Ubuntu':
            os.system('apt purge opera-stable pepperflashplugin-nonfree -y && apt autoremove -y')
        elif g.distro == 'Arch':
            os.system('pacman -Runs --noconfirm  opera opera-ffmpeg-codecs flashplugin')
    elif g.CA == 'snapd':
        if g.distro == 'Ubuntu':
            os.system('apt install snapd -y && snap install snap-store -y')
        elif g.distro == 'Arch':
            with open("logname.sh") as f:
                lines = f.readlines()
            lines[4] = 'runuser -l $persist -c "echo $USER && cd && git clone https://aur.archlinux.org/snapd.git && cd snapd && makepkg -rc"'
            with open("logname.sh", "w") as f:
                f.writelines(lines)
            os.system('./logname.sh')
            pkg = os.popen('ls /home/%s/snapd/' % g.user).read()
            pkg = pkg.split()
            pkg = pkg[1]
            print(pkg)
            os.system('pacman -U --noconfirm /home/%s/snapd/%s && systemctl enable --now snapd.socket && ln -s /var/lib/snapd/snap /snap && rm -rf /home/%s/snapd' % (g.user, pkg, g.user))
            wx.MessageBox('Reboot is required to apply all changes. After reboot just run "sudo snap install snap-store -y" to install snapstore.', 'Note', wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)
    elif g.CA == 'snapdR':
        if g.distro == 'Ubuntu':
            os.system('snap remove snap-store -y && apt purge snapd -y && apt autoremove -y')
        elif g.distro == 'Arch':
            os.system('pacman -Runs --noconfirm snapd && systemctl disable --now snapd.socket')
    elif g.CA == 'libreoffice':
        if g.distro == 'Ubuntu':
            os.system('apt install libreoffice libreoffice-gtk -y')
        elif g.distro == 'Arch':
            os.system('pacman -Sq --noconfirm libreoffice-fresh')
    elif g.CA == 'libreofficeR':
        if g.distro == 'Ubuntu':
            os.system('apt purge libreoffice-* -y && apt autoremove -y')
        elif g.distro == 'Arch':
            os.system('pacman -Runs --noconfirm libreoffice-fresh')
    elif g.CA == 'wps-office':
        if g.distro == 'Ubuntu':
            os.system('wget http://kdl.cc.ksosoft.com/wps-community/download/8722/wps-office_11.1.0.8722_amd64.deb')
            os.system('apt install -f wps-office_11.1.0.8722_amd64.deb')
            os.system('rm wps-office_11.1.0.8722_amd64.deb')
        elif g.distro == 'Arch':
            with open("logname.sh") as f:
                lines = f.readlines()
            lines[4] = 'runuser -l $persist -c "echo $USER && cd && git clone https://aur.archlinux.org/wps-office.git && cd wps-office && makepkg -rc"'
            with open("logname.sh", "w") as f:
                f.writelines(lines)
            os.system('./logname.sh')
            pkg = os.popen('ls /home/%s/wps-office/' % g.user).read()
            pkg = pkg.split()
            pkg = pkg[5]
            print(pkg)
            os.system('pacman -U --noconfirm /home/%s/wps-office/%s && rm -rf /home/%s/wps-office' % (g.user, pkg, g.user))
            with open("logname.sh") as f:
                lines = f.readlines()
            lines[4] = 'runuser -l $persist -c "echo $USER && cd && git clone https://aur.archlinux.org/ttf-wps-fonts.git && cd ttf-wps-fonts && makepkg -rc"'
            with open("logname.sh", "w") as f:
                f.writelines(lines)
            os.system('./logname.sh')
            pkg = os.popen('ls /home/%s/ttf-wps-fonts/' % g.user).read()
            pkg = pkg.split()
            pkg = pkg[2]
            print(pkg)
            os.system('pacman -U --noconfirm /home/%s/wps-office/%s && rm -rf /home/%s/ttf-wps-fonts' % (g.user, pkg, g.user))
    elif g.CA == 'wps-officeR':
        if g.distro == 'Ubuntu':
            os.system('apt purge wps-office -y && apt autoremove -y')
        elif g.distro == 'Arch':
            os.system('pacman -Runs --noconfirm wps-office ttf-wps-fonts')
    elif g.CA == 'etcher-electron':
        if g.distro == 'Ubuntu':
            with open("/etc/apt/sources.list") as f:
                lines = f.readlines()
            if 'deb https://deb.etcher.io stable etcher\n' in lines:
                print('repository found')
            else:
                os.system('echo "deb https://deb.etcher.io stable etcher" | tee -a /etc/apt/sources.list')
                os.system('apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 379CE192D401AB61')
            os.system('apt update && apt install etcher-electron -y')
        elif g.distro == 'Arch':
            with open("logname.sh") as f:
                lines = f.readlines()
            lines[4] = 'runuser -l $persist -c "echo $USER && cd && git clone https://aur.archlinux.org/electron3-bin.git && cd electron3-bin && makepkg -rc"'
            with open("logname.sh", "w") as f:
                f.writelines(lines)
            os.system('./logname.sh')
            pkg = os.popen('ls /home/%s/electron3-bin/' % g.user).read()
            pkg = pkg.split()
            pkg = pkg[3]
            print(pkg)
            os.system('pacman -U --noconfirm /home/%s/electron3-bin/%s && rm -rf /home/%s/electron3-bin' % (g.user, pkg, g.user))
            with open("logname.sh") as f:
                lines = f.readlines()
            lines[4] = 'runuser -l $persist -c "echo $USER && cd && git clone https://aur.archlinux.org/balena-etcher.git && cd balena-etcher && makepkg -rc"'
            with open("logname.sh", "w") as f:
                f.writelines(lines)
            os.system('./logname.sh')
            pkg = os.popen('ls /home/%s/balena-etcher/' % g.user).read()
            pkg = pkg.split()
            pkg = pkg[1]
            print(pkg)
            os.system('pacman -U --noconfirm /home/%s/balena-etcher/%s && rm -rf /home/%s/balena-etcher' % (g.user, pkg, g.user))
    elif g.CA == 'etcher-electronR':
        if g.distro == 'Ubuntu':
            os.system('apt purge etcher-electron -y && apt autoremove -y')
        elif g.distro == 'Arch':
            os.system('pacman -Runs --noconfirm balena-etcher electron3-bin')
    elif g.CA == 'wine':
        if g.distro == 'Ubuntu':
            os.system('apt install wine wine32 wine64 -y')
        elif g.distro == 'Arch':
            os.system('pacman -Sq --noconfirm wine')
    elif g.CA == 'wineR':
        if g.distro == 'Ubuntu':
            os.system('apt purge wine* -y && apt autoremove -y')
        elif g.distro == 'Arch':
            os.system('pacman -Runs --noconfirm wine')
    elif g.CA == 'virtualbox':
        if g.distro == 'Ubuntu':
            os.system('apt install virtualbox -y')
        elif g.distro == 'Arch':
            os.system('pacman -Sq --noconfirm virtualbox')
    elif g.CA == 'virtualboxR':
        if g.distro == 'Ubuntu':
            os.system('apt purge virtualbox* -y && apt autoremove -y')
        elif g.distro == 'Arch':
            os.system('pacman -Runs --noconfirm virtualbox')
    elif g.CA == 'woeusb':
        if g.distro == 'Ubuntu':
            os.system('add-apt-repository ppa:nilarimogard/webupd8 -y && apt update -y && apt install woeusb -y')
        elif g.distro == 'Arch':
            with open("logname.sh") as f:
                lines = f.readlines()
            lines[4] = 'runuser -l $persist -c "echo $USER && cd && git clone https://aur.archlinux.org/woeusb.git && cd woeusb && makepkg -rc"'
            with open("logname.sh", "w") as f:
                f.writelines(lines)
            os.system('./logname.sh')
            pkg = os.popen('ls /home/%s/woeusb/' % g.user).read()
            pkg = pkg.split()
            pkg = pkg[1]
            print(pkg)
            os.system('pacman -U --noconfirm /home/%s/woeusb/%s && rm -rf /home/%s/woeusb' % (g.user, pkg, g.user))
    elif g.CA == 'woeusbR':
        if g.distro == 'Ubuntu':
            os.system('apt purge woeusb -y && apt autoremove -y')
        elif g.distro == 'Arch':
            os.system('pacman -Runs --noconfirm woeusb')
    elif g.CA == 'gparted':
        if g.distro == 'Ubuntu':
            os.system('apt install gparted gpart -y')
        elif g.distro == 'Arch':
            os.system('pacman -Sq --nocpnfirm gparted gpart')
    elif g.CA == 'gpartedR':
        if g.distro == 'Ubuntu':
            os.system('apt purge gpart* -y && apt autoremove -y')
        elif g.distro == 'Arch':
            os.system('pacman -Runs --noconirm gparted gpart')
    elif g.CA == 'audacity':
        if g.distro == 'Ubuntu':
            os.system('apt install audacity -y')
        elif g.distro == 'Arch':
            os.system('pacman -Sq --noconfirm audacity')
    elif g.CA == 'audacityR':
        if g.distro == 'Ubuntu':
            os.system('apt purge audacity* -y && apt autoremove -y')
        elif g.distro == 'Arch':
            os.system('pacman -Runs --noconfirm audacity')
    elif g.CA == 'deja-dup':
        if g.distro == 'Ubuntu':
            os.system('apt install deja-dup* -y')
        elif g.distro == 'Arch':
            os.system('pacman -Sq --noconfirm deja-dup')
    elif g.CA == 'deja-dupR':
        if g.distro == 'Ubuntu':
            os.system('apt purge deja-dup* -y && apt autoremove -y')
        elif g.distro == 'Arch':
            os.system('pacman -Runs --noconfirm deja-dup')
    elif g.CA == 'timeshift':
        if g.distro == 'Ubuntu':
            os.system('apt install timeshift -y')
        elif g.distro == 'Arch':
            with open("logname.sh") as f:
                lines = f.readlines()
            lines[4] = 'runuser -l $persist -c "echo $USER && cd && git clone https://aur.archlinux.org/timeshift.git && cd timeshift && makepkg -rc"'
            with open("logname.sh", "w") as f:
                f.writelines(lines)
            os.system('./logname.sh')
            pkg = os.popen('ls /home/%s/timeshift/' % g.user).read()
            pkg = pkg.split()
            pkg = pkg[1]
            print(pkg)
            os.system('pacman -U --noconfirm /home/%s/timeshift/%s && rm -rf /home/%s/timeshift' % (g.user, pkg, g.user))
    elif g.CA == 'timeshiftR':
        if g.distro == 'Ubuntu':
            os.system('apt purge timeshift -y && apt autoremove -y')
        elif g.distro == 'Arch':
            os.system('pacman -Runs --noconfirm timeshift')
    elif g.CA == 'gestures':
        dial = wx.MessageDialog(None, 'You can currently only use this feature with Xorg based desktop. It does not support Wayland. Are you sure that you use Xorg?', 'Attention', wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION | wx.STAY_ON_TOP)
        result = dial.ShowModal()
        if result == wx.ID_YES:
            if g.distro == 'Ubuntu':
                os.system('apt install libinput-tools libinput-bin wmctrl python3 xdotools -y')
                os.system('gpasswd -a $USER input')
                os.system('git clone https://github.com/bulletmark/libinput-gestures.git && git clone https://gitlab.com/cunidev/gestures')
                os.system('cd libinput-gestures && ./libinput-gestures-setup install && cd && cd gestures && python3 setup.py install && cd && rm -rf libinput-gestures && rm -rf gestures')
            elif g.distro == 'Arch':
                with open("logname.sh") as f:
                    lines = f.readlines()
                lines[4] = 'runuser -l $persist -c "echo $USER && cd && git clone https://aur.archlinux.org/libinput-gestures.git && cd libinput-gestures && makepkg -rc"'
                with open("logname.sh", "w") as f:
                    f.writelines(lines)
                os.system('./logname.sh')
                pkg = os.popen('ls /home/%s/libinput-gestures/' % g.user).read()
                pkg = pkg.split()
                pkg = pkg[3]
                print(pkg)
                os.system('pacman -U --noconfirm /home/%s/libinput-gestures/%s && rm -rf /home/%s/libinput-gestures' % (g.user, pkg, g.user))
                with open("logname.sh") as f:
                    lines = f.readlines()
                lines[4] = 'runuser -l $persist -c "echo $USER && cd && git clone https://aur.archlinux.org/gestures.git && cd gestures && makepkg -rc"'
                with open("logname.sh", "w") as f:
                    f.writelines(lines)
                os.system('./logname.sh')
                pkg = os.popen('ls /home/%s/gestures/' % g.user).read()
                pkg = pkg.split()
                pkg = pkg[1]
                print(pkg)
                os.system('pacman -U --noconfirm /home/%s/gestures/%s && rm -rf /home/%s/gestures' % (g.user, pkg, g.user))
                wx.MessageBox('You need to reboot to apply all changes.' , 'Note', wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)
        else:
            print("No pressed")
    elif g.CA == 'gesturesR':
        if g.distro == 'Ubuntu':
            os.system('apt purge libinput-tools xdotools libinput-bin -y && apt autoremove -y')
            os.system('rm -rf /usr/local/bin/gestures && rm -rf /usr/bin/libinput-gestures && rm -rf /usr/share/applications/libinput-gestures.desktop && rm -rf /usr/share/applications/org.cunidev.gestures.desktop')
        elif g.distro == 'Arch':
            os.system('pacman -Runs --noconfirm libinput-gestures gestures')
    elif g.CA == 'skype':
        if g.distro == 'Ubuntu':
            os.system('wget https://go.skype.com/skypeforlinux-64.deb && apt install -f skypeforlinux-64.deb && rm -rf skypeforlinux-64.deb')
        elif g.distro == 'Arch':
            with open("logname.sh") as f:
                lines = f.readlines()
            lines[4] = 'runuser -l $persist -c "echo $USER && cd && git clone https://aur.archlinux.org/skypeforlinux-stable-bin.git && cd skypeforlinux-stable-bin && makepkg -rc"'
            with open("logname.sh", "w") as f:
                f.writelines(lines)
            os.system('./logname.sh')
            pkg = os.popen('ls /home/%s/skypeforlinux-stable-bin/' % g.user).read()
            pkg = pkg.split()
            pkg = pkg[2]
            print(pkg)
            os.system('pacman -U --noconfirm /home/%s/skypeforlinux-stable-bin/%s && rm -rf /home/%s/skypeforlinux-stable-bin' % (g.user, pkg, g.user))
    elif g.CA == 'skypeR':
        if g.distro == 'Ubuntu':
            os.system('apt purge skypeforlinux -y && apt autoremove -y')
        elif g.distro == 'Arch':
            os.system('pacman -Runs --noconfirm skypeforlinux-stable-bin')
    elif g.CA == 'screenfetch':
        if g.distro == 'Ubuntu':
            os.system('apt install screenfetch -y')
        elif g.distro == 'Arch':
            os.system('pacman -Sq --noconfirm screenfetch')
    elif g.CA == 'screenfetchR':
        if g.distro == 'Ubuntu':
            os.system('apt purge screenfetch -y && apt autoremove -y')
        elif g.distro == 'Arch':
            os.system('pacman -Runs --noconfirm screenfetch')
    elif g.CA == '0ad':
        if g.distro == 'Ubuntu':
            os.system('add-apt-repository -y ppa:wfg/0ad && apt update && apt install 0ad -y')
        elif g.distro == 'Arch':
            os.system('pacman -Sq --noconfirm 0ad')
    elif g.CA == '0adR':
        if g.distro == 'Ubuntu':
            os.system('apt purge 0ad -y && apt autoremove -y')
        elif g.distro == 'Arch':
            os.system('pacman -Runs --noconfirm 0ad')
    elif g.CA == 'powertop':
        if g.distro == 'Ubuntu':
            os.system('apt install powertop -y')
        elif g.distro == 'Arch':
            os.system('pacman -Sq --noconfirm powertop')
        dial = wx.MessageDialog(None, 'Would you like to configure powertop now??', 'Attention', wx.YES_NO | wx.YES_DEFAULT | wx.ICON_QUESTION | wx.STAY_ON_TOP)
        result = dial.ShowModal()
        if result == wx.ID_YES:
            wx.MessageBox('Configuring powertop. This will take a while... Do not let your PC to go to sleep!' , 'Attention', wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)
            os.system('powertop -c')
            os.system('powertop --auto-tune')
        else:
            print("No pressed")
    elif g.CA == 'powertopR':
        if g.distro == 'Ubuntu':
            os.system('apt purge powertop -y && apt autoremove -y')
        elif g.distro == 'Arch':
            os.system('pacman -Runs --noconfirm powertop')
    elif g.CA == 'steam':
        if g.distro == 'Ubuntu':
            os.system('apt install steam* -y')
        elif g.distro == 'Arch':
            os.system('pacman -Sq --noconfirm steam steam-native-runtime')
    elif g.CA == 'steamR':
        if g.distro == 'Ubuntu':
            os.system('apt purge steam* -y && apt autoremove -y')
        elif g.distro == 'Arch':
            os.system('pacman -Runs --noconfirm steam steam-native-runtime')
    elif g.CA == 'aptORaur':
        if g.distro == 'Ubuntu':
            os.system('add-apt-repository -y ppa:apt-fast/stable && apt update && echo debconf apt-fast/maxdownloads string 16 | debconf-set-selections && echo debconf apt-fast/dlflag boolean true | debconf-set-selections && echo debconf apt-fast/aptmanager string apt | debconf-set-selections && apt install apt-fast -y')
        elif g.distro == 'Arch':
            with open("logname.sh") as f:
                lines = f.readlines()
            lines[4] = 'runuser -l $persist -c "echo $USER && cd && git clone https://aur.archlinux.org/pakku.git && cd pakku && makepkg -rc"'
            with open("logname.sh", "w") as f:
                f.writelines(lines)
            os.system('./logname.sh')
            pkg = os.popen('ls /home/%s/pakku/' % g.user).read()
            pkg = pkg.split()
            pkg = pkg[1]
            print(pkg)
            os.system('pacman -U --noconfirm /home/%s/pakku/%s && rm -rf /home/%s/pakku' % (g.user, pkg, g.user))
            os.system('pakku -S --noconfirm pamac-classic pamac-aur pamac-tray-appindicator')
    elif g.CA == 'aptORaurR':
        if g.distro == 'Ubuntu':
            os.system('apt purge apt-fast -y && apt autoremove -y')
        elif g.distro == 'Arch':
            os.system('pacman -Runs --noconfirm pakku pamac-classic pamac-aur pamac-tray-appindicator')
    else:
        print('Error 3')

class OtherFrame(wx.Frame):
    
    def __init__(self, title, parent=None):
        wx.Frame.__init__(self, parent=parent, title=title, size=(g.sx, g.sy))
        self.Centre()
        self.SetPosition((g.x,g.y))
        self.InitUI()
        self.Show()
    
        self.Bind(wx.EVT_MOVE, self.OnMove)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        
    def InitUI(self):
    
        if g.newtitle == 'App Spotlight (root)':
            
            if os.geteuid() != 0:
            
                dial = wx.MessageDialog(None, 'You need to rerun the application as root. Restart now?', 'Prompt', wx.YES_NO | wx.YES_DEFAULT | wx.ICON_QUESTION | wx.STAY_ON_TOP)
                result = dial.ShowModal()
                if result == wx.ID_YES:
                    self.Destroy()
                    os.system('./bashLayer.sh')
                else:
                    print("No pressed")
                    g.sx, g.sy = self.GetSize()
                    f1 = Frame(None, title='HSuite '+str(g.version))
                    f1.Show()
                    self.Destroy()
            with open("commonBash.sh") as f:
                lines = f.readlines()
            lines[1] = "distro=%s\n" % g.distro
            with open("commonBash.sh", "w") as f:
                f.writelines(lines)
            if g.doIt:
                os.system('rm -rf /etc/pacman.conf && cp pacman.conf /etc/ && pacman -Sy')
                os.system('touch /etc/hsuite.conf')
            g.stat = 'show'
            gs = wx.GridSizer(5, 4, 3, 3)
            opera = wx.Button(self,label = 'Opera Browser')
            snapd = wx.Button(self,label = 'Snap support')
            loffice = wx.Button(self,label = 'Libreoffice')
            wine = wx.Button(self,label = 'Wine')
            etcher = wx.Button(self,label = 'Etcher')
            steam = wx.Button(self,label = 'Steam')
            vbox = wx.Button(self,label = 'Virtualbox')
            gparted = wx.Button(self,label = 'GParted')
            audac = wx.Button(self,label = 'Audacity')
            dejadup = wx.Button(self,label = 'Déja Dup')
            touchges = wx.Button(self,label = 'Touchpad gestures')
            skype = wx.Button(self,label = 'Skype')
            sfetch = wx.Button(self,label = 'Screenfetch')
            timsift = wx.Button(self,label = 'Timeshift')
            aptORaur = wx.Button(self,label = g.distroSpec)
            woffice = wx.Button(self,label = 'WPS Office')
            woe = wx.Button(self,label = 'Woe USB')
            ad = wx.Button(self,label = '0 A.D.')
            powtop = wx.Button(self,label = 'Powertop')
            update = wx.Button(self,label = 'Check for system Updates')

            gs.Add(opera,2,wx.EXPAND)
            gs.Add(snapd,1,wx.EXPAND)
            gs.Add(loffice,3,wx.EXPAND)
            gs.Add(woffice,4,wx.EXPAND)
            gs.Add(wine,8,wx.EXPAND)
            gs.Add(etcher,9,wx.EXPAND)
            gs.Add(woe,10,wx.EXPAND)
            gs.Add(vbox,11,wx.EXPAND)
            gs.Add(gparted,12,wx.EXPAND)
            gs.Add(audac,17,wx.EXPAND)
            gs.Add(dejadup,18,wx.EXPAND)
            gs.Add(timsift,19,wx.EXPAND)
            gs.Add(touchges,20,wx.EXPAND)
            gs.Add(skype,21,wx.EXPAND)
            gs.Add(sfetch,23,wx.EXPAND)
            gs.Add(aptORaur,24,wx.EXPAND)
            gs.Add(steam,25,wx.EXPAND)
            gs.Add(ad,26,wx.EXPAND)
            gs.Add(powtop,27,wx.EXPAND)
            gs.Add(update,28,wx.EXPAND)

            opera.Bind(wx.EVT_BUTTON, self.OnPreOpera)
            snapd.Bind(wx.EVT_BUTTON, self.OnSnapd)
            loffice.Bind(wx.EVT_BUTTON, self.OnLoffice)
            woffice.Bind(wx.EVT_BUTTON, self.OnWoffice)
            wine.Bind(wx.EVT_BUTTON, self.OnWine)
            etcher.Bind(wx.EVT_BUTTON, self.OnEtcher)
            woe.Bind(wx.EVT_BUTTON, self.OnWoe)
            vbox.Bind(wx.EVT_BUTTON, self.OnVbox)
            gparted.Bind(wx.EVT_BUTTON, self.OnGparted)
            audac.Bind(wx.EVT_BUTTON, self.OnAudac)
            dejadup.Bind(wx.EVT_BUTTON, self.OnDeja)
            timsift.Bind(wx.EVT_BUTTON, self.OnTimi)
            touchges.Bind(wx.EVT_BUTTON, self.OnTocsG)
            skype.Bind(wx.EVT_BUTTON, self.OnSkype)
            sfetch.Bind(wx.EVT_BUTTON, self.OnSfetch)
            aptORaur.Bind(wx.EVT_BUTTON, self.OnAptORaur)
            steam.Bind(wx.EVT_BUTTON, self.OnSteam)
            ad.Bind(wx.EVT_BUTTON, self.OnAd)
            powtop.Bind(wx.EVT_BUTTON, self.OnPow)
            update.Bind(wx.EVT_BUTTON, self.OnUpdate)

            self.SetSizer(gs)
        
        elif g.newtitle == 'Gallery (root)':
            g.stat = 'show'
            bitmap = wx.Bitmap(g.img)
            g.sx, g.sy = self.GetSize()
            g.sy = g.sy-35
            bitmap = self.scale_bitmap(bitmap, g.sx, g.sy)
            image = wx.StaticBitmap(self, wx.ID_ANY, bitmap)
        
        else: #g.newtitle == 'Opera Browser (root)':
            g.stat = 'show'
            if 'Touchpad' in g.newtitle:
                vane = os.path.exists("/usr/share/applications/org.cunidev.gestures.desktop")
                print(vane)
                if vane:
                    g.status = 'Remove'
                else:
                    g.status = 'Install'
            else:
                dat = os.popen('bash commonBash.sh').read()
                print(dat)
                if "No" in str(dat):
                    print('Not found')
                    g.status = 'Install'
                else:
                    print('Found')
                    g.status = 'Remove'
            gs = wx.GridSizer(1, 2, 5, 5)
            gsImage = wx.GridSizer(3, 1, 4, 4)
            gsText = wx.GridSizer(2, 1, 1, 1)
            gsButton = wx.GridSizer(5, 4, 5, 5)
            gsDesc = wx.GridSizer(1, 1, 0, 0) 
            ins = wx.Button(self,label = g.status)
            desc = wx.TextCtrl(self, -1, g.label, style = wx.TE_LEFT | wx.TE_READONLY | wx.TE_MULTILINE)
            pic1 = wx.Button(self,label = 'View Image 1')
            pic2 = wx.Button(self,label = 'View Image 2')
            pic3 = wx.Button(self,label = 'View Image 3')
            
            gs.Add(gsDesc,1,wx.EXPAND)
            gs.Add(gsText,2,wx.EXPAND)
            gsText.Add(gsImage,3,wx.EXPAND)
            gsText.Add(gsButton,4,wx.EXPAND)
            gsImage.Add(pic1,7,wx.EXPAND)
            gsImage.Add(pic2,7,wx.EXPAND)
            gsImage.Add(pic3,7,wx.EXPAND)
            i = 0
            while i < 19:
                gsButton.Add(wx.StaticText(self),wx.EXPAND)
                i+=1
            gsButton.Add(ins,5,wx.EXPAND)
            gsDesc.Add(desc,6,wx.EXPAND)
            
            pic1.Bind(wx.EVT_BUTTON, self.OnPic1)
            pic2.Bind(wx.EVT_BUTTON, self.OnPic2)
            pic3.Bind(wx.EVT_BUTTON, self.OnPic3)
            
            if g.status == 'Install':
                g.stat = 'install'
            elif g.status == 'Remove':
                g.stat = 'remove'
###################################################################################################################################################################################################
            if g.newtitle == 'Opera Browser (root)':
                ins.Bind(wx.EVT_BUTTON, self.OnPreOpera)
            elif g.newtitle == 'Snap support (root)':
                ins.Bind(wx.EVT_BUTTON, self.OnSnapd)
            elif g.newtitle == 'Libreoffice (root)':
                ins.Bind(wx.EVT_BUTTON, self.OnLoffice)
            elif g.newtitle == 'WPS Office (root)':
                ins.Bind(wx.EVT_BUTTON, self.OnWoffice)
            elif g.newtitle == 'Etcher (root)':
                ins.Bind(wx.EVT_BUTTON, self.OnEtcher)
            elif g.newtitle == 'Wine (root)':
                ins.Bind(wx.EVT_BUTTON, self.OnWine)
            elif g.newtitle == 'WoeUSB (root)':
                ins.Bind(wx.EVT_BUTTON, self.OnWoe)
            elif g.newtitle == 'Virtualbox (root)':
                ins.Bind(wx.EVT_BUTTON, self.OnVbox)
            elif g.newtitle == 'GParted (root)':
                ins.Bind(wx.EVT_BUTTON, self.OnGparted)
            elif g.newtitle == 'Audacity (root)':
                ins.Bind(wx.EVT_BUTTON, self.OnAudac)
            elif g.newtitle == 'Déjadup (root)':
                ins.Bind(wx.EVT_BUTTON, self.OnDeja)
            elif g.newtitle == 'Timeshift (root)':
                ins.Bind(wx.EVT_BUTTON, self.OnTimi)
            elif g.newtitle == 'Touchpad Gestures (root)':
                ins.Bind(wx.EVT_BUTTON, self.OnTocsG)
            elif g.newtitle == 'Skype (root)':
                ins.Bind(wx.EVT_BUTTON, self.OnSkype)
            elif g.newtitle == 'Screenfetch (root)':
                ins.Bind(wx.EVT_BUTTON, self.OnSfetch)
            elif g.newtitle == '0 A.D. (root)':
                ins.Bind(wx.EVT_BUTTON, self.OnAd)
            elif g.newtitle == 'Powertop (root)':
                ins.Bind(wx.EVT_BUTTON, self.OnPow)
            elif g.newtitle == 'Steam (root)':
                ins.Bind(wx.EVT_BUTTON, self.OnPow)
            elif 'Apt' or 'AUR' in g.newtitle:
                ins.Bind(wx.EVT_BUTTON, self.OnAptORaur)
                
####################################################################################################################################################################################################
            self.SetSizer(gs)
            print('READY')
    
    def scale_bitmap(self, bitmap, width, height):
        image = wx.ImageFromBitmap(bitmap)
        image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
        result = wx.BitmapFromImage(image)
        return result
    
    def OnPic1(self, e):
        g.newtitle = 'Gallery (root)'
        g.img = g.num1
        title = g.newtitle
        g.sx, g.sy = self.GetSize()
        frame = OtherFrame(title=title)
        self.Destroy()
            
    def OnPic2(self, e):
        g.newtitle = 'Gallery (root)'
        g.img = g.num2
        title = g.newtitle
        g.sx, g.sy = self.GetSize()
        frame = OtherFrame(title=title)
        self.Destroy()
        
    def OnPic3(self, e):
        g.newtitle = 'Gallery (root)'
        g.img = g.num3
        title = g.newtitle
        g.sx, g.sy = self.GetSize()
        frame = OtherFrame(title=title)
        self.Destroy()            
            
    def OnRe(self, e):
        g.status = 'show'
        title = g.newtitle
        g.sx, g.sy = self.GetSize()
        frame = OtherFrame(title=title)
        self.Destroy()
            
    def OnNeed(self, e):
        
        if g.stat == 'show':
            title = g.newtitle
            g.sx, g.sy = self.GetSize()
            frame = OtherFrame(title=title)
            self.Destroy()
        elif g.stat == 'install':
            t1 = myThread(1, "Thread-1")
            t1.start()
            counter = 0
            dlg = wx.ProgressDialog(g.inMsg, 'Please wait...     It will take around %d minutes.' % g.kbTime, style=wx.PD_APP_MODAL | wx.PD_ELAPSED_TIME | wx.STAY_ON_TOP)
            while t1.isAlive():
                wx.MilliSleep(50)
                dlg.Pulse()
                wx.GetApp().Yield()
                counter += 1
            del dlg
            t1.join()
            wx.MessageBox(g.indMsg , 'Done', wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)
            self.OnRe(e)
            self.Destroy()
        elif g.stat == 'remove':
            t1 = myThread(1, "Thread-1")
            t1.start()
            counter = 0
            dlg = wx.ProgressDialog(g.rmMsg, 'Please wait...', style=wx.PD_APP_MODAL | wx.PD_ELAPSED_TIME | wx.STAY_ON_TOP)
            while t1.isAlive():
                wx.MilliSleep(50)
                dlg.Pulse()
                wx.GetApp().Yield()
                counter += 1
            del dlg
            t1.join()
            wx.MessageBox(g.rmdMsg , 'Done', wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)
            self.OnRe(e)
            self.Destroy()
            
    def OnUpdate(self, e):

#        if distro == 'Ubuntu':
#            
#        elif distro == 'Arch':
#            print('Arch')
#        else:
#            print('Error 1')
        g.CA = 'update'
        t1 = myThread(1, "Thread-1")
        t1.start()
        counter = 0
        dlg = wx.ProgressDialog('Checking for updates...', 'Please wait...', style=wx.PD_APP_MODAL | wx.PD_ELAPSED_TIME | wx.STAY_ON_TOP)
        while t1.isAlive():
            wx.MilliSleep(50)
            dlg.Pulse()
            wx.GetApp().Yield()
            counter += 1
        del dlg
        t1.join()
        if g.p != 0:
            dial = wx.MessageDialog(None, 'Would you like to install '+str(g.p)+' updates?', 'Question', wx.YES_NO | wx.YES_DEFAULT | wx.ICON_QUESTION | wx.STAY_ON_TOP)
            result = dial.ShowModal()
            if result == wx.ID_YES:
                g.CA = 'upgrade'
                t1 = myThread(1, "Thread-1")
                t1.start()
                counter = 0
                dlg = wx.ProgressDialog('Installing updates...', 'Please wait...', style=wx.PD_APP_MODAL | wx.PD_ELAPSED_TIME | wx.STAY_ON_TOP)
                while t1.isAlive():
                    wx.MilliSleep(50)
                    dlg.Pulse()
                    wx.GetApp().Yield()
                    counter += 1
                del dlg
                t1.join()
            else:
                print("No pressed")
            wx.MessageBox('Operation sucsesfully completed!' , 'Done', wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)
        else:
            wx.MessageBox('Your system is up to date!' , 'Done', wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)

    def OnPreOpera(self, e):
        
        if g.distro == 'Ubuntu':
            name = 'opera-stable'
        elif g.distro == 'Arch':
            name = 'opera'
        if g.stat == 'show':
            with open("commonBash.sh") as f:
                lines = f.readlines()
            lines[0] = "name=%s\n" % name
            with open("commonBash.sh", "w") as f:
                f.writelines(lines)
            g.newtitle = 'Opera Browser (root)'
            g.label = """Fast, secure, easy-to-use browser
Try the Opera browser - now with a built-in ad blocker, battery saver and free VPN.

Opera is one of the most underrated browsers out yet. However, it's one of the bests, if not the best. 
It's based on Chromium, so it's basicly Chrome on steroids. It's faster, lighter, more secure and more productive.
The Opera Sync is the best on the market, and the sidebar with integrated messengers is really productive. 

Give the web browser of the future a try!"""
            name = 'opera-stable'
            g.num1 = 'images/'+name+'1.png'
            g.num2 = 'images/'+name+'2.jpeg'
            g.num3 = 'images/'+name+'3.png'
        elif g.stat == 'install':
            name = 'opera-stable'
            g.kbTime = 0
            g.CA = name
            g.inMsg = 'Installing '+name+'...'
            g.indMsg = name+' installed sucsesfully!'
        elif g.stat == 'remove':
            name = 'opera-stable'
            g.CA = name+'R'
            g.rmMsg = 'Removing '+name+'...'
            g.rmdMsg = name+' removed sucsesfully.'
        self.OnNeed(e)
            
    def OnSnapd(self, e):
    
        name = 'snapd'
        if g.stat == 'show':
            with open("commonBash.sh") as f:
                lines = f.readlines()
            lines[0] = "name=%s\n" % name
            with open("commonBash.sh", "w") as f:
                f.writelines(lines)
            g.newtitle = 'Snap support (root)'
            g.label = """Snap is a new package manager for Linux, an alternative to Apt, rpm, yum, etc. I specifically use the word Linux as opposed to any one distro because they are designed to run on many, many distributions. You can install Snap packages on Ubuntu, various Ubuntu flavors, Debian, elementary OS, Fedora, Linux Mint, and more.

Inspired by how applications are installed on mobile operating systems such as Android and iOS, snaps are installable apps, CLIs, GUIs, etc that are installed from the Snap Store in a managed and secure fashion. 

Visit Snap Store at https://snapcraft.io/store

Features:
    - Auto-updating
    - Secure
    - Packaging is easy for developers
    - Chanels (developer, stable, etc)
            """
            g.num1 = 'images/'+name+'1.jpg'
            g.num2 = 'images/'+name+'2.jpg'
            g.num3 = 'images/'+name+'3.jpg'
        elif g.stat == 'install':
            g.kbTime = 0
            g.CA = name
            g.inMsg = 'Installing '+name+'...'
            g.indMsg = name+' installed sucsesfully!'
        elif g.stat == 'remove':
            g.CA = name+'R'
            g.rmMsg = 'Removing '+name+'...'
            g.rmdMsg = name+' removed sucsesfully.'
        self.OnNeed(e)
        
    def OnLoffice(self, e):
    
        name = 'libreoffice'
        if g.stat == 'show':
            with open("commonBash.sh") as f:
                lines = f.readlines()
            lines[0] = "name=%s\n" % name
            with open("commonBash.sh", "w") as f:
                f.writelines(lines)
            g.newtitle = 'Libreoffice (root)'
            g.label = """LibreOffice is community-driven and developed MS Office alternative software, and is a project of the not-for-profit organization, The Document Foundation. LibreOffice is free and open source software, originally based on OpenOffice.org (commonly known as OpenOffice), and is the most actively developed OpenOffice.org successor project.

LibreOffice is developed by users who, just like you, believe in the principles of Free Software and in sharing their work with the world in non-restrictive ways. At the core of these principles are the four essential freedoms and the tenets of The Document Foundation's Next Decade Manifesto.

We believe that users should have the freedom to run, copy, distribute, study, change and improve the software that we distribute. While we do offer no-cost downloads of the LibreOffice suite of programs, Free Software is first and foremost a matter of liberty, not price. We campaign for these freedoms because we believe that everyone deserves them.
            """
            g.num1 = 'images/'+name+'1.jpeg'
            g.num2 = 'images/'+name+'2.png'
            g.num3 = 'images/'+name+'3.png'
        elif g.stat == 'install':
            g.kbTime = 0
            g.CA = name
            g.inMsg = 'Installing '+name+'...'
            g.indMsg = name+' installed sucsesfully!'
        elif g.stat == 'remove':
            g.CA = name+'R'
            g.rmMsg = 'Removing '+name+'...'
            g.rmdMsg = name+' removed sucsesfully.'
        self.OnNeed(e)

    def OnWoffice(self, e):
        name = 'wps-office'
        if g.stat == 'show':
            with open("commonBash.sh") as f:
                lines = f.readlines()
            lines[0] = "name=%s\n" % name
            with open("commonBash.sh", "w") as f:
                f.writelines(lines)
            g.newtitle = 'WPS Office (root)'
            g.label = """WPS Office is the complete free office suite, integrates all office word processor functions: Word, Presentation, Spreadsheet, PDF, and fully compatible with Microsoft Word, Excel, PowerPoint, Google Doc and Adobe PDF format. If you need to use advanced features(e.g.: PDF2WORD, more cloud storage space), you can subscribe Preminum.

The aim of WPS Office is to provide you one-stop working solution since 1989. Various of office tools and unique and intuitive UI design ensures you enjoy the best office experience. You could easy to do all office documents processing on-the-go on Windows PC. WPS Office suite allows you can create, view, edit and share office documents.

It's the best free MS Office alternative for Linux in my opinion.
            """
            g.num1 = 'images/'+name+'1.jpg'
            g.num2 = 'images/'+name+'2.png'
            g.num3 = 'images/'+name+'3.png'
        elif g.stat == 'install':
            g.kbTime = 0
            g.CA = name
            g.inMsg = 'Installing '+name+'...'
            g.indMsg = name+' installed sucsesfully!'
        elif g.stat == 'remove':
            g.CA = name+'R'
            g.rmMsg = 'Removing '+name+'...'
            g.rmdMsg = name+' removed sucsesfully.'
        self.OnNeed(e)
            
    def OnEtcher(self, e):
        if g.distro == 'Ubuntu':
            name = 'etcher-electron'
        elif g.distro == 'Arch':
            name = 'balena-etcher'
        else:
            print('Error 4')
        if g.stat == 'show':
            with open("commonBash.sh") as f:
                lines = f.readlines()
            lines[0] = "name=%s\n" % name
            with open("commonBash.sh", "w") as f:
                f.writelines(lines)
            g.newtitle = 'Etcher (root)'
            g.label = """Write Disc image to removable storage.
            
Etcher is a free and open-source utility used for burning image files such as .iso and .img files, as well as zipped folders to create live SD cards and USB flash drives. It is developed by balena, and licensed under Apache License 2.0.

Etcher was developed using the Electron framework and supports Windows, macOS and Linux.

Etcher is primarily used through a graphical user interface, however there is also a command line interface though it's still in development.

Future planned features include support for persistent storage allowing the live SD card or USB flash drive to be used as a hard drive, as well as support for flashing multiple boot partitions to a single SD card or USB flash drive.
            """
            name = 'etcher-electron'
            g.num1 = 'images/'+name+'1.jpg'
            g.num2 = 'images/'+name+'2.jpg'
            g.num3 = 'images/'+name+'3.png'
        elif g.stat == 'install':
            name = 'etcher-electron'
            g.kbTime = 0
            g.CA = name
            g.inMsg = 'Installing '+name+'...'
            g.indMsg = name+' installed sucsesfully!'
        elif g.stat == 'remove':
            name = 'etcher-electron'
            g.CA = name+'R'
            g.rmMsg = 'Removing '+name+'...'
            g.rmdMsg = name+' removed sucsesfully.'
        self.OnNeed(e)
            
    def OnWine(self, e):
        name = 'wine'
        if g.stat == 'show':
            with open("commonBash.sh") as f:
                lines = f.readlines()
            lines[0] = "name=%s\n" % name
            with open("commonBash.sh", "w") as f:
                f.writelines(lines)
            g.newtitle = 'Wine (root)'
            g.label = """Run Windows programs on Linux
            
Wine (originally an acronym for "Wine Is Not an Emulator") is a compatibility layer capable of running Windows applications on several POSIX-compliant operating systems, such as Linux, macOS, & BSD. Instead of simulating internal Windows logic like a virtual machine or emulator, Wine translates Windows API calls into POSIX calls on-the-fly, eliminating the performance and memory penalties of other methods and allowing you to cleanly integrate Windows applications into your desktop.
            """
            g.num1 = 'images/'+name+'1.jpg'
            g.num2 = 'images/'+name+'2.png'
            g.num3 = 'images/'+name+'3.jpg'
        elif g.stat == 'install':
            g.kbTime = 0
            g.CA = name
            g.inMsg = 'Installing '+name+'...'
            g.indMsg = name+' installed sucsesfully!'
        elif g.stat == 'remove':
            g.CA = name+'R'
            g.rmMsg = 'Removing '+name+'...'
            g.rmdMsg = name+' removed sucsesfully.'
        self.OnNeed(e)
        
    def OnWoe(self, e):
        name = 'woeusb'
        if g.stat == 'show':
            with open("commonBash.sh") as f:
                lines = f.readlines()
            lines[0] = "name=%s\n" % name
            with open("commonBash.sh", "w") as f:
                f.writelines(lines)
            g.newtitle = 'WoeUSB (root)'
            g.label = """Write Windows ISO to removable storage.
            
WoeUSB is Linux tool for creating Windows USB stick installer from a real Windows DVD or an image. It contains two programs, woeusb and woeusbgui. It’s a fork of Congelli501’s WinUSB software which received its last update in 2012.

woeusb is a CLI utility that does the actual creation of a bootable Windows installation USB storage device from either an existing Windows installation or a disk image. woeusbgui (as the name suggests,) is a woeusb GUI wrapper based on WxWidgets.
            """
            g.num1 = 'images/'+name+'1.jpg'
            g.num2 = 'images/'+name+'2.png'
            g.num3 = 'images/'+name+'3.png'
        elif g.stat == 'install':
            g.kbTime = 0
            g.CA = name
            g.inMsg = 'Installing '+name+'...'
            g.indMsg = name+' installed sucsesfully!'
        elif g.stat == 'remove':
            g.CA = name+'R'
            g.rmMsg = 'Removing '+name+'...'
            g.rmdMsg = name+' removed sucsesfully.'
        self.OnNeed(e)
     
    def OnVbox(self, e):
        name = 'virtualbox'
        if g.stat == 'show':
            with open("commonBash.sh") as f:
                lines = f.readlines()
            lines[0] = "name=%s\n" % name
            with open("commonBash.sh", "w") as f:
                f.writelines(lines)
            g.newtitle = 'Virtualbox (root)'
            g.label = """Run virtual machines on your PC
            
A VirtualBox or VB is a software virtualization package that installs on an operating system as an application. VirtualBox allows additional operating systems to be installed on it, as a Guest OS, and run in a virtual environment. In 2010, VirtualBox was the most popular virtualization software application. Supported operating systems include Windows XP, Windows Vista, Windows 7, macOS X, Linux, Solaris, and OpenSolaris.

VirtualBox was originally developed by Innotek GmbH and released in 2007 as an open-source software package. The company was later purchased by Sun Microsystems. Oracle Corporation now develops the software package and titles it Oracle VM VirtualBox.
            """
            g.num1 = 'images/'+name+'1.jpg'
            g.num2 = 'images/'+name+'2.png'
            g.num3 = 'images/'+name+'3.png'
        elif g.stat == 'install':
            g.kbTime = 0
            g.CA = name
            g.inMsg = 'Installing '+name+'...'
            g.indMsg = name+' installed sucsesfully!'
        elif g.stat == 'remove':
            g.CA = name+'R'
            g.rmMsg = 'Removing '+name+'...'
            g.rmdMsg = name+' removed sucsesfully.'
        self.OnNeed(e)
        
    def OnGparted(self, e):
        name = 'gparted'
        if g.stat == 'show':
            with open("commonBash.sh") as f:
                lines = f.readlines()
                lines[0] = "name=%s\n" % name
            with open("commonBash.sh", "w") as f:
                f.writelines(lines)
            g.newtitle = 'GParted (root)'
            g.label = """The ultimate partition manager for Linux
            
The gparted application is the GNOME partition editor for creating, reorganizing, and deleting disk partitions.
A disk device can be subdivided into one or more partitions. The gparted application enables you to change the partition organization on a disk device while preserving the contents of the partition.

With gparted you can accomplish the following tasks: 
- Create a partition table on a disk device. 
- Enable and disable partition flags such as boot and hidden. 
- Perform actions with partitions such as create, delete, resize, move, check, label, copy, and paste.

More documentation can be found in the application help manual, and online at: 
http://gparted.org
            """
            g.num1 = 'images/'+name+'1.png'
            g.num2 = 'images/'+name+'2.png'
            g.num3 = 'images/'+name+'3.png'
        elif g.stat == 'install':
            g.kbTime = 0
            g.CA = name
            g.inMsg = 'Installing '+name+'...'
            g.indMsg = name+' installed sucsesfully!'
        elif g.stat == 'remove':
            g.CA = name+'R'
            g.rmMsg = 'Removing '+name+'...'
            g.rmdMsg = name+' removed sucsesfully.'
        self.OnNeed(e)
        
    def OnAudac(self, e):
        name = 'audacity'
        if g.stat == 'show':
            with open("commonBash.sh") as f:
                lines = f.readlines()
                lines[0] = "name=%s\n" % name
            with open("commonBash.sh", "w") as f:
                f.writelines(lines)
            g.newtitle = 'Audacity (root)'
            g.label = """The free and open-source audio tool
            
Audacity is the name of a popular open source multilingual audio editor and recorder software that is used to record and edit sounds. It is free and works on Windows, Mac OS X, GNU/Linux and other operating systems.

Audacity can be used to perform a number of audio editing and recording tasks such as making ringtones, mixing stero tracks, transferring tapes and records to computer or CD, splitting recordings into separate tracks and more. The Audacity Wiki provides indepth tutorials on how to do these types of tasks in Audacity. Vendors can also freely bundle Audacity with their products or sell or distribute copies of Audacity under the GNU General Public License (GPL). 
            """
            g.num1 = 'images/'+name+'1.png'
            g.num2 = 'images/'+name+'2.png'
            g.num3 = 'images/'+name+'3.jpg'
        elif g.stat == 'install':
            g.kbTime = 0
            g.CA = name
            g.inMsg = 'Installing '+name+'...'
            g.indMsg = name+' installed sucsesfully!'
        elif g.stat == 'remove':
            g.CA = name+'R'
            g.rmMsg = 'Removing '+name+'...'
            g.rmdMsg = name+' removed sucsesfully.'
        self.OnNeed(e) 
        
    def OnDeja(self, e):
        name = 'deja-dup'
        if g.stat == 'show':
            with open("commonBash.sh") as f:
                lines = f.readlines()
                lines[0] = "name=%s\n" % name
            with open("commonBash.sh", "w") as f:
                f.writelines(lines)
            g.newtitle = 'Déjadup (root)'
            g.label = """One of the most powerful backup solutions for Linux
            
Deja-dup: is a simple yet powerful backup tool included with Ubuntu. It offers the power of resync with incremental backups, encryption, scheduling, and support for remote services. With Deja-dup, you can quickly revert files to previous versions or restore missing files from a file manager window. 

You can do full system backups, Home folder backup or even settings backup in Ubuntu. You can backup to your GDrive storage also.
            """
            g.num1 = 'images/'+name+'1.png'
            g.num2 = 'images/'+name+'2.png'
            g.num3 = 'images/'+name+'3.png'
        elif g.stat == 'install':
            g.kbTime = 0
            g.CA = name
            g.inMsg = 'Installing '+name+'...'
            g.indMsg = name+' installed sucsesfully!'
        elif g.stat == 'remove':
            g.CA = name+'R'
            g.rmMsg = 'Removing '+name+'...'
            g.rmdMsg = name+' removed sucsesfully.'
        self.OnNeed(e)
        
    def OnTimi(self, e):
        name = 'timeshift'
        if g.stat == 'show':
            with open("commonBash.sh") as f:
                lines = f.readlines()
                lines[0] = "name=%s\n" % name
            with open("commonBash.sh", "w") as f:
                f.writelines(lines)
            g.newtitle = 'Timeshift (root)'
            g.label = """The best backup solution (in my opinion) for Linux
            
Timeshift for Linux is an application that provides functionality similar to the System Restore feature in Windows and the Time Machine tool in Mac OS. Timeshift protects your system by taking incremental snapshots of the file system at regular intervals. These snapshots can be restored at a later date to undo all changes to the system.

In RSYNC mode, snapshots are taken using rsync and hard-links. Common files are shared between snapshots which saves disk space. Each snapshot is a full system backup that can be browsed with a file manager.

In BTRFS mode, snapshots are taken using the in-built features of the BTRFS filesystem. BTRFS snapshots are supported only on BTRFS systems having an Ubuntu-type subvolume layout (with @ and @home subvolumes).

Timeshift is similar to applications like rsnapshot, BackInTime and TimeVault but with different goals. It is designed to protect only system files and settings. User files such as documents, pictures and music are excluded. This ensures that your files remains unchanged when you restore your system to an earlier date.
            """
            g.num1 = 'images/'+name+'1.png'
            g.num2 = 'images/'+name+'2.png'
            g.num3 = 'images/'+name+'3.png'
        elif g.stat == 'install':
            g.kbTime = 0
            g.CA = name
            g.inMsg = 'Installing '+name+'...'
            g.indMsg = name+' installed sucsesfully!'
        elif g.stat == 'remove':
            g.CA = name+'R'
            g.rmMsg = 'Removing '+name+'...'
            g.rmdMsg = name+' removed sucsesfully.'
        self.OnNeed(e)
        
    def OnTocsG(self, e):
        name = 'gestures'
        if g.stat == 'show':
            g.newtitle = 'Touchpad Gestures (root)'
            g.label = """The app is called ‘Gestures’ and is described by its developer as being a “minimal Gtk+ GUI app for libinput-gestures”.

Windows and macOS both come with a variety of useful touchpad gestures pre-configured out of the box, and offer easy-to-access settings for adjusting or changing gesture behaviour to your liking.

Alas Ubuntu, like many Linux distributions, is a little lacking in this regard. Only a handful of basic gestures for scrolling and right-click available out of the box on Ubuntu 18.04 LTS, for instance.

But by using the “Gestures” app you can quickly effect a set of custom trackpad gestures that are on par with other operating systems, and in some cases, far more useful!
            """
            g.num1 = 'images/'+name+'1.jpg'
            g.num2 = 'images/'+name+'2.png'
            g.num3 = 'images/'+name+'3.png'
        elif g.stat == 'install':
            g.kbTime = 0
            g.CA = name
            g.inMsg = 'Installing '+name+'...'
            g.indMsg = name+' installed sucsesfully!'
        elif g.stat == 'remove':
            g.CA = name+'R'
            g.rmMsg = 'Removing '+name+'...'
            g.rmdMsg = name+' removed sucsesfully.'
        self.OnNeed(e)
          
    def OnSkype(self, e):
        if g.distro == 'Ubuntu':
            name = 'skypeforlinux'
        elif g.distro == 'Arch':
            name = 'skypeforlinux-stable-bin'
        else:
           print('Error 4')
        if g.stat == 'show':
            with open("commonBash.sh") as f:
                lines = f.readlines()
                lines[0] = "name=%s\n" % name
            with open("commonBash.sh", "w") as f:
                f.writelines(lines)
            g.newtitle = 'Skype (root)'
            g.label = """Skype is for connecting with the people that matter most in your life and work. It's built for both one-on-one and group conversations and works wherever you are – via mobile, PC, Xbox and Alexa. Skype messaging and HD voice and video calling will help you share experiences and get things done with others.

With Skype, you can have meetings and create great things with your workgroup, share a story or celebrate a birthday with friends and family, and learn a new skill or hobby with a teacher. It’s free to use Skype – to send messages and have audio and video calls with groups of up to 50 people!

If you pay a little, you can do more things, in more ways, with more people – like call phones or SMS messages. You can pay as you go or buy a subscription, whatever works for you.

Try Skype out today and start adding your friends, family and colleagues. They won’t be hard to find; hundreds of millions of people are already using Skype to do all sorts of things together.
            """
            g.num1 = 'images/'+name+'1.png'
            g.num2 = 'images/'+name+'2.png'
            g.num3 = 'images/'+name+'3.png'
        elif g.stat == 'install':
            name = 'skype'
            g.kbTime = 0
            g.CA = name
            g.inMsg = 'Installing '+name+'...'
            g.indMsg = name+' installed sucsesfully!'
        elif g.stat == 'remove':
            name = 'skype'
            g.CA = name+'R'
            g.rmMsg = 'Removing '+name+'...'
            g.rmdMsg = name+' removed sucsesfully.'
        self.OnNeed(e)
        
    def OnSfetch(self, e):
        name = 'screenfetch'
        if g.stat == 'show':
            with open("commonBash.sh") as f:
                lines = f.readlines()
                lines[0] = "name=%s\n" % name
            with open("commonBash.sh", "w") as f:
                f.writelines(lines)
            g.newtitle = 'Screenfetch (root)'
            g.label = """This small script shows some useful information about your computer when you type "screenfetch" into the terminal.
            """
            g.num1 = 'images/'+name+'1.png'
            g.num2 = 'images/'+name+'2.png'
            g.num3 = 'images/'+name+'3.png'
        elif g.stat == 'install':
            g.kbTime = 0
            g.CA = name
            g.inMsg = 'Installing '+name+'...'
            g.indMsg = name+' installed sucsesfully!'
        elif g.stat == 'remove':
            g.CA = name+'R'
            g.rmMsg = 'Removing '+name+'...'
            g.rmdMsg = name+' removed sucsesfully.'
        self.OnNeed(e)
        
    def OnAd(self, e):
        name = '0ad'
        if g.stat == 'show':
            with open("commonBash.sh") as f:
                lines = f.readlines()
                lines[0] = "name=%s\n" % name
            with open("commonBash.sh", "w") as f:
                f.writelines(lines)
            g.newtitle = '0 A.D. (root)'
            g.label = """The best strategic game for Linux (in my opinion)
            
0 A.D. (pronounced "zero ey-dee") is a free, open-source, cross-platform real-time strategy (RTS) game of ancient warfare. In short, it is a historically-based war/economy game that allows players to relive or rewrite the history of Western civilizations, focusing on the years between 500 B.C. and 500 A.D. The project is highly ambitious, involving state-of-the-art 3D graphics, detailed artwork, sound, and a flexible and powerful custom-built game engine.

It also supports online and LAN multiplayer, custom map creation, adding mods to the game and if you would like to take part in the development you can do that also.
            """
            g.num1 = 'images/'+name+'1.jpg'
            g.num2 = 'images/'+name+'2.jpg'
            g.num3 = 'images/'+name+'3.jpg'
        elif g.stat == 'install':
            g.kbTime = 0
            g.CA = name
            g.inMsg = 'Installing '+name+'...'
            g.indMsg = name+' installed sucsesfully!'
        elif g.stat == 'remove':
            g.CA = name+'R'
            g.rmMsg = 'Removing '+name+'...'
            g.rmdMsg = name+' removed sucsesfully.'
        self.OnNeed(e)
        
    def OnPow(self, e):
        name = 'powertop'
        if g.stat == 'show':
            with open("commonBash.sh") as f:
                lines = f.readlines()
                lines[0] = "name=%s\n" % name
            with open("commonBash.sh", "w") as f:
                f.writelines(lines)
            g.newtitle = 'Powertop (root)'
            g.label = """Powertop is a program that helps to diagnose various issues with power consumption and power management. It also has an interactive mode allowing one to experiment with various power management settings. When invoking powertop without arguments powertop starts in interactive mode.
            """
            g.num1 = 'images/'+name+'1.png'
            g.num2 = 'images/'+name+'2.png'
            g.num3 = 'images/'+name+'3.jpeg'
        elif g.stat == 'install':
            g.kbTime = 0
            g.CA = name
            g.inMsg = 'Installing '+name+'...'
            g.indMsg = name+' installed sucsesfully!'
        elif g.stat == 'remove':
            g.CA = name+'R'
            g.rmMsg = 'Removing '+name+'...'
            g.rmdMsg = name+' removed sucsesfully.'
        self.OnNeed(e)
            
    def OnSteam(self, e):
        name = 'steam'
        if g.stat == 'show':
            with open("commonBash.sh") as f:
                lines = f.readlines()
                lines[0] = "name=%s\n" % name
            with open("commonBash.sh", "w") as f:
                f.writelines(lines)
            g.newtitle = 'Steam (root)'
            g.label = """Steam is the ultimate game platform, also for Linux. It offers Steam Play feature. Steam Play allows you to purchase your games once and play anywhere. Whether you have purchased your Steam Play enabled game on a Mac or PC (both Windows and Linux), you will be able to play on the other platform free of charge. So a lots of Windows only games can be played on Linux without problems.
            """
            g.num1 = 'images/'+name+'1.jpg'
            g.num2 = 'images/'+name+'2.png'
            g.num3 = 'images/'+name+'3.jpg'
        elif g.stat == 'install':
            g.kbTime = 0
            g.CA = name
            g.inMsg = 'Installing '+name+'...'
            g.indMsg = name+' installed sucsesfully!'
        elif g.stat == 'remove':
            g.CA = name+'R'
            g.rmMsg = 'Removing '+name+'...'
            g.rmdMsg = name+' removed sucsesfully.'
        self.OnNeed(e)

            
    def OnAptORaur(self, e):
        if g.distro == 'Arch':
            name = 'pakku'
            g.label = """Pakku is another pacman wrapper which is still in its initial stage. However, just because its new doesn’t mean its lacking any of the features supported by other AUR helper. It does its job pretty nice and along with searching and installing applications from AUR, it removes dependencies after a build.

Features of pakku
    - Searching and installing packages from Arch User Repository.
    - Viewing files and changes between builds.
    - Building packages from official repositories and removing make dependencies after a build.
    - PKGBUILD retrieving and Pacman integration.
    - Pacman-like user interface and pacman options supports.
    - Pacman configuration supports and no PKGBUILD sourcing.
            """
            g.num1 = 'images/'+name+'1.png'
            g.num2 = 'images/'+name+'2.png'
            g.num3 = 'images/'+name+'3.png'
        elif g.distro == 'Ubuntu':
            name = 'apt-fast'
            g.label = """Apt-fast is a shell script wrapper for apt-get and aptitude that can drastically improve APT download times by downloading packages with multiple connections per package. Apt-Fast uses the Axel download accelerator in Ubuntu 12.04 or the aria2 download accelerator in Ubuntu 14.04 and beyond to download different pieces of a package simultaneously, lowering the total time it takes to download a package.
            """
            g.num1 = 'images/'+name+'1.png'
            g.num2 = 'images/'+name+'2.jpg'
            g.num3 = 'images/'+name+'3.png'
        if g.stat == 'show':
            with open("commonBash.sh") as f:
                lines = f.readlines()
                lines[0] = "name=%s\n" % name
            with open("commonBash.sh", "w") as f:
                f.writelines(lines)
            g.newtitle = g.distroSpec+' (root)'
        elif g.stat == 'install':
            name = 'aptORaur'
            g.kbTime = 0
            g.CA = name
            if g.distro == 'Arch':
                name = 'pakku'
            elif g.distro == 'Ubuntu':
                name = 'apt-fast'
            g.inMsg = 'Installing '+name+'...'
            g.indMsg = name+' installed sucsesfully!'
        elif g.stat == 'remove':
            name = 'aptORaur'
            g.CA = name+'R'
            if g.distro == 'Arch':
                name = 'pakku'
            elif g.distro == 'Ubuntu':
                name = 'apt-fast'
            g.rmMsg = 'Removing '+name+'...'
            g.rmdMsg = name+' removed sucsesfully.'
        self.OnNeed(e)
     
    def OnClose(self, e):
        if g.newtitle == 'App Spotlight (root)':
            g.sx, g.sy = self.GetSize()
            f1 = Frame(None, title='HSuite '+str(g.version)+' (root)')
            f1.Show()
            self.Destroy()
        elif g.newtitle == 'Gallery (root)':
            g.status = 'show'
            if 'opera' in g.img:
                self.OnPreOpera(e)
            elif 'snapd' in g.img:
                self.OnSnapd(e)
            elif 'libreoffice' in g.img:
                self.OnLoffice(e)
            elif 'wps-office' in g.img:
                self.OnWoffice(e)
            elif 'etcher' in g.img:
                self.OnEtcher(e)
            elif 'wine' in g.img:
                self.OnWine(e)
            elif 'woeusb' in g.img:
                self.OnWoe(e)
            elif 'virtualbox' in g.img:
                self.OnVbox(e)
            elif 'gparted' in g.img:
                self.OnGparted(e)
            elif 'audacity' in g.img:
                self.OnAudac(e)
            elif 'deja-dup' in g.img:
                self.OnDeja(e)
            elif 'timeshift' in g.img:
                self.OnTimi(e)
            elif 'gestures' in g.img:
                self.OnTocsG(e)
            elif 'skype' in g.img:
                self.OnSkype(e)
            elif 'screen' in g.img:
                self.OnSfetch(e)
            elif '0ad' in g.img:
                self.OnAd(e)
            elif 'power' in g.img:
                self.OnPow(e)
            elif 'steam' in g.img:
                self.OnSteam(e)
            elif 'apt-fast' or 'pakku' in g.img:
                self.OnAptORaur(e)
        else:
            g.newtitle = 'App Spotlight (root)'
            title = g.newtitle
            g.sx, g.sy = self.GetSize()
            frame = OtherFrame(title=title)
            self.Destroy()
        
    def OnMove(self, e):
        g.x, g.y = e.GetPosition()

class Frame(wx.Frame):

    def __init__(self, parent, title):
        super(Frame, self).__init__(parent, title=title, size=(g.sx, g.sy))
        self.Centre()
        self.SetPosition((g.x,g.y))
        self.InitUI()
        
    def InitUI(self):

        if g.distro == 'Error 4':
            wx.MessageBox('Currently only Arch & Debian/Ubuntu based distros are supported. Your distro is currently unsupported or there was an identication error. In this case visit https://github.com/swanux/hsuite/issues/new/choose' , 'Compatibility error', wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)
            self.Destroy()

        if updated:
            wx.MessageBox('HSuite is updated sucsesfully! You can view changes in the "About" section.', 'Info', wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)

        gs = wx.GridSizer(3, 2, 7, 7)
        fbak = wx.Button(self,label = 'Feedback')
        exit = wx.Button(self,label = 'About')
        tools = wx.Button(self,label = 'HTools')
        upd8 = wx.Button(self,label = 'Android Tools')
        apps = wx.Button(self,label = 'App Spotlight')
        dist = wx.Button(self,label = 'Distro Boutique')

        gs.Add(apps,2,wx.EXPAND)
        gs.Add(dist,1,wx.EXPAND)
        gs.Add(tools,3,wx.EXPAND)
        gs.Add(upd8,4,wx.EXPAND)
        gs.Add(fbak,5,wx.EXPAND)
        gs.Add(exit,0,wx.EXPAND)

        exit.Bind(wx.EVT_BUTTON, self.OnAbout)
        apps.Bind(wx.EVT_BUTTON, self.OnApp)
        upd8.Bind(wx.EVT_BUTTON, self.OnPrompt)
        fbak.Bind(wx.EVT_BUTTON, self.OnRun)
        tools.Bind(wx.EVT_BUTTON, self.OnPrompt)
        dist.Bind(wx.EVT_BUTTON, self.OnPrompt)
        self.Bind(wx.EVT_MOVE, self.OnMove)

        self.SetSizer(gs)
        self.Bind(wx.EVT_CLOSE, self.ShowMessage1)

    def OnApp(self, e):
        
        g.newtitle = 'App Spotlight (root)'
        self.OnSwitch(e)

    def OnAbout(self, e):
        description = """HSuite (previously Helen) is the SSU (Simple, Small, Useful) Swiss army for the Linux operating system. Features include powerful built-in custom tools,
easy installation of the best quality programs, choosing Linux distribution, helping in everyday tasks and more features are coming.
To view recent changes visit the link below.
"""
        licence = """HSuite is free software; you can redistribute
it and/or modify it under the terms of the GNU General Public License as
published by the Free Software Foundation; either version 3 of the License,
or any later version.

HSuite is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details. You should have
received a copy of the GNU General Public License along with HSuite;
if not, write to the Free Software Foundation, Inc., 59 Temple Place,
Suite 330, Boston, MA  02111-1307  USA"""

        info = wx.adv.AboutDialogInfo()

        info.SetIcon(wx.Icon('icons/about.png', wx.BITMAP_TYPE_PNG))
        info.SetName('HSuite Beta')
        info.SetVersion('v0.3 | Perseus')
        info.SetDescription(description)
        info.SetCopyright('(C) 2018 - 2019 Dániel Kolozsi (@Swanux)')
        info.SetWebSite('https://github.com/swanux/hsuite')
        info.SetLicence(licence)
        info.AddDeveloper('Swanux')
        info.AddDocWriter('Swanux')
        info.AddArtist('Seh')
        info.AddTranslator('Swanux')

        wx.adv.AboutBox(info)

    def OnPrompt(self, e):
        wx.MessageBox(g.txt1, 'Info', wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)

    def OnSwitch(self, e):
        title = g.newtitle
        g.sx, g.sy = self.GetSize()
        frame = OtherFrame(title=title)
        self.Destroy()

    def OnRun(self, e):
    
        os.system(g.fbakker)
    
    def OnMove(self, e):
    
        g.x, g.y = e.GetPosition()
        
    def ShowMessage1(self, event):
        dial = wx.MessageDialog(None, 'Do you really would like to exit?', 'Question', wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION | wx.STAY_ON_TOP)
        result = dial.ShowModal()
        if result == wx.ID_YES:
            self.Destroy()
        else:
            print("No pressed")

def main():

    app = wx.App()
    if os.geteuid() != 0:
        f1 = Frame(None, title='HSuite '+str(g.version))
    else:
        f1 = Frame(None, title='HSuite '+str(g.version)+' (root)')
    f1.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
