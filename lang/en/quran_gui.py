import requests
import os
import sys
import time
from os.path import isfile,isdir

t = 1
def help():
  print("\nlist --> to list all surah\ninfo --> information of this module\nexit --> Exit this script\n")
  

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
  os.system("POG=$(dialog --stdout --no-cancel --title \"Quran in Linux 1.0\" --menu \"Select Surah\" 12 45 46 Exit \"Exit this program\" %s); echo $POG > ans" % final_comb_str)
  time.sleep(3)
  if isfile("ans"):
    f = open("ans")
    f = f.readline()
    if f == "Exit\n":
      exit("Exit!")
    try:
      os.system("python quran_part2.py %s" % f)
    except KeyboardInterrupt:
      os.system("python quran_part2.py %s" % f)
  else:
    return "fail;An Error Occured During Start Operation!"
#  surah = input("Index of surah (example: if you wan't to select Al-Baqara you can use number 2, if you wan't Ali-Imran you can use number 3):")
  #ayah = input("Ayah (Enter Blank to select ayah 1:")
   
if __name__ == "__main__":
  td = main()
  if td != None and "fail" in td:
    t = td.split(";")
    print(t[-1])
    sys.exit(2)
