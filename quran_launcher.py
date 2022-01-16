import os
import configparser
from os.path import isfile,isdir
import signal
import time

def r(sig,dr):
  print("Trapped CTRL+C, don't use CTRL+C To exit this script. may can cause error")
  print("Except it needed for exiting state")
  time.sleep(3)
  os.system("python quran_gui.py")


print("If you see the keyboard interrupt error message : dont use CTRL+C to exit\nbut if the CTRL+C set for a exit, you can ignore the error message")
time.sleep(5)
signal.signal(signal.SIGINT,r)
config = configparser.ConfigParser()
if isfile('quran_conf.ini'):
  config.read('quran_conf.ini')
else:
  exit("Error! : Config file unavaible or corrupt!")

lang = config['QuranConf']['lang']

if isdir("lang/%s" % lang):
  os.system("cp lang/%s/* ." % lang)
  os.system("python quran_gui.py")
else:
  exit("Lang not found! : Change it in quran_conf.ini file")
