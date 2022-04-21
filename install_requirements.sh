# Installs all requirements for every script

for i in **/requirements.txt; do
   pip install -r $i
done