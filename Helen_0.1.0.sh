#!/bin/bash -e
sleep 0.01
wmctrl -r :ACTIVE: -b add,maximized_vert,maximized_horz
clear
#Set title
mytitle="Helen ~ 0.1.0"
echo -e '\033]2;'$mytitle'\007'
#Intro screen
echo "       
 __ __     _         
|  |  |___| |___ ___ 
|     | -_| | -_|   |
|__|__|___|_|___|_|_|
                     
        Version 0.1.0

      Dániel Kolozsi

================================================================

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

================================================================

Changes (09.02.2019) :

    ~ Added comments to the code
    ~ Added legal stuff & changelog at start
    ~ Added multiselection menu
    ~ Removed simple mode because of instability
    ~ Fixed some bugs
    ~ Added a bunch of apps
    ~ Added maximised mode as default in terminal
    ~ Added title to terminal
    
"
echo ''
read -p "Press enter to continue..."
#Going to Home and declaring variables
cd
list=""
nam=""
num=0
what=apt
clear
echo 'Welcome '$USER'!'
#Defining functions
program () {
    exitter () {    #Exit immadietly
        if [[ $list == *"$nam"* ]]
        then
            echo 'Beye for now!'
            sleep 1
            clear
            wmctrl -r :ACTIVE: -b remove,maximized_vert,maximized_horz
            exit
        fi
        }
    choice () {     #Menu func.
        clear
        local choice=$1
        if [[ ${opts[choice]} ]]
        then
            delete=($nam)
            list=( "${list[@]/$delete}" )
            opts[choice]=
        else
            list="$list $nam"
            if [[ $num == 34 ]]
            then
                exitter
            fi
            opts[choice]=*
        fi
        }
    promptDialogSpec () {   #Feedback for user (for func.s)
        if [[ $list == *"$nam"* ]]
        then
            echo 'Installing '$nam'...'
            $nam
            echo 'Done!'
        fi
        }
    promptDialog () {   #Same.. Just for single apps from repo or snap
        if [[ $list == *"$nam"* ]]
        then
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
        echo 'Installing 0ad from 0ad repository... This will take a while, pleasw be patient...'
        eval sudo add-apt-repository -y ppa:wfg/0ad $mut
        eval sudo apt-get update $mut
        eval sudo apt-get install 0ad -y $mut
        }
    rebooter () {   #Rebboot confirmation
        if [[ $list == *"$nam"* ]]
        then
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
        fi
        }
    updater () {    #Update system
        if [[ $list == *"$nam"* ]]
        then
            echo 'Updating system...'
            eval sudo apt full-upgrade -y $mut
            echo 'Done!'
        fi
        }
    clear
    #Multichoose menu
    PS3='Please enter your choice: '
    while :
        do
        options=("snapd ${opts[1]}" "Libreoffice ${opts[2]}" "git ${opts[3]}" "python3 ${opts[4]}" "cmatrix ${opts[5]}" "sl ${opts[6]}" "mesa-utils ${opts[7]}" "wine ${opts[8]}" "software-properties-common ${opts[9]}" "image burner ${opts[10]}" "steam ${opts[11]}" "virtualbox ${opts[12]}" "gparted ${opts[13]}" "dconf editor ${opts[14]}" "extra audio codecs ${opts[15]}" "flash player ${opts[16]}" "archive management tools ${opts[17]}" "audacity ${opts[18]}" "déja dup ${opts[19]}" "laptop mode tools ${opts[20]}" "Touchpad gestures ${opts[21]}" "opera ${opts[22]}" "skype ${opts[23]}" "visualstudio code ${opts[24]}" "WPS Office ${opts[25]}" "0ad ${opts[26]}" "elementary tweaks ${opts[27]}" "screenfetch ${opts[28]}" "timeshift ${opts[29]}" "apt-fast ${opts[30]}" "Install everything ${opts[31]}" "Upgrade ${opts[32]}" "Reboot ${opts[33]}" "Exit program ${opts[34]}" "Done")
        select opt in "${options[@]}"
        do
            case $opt in
                "snapd ${opts[1]}")
                    nam=snapd
                    num=1
                    choice 1
                    break
                    ;;
                "Libreoffice ${opts[2]}")
                    nam='libreoffice libreoffice-gtk*'
                    num=2
                    choice 2
                    break
                    ;;
                "git ${opts[3]}")
                    nam=git
                    num=3
                    choice 3 
                    break
                    ;;
                "python3 ${opts[4]}")
                    nam='python3 python3-setuptools python3-gi python-gobject python3-pip'
                    num=4
                    choice 4
                    break
                    ;;
                "cmatrix ${opts[5]}")
                    nam=cmatrix
                    num=5
                    choice 5
                    break
                    ;;
                "sl ${opts[6]}")
                    nam=sl
                    num=6
                    choice 6
                    break
                    ;;
                "mesa-utils ${opts[7]}")
                    nam=mesa-utils
                    num=7
                    choice 7
                    break
                    ;;
                "wine ${opts[8]}")
                    nam=wine-stable
                    num=8
                    choice 8
                    break
                    ;;
                "software-properties-common ${opts[9]}")
                    nam=software-properties-common
                    num=9
                    choice 9
                    break
                    ;;
                "image burner ${opts[10]}")
                    nam=imagemagick
                    num=10
                    choice 10
                    break
                    ;;
                "steam ${opts[11]}")
                    nam=steam-installer
                    num=11
                    choice 11
                    break
                    ;;
                "virtualbox ${opts[12]}")
                    nam=virtualbox
                    num=12
                    choice 12
                    break
                    ;;
                "gparted ${opts[13]}")
                    nam=gparted
                    num=13
                    choice 13
                    break
                    ;;
                "dconf editor ${opts[14]}")
                    nam=dconf-editor
                    num=14
                    choice 14
                    break
                    ;;
                "extra audio codecs ${opts[15]}")
                    nam='ubuntu-restricted-extras libavcodec-extra'
                    num=15
                    choice 15
                    break
                    ;;
                "flash player ${opts[16]}")
                    nam='flashplugin-installer pepperflashplugin-nonfree'
                    num=16
                    choice 16
                    break
                    ;;
                "archive management tools ${opts[17]}")
                    nam='unace rar unrar p7zip-rar p7zip sharutils uudeview mpack arj cabextract lzip lunzip'
                    num=17
                    choice 17
                    break
                    ;;
                "audacity ${opts[18]}")
                    nam=audacity
                    num=18
                    choice 18
                    break
                    ;;
                "déja dup ${opts[19]}")
                    nam=deja-dup
                    num=19
                    choice 19
                    break
                    ;;
                "laptop mode tools ${opts[20]}")
                    nam=laptop-mode-tools
                    num=20
                    choice 20
                    break
                    ;;
                "Touchpad gestures ${opts[21]}")
                    nam=gesturesSetup
                    num=21
                    choice 21
                    break
                    ;;
                "opera ${opts[22]}")
                    nam=operaInstall
                    num=22
                    choice 22
                    break
                    ;;
                "skype ${opts[23]}")
                    nam=skype
                    num=23
                    choice 23
                    break
                    ;;
                "visualstudio code ${opts[24]}")
                    nam=vscode
                    num=24
                    choice 24
                    break
                    ;;
                "WPS Office ${opts[25]}")
                    nam=wpsInstall
                    num=25
                    choice 25
                    break
                    ;;
                "0ad ${opts[26]}")
                    nam=adIns
                    num=26
                    choice 26
                    break
                    ;;
                "elementary tweaks ${opts[27]}")
                    nam=tweakIns
                    num=27
                    choice 27
                    break
                    ;;
                "screenfetch ${opts[28]}")
                    nam=screenfetch
                    num=28
                    choice 28
                    break
                    ;;
                "timeshift ${opts[29]}")
                    nam=timsIns
                    num=29
                    choice 29
                    break
                    ;;
                "apt-fast ${opts[30]}")
                    nam=aptFast
                    num=30
                    choice 30
                    break
                    ;;
                "Upgrade ${opts[32]}")
                    nam=updater
                    num=32
                    choice 32
                    break
                    ;;
                "Reboot ${opts[33]}")
                    nam=rebooter
                    num=33
                    choice 33
                    break
                    ;;
                "Install everything ${opts[31]}")
                    nam='snapd libreoffice libreoffice-gtk* python3 python3-setuptools python3-gi python-gobject python3-pip git cmatrix sl software-properties-common imagemagick steam-installer virtualbox gparted dconf-editor ubuntu-restricted-extras libavcodec-extra flashplugin-installer pepperflashplugin-nonfree unace rar unrar p7zip-rar p7zip sharutils uudeview mpack arj cabextract lzip lunzip audacity deja-dup laptop-mode-tools screenfetch gesturesSetup operaInstall wpsInstall adIns tweakIns timsIns aptFast vscode skype'
                    num=31
                    choice 31
                    break
                    ;;
                "Exit program ${opts[34]}")
                    nam=exitter
                    num=34
                    choice 34
                    break
                    ;;
                "Done")
                    break 2
                    ;;
                *) printf '%s\n' 'invalid option';;
            esac
        done
    done
    clear
    #Doing selected operations
	nam=aptFast
    promptDialogSpec
    nam=snapd
    promptDialog
    nam='libreoffice libreoffice-gtk*'
    promptDialog
    nam=git
    promptDialog
    nam='python3 python3-setuptools python3-gi python-gobject python3-pip'
    promptDialog
    nam=cmatrix
    promptDialog
    nam=sl
    promptDialog
    nam=mesa-utils
    promptDialog
    nam=wine-stable
    promptDialog
    nam=software-properties-common
    promptDialog
    nam=imagemagick
    promptDialog
    nam=steam-installer
    promptDialog
    nam=virtualbox
    promptDialog
    nam=gparted
    promptDialog
    nam=dconf-editor
    promptDialog
    nam='ubuntu-restricted-extras libavcodec-extra'
    promptDialog
    nam='flashplugin-installer pepperflashplugin-nonfree'
    promptDialog
    nam='unace rar unrar p7zip-rar p7zip sharutils uudeview mpack arj cabextract lzip lunzip'
    promptDialog
    nam=audacity
    promptDialog
    nam=deja-dup
    promptDialog
    nam=laptop-mode-tools
    promptDialog
    nam=screenfetch
    promptDialog
    nam=gesturesSetup
    promptDialogSpec
    nam=operaInstall
    promptDialogSpec
    nam=wpsInstall
    promptDialogSpec
    nam=adIns
    promptDialogSpec
    nam=tweakIns
    promptDialogSpec
    nam=timsIns
    promptDialogSpec
    what=snap
    nam=vscode
    promptDialog
    nam=skype
    promptDialog
    nam=updater
    updater
    nam=rebooter
    rebooter
    sleep 2
    clear
    wmctrl -r :ACTIVE: -b remove,maximized_vert,maximized_horz
    }
#read -p "Simple or advanced mode? [s/a]: " prompt
#if [[ $prompt == "s" || $prompt == "S" ]]
#then
 #   mut='>/dev/null'
  #  eval program
#else
#    mut=''
 #   eval program
#fi
eval program
