# Nama File : IsAnA.py
# Pembuat : Muhammad Rafa Giovi Pradana
# Tanggal : 14 September 2025
# Deskripsi : Menentukan apakah huruf A atau bukan

# Buatlah notasi fungsional dari fungsi yang menerima satu parameter karakter dan mengeluarkan nilai benar jika karakter tersebut merupakan huruf ‘A’. (APAKAH HURUF A?)

# Definisi & Spesifikasi

# IsAnA : character -> boolean
# ISAnA (A) benar jika a adalah karakter (huruf) 'A'

# Realisasi

def IsAnA(A: str) -> bool:
    return A == 'A' or A == 'a'

# Aplikasi 

print(IsAnA('A'))
print(IsAnA('B'))
print(IsAnA('a'))
print(IsAnA('f'))