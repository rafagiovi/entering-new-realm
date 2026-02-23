# Nama File : Week 2
# Pembuat : Thomas Slebew
# Tanggal : 09 September 2025
# Deskripsi : Menentukan bilangan manakah yang terbesar menggunakan ekspresi kondisional

# Definisi & Spesifikasi
# max2_conditional : 2 integer -> integer
#max2_conditional(x, y) mengembalikan parameter dengan bilangan yang terbesar menggunakan ekspresi kondisional

#Realisasi
def max2_conditional(x: int, y: int) -> int:
    if x>= y:
        return x
    else:
        return y
    
#Aplikasi
print(max2_conditional(6,4))
print(max2_conditional(2,3))


# Definisi dan spesifikasi
# max2_conditional_v2 : 2 integer -> integer
# max2_conditional_v2(x, y) mengembalikan parameter dengan bilangan yang terbesar menggunakan ekspresi kondisional

# Realisasi
def max2_conditional_v2(x : int, y : int) -> int:
    return x if x>= y else y

# Aplikasi
print(max2_conditional_v2(7,2))
print(max2_conditional_v2(1,5))

# Definisi dan Spesifikasi
# max3: 3 integer -> integer
# max3(x, y , z) mengembalikan parameter dengan bilangan terbesar menggunakan ekspresi kondisional

def max3(x: int, y: int, z: int) -> int:
    if x > y:
        if x > z:
            return x
        else: 
            return z
    else: 
        if y > z:
            return y
        else:
            return z
        
# Aplikasi
print(max3(4,2,6))
print(max3(2,3,7))
print(max3(2,8,5))

#Definisi & Spesifikasi
#fx_abs: integer -> integer
#fx_abs(x) menghasilkan nilai absolut dari x

#Realisasi
def fx_abs(x:int)->int:
    if x>=0:
        return x
    else:
        return -x

#Aplikasi
print(fx_abs(5))
print(fx_abs(0))
print(fx_abs(-90))

# Definisi dan Spesifikasi
# wujud(x): add 1 float -> string
#      wujud (x) menyatakan wujud zat dari input besaran yang menyatakan temperatur air dalam
#      derajat Celcius pada tekanan 1 atm.

# Realisasi
def wujud(x: float) -> str:
    if x>0:
        if x>=100:
            return "Uap"
        else:
            return "Cair"
    else:
        return "Es (Padat)"

# Aplikasi
print(wujud(0))
print(wujud(37.5))
print(wujud(115.7))

# Definisi dan Spesifikasi
# Jenis_segitiga(x) : int -> str
#       Jenis_segitiga(x) menyatakan apakah 3 bilangan 
#   membentuk segitiga sama sisi, sama kaki atau sembarangan

#realisasi 
def jenis_segitiga(a:int, b:int, c:int) -> str:
    
    if a == b == c:
        return "Segitiga Sama Sisi"
    elif a == b or b == c or a == c:
        return "Segitiga Sama Kaki"
    else :
        return "Segitiga Sembarang"
    
#Aplikasi 
print(jenis_segitiga(11,11,11))
print(jenis_segitiga(11,12,13))
print(jenis_segitiga(11,12,11))

# Definisi dan Spesifikasi
# konfersi_suhu: a: float, b:str -> float
#   konversi_suhu(a,b) menentukan konversi suhu dari celcius ke reamur, fahrentheit, atau kelvin

# Realisasi
def konversi_suhu(a: float, b: str) -> float:
    if b == "reamur":
        return (4 / 5) * a
    elif b == "fahrentheit":
        return (9 / 5) * a + 32
    elif b == "kelvin":
        return a + 273.15
    
# Aplikasi
print(konversi_suhu(25.0, "reamur"))
print(konversi_suhu(45.0, "kelvin"))
print(konversi_suhu(25.0, "fahrentheit"))

# Definisi dan Spesifikasi
# HariKe : d: int, m:int, y:int -> int
# HariKe(d,m,y) menghitung hari ke berapa mulai dari tanggal 1 januari pada tahun tersebut

# dpm : b:int, -> int
# dpm(b) menghitung hari ke berapa setelah melewati bulan sebelumnya


# Realisasi
def Harike(d : int,m : int,y : int) -> int:
    return dpm(m) + d -1

def dpm(b : int) -> int :
    if b == 1:
        return 1
    elif b == 2:
        return 32
    elif b == 3:
        return 60
    elif b == 4:
        return 91
    elif b == 5:
        return 121
    elif b == 6:
        return 152
    elif b == 7:
        return 182
    elif b == 8:
        return 213
    elif b == 9:
        return 244
    elif b == 10:
        return 274
    elif b == 11:
        return 305
    elif b == 12:
        return 335
    else :
        print("Bulan tidak lebih dari 12")
        return 0
    
# Aplikasi
print(Harike(1,1,7))
print(Harike(31, 12, 7))    
             

