#!/bin/bash +e
echo $USER
persist=$("logname")
#pacman -Sq --noconfirm go go-tools python-docutils apparmor squashfs-tools xdg-utils glu openssl-1.0 sdl2 libxss gconf nodejs npm python2 jq wxgtk2 ntfs-3g rsync libgee cronie xapps vala python-gobject xdotool wmctrl asar nim
runuser -l  $persist -c 'echo $USER && cd && git clone https://aur.archlinux.org/snapd.git && cd snapd && makepkg -rc'


#            with open("logname.sh") as f:
#                lines = f.readlines()
#            lines[4] = 'runuser -l $persist -c "echo $USER && cd && git clone https://aur.archlinux.org/electron3-bin.git && cd snapd && makepkg -rc"'
#            with open("logname.sh", "w") as f:
#                f.writelines(lines)
#            os.system('./logname.sh')
#            pkg = os.popen('ls /home/%s/snapd/' % g.user).read()
#            pkg = pkg.split()
#            pkg = pkg[1]
#            print(pkg)
#            os.system('pacman -U --noconfirm /home/%s/snapd/%s && rm -rf /home/%s/snapd' % (g.user, pkg, g.user))
