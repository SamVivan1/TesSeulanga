Bahasa Indonesia:

# Program Pencari Flag

Program ini dibuat untuk mencari flag pada website http://mercury.picoctf.net:29649/ dengan mencoba berbagai nilai cookie 'name' dari 0 hingga 99.

## Cara Kerja Program

1. Mengimpor modul yang diperlukan: `signal`, `sys`, `requests`, dan `BeautifulSoup`.
2. Mendefinisikan URL target.
3. Mendefinisikan kode warna untuk output terminal.
4. Mendefinisikan fungsi `check_flag` untuk memeriksa apakah nilai yang ditemukan mengandung 'picoCTF'.
5. Mendefinisikan fungsi `signal_handler` untuk menangani sinyal `SIGINT` (Ctrl+C) dan mengakhiri program.
6. Melakukan loop dari 0 hingga 99.
7. Pada setiap iterasi, program akan:
   a. Membuat cookie dengan nama 'name' dan nilai iterasi saat ini.
   b. Mengirim permintaan GET ke URL target dengan cookie tersebut.
   c. Jika respons berhasil (status_code 200), program akan:
   i. Mengambil nilai dari kelas 'jumbotron' pada halaman HTML.
   ii. Memeriksa apakah nilai tersebut mengandung 'picoCTF' dengan memanggil fungsi `check_flag`.
   iii. Jika `check_flag` mengembalikan True, program akan keluar.
   iv. Jika tidak, program akan mencetak cookie dan nilai yang ditemukan.
   d. Jika terjadi error, program akan mencetak error tersebut.
8. Jika setelah 100 percobaan tidak ditemukan flag, program akan mencetak pesan bahwa flag tidak ditemukan.

English:

# Flag Finder Program

This program is designed to find the flag on the website http://mercury.picoctf.net:29649/ by trying various values of the 'name' cookie from 0 to 99.

## How the Program Works

1. Import the required modules: `signal`, `sys`, `requests`, and `BeautifulSoup`.
2. Define the target URL.
3. Define color codes for terminal output.
4. Define the `check_flag` function to check if the found value contains 'picoCTF'.
5. Define the `signal_handler` function to handle the `SIGINT` signal (Ctrl+C) and exit the program.
6. Loop from 0 to 99.
7. In each iteration, the program will:
   a. Create a cookie with the name 'name' and the current iteration value.
   b. Send a GET request to the target URL with the cookie.
   c. If the response is successful (status_code 200), the program will:
   i. Retrieve the value from the 'jumbotron' class on the HTML page.
   ii. Check if the value contains 'picoCTF' by calling the `check_flag` function.
   iii. If `check_flag` returns True, the program will exit.
   iv. If not, the program will print the cookie and the found value.
   d. If an error occurs, the program will print the error.
8. If after 100 attempts the flag is not found, the program will print a message that the flag was not found.
