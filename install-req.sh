#!/bin/bash

echo "Installing Requirements..."
echo "apt needed in this installer"
apt install python3 python3-pip
pip3 install requests mutagen pydub
echo "Testing Requirements..."
pip3 --version
python3 --version
read -p "Language (id,en) :" lang
if [ $lang == "id" ]; then
  echo -e "[QuranConf]\nlang = id" > quran_conf.ini
  echo "Selecting language id: indonesia"
elif [ $lang == "en" ]; then
  echo -e "[QuranConf]\nlang = en" > quran_conf.ini
  echo "Selecting language en: english (us)"
else
  echo "Language not found!, Selecting default language : id"
  echo -e "[QuranConf]\nlang = id" > quran_conf.ini
fi

echo "Requirements already satisfied, you can run the program by using command \"python3 quran_launcher.py\""
