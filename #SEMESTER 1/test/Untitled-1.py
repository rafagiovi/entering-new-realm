# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# Konso: elemen, List -> List
#  {Konso(e, L) menghasilkan sebuah list dari e dan L dengan e sebagai elemen pertama dari L.}
# Realisasi:
def Konso(E, L):
    return [E] + L
# Aplikasi:
print(Konso(7, [2, 4, 6])) # -> [7, 2, 4, 6]
# Konsi: elemen, List -> List
#  {Konsi(e, L) menghasilkan sebuah list dari e dan dengan e sebagai elemen terakhir dari L.}
# Realisasi:
def Konsi(L,E):
    return L+[E]
# Aplikasi:
print(Konsi([6,7,8],9))# -> [6, 7, 8, 9]


 # DEFINISI DAN SPESIFIKASI SELEKTOR
 # FirstElmt(L): List tidak kosong -> elemen
 #  {FirstElmt(L) mengembalikan elemen pertama dari L.}
 # Realisasi:
def FirstElmt(L):
    return L[0]
 # Aplikasi:
print(FirstElmt([83,202,79,44]))# -> 83
 # LastElmt(L): List tidak kosong -> elemen
 #  {LastElmt(L) mengembalikan elemen terakhir dari L.}
 # Realisasi:
def LastElmt(L):
    return L[-1]
 # Aplikasi:
print(LastElmt([83,202,79,44]))# -> 44
 # Head(L): List tidak kosong -> List
 #  {Head(L) mengembalikan list L tanpa elemen terakhir dari L; dapat menghasilkan list kosong.}
 # Realisasi:
def Head(L):
    return L[:-1]
 # Aplikasi:
print(Head([83,202,79,44]))# -> [83, 202, 79]
 # Tail(L): List tidak kosong -> List
 #  {Tail(L) mengembalikan list L tanpa elemen pertama dari L; dapat menghasilkan list kosong.}
 # Realisasi:
def Tail(L):
    return L[1:]
 # Aplikasi:
print(Tail([83,202,79,44]))# -> [202, 79, 44]



 # DEFINISI DAN SPESIFIKASI PREDIKAT
 # isEmpty(L): List -> boolean
 #  {isEmpty(L) bernilai True jika List merupakan list kosong.}
 # Realisasi:
def isEmpty(L):
    return L==[]
 # Aplikasi:
print(isEmpty([]))# -> True
print(isEmpty([2,7]))# -> False
 # IsOneElmt(L): List -> boolean
 #  {IsOneElmt(L) bernilai True jika List hanya memiliki tepat satu elemen.}
 # Realisasi:
def IsOneElmt(L):
    if isEmpty(L):
        return False
    else:
        return Tail(L)==[] and Head(L)==[]
 # Aplikasi:
print(IsOneElmt([8]))# -> True
print(IsOneElmt([2,3,5,7]))# -> False


 # DEFINISI DAN SPESIFIKASI FUNGSI YANG MENGOPERASIKAN LIST
 # NbElmt(L): List -> integer
 #  {NbElmt(L) menghasilkan banyaknya elemen dalam list L.}
 # Realisasi:
def NbElmt(L):
 if isEmpty(L):
    return 0
 else:
    return 1+NbElmt(Tail(L))
 # Aplikasi
print(NbElmt([]))# -> 0
print(NbElmt([2,7]))# -> 2
print(NbElmt([83,202,79,44]))# -> 4





 # --------------------Tugas Latihan-------------------
# ElmtKeN: integer ≥ 0, List -> elemen
 #  {ElmtKeN(N, L) menghasilkan elemen ke-N dari list L.}

def ElmtKeN(N,L):
    return L[N-1]

# Aplikasi
print(ElmtKeN(2,[1,9,3,45,6,2]))

 # IsMember: elemen, List -> boolean
 #  {IsMember(X, L) bernilai True apabila X merupakan elemen dari List.}

def IsMember(X,L) -> bool:
    if L[0] == X:
        return True
    else:
        return IsMember(X, L[1:])
    
# Aplikasi
print(IsMember(2,[1,2,3,4,5]))

# Copy: List -> List
#  {Copy(L) menghasilkan List yang identik dengan list asal.}

def Copy(L):
    return L

# Aplikasi
print(Copy([2,9,1,2]))

# Inverse: List -> List
 #  {Inverse(L) menghasilkan list L yang dibalik, yaitu yang urutan elemennya adalah kebalikan dari list awal.}

# Konkat: 2 List -> List
 #  {Konkat(L1, L2) menghasilkan List yang merupakan hasil konkatenasi list L1 dan L2.}

# SumElmt(L): List of integer -> integer
 #  {SumElmt(L) menghasilkan bilangan bulat yang merupakan jumlah nilai dari seluruh elemen L.}

def SumElmt(L):
    if L == []:
        return []
    else: 
        return SumElmt()


# Aplikasi

print(SumElmt(2,1,2,4,5,6))

# AvgElmt(L): List of integer -> real
 #  {AvgElmt(L) menghasilkan bilangan riil yang merupakan rata-rata nilai dari seluruh elemen L.}

# MaxElmt(L): List of integer -> integer
 #  {MaxElmt(L) mengembalikan elemen dengan nilai maksimum dari list L.}

# MaxNB: List of integer -> <integer, integer >= 1>
 #  {MaxNB(L) menghasilkan tipe bentukan yang berisikan bilangan maksimum pada list L dan seberapa banyak bilangan itu muncul di dalam list.}

# AddList: 2 List of integer -> List
 #  {AddList(L1, L2) menghasilkan list baru yang setiap elemennya adalah hasil penjumlahan setiap elemen di L1 dan L2 pada posisi yang sama.}

# IsPalindrom: List of character -> boolean
 #  {IsPalindrom(L) bernilai True jika L merupakan kata palindrom, yakni kata yang sama jika dibaca dari kiri atau kanan.}