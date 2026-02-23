# Nama File : MeanOlympique.py
# Pembuat : Muhammad Rafa Giovi Pradana
# Tanggal : 14 September 2025
# Deskripsi : Menentukan rata-rata dari bilangan terkecil kedua dan terbesar kedua dari empat bilangan bulat

# Buatlah notasi fungsional dari fungsi yang menerima empat parameter bilangan bulat dan mengeluarkan rata-rata dari bilangan terkecil kedua dan terbesar kedua. (Mean Olympique)

# Definisi & Spesifikasi

# MO : 4 integer -> real

# MO (a,b,c,d) menghitung rata-rata dari dua buah bilangan integer yang bukan maksimum dan minimum dari empat bilangan integer: (a+b+c+d-min2(a,b,c,d)-max2(a,b,c,d))/2

# Definisi & Spesifikasi Antara

# max1 : 2 integer -> integer
# max1 (x,y) menentukan nilai maksimum dari dua bilangan integer x dan y: (x + y + abs(x - y))/2

# min1 : 2 integer -> integer
# min1 (x,y) menentukan nilai minimum dari dua bilangan integer x dan y: (x + y - abs(x - y))/2

# max2 : 4 integer -> integer
# max2 (u,v,w,x) mennetukan nilai maksimum dari empat bilangan integer

# min2 : 4 integer -> integer
# min2 (u,v,w,x) mennetukan nilai minimum dari empat bilangan integer

# Realisasi

def MO(a: float, b: float, c: float, d:float) -> float:
    return (a + b + c + d - min2(a,b,c,d) - max2(a,b,c,d))/2

# Realisasi Antara

def max1(x,y):
    return (x + y + abs(x - y))/2

def min1(x,y):
    return (x + y - abs(x - y))/2

def max2(u,v,w,x):
    return max1(max1(u,v),max1(w,x))

def min2(u,v,w,x):
    return min1(min1(u,v),min1(w,x))

# Aplikasi

print(MO(2,4,4,9))
print(MO(41,23,144,2))
print(MO(10,2,9,5))
print(MO(1,2,3,4))
