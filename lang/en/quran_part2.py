# Copyright 2021 by gwbcil6
# Created by gwbcil6
# Contrib: None
# Module Used: os,sys,time,requests,mutagen,signal
# Github: https://github.com/gwbcil6
# This Github Reposity: https://github.com/gwbcil6/quran-cli/
# Requirements: libc 2.33 >, python 3.3 >, mpv, pip
# Lang.Avaible : id, en, fr (In progress), tk (In progress)
# Lang.Current : id
# Run this script as root may can cause error (permissions)
# 


import os
import sys
import time
import requests
from os.path import isfile,isdir
from mutagen.mp3 import MP3
import datetime
import multiprocessing
import signal
from pydub import AudioSegment
import http.server
import socketserver
att = 0
ath = 0

def sighandl(sig,fr):
  try:
    main(sys.argv[1],1)
  except IndexError:
    print("Error! : Error When Loading Argument : Argument not found!")

signal.signal(signal.SIGINT,sighandl)

handler = http.server.SimpleHTTPRequestHandler

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'quran.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

def show_host():
  signal.signal(signal.SIGINT, sighand)
  print("Press CTRL+C To Exit")
  PORT = 8000
  handler_object = MyHttpRequestHandler
  my_server = socketserver.TCPServer(("", PORT), handler_object)
  my_server.serve_forever()
  print("Server started on http://localhost:%s" % str(PORT))
  time.sleep(2)
  return

def sighand(sig,fr):
  try:
    print("Missing Argument! Rollback to previous state...")
    os.system("fuser -k 8000/tcp")
    main(sys.argv[1],1)
  except IndexError:
    main(1,1)

def fullplay(l,c,s,ma):
  global att
  print("\nUse CTRL+C to exit (Q Key error)\nInternet and Device Perfomance can affect play process\n")
  ayat = 1
  req0 = requests.get("https://api.quran.sutanlab.id/surah/%s/1" % s)
  res0 = req0.json()
  audio = eval(c)
  print(audio)
  os.system("wget -O perfecto-full.tmp.1.mp3 %s 2>/dev/null" % (audio))
  mp3f = MP3("perfecto-full.tmp.1.mp3")
  lengthmp3 = mp3f.info.length
  lengthmp3 = str(lengthmp3)
  lengthmp3 = lengthmp3.split('.')
  lengthmp3.pop()
  lengthmp3 = "".join(lengthmp3)
  lengthmp3 = int(lengthmp3)
  os.chdir("full-audio/")
  signal.signal(signal.SIGINT, sighand)
  for i in range(ma + 1):
    if i == 0:
      i += 1
      continue

    request = requests.get("https://api.quran.sutanlab.id/surah/%s/%d" % (s,i))
    response = request.json()
    if response["code"] == 404:
      print(response["message"])
    aud = response["data"]["audio"]["secondary"][0]
    os.system("wget -O perfecto-full.tmp.%s.mp3 %s 2>/dev/null" % (i,aud))
#    if att == 0:
 ##     att += 1
   #   continue
    os.system("mpv perfecto-full.tmp.%s.mp3" % i)
    i += 1
    time.sleep(lengthmp3 + 2)


def fullplay_offline(l="",s="",ma="",auto_run=False,d_only=False):
  signal.signal(signal.SIGINT, sighand)
  if d_only == True:
    if "full-audio" in os.getcwd():
      pass
    else:
      os.chdir("full-audio")

    os.system("mkdir %s" % s)
    time.sleep(1)
    os.chdir(s)
    for id in range(ma + 1):
#      if id == 0:
 #       id += 1
  #      continue
      req3 = requests.get("https://api.quran.sutanlab.id/surah/%s/%d" % (s,id))
      res3 = req3.json()
      audio_link = res3["data"]["audio"]["secondary"][0]
   #   audio_link = res2["data"]["audio"]["secondary"][0]
   #   print(res2)                                                                            
      tcd = open("PLAYLIST","a")
      tcd.write("perfecto-offleno.tmp.%s.mp3\n" % (id))
      tcd.close()
      os.system("wget -O perfecto-offleno.tmp.%s.mp3 %s 2>/dev/null" % (id,audio_link))
      id += 1
      time.sleep(0.2)
    print("Downloaded!")
    os.chdir("../")
    main(s,1)
  elif auto_run == True:
    os.system("mpv --playlist=PLAYLIST --volume=150")
    main(s,1)
  elif auto_run == True and d_only == True:
    main(s,1)
 # p = input("Simpan setelah pemutaran? :")
 # if p == "y" or p == "Y":

  req = requests.get("https://api.quran.sutanlab.id/surah/%s/1" % s)
  res = req.json()
  index1 = 1
  index2 = 2
  if "full-audio" in os.getcwd():
    pass
  else:
    os.chdir("full-audio")

  if res["code"] == 200:
   # audio_link = res["data"]["audio"]["secondary"][0]

   # os.system("wget -O perfecto-offleno.tmp.MP3Req.mp3 %s" % (audio_link))
   # mp3 = MP3("perfecto-offleno.tmp.MP3Req.mp3")
    for i in range(1,ma + 1):
      if i == 0:
        i += 1
        continue
      req2 = requests.get("https://api.quran.sutanlab.id/surah/%s/%d" % (s,i))
      res2 = req2.json()
      audio_link = res2["data"]["audio"]["secondary"][0]
   #   print(res2)
      os.system("wget -O perfecto-offleno.tmp.%s.mp3 %s 2>/dev/null" % (i,audio_link))
      f = open("PLAYLIST", "a")
      f.write("perfecto-offleno.tmp.%s.mp3\n" % i)
      f.close()
#      os.system("mpv perfecto-offleno.tmp.%s.mp3" % i)
      i += 1
      time.sleep(0.2)

    if isfile("PLAYLIST"):
      os.system("mpv --playlist=PLAYLIST --volume=150")
      p = input("Save audio? :")
      if p == "y" or p == "Y":
       os.system("mkdir %s" % s)
       os.system("mv * %s/" % s)
       print("Saved!")
      main(s,1)
    else:
      print("Error! : error NaN")
      main(s,1)

def play(f,surah,ayat):
  os.system("clear")
  print("\nEnter \"q\" to exit\n")
  os.system("mpv %s" % f)
  main(surah,ayat)

def xcplay_audio(audio,surah,ayat,method="NET"):
  if method == "NET":
    os.system("wget -O perfecto.tmp.mp3 %s" % audio)
    play("perfecto.tmp.mp3",surah,ayat)
  else:
    play(audio)

def fetch_quran(args,ayat_args=1):
#  print("Ketik \"help\" untuk bantuan")
  link1 = "https://api.quran.sutanlab.id/surah/%s/%d" % (args,ayat_args)
  comd1 = "res0[\"data\"][\"audio\"][\"secondary\"][0]"
  req1 = requests.get(link1)
  resp = req1.json()
  if resp["code"] == 404:
    exit("Error Occured!, Something is missing")
  ayat = 1
  nama_surah = resp["data"]["surah"]["name"]["transliteration"]["en"]
  audio = resp["data"]["audio"]["secondary"][0]
  jumlah_ayat = resp["data"]["surah"]["numberOfVerses"]
  ayat = resp["data"]["number"]["inSurah"]
  juz = resp["data"]["meta"]["juz"]
  page_in_alquran = resp["data"]["meta"]["page"]
  arab_ayat = resp["data"]["text"]["arab"]
  latin_arab_text = resp["data"]["text"]["transliteration"]["en"]
  arti_nama_surah = resp["data"]["surah"]["name"]["translation"]["en"]
  arti_ayat = resp["data"]["translation"]["en"]
  golongan_surah = resp["data"]["surah"]["revelation"]["en"]
  os.system("clear")
  str2 = "\nName of Surah: %s\nName of Surah [Mean]: %s\nTotal of ayah: %s\nAyah [Current]: %s\nLocated in Juz: %s\nPage in Quran: %s\nSurah Group: %s\n\nAyat: %s\nAyah [Latin]: %s\nAyah meaning: %s\n\n" % (nama_surah,arti_nama_surah,jumlah_ayat,ayat,juz,page_in_alquran,golongan_surah,arab_ayat,latin_arab_text,arti_ayat)
  print(str2)
  unm = "unknown"
  os.system("echo \"$(uname -o)\" > .g")
  if isfile(".g"):
    unm = open(".g")
    unm = unm.readline()
    unm = unm.replace("\n","")

  t = 1
  while t == 1:
    t -= 1
    c = input("guest:%s@localhost <{!}>:" % unm)
#    print(c)
    if c == "exit":
      exit("Exit!")
    elif c == "help":
      print("\nCommand:\n\texit  : Used to exit this program\n\thelp  : Used to show help and features\n\tnext  : Used to change ayah to next ayah\n\tprev  : Used to change ayah to previous ayah\n\tch_ayah  : Used to change Ayah (Number)\n\tch_surah : Used to change surah\n\tplay : play audio from this surah & ayah\n\tfull-play : play this surah (full)(Classic method, didn't recommended)(: download 1 file then play it)\n\tfull-play-offline : play audio from this surah (Efficien)(Modern Method)(: Download all audio then play it)\n\t\tfull-play-offline.save : Save audio to disk from this surah\n\t\tfull-play-offline.removesave : delete savedata\n\t\tfull-play-offline.load : to load savedata from this disk\n\tshow-arabic-ayat : Show ayat (arabic) in web")
      t += 1
    elif c == "ch_surah":
      x = input("Surah [Index of surah] :")
      try:
        x = int(x)
        if x > 114:
          print("Error! : Al - Qur'an have 114 Surah only!")
          t += 1
        else:
          if x < 1:
            print("Error! : Number must 0 > !")
            t += 1

          main(x)

      except ValueError:
        print("Error! : Cannot convert str into int because the str is not a number")
        t += 1

    elif c == "ch_ayah":
      x = input("Ayah - :")
      try:
        x = int(x)
        if x > jumlah_ayat:
          print("Error! : This surah only have %d ayah" % jumlah_ayat)
          t += 1
        else:
          if x < 1:
            print("Error! : Number must be 0 > !")
            t += 1

          fetch_quran(args,x)

      except ValueError:
        print("Error! : Tidak bisa dikonversi ke integer karena string bukanlah nomer!")
        t += 1

    elif c == "next":
      if ayat == jumlah_ayat:
        print("Warning! : Index ayah has reached the end -> %d" % jumlah_ayat)
        t += 1
      else:
        ayat += 1
        fetch_quran(args,ayat)

    elif c == "prev":
      if ayat <= 1:                                                                   
        print("Warning! : Index ayah has reached the end -> 0")
        t += 1
      else:                           
        ayat -= 1
        fetch_quran(args,ayat)

    elif c == "" or c == "\n":
      t += 1

    elif c == "play":
      print("Fetching audio from internet...")
      xcplay_audio(audio,args,ayat)
     # main(args,ayat,2) 

    elif c == "full-play":
      print("Fetching audio from internet...")
      fullplay(link1,comd1,args,jumlah_ayat)

    elif c == "clear-cache-fp":
      os.system("rm -rf full-play/*")
      print("Clearing Cache...")
      t += 1

    elif c == "full-play-offline.load":
      if "full-audio" in os.getcwd():
        pass
      else:
        os.chdir("full-audio")
      os.system("ls -d */ > lf")
      if isfile("lf"):
        f = open("lf")
        f = f.readlines()
        str = "".join(f)
        print("Registered SaveData:", str)
        d = input("Select SaveData:")
        try:
          os.chdir(d)
          if not isfile('PLAYLIST'):
            print("Error! : SaveData Corrupt/Error!!")
            t += 1
          elif isfile('PLAYLIST'):
            fullplay_offline(link1,args,auto_run=True)
        except FileNotFoundError:
          print("SaveData not found!")
          t += 1


    elif c == "full-play-offline":
      print("Downloading audio to disk...\nTips: Always clear full-play cache by using command \"clear-cache-fp\"")
      fullplay_offline(link1,args,jumlah_ayat)
    elif c == "full-play-offline.removesave":
      if "full-audio" in os.getcwd():
        pass
      else:
        os.chdir("full-audio")
      os.system("ls -d */ > lf")
      if isfile("lf"):
        f = open("lf")
        f = f.readlines()
        str = "".join(f)
        print("Registered Savedata:", str)
      p = input("Select Savedata to be Deleted:")
      if isdir("%s" % p):
        print("Delete SaveData: %s" % p)
        os.system("rm -r %s" % p)
        t += 1
      else:
        print("Error! : SaveData not found!")
        t += 1

    elif c == "full-play-offline.save":
      print("Downloading audio from internet...")
      fullplay_offline(s=args,ma=jumlah_ayat,d_only=True)

    elif c == "show-arabic-ayat":
      try:
        os.system("echo \"<!DOCTYPE html>\n<html>\n<head>\n<meta http-equiv=\\\"Content-Type\\\" content=\\\"text/html;charset=UTF-8\\\">\n<style>\n@import\nurl('https://fonts.googleapis.com/css2?family=Cairo: wght@300')\n</style>\n</head>\n<body>\n<h1 style=\\\"font-family: \\\"Cairo\\\"; font-size: 36px\\\" dir=\\\"rtl\\\" lang=\\\"ar\\\">%s</h1>\n</body,>\n</html>\" > quran.html" % arab_ayat)
        show_host()
      except KeyboardInterrupt:
        sighand(0,0)

#    elif c == "full-play-offline":
#      print("Downloading audio to disk...\nTips: Always clear cache because the cache is large file by using command \"clear-cache-fp\"")
#      fullplay_offline(link1,args,jumlah_ayat)
    else:
      print("Error! : Command Not Found!!")
      t += 1

def main(t,ayat=1,restart=0):

  print("Fetching Surah...")
  time.sleep(2)
  fetch_quran(t,ayat)
try:
  try:
    try:
      main(sys.argv[1])
    except KeyboardInterrupt:
      print("Use exit commands!")
      main(t,ayat)


  except EOFError:
    print("Use exit commands!")
    main(t,ayat)

except IndexError:
  exit("Need an 1 Argument")
