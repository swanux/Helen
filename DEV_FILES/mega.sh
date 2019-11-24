#!/bin/bash
# Updated by Swanux
# Syntax ./mega.sh
url=$1
echo "Url: "$url

# get id and key from url
id=`echo $url | awk -F '!' '{print $2}'`
echo "ID: "$id
key=`echo $url | awk -F '!' '{print $3}' | sed -e 's/-/+/g' -e 's/_/\//g' -e 's/,//g'`
echo "Key: "$key

# decode key
b64_hex_key=`echo -n $key | base64 --decode --ignore-garbage 2> /dev/null | xxd -p | tr -d '\n'`
echo "Hexkey: "$b64_hex_key
key[0]=$(( 0x${b64_hex_key:00:16} ^ 0x${b64_hex_key:32:16} ))
key[1]=$(( 0x${b64_hex_key:16:16} ^ 0x${b64_hex_key:48:16} ))
key=`printf "%016x" ${key[*]}`
echo "Key2: " $key
iv="${b64_hex_key:32:16}0000000000000000"
echo "Iv: " $iv

# send the request
json_data=`curl --silent --request POST --data-binary '[{"a":"g","g":1,"p":"'$id'"}]' https://eu.api.mega.co.nz/cs`
echo "json: " $json_data

# get the download url
#Formerly $12
#new_url=`echo $json_data | awk -F '"' '{print $14}'`
new_url='http://gfs262n172.userstorage.mega.co.nz/dl/WCyACnv-ER1WFwLJwiJhCJ5WYOQ5DT47H2pex7iaTsDtApNVLOeOtnu5zyIgQH-_WCt4vmCANQDxUl_RwF4yrB5U67R7xT2M32spDB8UvlmVC-RC6MrfOrdnHjnnBw'
echo "New url: "$new_url

# get the file name, have to do a lot of weird things because openssl is tricky
tmp=`echo $json_data | awk -F '"' '{print $6}' | sed -e 's/-/+/g' -e 's/_/\//g' -e 's/,//g' | base64 --decode --ignore-garbage 2> /dev/null | xxd -p | tr -d '\n' > enc_attr.mdtmp`
tmp=`xxd -p -r enc_attr.mdtmp > enc_attr2.mdtmp`
openssl enc -d -aes-128-cbc -K $key -iv 0 -nopad -in enc_attr2.mdtmp -out dec_attr.mdtmp
#Changed this too, can't remember where from
file_name=`cat dec_attr.mdtmp | awk -F '"' '{print $8}'`
echo "File: "$file_name
rm -f *.mdtmp

# download the file and decrypt it
enc_file=${file_name}.enc

curl --output /home/$USER/Downloads/$enc_file $new_url
openssl enc -d -aes-128-ctr -K $key -iv $iv -in /home/$USER/Downloads/$enc_file -out /home/$USER/Downloads/$file_name
rm -f /home/$USER/Downloads/$enc_file
