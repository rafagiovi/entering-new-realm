# Nama File : TempConverter.py
# Pembuat : Muhammad Rafa Giovi Pradana
# Tanggal : 14 September 2025
# Deskripsi : Menentukan rata-rata dari bilangan terkecil kedua dan terbesar kedua dari empat bilangan bulat

# Tuliskan sebuah fungsi yang menerima suatu besaran dalam derajat Celcius dan kode konversi ke derajat Reamur, Fahrenheit, atau Kelvin, dan mengirimkan nilai derajat sesuai kode konversi. 

# Definisi & Spesifikasi 

# Realisasi

def Reamur(Celcius: int) -> float:
    print("Celcius -> Reamur")
    return Celcius * 4/5

def Fahrenheit(Celcius: int) -> float:
    print("Celcius -> Fahrenheit")
    return (Celcius * 9/5) + 32

def Kelvin(Celcius: int) -> float:
    print("Celcius -> Kelvin")
    return Celcius + 273.15

# Aplikasi
print(Reamur(23))
print(Fahrenheit(30))
print(Kelvin(24))