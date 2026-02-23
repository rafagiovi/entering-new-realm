# Nama/NIM:
# Tanggal:

# Definisi TanggalXaverich
# type TanggalXaverich: <hari: int, bulan: int, tahun: int>
# {}
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

def bulan1_4(hari, bulan, tahun):
    if TX[0]%2 == 0:
        return "Hari Libur"
    else:
        return "Hari Kerja"
    

    
def ClassifyXaverichDate(TX: TanggalXaverich):
    if TX[1] < 4:
        return(bulan1_4) # Happy coding!

# --
# DENGAN INI SAYA MENYATAKAN BAHWA SAYA MENGERJAKAN SENDIRI TANPA BANTUAN KECERDASAN ARTIFISAL
# --
# JANGAN DIUBAH
print(eval(input(ClassifyXaverichDate(MakeTanggalXaverich(1, 1, 2025)))))