#!/bin/bash +e

CMD="apt purge libinput-tools xdotool libinput-bin python3-setuptools -y ; apt autoremove -y ; rm -rf /usr/local/bin/gestures ; rm -rf /usr/bin/libinput-gestures ; rm -rf /usr/share/applications/libinput-gestures.desktop ; rm -rf /usr/share/applications/org.cunidev.gestures.desktop"
pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY bash -c "$CMD"
exit
