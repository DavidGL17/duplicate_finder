#!/bin/bash
# This script allows to check for updates on all apps installed, including gnome extension
echo 'Checking updates in dnf...'
sudo dnf update
echo 'Checking for obsolete packages...'
sudo dnf autoremove
echo 'Checking updates in gnome extensions...'
gnome-shell-extension-installer --yes --update