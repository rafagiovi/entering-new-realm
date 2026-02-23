# Nama File : IsSolidLiauidSteam.py
# Pembuat : Muhammad Rafa Giovi Pradana
# Tanggal : 22 September 2025
# Deskripsi : Menentukan bujud air berdasarkan suhu derajat Celcius

# Buatlah program fungsional yang menerima masukan suatu besaran yang menyatakan temperature air dalam derajat Celcius dan pada tekanan 1 atm dan menghasilkan bujudnya; apakah berbujud es (padat), cair, atau uap.

# Definisi & Spesifikasi 

# Suhu : 1 integer -> string
# Suhu(a) menentukan apakah air berbujud Beku, Cair, atau Uap berdasarkan suhu dalam derajat Celcius

# Realisasi

def Suhu(a: int) -> str:
    if a <= 0:
        return "Beku"
    elif 0 <= a <= 100:
        return "Cair"
    else:
        return "Uap"
    
# Aplikasi

print(Suhu(8))
print(Suhu(129))
print(Suhu(-24))