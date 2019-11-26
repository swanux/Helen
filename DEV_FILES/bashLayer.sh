#!/bin/bash +e

CMD="apt install firefox-esr -y"
pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY bash -c "$CMD"
exit
