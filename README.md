## English

This script is a tool for solving the picoCTF Cookies Challenge. It sends HTTP requests to a target URL with different cookie values and searches for the flag in the response.

## How to install

1. Install Python: `pkg install python`
2. Install required libraries: `pip install -r requirements.txt`
3. Clone the repository: `git clone https://github.com/SamVivan1/picoCTF_Cookies.git`
4. Navigate to the project directory: `cd picoCTF_Cookies`
5. List the files: `ls`
6. Make the script executable: `chmod +x picoctf-cookies.py`
7. Run the script: `python3 picoctf-cookies.py`

### Usage:

1. Run the script.
2. Enter the target URL when prompted.
3. The script will try 100 different cookie values (0 to 99) and print the response for each attempt.
4. If the flag is found in the response, it will be printed in green color, and the script will exit.

### Libraries:

- signal: for handling keyboard interrupts (Ctrl+C)
- sys: for exiting the script
- requests: for sending HTTP requests
- BeautifulSoup: for parsing HTML responses

### Functions:

- check_flag(value): Checks if the given value contains the string 'picoCTF'. If so, it prints the cookie value and the flag in green color, and returns True.
- signal_handler(sig, frame): Handles the keyboard interrupt signal (Ctrl+C) by printing a message in red color and exiting the script.

Note: This script is intended for educational purposes only and should not be used for any malicious activities.

## Bahasa Indonesia

Skrip ini adalah alat untuk menyelesaikan tantangan picoCTF Cookies. Skrip ini mengirimkan permintaan HTTP ke URL target dengan nilai cookie yang berbeda dan mencari bendera dalam respons.

### Cara Instalasi

1. Instal Python: `pkg install python`
2. Instal pustaka yang diperlukan: `pip install -r requirements.txt`
3. Kloning repositori: `git clone https://github.com/SamVivan1/picoCTF_Cookies.git`
4. Navigasi ke direktori proyek: `cd picoCTF_Cookies`
5. Daftar file: `ls`
6. Buat skrip dapat dieksekusi: `chmod +x picoctf-cookies.py`
7. Jalankan skrip: `python3 picoctf-cookies.py`

### Penggunaan:

1. Jalankan skrip.
2. Masukkan URL target saat diminta.
3. Skrip akan mencoba 100 nilai cookie yang berbeda (0 hingga 99) dan mencetak respons untuk setiap upaya.
4. Jika bendera ditemukan dalam respons, itu akan dicetak dengan warna hijau, dan skrip akan keluar.

### Pustaka:

- signal: untuk menangani interupsi keyboard (Ctrl+C)
- sys: untuk keluar dari skrip
- requests: untuk mengirim permintaan HTTP
- BeautifulSoup: untuk mengurai respons HTML

### Fungsi:

- check_flag(value): Memeriksa apakah nilai yang diberikan berisi string 'picoCTF'. Jika demikian, fungsi ini akan mencetak nilai cookie dan bendera dengan warna hijau, dan mengembalikan True.
- signal_handler(sig, frame): Menangani sinyal interupsi keyboard (Ctrl+C) dengan mencetak pesan dalam warna merah dan keluar dari skrip.

Catatan: Skrip ini hanya untuk tujuan pendidikan dan tidak boleh digunakan untuk aktivitas ilegal.
