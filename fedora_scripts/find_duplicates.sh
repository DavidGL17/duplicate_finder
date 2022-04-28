#!/bin/bash
# finds duplicates created in OneDrive folder

target="*hp-david*"
echo "Searching duplicates..."
cd /home/david/OneDrive/
find . -name $target
lines=$(find . -name $target | wc -l)
if [[ $lines -ne 0 ]]; then
   echo 'Do you want the duplicates files to be removed (y/n)?'
   read var

   if [[ "$var" = "y" ]]; then
      find . -name $target -exec rm -rf {} \;
   fi
else
   echo "No duplicates found!"
fi
