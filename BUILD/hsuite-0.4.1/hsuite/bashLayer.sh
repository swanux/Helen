#!/bin/bash +e

pkill -f hsuite.py
pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY /usr/share/hsuite/./hsuite.py
exit
