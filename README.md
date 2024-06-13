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