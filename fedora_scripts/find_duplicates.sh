#!/bin/bash
# finds duplicates created in OneDrive folder
echo "Searching duplicates..."
cd /home/david/OneDrive/
find . -name "*fedora*"
lines=$(find . -name "*fedora*" | wc -l)
if [[ $lines -ne 0 ]]; then
   echo 'Do you want the duplicates files to be removed (y/n)?'
   read var

   if [[ "$var" = "y" ]]; then
      find . -name "*fedora*" -exec rm -rf {} \;
   fi
else
   echo "No duplicates found!"
fi
