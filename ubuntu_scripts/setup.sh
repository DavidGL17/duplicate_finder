echo "Checking for gnome-shell-extension-installer..."
if [[ ! -f "/usr/bin/gnome-shell-extension-installer" ]]; then
   wget -O gnome-shell-extension-installer "https://github.com/brunelli/gnome-shell-extension-installer/raw/master/gnome-shell-extension-installer"
   chmod +x gnome-shell-extension-installer
   sudo mv gnome-shell-extension-installer /usr/bin/
else 
   echo "Already here"
fi
echo "Copying scripts..."
chmod +x run_update.sh
sudo cp run_update.sh /usr/bin/
echo "Done!"