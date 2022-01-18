# Copyright 2021 by turtleion
# Created by turtleion
# Contrib: None
# Module Used: os,sys,time,requests,mutagen,signal
# Github: https://github.com/gwbcil6
# This Github Reposity: https://github.com/turtleion/quran-cli/
# Requirements: libc 2.33 >, python 3.3 >, mpv, pip
# Lang.Avaible : id, en
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

handler = http.server.SimpleHTTPRequestHandler

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'quran.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

def show_host(sig,fr):
  signal.signal(signal.SIGINT, sighand)
  print("Tekan CTRL+C untuk keluar")
  PORT = 8000
  handler_object = MyHttpRequestHandler
  my_server = socketserver.TCPServer(("", PORT), handler_object)
  my_server.serve_forever()
  print("Server dimulai pada lokasi http://localhost:%s" % str(PORT))
  time.sleep(2)
  return

def sighand(sig,fr):
  try:
    print("Argumen Hilang! Mengembalikan Surah Yang Lama (Sebelum Mengganti Surah)...")
    os.system("fuser -k 8000/tcp")
    main(sys.argv[1],1)
  except IndexError:
    main(1,1)

def fullplay(l,c,s,ma):
  global att
  print("\nGunakan CTRL+C untuk keluar (akan gagal jika menggunakan huruf q)\nInternet dan Kecepatan Proses Device Akan Mempengaruhi Kecepatan Pemutaran (Jeda 1-3 Detik => Low-Mid End Device)\n")
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
    if att == 0:
      att += 1
      continue
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
      if id == 0:
        id += 1
        continue
      req3 = requests.get("https://api.quran.sutanlab.id/surah/%s/%d" % (s,id))
      res3 = req3.json()
      audio_link = res3["data"]["audio"]["secondary"][0]
   #   audio_link = res2["data"]["audio"]["secondary"][0]
   #   print(res2)                                                                     >
      tcd = open("PLAYLIST","a")
      tcd.write("perfecto-offleno.tmp.%s.mp3\n" % (id))
      tcd.close()
      os.system("wget -O perfecto-offleno.tmp.%s.mp3 %s 2>/dev/null" % (id,audio_link))
      id += 1
      time.sleep(0.2)
    print("Terdownload!")
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
      p = input("Simpan setelah pemutaran? :")
      if p == "y" or p == "Y":
       os.system("mkdir %s" % s)
       os.system("mv * %s/" % s)
       print("TerSimpan!")
      main(s,1)
    else:
      print("Kesalahan tidak diketahui terjadi!")
      main(s,1)

def play(f,surah,ayat):
  os.system("clear")
  print("\nTekan \"q\" untuk keluar\n")
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
    exit("Error Terjadi!, Diketahui Sesuatu Tidak Ditemukan")
  ayat = 1
  nama_surah = resp["data"]["surah"]["name"]["transliteration"]["id"]
  audio = resp["data"]["audio"]["secondary"][0]
  jumlah_ayat = resp["data"]["surah"]["numberOfVerses"]
  ayat = resp["data"]["number"]["inSurah"]
  juz = resp["data"]["meta"]["juz"]
  page_in_alquran = resp["data"]["meta"]["page"]
  arab_ayat = resp["data"]["text"]["arab"]
  latin_arab_text = resp["data"]["text"]["transliteration"]["en"]
  arti_nama_surah = resp["data"]["surah"]["name"]["translation"]["id"]
  arti_ayat = resp["data"]["translation"]["id"]
  golongan_surah = resp["data"]["surah"]["revelation"]["id"]
  os.system("clear")
  str2 = "\nNama Surah: %s\nNama Surah [Arti]: %s\nJumlah Ayat: %s\nayat [Sekarang]: %s\nTerletak Pada Juz: %s\nHalaman di Al-Quran: %s\nGolongan Surah: %s\n\nAyat: %s\nAyat [Latin]: %s\nArti Ayat: %s\n\n" % (nama_surah,arti_nama_surah,jumlah_ayat,ayat,juz,page_in_alquran,golongan_surah,arab_ayat,latin_arab_text,arti_ayat)
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
      print("\nCommand:\n\texit  : Digunakan untuk keluar program ini\n\thelp  : Digunakan untuk menampilkan bantuan\n\tnext  : Digunakan untuk mengganti ayat (ke depan)\n\tprev  : Digunakan untuk mengganti ayat (ke belakang)\n\tch_ayat  : Digunakan untuk mengganti ayat (Nomer)\n\tch_surah  : Digunakan untuk mengganti surah\n\tplay : Memutar audio orang membaca ayat tersebut\n\tfull-play : Memutar surah ini secara full (Menggunakan Cara Memutar Klasik : Tidak Efisien)\n\tfull-play-offline : Sama fungsinya dengan full-play tetapi audio didownload semua terlebih dahulu lalu diputar (Efisien tapi memakan banyak waktu)\n\t\tfull-play-offline.save : Ini adalah method dari full-play-offline | Digunakan untuk mendownload audio saja\n\t\tfull-play-offline.removesave : Ini adalah method dari full-play-offline | Digunakan untuk menghapus save data yang ada di memori\n\t\tfull-play-offline.load : Ini adalah method dari full-play-offline | Digunakan untuk memuat save data yang ada di memori\n\tshow-arabic-ayat : Menampilkan ayat dalam bentuk web")
      t += 1
    elif c == "ch_surah":
      x = input("Surah ke- :")
      try:
        x = int(x)
        if x > 114:
          print("Kesalahan! : Al - Qur'an hanya memiliki 114 surah saja!")
          t += 1
        else:
          if x < 1:
            print("Kesalahan! : Nomer tidak boleh kurang dari 1!")
            t += 1

          main(x)

      except ValueError:
        print("Kesalahan! : Tidak bisa dikonversi ke integer karena string bukanlah nomer")
        t += 1

    elif c == "ch_ayat":
      x = input("Ayat ke- :")
      try:
        x = int(x)
        if x > jumlah_ayat:
          print("Kesalahan! : Surah ini hanya memiliki ayat sampai %d" % jumlah_ayat)
          t += 1
        else:
          if x < 1:
            print("Kesalahan! : Nomer tidak boleh kurang dari 1!")
            t += 1

          fetch_quran(args,x)

      except ValueError:
        print("Kesalahan! : Tidak bisa dikonversi ke integer karena string bukanlah nomer!")
        t += 1

    elif c == "next":
      if ayat == jumlah_ayat:
        print("Peringatan! : Index ayat sudah mencapai akhir -> %d" % jumlah_ayat)
        t += 1
      else:
        ayat += 1
        fetch_quran(args,ayat)

    elif c == "prev":
      if ayat <= 1:                                                                   
        print("Peringatan! : Index ayat sudah mencapai akhir -> 0")
        t += 1
      else:                           
        ayat -= 1
        fetch_quran(args,ayat)

    elif c == "" or c == "\n":
      t += 1

    elif c == "play":
      print("Mengambil audio dari internet..")
      xcplay_audio(audio,args,ayat)
     # main(args,ayat,2) 

    elif c == "full-play":
      print("Mengambil audio dari internet...")
      fullplay(link1,comd1,args,jumlah_ayat)

    elif c == "clear-cache-fp":
      os.system("rm -rf full-play/*")
      print("Membersihkan Cache...")
      t += 1

    elif c == "full-play-offline.save":
      print("Medownload audio dari internet...")
      fullplay_offline(s=args,ma=jumlah_ayat,d_only=True)


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
        print("Simpanan Yang Terdaftar:", str)
        d = input("Pilih Simpanan:")
        try:
          os.chdir(d)
          if not isfile('PLAYLIST'):
            print("Kesalahan! : Simpanan Corrupt/Error!!")
            t += 1
          elif isfile('PLAYLIST'):
            fullplay_offline(link1,args,auto_run=True)
        except FileNotFoundError:
          print("Simpanan Tidak Ditemukan!")
          t += 1


    elif c == "full-play-offline":
      print("Mendownload audio ke disk...\nTips: Selalu Bersihkan Cache Dengan Perintah \"clear-cache-fp\" agar tidak memenuhi disk")
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
        print("Simpanan Yang Terdaftar:", str)
      p = input("Pilih SaveData Untuk di Hapus:")
      if isdir("%s" % p):
        print("Menghapus SaveData: %s" % p)
        os.system("rm -r %s" % p)
        t += 1
      else:
        print("Kesalahan! : SaveData Tidak Ditemukan!")
        t += 1
    elif c == "show-arabic-ayat":
      try:
        os.system("echo \"<!DOCTYPE html>\n<html>\n<head>\n<meta http-equiv=\\\"Content-Type\\\" content=\\\"text/html;charset=UTF-8\\\">\n<style>\n@import\nurl('https://fonts.googleapis.com/css2?family=Cairo: wght@300')\n</style>\n</head>\n<body>\n<h1 style=\\\"font-family: \\\"Cairo\\\"; font-size: 36px;\\\" dir=\\\"rtl\\\" lang=\\\"ar\\\">%s</h1>\n</body,>\n</html>\" > quran.html" % arab_ayat)
        show_host(args,ayat)
      except KeyboardInterrupt:
        sighand(0,0)
    else:
      print("Kesalahan! : Perintah tidak ditemukan!")
      t += 1

def main(t,ayat=1,restart=0):

  print("Mengambil Surah...")
  time.sleep(2)
  try:
    fetch_quran(t,ayat)
  except KeyboardInterrupt:
    sighand(0,0)
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
