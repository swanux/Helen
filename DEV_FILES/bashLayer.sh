#!/bin/bash +e

CMD="DEBIAN_FRONTEND=noninteractive apt install opera-stable -y"
pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY bash -c "$CMD"
exit
