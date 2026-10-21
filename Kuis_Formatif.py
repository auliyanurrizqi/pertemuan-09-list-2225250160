print("=" * 50)
print("       KUIS FORMATIF 3")
print(" List dan Pengolahan Data Numerik")
print("=" * 50)

soal = [
    {
        "pertanyaan": "1. Mengapa list lebih tepat daripada banyak variabel terpisah untuk menyimpan 30 nilai?",
        "jawaban": ["memudahkan pengolahan data", "lebih mudah mengolah data",
                    "memudahkan penyimpanan dan pengolahan data"]
    },
    {
        "pertanyaan": "2. Berapa indeks elemen pertama pada list Python?",
        "jawaban": ["0", "nol"]
    },
    {
        "pertanyaan": "3. Apa arti indeks -1 pada list Python?",
        "jawaban": ["elemen terakhir", "data terakhir", "nilai terakhir"]
    },
    {
        "pertanyaan": "4. Apa hasil dari [10, 20, 30, 40][1:3]?",
        "jawaban": ["[20, 30]", "[20,30]"]
    },
    {
        "pertanyaan": "5. Apa perbedaan append() dan insert()?",
        "jawaban": [
            "append menambah di akhir dan insert pada indeks tertentu",
            "append menambahkan di akhir sedangkan insert pada posisi tertentu",
            "append menambah di akhir, insert menyisipkan pada indeks tertentu"
        ]
    },
    {
        "pertanyaan": "6. Apa risiko mengakses indeks yang tidak ada dalam list?",
        "jawaban": ["indexerror", "terjadi indexerror", "error indexerror"]
    },
    {
        "pertanyaan": "7. Fungsi apa yang digunakan untuk menghitung banyak elemen list?",
        "jawaban": ["len", "len()"]
    },
    {
        "pertanyaan": "8. Bagaimana cara menghitung rata-rata list numerik menggunakan sum dan len?",
        "jawaban": [
            "sum(data) / len(data)",
            "sum dibagi len",
            "jumlah seluruh nilai dibagi banyak data"
        ]
    },
    {
        "pertanyaan": "9. Mengapa list kosong perlu diperiksa sebelum menghitung rata-rata?",
        "jawaban": [
            "agar tidak membagi dengan nol",
            "karena len bernilai nol",
            "menghindari pembagian dengan nol",
            "agar tidak terjadi zerodivisionerror"
        ]
    },
    {
        "pertanyaan": "10. Apa perintah Git untuk mengirim commit lokal ke GitHub?",
        "jawaban": ["git push"]
    }
]