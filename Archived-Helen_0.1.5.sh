#!/bin/bash -e
wmctrl -r :ACTIVE: -b add,maximized_vert,maximized_horz
sleep 0.5
clear
#Set title
mytitle="Helen ~ 0.1.5"
echo -e '\033]2;'$mytitle'\007'
#Intro screen
dialog --title "Welcome "$USER"!" --msgbox "       

                        
 | |  | |                   
 | |__| | ___| | ___ _ __  
 |  __  |/ _ \ |/ _ \ '_ \ 
 | |  | |  __/ |  __/ | | |
 |_|  |_|\___|_|\___|_| |_|
                           
                           

      Version 0.1.5

      Dániel Kolozsi

=======================================================================

Copyright (C) [2018] [Dániel Kolozsi]

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

=======================================================================

Changes (07.02.2019):

    ~ Added GUI support with 'whiptail'
    ~ Fixed some bugs
    ~ Shortened the code by 179 lines! 
    " 160 75
clear
#Going to Home and declaring variables
cd
list=""
nam=""
num=0
what=apt
clear
echo 'Welcome '$USER'!'
#Defining functions
    promptDialogSpec () {   #Feedback for user (for func.s)
        echo 'Installing '$nam'...'
        $nam
        echo 'Done!'
        }
    promptDialog () {   #Same.. Just for single apps from repo or snap
	    if [[ $what == "snap" ]]
		then
		    echo 'Installing '$nam'...'
		    eval sudo $what install $nam --classic $mut
		    echo 'Done!'
        else
            echo 'Installing '$nam'...'
		    eval sudo $what install $nam -y $mut
		    echo 'Done!'
		fi
        }
    timsIns () {    #Timeshift
        sleep 0.5
        echo 'Installing timeshift...'
        eval sudo add-apt-repository -y ppa:teejee2008/ppa $mut
        eval sudo apt update $mut
        eval sudo apt install timeshift -y $mut
        }
    aptFast () {    #Apt-fast
        sleep 0.5
        echo 'Installing apt-fast...'
        eval sudo add-apt-repository -y ppa:apt-fast/stable $mut
        eval sudo apt update $mut
        eval sudo apt install apt-fast -y $mut
        }
    operaInstall () {   #Opera
        echo 'Installing Opera from Opera website...'
        eval wget https://download1.operacdn.com/pub/opera/desktop/57.0.3098.110/linux/opera-stable_57.0.3098.110_amd64.deb $mut
        eval sudo dpkg -i opera-stable_57.0.3098.110_amd64.deb $mut
        eval sudo apt update $mut
        eval sudo rm opera-stable_57.0.3098.110_amd64.deb $mut 
        }
    gesturesSetup () {  #Libinput gestures + GUI
        echo 'Installing xdotool and wmctrl...'
        eval sudo apt install xdotool wmctrl -y $mut
        echo 'Done!'
        echo 'Installing libinput-tools...'
        eval sudo apt install libinput-tools -y $mut
        echo 'Done!'
        echo 'Setting input permisson for gestures...'
        eval sudo gpasswd -a $USER input $mut
        echo 'Done! ATTENTION!! You need to reboot to apply this operation!'
        sleep 1
        echo 'Cloning libinput gestures and gestures GUI from github...'
        eval git clone https://github.com/bulletmark/libinput-gestures.git $mut
        eval git clone https://gitlab.com/cunidev/gestures $mut
        echo 'Done!'
        echo 'Building packages...'
        eval cd libinput-gestures $mut
        eval sudo ./libinput-gestures-setup install $mut
        eval cd $mut
        eval cd gestures $mut
        eval sudo python3 setup.py install $mut
        eval cd $mut
        eval sudo rm -rf libinput-gestures $mut
        eval sudo rm -rf gestures $mut
        }
    wpsInstall () { #WPS office
        echo 'Downloading and installing WPS Office and WPS Office symbols (it takes around 7 min)...'
        eval wget http://kdl.cc.ksosoft.com/wps-community/download/6757/wps-office_10.1.0.6757_amd64.deb $mut
        eval wget https://github.com/IamDH4/ttf-wps-fonts/archive/master.zip $mut
        eval sudo dpkg -i wps-office_10.1.0.6757_amd64.deb $mut
        eval sudo rm wps-office_10.1.0.6757_amd64.deb $mut
        eval unzip master.zip $mut
        eval cd ttf-wps-fonts-master $mut
        eval bash install.sh $mut
        eval cd $mut
        eval sudo rm -rf ttf-wps-fonts-master $mut
        eval sudo rm master.zip $mut
        }
    tweakIns () { #Elementary-tweaks
        sleep 0.5
        echo 'Installing elementary tweaks...'
        eval sudo add-apt-repository -y ppa:philip.scott/elementary-tweaks $mut
        eval sudo apt update $mut
        eval sudo apt install elementary-tweaks -y $mut
        }
    adIns () {  #0AD
        sleep 0.5
        echo 'Installing 0ad from 0ad repository... This will take a while, please be patient...'
        eval sudo add-apt-repository -y ppa:wfg/0ad $mut
        eval sudo apt-get update $mut
        eval sudo apt-get install 0ad -y $mut
        }
    rebooter () {   #Rebboot confirmation
        read -p "Do you really want to reboot? [y/n]: " prompt
        if [[ $prompt == "y" || $prompt == "Y" || $prompt == "yes" || $prompt == "Yes" ]]
        then
                systemctl reboot
        elif [[ $prompt == "n" || $prompt == "N" || $prompt == "no" || $prompt == "No" ]]
        then
            echo "OK, system won't reboot now."
        else
            echo 'Invalid command!'
        fi
        }
    updater () {    #Update system
        echo 'Updating system...'
        eval sudo apt full-upgrade -y $mut
        echo 'Done!'
        }
    clear
    #Multichoose menu
    cmd=(whiptail --title "Selection menu" --separate-output --checklist "Select options:" 44 50 32)
    options=(1 "Snapd" off    # Selection menu 3.5 using 'dialog'
             2 "Libreoffice" off
             3 "Git" off
             4 "python3" off
             5 "cmatrix" off
             6 "sl" off
             7 "mesa utils" off
             8 "Wine" off
             9 "software-properties-common" off
             10 "Opera browser" off
             11 "Steam" off
             12 "Virtualbox" off
             13 "GParted" off
             14 "Dconf Editor" off
             15 "Additional audio codecs" off
             16 "Flash player support for browsers" off
             17 "Archive management tools" off
             18 "Audacity" off
             19 "Déja dup" off
             20 "Touchpad gestures" off
             21 "Skype" off
             22 "Visualstudio Code" off
             23 "Screenfetch" off
             24 "Timeshift" off
             25 "Apt-fast" off
             26 "Upgrade system" on
             27 "Reboot after operation" on
             28 "0 A.D." off
             29 "WPS Office" off)
    choices=$("${cmd[@]}" "${options[@]}" 2>&1 >/dev/tty)
    clear
    for choice in $choices
    do
        case $choice in
            1)
                nam=snap
                promptDialogSpec
                ;;
            2)
                nam='libreoffice libreoffice-gtk*'
                promptDialog
                ;;
            3)
                nam=git
                promptDialog
                ;;
            4)
                nam='python3 python3-setuptools python3-gi python-gobject python3-pip'
                promptDialog
                ;;
            5)
                nam=cmatrix
                promptDialog
                ;;
            6)
                nam=sl
                promptDialog
                ;;
            7)
                nam=mesa-utils
                promptDialog
                ;;
            8)
                nam=wine-stable
                promptDialog
                ;;
            9)
                nam=software-properties-common
                promptDialog
                ;;
            10)
                nam=operaInstall
                promptDialogSpec
                ;;
            11)
                nam=steam-installer
                promptDialog
                ;;
            12)
                nam=virtualbox
                promptDialog
                ;;
            13)
                nam=gparted
                promptDialog
                ;;
            14)
                nam=dconf-editor
                promptDialog
                ;;
            15)
                nam='ubuntu-restricted-extras libavcodec-extra'
                promptDialog
                ;;
            16)
                nam='flashplugin-installer pepperflashplugin-nonfree'
                promptDialog
                ;;
            17)
                nam='unace rar unrar p7zip-rar p7zip sharutils uudeview mpack arj cabextract lzip lunzip'
                promptDialog
                ;;
            18)
                nam=audacity
                promptDialog
                ;;
            19)
                nam=deja-dup
                promptDialog
                ;;
            20)
                nam=gesturesSetup
                promptDialogSpec
                ;;
            21)
                what=snap
                nam=skype
                promptDialog
                ;;
            22)
                what=snap
                nam=vscode
                promptDialog
                ;;
            23)
                what=apt
                nam=screenfetch
                promptDialog
                ;;
            24)
                nam=timsIns
                promptDialogSpec
                ;;
            25)
                nam=aptFast
                promptDialogSpec
                ;;
            26)
                nam=updater
                updater
                ;;
            27)
                nam=rebooter
                rebooter
                ;;
            28)
                nam=adIns
                promptDialogSpec
                ;;
            29)
                nam=wpsInstall
                promptDialogSpec
                ;;
        esac
    done
