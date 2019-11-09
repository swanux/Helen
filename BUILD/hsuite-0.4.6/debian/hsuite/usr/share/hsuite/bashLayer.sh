#!/bin/bash +e

CMD="apt purge barrier -y ; apt autoremove -y"
pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY bash -c "$CMD"
exit
