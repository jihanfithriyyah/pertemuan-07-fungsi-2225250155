# Pertemuan 07 Fungsi Python

Nama: [Jihan Fithriyyah]  
NIM: [2225250155]  
Kelas: [3A]  

## Tujuan
Menggunakan fungsi, parameter, return value, dan scope untuk membuat program modular dalam bahasa pemrograman Python.

## Cara Menjalankan
1. Pastikan Anda sudah menginstal Python di komputer Anda.
2. Buka terminal atau Command Prompt di direktori/folder tempat file proyek disimpan.
3. Jalankan program utama melalui terminal VS Code dengan perintah berikut:
4. Pilih menu operasi matematika yang diinginkan (ketik angka 1 sampai 4) lalu tekan Enter.
5. Masukkan nilai atau angka sesuai dengan instruksi yang muncul di terminal.
   
## Cara Menjalankan
   ```bash
python3 praktik/utilitas_matematika.py
   
## Struktur Fungsi
Berikut adalah fungsi-fungsi yang didefinisikan dalam program utilitas matematika:luas_persegi_panjang(p, l)Parameter: p (panjang), l (lebar).Return: Mengembalikan hasil perkalian p * l.luas_segitiga(a, t)Parameter: a (alas), t (tinggi).Return: Mengembalikan hasil perhitungan luas segitiga 0.5 * a * t.jumlah_n(n)Parameter: n (batas angka penjumlahan).Return: Mengembalikan total penjumlahan angka dari 1 sampai n menggunakan perulangan.faktorial(n)Parameter: n (angka yang akan dihitung faktorialnya).Return: Mengembalikan hasil perhitungan faktorial dari n.tampilkan_menu()Parameter: Tidak ada.Return: Menampilkan daftar menu pilihan operasi matematika ke layar.

## Hasil Pengujian
Berikut adalah tabel uji coba (test case) program:Operasi / FungsiInputHasil yang DiharapkanHasil AktualStatusLuas Persegi Panjangp = 8, l = 54040BerhasilLuas Segitigaa = 10, t = 630.030.0BerhasilJumlah 1..nn = 105555BerhasilFaktorialn = 5120120BerhasilFaktorial (Batas 0)n = 011Berhasil

## Refleksi
Satu bagian program yang menjadi jauh lebih sederhana setelah dipisah menjadi fungsi adalah bagian pengulangan rumus perhitungan matematika di dalam menu utama. Dengan menggunakan fungsi, kode rumus tidak perlu ditulis ulang secara berulang-ulang, sehingga program utama menjadi jauh lebih bersih, terstruktur, mudah dibaca, dan lebih mudah diperbaiki jika terjadi kesalahan pada rumus tertentu.
