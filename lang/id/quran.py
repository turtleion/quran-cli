import requests
import os
import sys
import time

def help():
  print("\nlist --> to list all surah\ninfo --> information of this module\nexit --> Exit this script\n")
  

def main():
  surah = input("Index surah (contoh: surah nomer 2 itu Al-Baqarah, Kamu bisa memilih surah Al-Baqarah dengan mengetik 2 dan surat lainnya contoh Ali-Imran Kalian bisa mengetik 3 untuk memilih surah Ali-Imran ) -- masukkan \"help\" untuk bantuan :")
  ayah = input("Ayah/Ayat (Masukkan Blank untuk memilih Ayah/Ayat 1 atau kamu bisa memilih Ayah/Ayat Yang lain [Ayah/Ayat Harus Ada!]):")
  if surah == "" or surah == None or ayah == None:
    return "fail;User tidak memasukan apapun dalam input penting : Surah"
  else:
    if surah == "help":
      help()
      main()
    elif surah == "info":
      info()
      main()
    elif surah == "exit":
      exit()
    else:
      req = requests.get("https://api.quran.sutanlab.id/surah/%s/%s" % (surah,ayah))
      res = req.json()
#      print(res)
      if res["code"] == 404 and "Ayah \"%s\" in surah \"%s\" is not found" % (ayah,surah) in res["message"]:
        return "fail;Ayah/Ayat tidak ditemukan"
      elif res["code"] == 404 and "Surah \"%s\" is not found" % surah in res["message"]:
        return "fail;Surah tidak ditemukan"
      else:
        print("Surah ditemukan!")
        time.sleep(2)
        os.system("clear")
        if res["code"] == 200:
          nama_surah = res["data"]["surah"]["name"]["transliteration"]["id"]
          jumlah_ayah = res["data"]["surah"]["numberOfVerses"]
          ayat = res["data"]["number"]["inSurah"]
          juz = res["data"]["meta"]["juz"]
          page_in_alquran = res["data"]["meta"]["page"]
          arab_ayah = res["data"]["text"]["arab"]
          latin_arab_text = res["data"]["text"]["transliteration"]["en"]
          arti_nama_surah = res["data"]["surah"]["name"]["translation"]["id"]
          arti_ayah = res["data"]["translation"]["id"]
          golongan_surah = res["data"]["surah"]["revelation"]["id"]
        #  print(nama_surah) 
          print("Nama Surah: %s\nArti Nama Surah (Arab -> Indonesia Translasi): %s\nAyah [Sekarang]: %s\nJumlah Ayah/Ayat: %s\nJuz: %s\nHalaman di Al-Qur'an: %s\nGolongan Surah: %s\n\nAyah/Ayat [Arab]: %s\nAyah/Ayat [Latin - ID]: %s\nArti Ayah/Ayat: %s\n\n" % (nama_surah,arti_nama_surah,ayat,jumlah_ayah,juz,page_in_alquran,golongan_surah,arab_ayah,latin_arab_text,arti_ayah))
                                                                                                                      
if __name__ == "__main__":
  td = main()
  if td != None and "fail" in td:
    t = td.split(";")
    print(t[-1])
    sys.exit(2)
