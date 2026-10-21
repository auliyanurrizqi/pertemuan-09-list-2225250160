
# Praktik Pertemuan 09
# Analisis Nilai Mahasiswa Menggunakan List

def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


def nilai_lulus(data, batas=60):
    hasil = []

    for nilai in data:
        if nilai >= batas:
            hasil.append(nilai)

    return hasil


# Input jumlah mahasiswa
jumlah = int(input("Masukkan jumlah mahasiswa: "))

nilai = []

# Input nilai melalui terminal
for i in range(jumlah):
    angka = float(input(f"Masukkan nilai mahasiswa ke-{i + 1}: "))
    nilai.append(angka)

# Mengolah data
lulus = nilai_lulus(nilai)
belum_lulus = len(nilai) - len(lulus)

# Menampilkan hasil
print("\n===== HASIL ANALISIS NILAI =====")
print("Daftar nilai    :", nilai)
print("Banyak data     :", len(nilai))

if len(nilai) > 0:
    print("Total nilai     :", sum(nilai))
    print("Rata-rata       :", f"{rata_rata(nilai):.2f}")
    print("Nilai minimum   :", min(nilai))
    print("Nilai maksimum  :", max(nilai))
else:
    print("Belum ada nilai yang dimasukkan.")

print("Nilai lulus     :", lulus)
print("Jumlah lulus    :", len(lulus))
print("Belum lulus     :", belum_lulus)
