# Nama/NIM: Muhammad Rafa Giovi Pradana/ 24060125130114
# Tanggal: 1

# Definisi TanggalXaverich
# type TanggalXaverich: <hari: int, bulan: int, tahun: int>
# {TanggalXaverich adalah tipe bentukan yang terdiri dari tiga integer: hari, bulan, dan tahun}
type TanggalXaverich = tuple[int, int, int]

# -------------------------------------
# Definisi dan Spesifikasi Konstruktor
# MakeTanggalXaverich: 3 integer -> TanggalXaverich
# {}
# Realisasi:
def MakeTanggalXaverich(hari: int, bulan: int, tahun: int) -> TanggalXaverich:
    return (hari, bulan, tahun)

# -------------------------------------
# Definisi dan Spesifikasi Selektor
# hari(TX): TanggalXaverich -> int
#     {}
# bulan(TX): TanggalXaverich -> int
#     {}
# tahun(TX): TanggalXaverich -> int
#     {}
# Realisasi:
def hari(TX: TanggalXaverich) -> int:
    return TX[0]
def bulan(TX: TanggalXaverich) -> int:
    return TX[1]
def tahun(TX: TanggalXaverich) -> int:
    return TX[2]

def bulan1_4(TX):
    if TX[0]%2 == 0:
        return "Hari Libur"
    else:
        return "Hari Kerja"
    
def bulan5_8(TX):
    if TX[0]%3 == 0:
        return "Hari Istirahat"
    else:
        return "Hari Produktif"
    
def bulan9_13(TX):
    if TX[0]%2 == 0:
        return  "Hari Biasa"
    else:
        return "Hari Pengingat"
     
    

    
def ClassifyXaverichDate(TX: TanggalXaverich):
    if TX[2] % 21 == 0 and TX[0]%7 == 0 :
        return "Hari Pengingat"
    else:
        if 1 <= TX[1] <= 4:
            return(bulan1_4(TX)) # Happy coding!
        if 5 <= TX[1] <= 8:
            return(bulan5_8(TX))
        if 9 <= TX[1] <= 13:
            return(bulan9_13(TX))
 
# --
# DENGAN INI SAYA MENYATAKAN BAHWA SAYA MENGERJAKAN SENDIRI TANPA BANTUAN KECERDASAN ARTIFISAL
# --
# JANGAN DIUBAH
print(eval(input()))