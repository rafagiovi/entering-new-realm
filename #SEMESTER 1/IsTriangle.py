# Nama File : 
# Pembuat : Muhammad Rafa Giovi Pradana
# Tanggal : 22 September 2025
# Deskripsi : 

# Buatlah program fungsional yang menerima sebuah masukan berupa 3 buah bilangan integer lebih besar dari 0, yaitu a, b, dan c yang menyatakan panjang setiap sisi pada sebuah segitiga. Tentukan apakah segitiga tersebut sama sisi, sama kaki, atau sembarang.

# Definisi & Spesifikasi

# Realisasi

def IsTriangle(a: int, b: int, c: int) -> str:
    if a == b == c:
        return "Segitiga sama sisi"
    elif a > b == c or a < b == c or c > a == b  or c < a == b :
        return "Segitiga sama kaki"
    else:
        return "Segitiga sembarang"

# Aplikasi

print(IsTriangle(23, 42, 25))
print(IsTriangle(4, 4, 4))
print(IsTriangle(73, 23, 23))
