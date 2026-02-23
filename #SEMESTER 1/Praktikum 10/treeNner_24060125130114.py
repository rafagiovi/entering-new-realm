# Nama: Muhammad Rafa Giovi Pradana
# NIM: 24060125130114

from list_24060125130114 import *

print("########## TREE ##########")
 # DEFINISI DAN SPESIFIKASI KONSTRUKTOR
 # MakePN: elemen, list of Pohon N-ner -> Pohon N-ner
 #  {MakePN(A, C) membuat pohon N-ner dengan A sebagai akar dan C sebagai anak-anaknya. 
#   Bisa berupa daun maupun pohonN-ner utuh.}
def MakePN(A,C):
    return(A,C)

 # DEFINISI DAN SPESIFIKASI SELEKTOR
 # Akar: Pohon N-ner tidak kosong -> Elemen
 #  {Akar(P) adalah Akar dari P. Jika P adalah (A, PN) = Akar(P) adalah A.}
def Akar(PN):  
    return PN[0]

 # Anak: PohonN-er tidak kosong -> List of Pohon N-ner
 #  {Anak(P) adalah list of pohon N-ner yang merupakan anak-anak dari P. 
#   Jika P adalah (A, PN) = Anak (P) adalah PN.}

def Anak(PN):
    return  PN[1]

 # DEFINISI DAN SPESIFIKASI PREDIKAT
 # IsTreeNEmpty: PohonN-ner -> boolean
 #  {IsTreeNEmpty(PN) bernilai True jika PN kosong : []}
def isTreeNEmpty(PN):
    return PN==[]

 # IsOneElmt: PohonN-ner -> boolean
 #  {IsOneElmt(PN) bernilai True jika PN hanya terdiri dari Akar.}
def isOneElmt(PN):
    return (not isTreeNEmpty(PN)) and (isTreeNEmpty(Anak(PN)))

 # NBNElmt: PohonN-ner -> integer >= 0
 #  {NBNElmt(P) memberikan banyaknya node dari pohon P:
 #     Basis 0: IsTreeNEmpty((A)) = 0
 #     Basis 1: IsOneElmt((A)) = 1
 #     Rekurens: NBNElmt((A, PN)) = 1 + NBElmt(PN)}
 
def NBNElmt(PN):
 # Basis: Jika pohon kosong
    if isTreeNEmpty(PN):
        return 0
 # Basis 2: Jika merupakan daun
    if isOneElmt(PN):
        return 1
 # Hitung 1 untuk akar, lalu rekursif pada setiap anak pohon
    return 1+NBNElmtChild(Anak(PN))

 # NBNElmtChild: List of PohonN-ner -> integer >= 0
 #  {NBNElmtChild(PN) merekursif list of PohonN-ner yang merupakan 
#   anak-anak dari suatu akar:
 #     Basis: IsTreeNEmpty((A)) = 0
 #     Rekurens: NBNElmtChild(PN) = NBNElmt(FirstElmt(PN)) + NBNElmtChild(TailList(PN))}

def NBNElmtChild(PN):
 # Basis: Jika semua anak selesai direkursif
    if isTreeNEmpty(PN):
        return 0
 # Masukkan FirstElmt dari PN sebagai input NBNElmt, 
#  lalu rekursif tailnya terhadap NBNElmtChild.
    return NBNElmt(FirstElmt(PN)) + NBNElmtChild(Tail(PN))

 # --------------------Tugas Latihan-------------------
# Misal diberikan pohon N-ner:
P = (
    (2, [
       (3, [
          (1, []),
          (4, []),
          (5, [
             (9, [])
          ])
       ]),
       (7, [
          (6, []),
          (8, [])
       ])
    ])
)

 # NBNDaun: PohonN-ner -> integer >= 0
 #  {NBNElmt(P) memberikan banyaknya daun dari pohon P:
 #  Basis 0: IsTreeNEmpty((A)) = 0
 #  Basis 1: IsOneElmt((A)) = 1
 #  Rekurens: NBNDaun((A, PN)) = NBNDaun(PN)}
 #  Contoh: 
#  NBNDaun(P) -> 5 
#  {terdapat 5 daun pada pohonN-ner P}

def NBNDaun(P):
    if isTreeNEmpty(P): 
        return 0
    if isOneElmt(P):  
        return 1
    else: 
        return NBNElmtChild(Anak(P))

print(NBNDaun(P))

 # IsMemberPN: PohonN-ner, elemen -> integer >= 0
 #  {IsMemberPN(P, X) mengembalikan True jika X merupakan bagian dari P.
 #  Basis 0: IsTreeNEmpty((A)) = False
 #  Basis 1: IsOneElmt((A)) = A == X
 #  Rekurens: IsMember((A, PN)) = IsMemberPN(PN)}
 #  Contoh: 
#  IsMemberPN(P, 10) -> False 
#  {Tidak ada 10 pada pohon}
 #  IsMemberPN(P, 8) -> True 
#  {Elemen 8 ada pada pohon}

def IsMemberPNChild(PN, X):
    if isTreeNEmpty(PN):
        return False
    else:
        return IsMemberPN(FirstElmt(PN), X) or IsMemberPNChild(Tail(PN), X)

def IsMemberPN(PN, X):
    print(f"IsMemberPN = {PN}, {X}")
    if isTreeNEmpty(PN):
        return False
    elif isOneElmt(PN):
       if (Akar(PN)) == X:
           return True
    else:
        return IsMemberPNChild(Anak(PN), X)
    
print(IsMemberPN(P, 10))
print(IsMemberPN(P, 4))