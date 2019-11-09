#!/bin/bash +e
echo $USER
persist=$("logname")
# editable dynamic line for functions
runuser -l $persist -c "mkdir .tmp_hsuite && echo $USER && cd /home/daniel/.tmp_hsuite && git clone https://aur.archlinux.org/popsicle-git.git && cd popsicle-git && makepkg -rc"