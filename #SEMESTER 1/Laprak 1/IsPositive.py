# Nama File : IsPositive.py
# Pembuat : Muhammad Rafa Giovi Pradana
# Tanggal : 14 September 2025
# Deskripsi : Menentukan bilangan positif atau bukan

#Buatlah notasi fungsional dari fungsi yang menerima satu parameter bilangan bulat dan mengeluarkan nilai benar jika bilangan tersebut bernilai positif dan bukan nol. (APAKAH POSITIF?)

# Definisi & Spesifikasi

# IsPositive : integer -> boolean
# IsPositive (x) benar jika x positif

# Realisasi

def IsPositive(x: int) -> bool:
    return x >= 0

# Aplikasi

print(IsPositive(12))
print(IsPositive(-453))
print(IsPositive(8))
print(IsPositive(-34))