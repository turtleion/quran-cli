import requests
import os
import sys
import time
from os.path import isfile,isdir

t = 1

def main():
  global t
  req1 = requests.get("https://api.quran.sutanlab.id/surah")
  resp = req1.json()
  data1 = resp["data"]
  sub = []
  nama = []
  semi_nama_str = []
  for v in range(0,115):
    sub.append(v)

  for i in data1:
    value = i["name"]["transliteration"]["id"]
    nama.append(value)

  for c in nama:
    semi_nama_str.append("\"%d\" \"Surah %s\" " % (t,c))
    t += 1

  final_comb_str = "".join(semi_nama_str)
  #  print(value)
  print(final_comb_str)
  os.system("POG=$(dialog --stdout --no-cancel --title \"Quran in Linux 1.0\" --menu \"Pilih Surah\" 12 45 46 Exit \"Keluar Program Ini\" %s); echo $POG > ans" % final_comb_str)
  time.sleep(3)
  if isfile("ans"):
    f = open("ans")
    f = f.readline()
    if f == "Exit\n":
      exit("Exit!")
      os.system("python quran_part2.py %s" % f)
  else:
    return "fail;Kesalahan! : Kesalahan Tidak Diketahui!"
 # surah = input("Index surah (contoh: surah nomer 2 itu Al-Baqarah, Kamu bisa memilih surah Al-Baqarah dengan mengetik 2 dan surat lainnya contoh Ali-Imran Kalian bisa mengetik 3 untuk memilih surah Ali-Imran ) -- masukkan \"help\" untuk bantuan :")
#  ayah = input("Ayah/Ayat (Masukkan Blank untuk memilih Ayah/Ayat 1 atau kamu bisa memilih Ayah/Ayat Yang lain [Ayah/Ayat Harus Ada!]):")

if __name__ == "__main__":
  td = main()
  if td != None and "fail" in td:
    t = td.split(";")
    print(t[-1])
    sys.exit(2)
