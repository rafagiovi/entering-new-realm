# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# Konso: elemen, List -> List
#  {Konso(e, L) menghasilkan sebuah list dari e dan L dengan e sebagai elemen pertama dari L.}
# Realisasi:
def Konso(E, L):
    return [E] + L

# Konsi: elemen, List -> List
#  {Konsi(e, L) menghasilkan sebuah list dari e dan dengan e sebagai elemen terakhir dari L.}
# Realisasi:
def Konsi(L,E):
    return L+[E]

 # DEFINISI DAN SPESIFIKASI SELEKTOR
 # FirstElmt(L): List tidak kosong -> elemen
 #  {FirstElmt(L) mengembalikan elemen pertama dari L.}
 # Realisasi:
def FirstElmt(L):
    return L[0]

 # LastElmt(L): List tidak kosong -> elemen
 #  {LastElmt(L) mengembalikan elemen terakhir dari L.}
 # Realisasi:
def LastElmt(L):
    return L[-1]

 # Head(L): List tidak kosong -> List
 #  {Head(L) mengembalikan list L tanpa elemen terakhir dari L; dapat menghasilkan list kosong.}
 # Realisasi:
def Head(L):
    return L[:-1]

 # Tail(L): List tidak kosong -> List
 #  {Tail(L) mengembalikan list L tanpa elemen pertama dari L; dapat menghasilkan list kosong.}
 # Realisasi:
def Tail(L):
    return L[1:]

 # firstList: List of List tidak kosong -> List
 #   {firstList(S) menghasilkan elemen pertama list (mungkin sebuah list atau atom).}
 # Realisasi:
def firstList(S):
    return S[0]

 # lastList: List of List tidak kosong -> List
 #   {lastList(S) menghasilkan elemen terakhir list (mungkin sebuah list atau atom).}
 # Realisasi:
def lastList(S):
    return S[-1]

 # tailList: List of List tidak kosong -> List of List
 #   {tailList(S) menghasilkan sisa list of list S tanpa elemen pertamanya.}
 # Realisasi:
def tailList(S):
    return S[1:]

 # headList: List of List tidak kosong -> List of List
 #   {headList(S) menghasilkan sisa list of list S tanpa elemen terakhirnya.}
 # Realisasi:
def headList(S):
    return S[:-1]

 # DEFINISI DAN SPESIFIKASI PREDIKAT
 # isEmpty(L): List -> boolean
 #  {isEmpty(L) bernilai True jika List merupakan list kosong.}
 # Realisasi:
def isEmpty(L):
    return L==[]

 # IsOneElmt(L): List -> boolean
 #  {IsOneElmt(L) bernilai True jika List hanya memiliki tepat satu elemen.}
 # Realisasi:
def IsOneElmt(L):
    if isEmpty(L):
        return False
    else:
        return Tail(L)==[] and Head(L)==[]
    
 # isAtom: List of List -> boolean
 #   {isAtom(S) benar jika S adalah sebuah atom.}
 # Realisasi:
def isAtom(S):
    return type(S)!=list

 # isList: List of List -> boolean
 #   {isList(S) benar jika S adalah sebuah list.}
 # Realisasi:
def isList(S):
    return type(S)==list

 # DEFINISI DAN SPESIFIKASI FUNGSI YANG MENGOPERASIKAN LIST
 # NbElmt(L): List -> integer
 #  {NbElmt(L) menghasilkan banyaknya elemen dalam list L.}
 # Realisasi:
def NbElmt(L):
 if isEmpty(L):
    return 0
 else:
    return 1+NbElmt(Tail(L))
 
