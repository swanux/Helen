name=apt-fast
distro=Ubuntu
if [ $distro == "Ubuntu" ]; then
    dat=$(dpkg-query -W $name)
    echo "Checking for "$name": "
    echo "$dat"
    if [ "" == "$dat" ]; then
        echo "No "$name""
    else
        echo $name" is installed already."
    fi
elif [ $distro == "Arch" ]; then
    if pacman -Qi $name > /dev/null ; then
      echo $name" is installed already."
    else
      echo "No "$name""
    fi
else
    echo "Error 4 in module commonBash.sh"
fi
