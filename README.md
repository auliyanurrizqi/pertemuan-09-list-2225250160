
# Pertemuan 09 - List dan Pengolahan Data Numerik

## Identitas Mahasiswa

- **Nama:** Aulia Nurrizqi
- **NIM:** 2225250160
- **Kelas:** 3A
- **Program Studi:** Pendidikan Matematika
- **Fakultas:** FKIP
- **Universitas:** Universitas Sultan Ageng Tirtayasa

## Deskripsi

Repositori ini berisi latihan dan praktik mata kuliah Algoritma dan Pemrograman pada Pertemuan 09 dengan materi List/Array dan Pengolahan Data Numerik Sederhana menggunakan Python di Visual Studio Code (VS Code).

Program dibuat untuk memahami penggunaan list dalam menyimpan, mengakses, memodifikasi, dan mengolah sekumpulan data numerik, serta menerapkan perulangan, seleksi, dan fungsi.

## Tujuan Pembelajaran

1. Memahami konsep list dalam Python.
2. Membuat list kosong dan list yang berisi data.
3. Mengakses elemen menggunakan indeks positif dan negatif.
4. Menggunakan slicing untuk mengambil sebagian elemen.
5. Menambah, mengubah, menyisipkan, dan menghapus elemen list.
6. Mengolah data menggunakan perulangan dan fungsi.
7. Menghitung total, rata-rata, nilai minimum, dan maksimum.
8. Menghitung jumlah mahasiswa yang lulus dan belum lulus.
9. Menguji program di VS Code dan mengunggah proyek ke GitHub.

## Struktur Folder

```text
pertemuan-09-list-NIM/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_buat_list.py
│   ├── 02_indeks_slicing.py
│   ├── 03_manipulasi_list.py
│   ├── 04_agregasi_nilai.py
│   ├── 05_filter_kelulusan.py
│   └── 06_fungsi_statistik.py
└── praktik/
    └── analisis_nilai_mahasiswa.py
```

## Materi yang Dipelajari

### 1. Pembuatan List
Menyimpan beberapa data dalam satu variabel menggunakan tanda kurung siku `[]`.

### 2. Indeks dan Slicing
Mengakses elemen berdasarkan indeks yang dimulai dari 0 serta mengambil sebagian elemen menggunakan slicing.

### 3. Manipulasi List
Menggunakan operasi:
- `append()` untuk menambahkan elemen di akhir.
- `insert()` untuk menyisipkan elemen.
- `remove()` untuk menghapus elemen berdasarkan nilai.
- `pop()` untuk menghapus elemen berdasarkan indeks.

### 4. Pengolahan Data Numerik
Menggunakan fungsi bawaan Python:
- `len()` untuk menghitung banyak data.
- `sum()` untuk menghitung jumlah seluruh data.
- `min()` untuk mencari nilai minimum.
- `max()` untuk mencari nilai maksimum.

### 5. Fungsi dan Perulangan
Menggunakan `for` untuk menelusuri data dan fungsi untuk mengolah list agar kode lebih terstruktur serta dapat digunakan kembali.

## Cara Menjalankan Program

1. Buka folder proyek melalui VS Code.
2. Pastikan Python 3 telah terpasang.
3. Buka terminal melalui menu **Terminal > New Terminal**.
4. Jalankan salah satu file latihan dengan perintah:

```bash
python latihan/01_buat_list.py
```

Untuk menjalankan program praktik utama:

```bash
python praktik/analisis_nilai_mahasiswa.py
```

Jika perintah `python` tidak berfungsi, coba gunakan `py` pada Windows atau `python3` pada macOS/Linux.

## Praktik Analisis Nilai Mahasiswa

Program praktik utama menggunakan list yang berisi minimal 10 nilai mahasiswa dan menghasilkan informasi berikut:

- Seluruh data nilai.
- Banyak data mahasiswa.
- Total nilai.
- Rata-rata nilai.
- Nilai minimum dan maksimum.
- Daftar nilai mahasiswa yang lulus.
- Jumlah mahasiswa yang lulus.
- Jumlah mahasiswa yang belum lulus.

Batas kelulusan yang digunakan adalah nilai 60. Mahasiswa dinyatakan lulus apabila memperoleh nilai lebih besar dari atau sama dengan 60.

## Pengujian Program (Test Case)

| No. | Data Input | Pengujian | Hasil yang Diharapkan |
|---|---|---|---|
| 1 | `[60, 70, 80]` | Rata-rata | `70.00` |
| 2 | `[60, 70, 80]` | Minimum dan maksimum | `60` dan `80` |
| 3 | `[60, 70, 80]` | Jumlah mahasiswa lulus | `3` |
| 4 | `[59, 60, 61]` | Kelulusan dengan batas 60 | `2` mahasiswa lulus |
| 5 | `[]` | Fungsi rata-rata menerima list kosong | Tidak terjadi error pembagian dengan nol |

## Hasil Pengujian

Catat hasil setelah seluruh program dijalankan di VS Code.

- [ ] Seluruh file latihan dapat dijalankan.
- [ ] Indeks dan slicing menghasilkan elemen yang tepat.
- [ ] Manipulasi list berjalan sesuai kebutuhan.
- [ ] Perhitungan statistik menghasilkan nilai yang benar.
- [ ] Pengelompokan nilai lulus dan belum lulus sesuai batas 60.
- [ ] Fungsi rata-rata menangani list kosong.
- [ ] Program praktik utama berjalan tanpa error.

## Refleksi Pembelajaran

**1. Hal yang saya pahami tentang list:**

List memudahkan penyimpanan dan pengolahan banyak data dalam satu variabel. Elemen list dapat diakses melalui indeks dan dimodifikasi sesuai kebutuhan.

**2. Kesalahan yang berhasil saya perbaiki:**

[Isi dengan kesalahan yang benar-benar kamu alami selama membuat dan menjalankan program.]

**3. Manfaat materi ini:**

Materi list membantu pengolahan data numerik secara lebih efisien, misalnya untuk menghitung statistik nilai mahasiswa dan menentukan kelulusan.