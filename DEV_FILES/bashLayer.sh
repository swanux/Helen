#!/bin/bash +e

CMD="apt install libinput-tools libinput-bin wmctrl python3 xdotool python3-setuptools -y ; gpasswd -a daniel input ; git clone https://github.com/bulletmark/libinput-gestures.git ; git clone https://gitlab.com/cunidev/gestures ; cd /home/sources/HSUITE/DEV_FILES ; cd libinput-gestures ; ./libinput-gestures-setup install ; cd .. ; cd gestures ; python3 setup.py install ; cd .. ; rm -rf libinput-gestures ; rm -rf gestures ; cp /usr/share/hsuite/confs/libinput-gestures.conf ~/.config"
pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY bash -c "$CMD"
exit
