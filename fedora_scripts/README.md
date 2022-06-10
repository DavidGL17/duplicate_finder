# Fedora scripts

These scripts are the ones I use to maintain my fedora laptop up to date.

-   run_update : pretty straightforward, just updates the system with dnf and the gnome extensions (need to install gnome-shell-extension-installer for it to work, this is handled in the setup script)
-   synchronize_onedrive : synchs my onedrive folder with the cloud (uses the onedrive package by abraunegg (https://github.com/abraunegg/onedrive)). Different options are available (only download,...)
-   find_duplicates : just finds duplicate file that may pop up when synching one drive (you will need to replace the target variable by your hostname).

# Install

To install these scripts, just execute `./setup.sh`. It will download the dependencies and copy the scripts to /usr/bin
