**Pertemuan 07 - Fungsi Python

Nama: Jihan Fithriyyah
NIM: 2225250155
Kelas: 3A**

## Tujuan
Menggunakan fungsi, parameter, return value, dan scope untuk membuat program modular, rapi, dan mudah diuji pada bahasa pemrograman Python.

## Cara Menjalankan
1. Pastikan Anda sudah menginstal Python di komputer Anda.
2. Buka terminal atau Command Prompt di direktori/folder tempat file proyek disimpan.
3. Jalankan program utama melalui terminal VS Code dengan perintah berikut:
4. Pilih menu operasi matematika yang diinginkan (ketik angka 1 sampai 4) lalu tekan Enter.
5. Masukkan nilai atau angka sesuai dengan instruksi yang muncul di terminal.

## Cara Menjalankan
   Buka terminal pada direktori proyek, lalu jalankan perintah berikut:python3 praktik/utilitas_matematika.py

## Struktur Fungsi
Berikut adalah rincian fungsi-fungsi yang terdapat dalam berkas praktik/utilitas_matematika.py:
1. luas_persegi_panjang(p, l)
Parameter: p (panjang), l (lebar).
Return Value: Mengembalikan hasil perkalian p * l (luas persegi panjang).
2. luas_segitiga(a, t)
Parameter: a (alas), t (tinggi).
Return Value: Mengembalikan hasil perhitungan 0.5 * a * t (luas segitiga).
3. jumlah_n(n)
Parameter: n (bilangan bulat nonnegatif).
Return Value: Mengembalikan hasil akumulasi penjumlahan dari 1 hingga n ($1 + 2 + \dots + n$).
4. faktorial(n)
Parameter: n (bilangan bulat nonnegatif).
Return Value: Mengembalikan hasil perkalian faktorial dari n ($n!$).5
5. tampilkan_menu()
Parameter: Tidak ada.
Return Value: None (Hanya menampilkan pilihan menu operasi ke layar).

## Hasil Pengujian
Pengujian dilakukan dengan menggunakan test case wajib yang tercantum pada modul praktik:
Operasi Input Hasil yang Diharapkan Hasil Aktual Status 
Luas Persegi Panjang $p = 8, l = 5$40 40 Lulus
Luas Segitiga $a = 10, t = 6$30.0 30.0 Lulus 
Jumlah 1..n$n = 10$5555 Lulus
Faktorial $n = 5$120120Lulus
Faktorial (Kasus Batas)$n = 0$11Lulus

## Refleksi
Setelah memecah program menjadi fungsi-fungsi modular, bagian program yang menjadi jauh lebih sederhana adalah alur logika utama dan proses pengujian perhitungan matematika.
Sebelum dimodularisasi, rumus matematika dan perulangan tercampur langsung dengan penerimaan masukan (input) serta pencetakan (print). Setelah dipisah ke dalam fungsi terpisah:
1. Rumus matematika cukup ditulis satu kali dan dapat dipanggil kapan saja tanpa perlu menyalin kode (code duplication).
2. Fungsi perhitungan menjadi terisolasi dari antarmuka pengguna, sehingga pengujian fungsi (unit testing) dan proses pencarian kesalahan (debugging) dapat dilakukan dengan jauh lebih cepat dan terfokus.
3. Struktur program utama menjadi lebih pendek, bersih, serta mudah dibaca.
