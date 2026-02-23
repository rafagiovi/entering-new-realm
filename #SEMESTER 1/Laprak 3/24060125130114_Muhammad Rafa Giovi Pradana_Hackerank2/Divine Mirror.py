# Nama/NIM:
# Tanggal:

# Definisi Point
# type Point: <x: real, y: real>
#     {<x, y> adalah tipe bentukan point pada koordinat kartesian.}
type Point = tuple[float, float]

# -------------------------------------
# Definisi dan Spesifikasi Konstruktor
# MakePoint: 2 real  point
#     {MakePoint(x, y) membentuk tipe data point dari input (x, y).}
# Realisasi:
def MakePoint(x: float, y: float) -> Point:
    return (x, y)

# -------------------------------------
# Definisi dan Spesifikasi Selektor
# getAbsis(p): Point  real
#     {getAbsis(p) mengembalikan absis dari point (p).}
# getOrdinat(p): Point  real
#     {getOrdinat(p) mengembalikan ordinat dari point (p).}
# Realisasi:
def getAbsis(p: Point) -> float:
    return p[0]
def getOrdinat(p: Point) -> float:
    return p[1]
  
def DivineMirror(P: Point, RF: str, RT: int) -> Point:
    if getAbsis(P) == 0.0 and getOrdinat(P) == 0.0:
        return (getAbsis(P),getOrdinat(P))
    elif getAbsis(P) == 0.0:
        if RF == "Y":
            if RT == 90:
                return (-getOrdinat(P), getAbsis(P))
            elif RT == 180:
                return (getAbsis(P), -getOrdinat(P))
            elif RT == 270:
                return (getOrdinat(P), getAbsis(P))
            elif RT == 360 or RT == 0:
                return (-getAbsis(P), getOrdinat(P))       
        if RF == "X":
            if RT == 90:
                return (getOrdinat(P), getAbsis(P))
            if RT == 180:
                return (getAbsis(P), getOrdinat(P))
            if RT == 270:
                return (-getOrdinat(P), getAbsis(P))
            if RT == 360 or RT == 0:
                return (getAbsis(P), -getOrdinat(P)) 
    elif getOrdinat(P) == 0.0:
        if RF == "Y":
            if RT == 90:
                return (getOrdinat(P), -getAbsis(P))
            elif RT == 180:
                return (getAbsis(P), getOrdinat(P))
            elif RT == 270:
                return (getOrdinat(P), getAbsis(P))
            elif RT == 360 or RT == 0:
                return (-getAbsis(P), getOrdinat(P))       
        if RF == "X":
            if RT == 90:
                return (getOrdinat(P), getAbsis(P))
            if RT == 180:
                return (-getAbsis(P), getOrdinat(P))
            if RT == 270:
                return (getOrdinat(P), -getAbsis(P))
            if RT == 360 or RT == 0:
                return (getAbsis(P), getOrdinat(P))     
    else:
        if RF == "Y":
            if RT == 90:
                return (-getOrdinat(P), -getAbsis(P))
            elif RT == 180:
                return (getAbsis(P), -getOrdinat(P))
            elif RT == 270:
                return (getOrdinat(P), getAbsis(P))
            elif RT == 360 or RT == 0:
                return (-getAbsis(P), getOrdinat(P))       
        if RF == "X":
            if RT == 90:
                return (getOrdinat(P), getAbsis(P))
            if RT == 180:
                return (-getAbsis(P), getOrdinat(P))
            if RT == 270:
                return (-getOrdinat(P), -getAbsis(P))
            if RT == 360 or RT == 0:
                return (getAbsis(P), -getOrdinat(P))  


# --
# DENGAN INI SAYA MENYATAKAN BAHWA SAYA MENGERJAKAN SENDIRI TANPA BANTUAN KECERDASAN ARTIFISAL
# --
# JANGAN DIUBAH
print(eval(input()))