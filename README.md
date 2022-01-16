# Quran di Linux (CLI)
![Quran](https://www.kindpng.com/picc/b/204-2047243_quran-png.png){: width="200" height="150" }.

> Quran di Linux dengan Audio ***Syekh. Mishary Rashid Al-Afasy murrotal***.

> API Dari Sutanlab

## API : https://api.quran.sutanlab.id

[EN - README | For English Language](en-README.md)

### Introduksi
Selamat datang di ***Al-Quran in Linux***. Ini adalah E-Quran di Linux, Aplikasi ini dapat digunakan untuk menghafal Al-Quran. Aplikasi ini menggunakan bahasa Python. Aplikasi ini berbasis **Command Line Interface (CLI)**

### Fitur
- [x] Audio (***Syekh. Mishary Rashid Al Afasy*** murrotal edition)
- [x] 2 Bahasa (en,id)
- [x] Arti Ayat
- [x] Transliterasi Arab
- [ ] Request mu?

### Sumber data
- [x] api.quran.sutanlab.id

### Instalasi
- `git clone https://github.com/gwbcil6/quran-cli`
- `cd quran-cli/ && chmod +x install-req.sh`
- `./install-req.sh`
- `python quran-launcher.py`

#### ------ One Line Code`
- `git clone https://github.com/gwbcil6/quran-cli; cd quran-cli; chmod +x install-req.sh; ./install-req.sh; python quran-launcher.py`

### Masalah
- `Tulisan Arab di Linux menjadi aneh`
- `Masalah pada RTL Mode`
- `Masalah Installasi Pada Linux di Android terutama termux (Jarang)`
- `Bugs Aneh`

### Masalah Terselesaikan
- `Tulisan Arab di Linux menjadi aneh -> menampilkan tulisan arab lewat web`
- `RTL Mode Sudah bisa digunakan tetapi ada 1 masalah lagi pada permission yang dibutuhkan`
- `Beberapa Bugs Sudah di Fix`

### Penjelasan Library dan Aplikasi
- `requests : Untuk meminta data dari api`
- `urllib3 : Merupakan Library yang dibutuhkan oleh "requests"`
- `mutagen & pydub : Untuk memodifikasi dan mengambil data MPEG3 / MP3`
- `apt & pip3 : Digunakan untuk menginstal keperluan`
- `python3 : Digunakan untuk mengeksekusi program`
- `mpv : Media Player`

### Library Yang Digunakan
- `requests`
- `urllib3`
- `mutagen`
- `pydub`

### Aplikasi yang dibutuhkan
- `python3`
- `apt`
- `pip3`
- `mpv`

### Credit
Aplikasi ini diciptakan oleh ***gwbcil6***.
Aplikasi ini menggunakan API Dari ***Sutanlab***.

### Nota & Akhir
Maaf klo b. inggris saya masih jelek karena masih belajar wkwk --> untuk en-README.md

(C) Copyrigth By GWBcil6
