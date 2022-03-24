#!/bin/bash
# Asks for what synchronisation is wanted
echo -e "Type the synchro you want to do\n - Download only : type 'd'\n - Upload only : type 'u'\n - Both : 'b'\n - Resync : 'r'"
read var
flags="--synchronize --enable-logging"
if [[ "$var" = "d" ]]; then
    flags="$flags --download-only"
elif [[ "$var" = "u" ]]; then
    flags="$flags --upload-only --no-remote-delete"
elif [[ "$var" = "b" ]]; then
    flags=$flags
elif [[ "$var" = "r" ]]; then
    flags="$flags --resync"
else
    echo 'Wrong input try again'
fi

while : ; do
    onedrive $flags
    if [[ $? -ne 141 ]]; then
        exit $?
    fi
done