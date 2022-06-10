#!/bin/bash
# This script allows to check for updates on all apps installed, including gnome extension
echo 'Checking updates in apt-get...'
sudo apt-get update
sudo apt-get dist-upgrade
echo 'Checking for obsolete packages...'
sudo apt-get autoremove
sudo apt-get autoclean