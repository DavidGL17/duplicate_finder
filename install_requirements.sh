# Installs all requirements for every script

pip install black

for i in **/requirements.txt; do
   pip install -r $i
done