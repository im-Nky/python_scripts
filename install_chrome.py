import os

os.system('sudo apt-get install gdebi')
os.system('sudo apt-get install libxss1 libappindicator1 libindicator7')
os.system('wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb')
os.system('sudo gdebi google-chrome-stable_current_amd64.deb ')
