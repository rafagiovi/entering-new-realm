# Nama File : NilaiAkhir.py
# Pembuat : Muhammad Rafa Giovi Pradana
# Tanggal : 14 September 2025
# Deskripsi : Menentukan nilai akhir dari lima buah bilangan bulat dengan bobot yang berbeda

# Buatlah notasi fungsional dari sebuah fungsi yang menerima lima parameter nilai dan mengeluarkan nilai akhir dari rata-rata semua nilai tersebut, dengan catatan bahwa setiap nilai memiliki bobot persentase yang berbeda:
# - Nilai Aktivitas Partisipatif → 10%
# - Nilai Tugas → 20%
# - Nilai Proyek → 40%
# - Nilai UTS → 15%
# - Nilai UAS → 15%

# Defini & Spesifikasi

# Nilai_Akhir : 5 integer -> real
# Nilai_Akhir (a,b,c,d,e) menghitung nilai akhir dari lima buah bilangan bulat a,b,c,d,e dengan bobot masing-masing 10%,20%,40%,15%,15%

# Realisasi

def Nilai_Akhir(a: int, b: int, c: int, d: int, e: int) -> float:
    return (a * .1) + (b * .2) + (c * .4) + (d * .15) + (e * .15)

# Aplikasi

print(Nilai_Akhir(100,100,100,100,100))
print(Nilai_Akhir(50,60,70,80,90))
print(Nilai_Akhir(80,72,87,93,68))