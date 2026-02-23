# Nama File : ModifiedLeastSquare.py
# Pembuat : Muhammad Rafa Giovi Pradana
# Tanggal : 14 September 2025
# Deskripsi : Menentukan jarak titik (x,y) dari titik origin (0,0)

# Buatlah notasi fungsional dari sebuah fungsi yang menerima dua parameter bilangan riil x dan y, dan mengeluarkan jarak titik tersebut dari titik origin. (Modified Least Square)

# Definisi & Spesifikasi

# LS : 2 real -> real
# LS(x,y) adalah jarak antara titik (x,y) dengan titik origin(0,0)

# Realisasi

def LS(x: float, y:float) -> float:
    return ((x * x) + (y * y)) ** 0.5

# Aplikasi

print(LS(4,3))
print(LS(24,7))
print(LS(1314,1262))
print(LS(12,5))


