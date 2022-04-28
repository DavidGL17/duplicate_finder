echo "Checking for gnome-shell-extension-installer..."
if [[ ! -f "/usr/bin/gnome-shell-extension-installer" ]]; then
   wget -O gnome-shell-extension-installer "https://github.com/brunelli/gnome-shell-extension-installer/raw/master/gnome-shell-extension-installer"
   chmod +x gnome-shell-extension-installer
   sudo mv gnome-shell-extension-installer /usr/bin/
else 
   echo "Already here"
fi
echo "Copying scripts..."
chmod +x find_duplicates.sh run_update.sh synchronize_onedrive.sh
sudo cp find_duplicates.sh /usr/bin/
sudo cp run_update.sh /usr/bin/
sudo cp synchronize_onedrive.sh /usr/bin/
echo "Done!"