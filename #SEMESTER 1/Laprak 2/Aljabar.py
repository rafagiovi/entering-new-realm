# Nama File : 
# Pembuat : Muhammad Rafa Giovi Pradana
# Tanggal : 22 September 2025
# Deskripsi : 

# Buatlah program fungsional untuk menghitung hasil pembagian antar akar-akar persamaan kuadrat ax^2 + bx + c = 0 dengan masukan berupa 3 buah koefisien, yaitu a, b dan c.

# Definisi & Spesifikasi

# Aljabar : 3 integer -> real
# Aljabar(a,b,c) menentukan hasil dari persamaan kuadrat ax^2 + bx + c = 0 


# Definisi & Spesifikasi Antara

# Akar1 : 3 real -> real
# Akar1(a,b,c) menentukan Akar pertama dari tiga koefisien real a, b, dan b: (abs(-b - D(a, b, b) ** 0.5)/(2*a))

# Akar2 : 3 real -> real
# Akar1(a,b,c) menentukan Akar kedua dari tiga koefisien real a, b, dan b: (abs(-b + D(a, b, b) ** 0.5)/(2*a))

# Hasil : 3 real -> real
# Hasil(a,b,c) menentukan hasil pembagian dari Aljabar



# Realisasi

def Akar1(a: float, b: float, c: float) -> float:
    return(abs(-b - ((b*b) - (4*a*c)) ** 0.5)/(2*a))

def Akar2(a: float, b: float, c: float) -> float:
    return(abs(-b + ((b*b) - (4*a*c)) ** 0.5)/(2*a))

def Aljabar(a: int, b: int, c: int) -> float:
    if ((b*b) - (4*a*c)) < 0:
        return -999
    else:
        if Akar1(a,b,c) < Akar2(a,b,c):
            return Akar1(a,b,c) / Akar2(a,b,c)
        else:
            return Akar2(a,b,c) / Akar1(a,b,c)
    
# Aplikasi

print(Aljabar(2, 3, 6))
print(Aljabar(1, -5, 6))
print(Aljabar(1, 2, 1))