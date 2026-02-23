# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
 # Konso: elemen, List -> List
 #  {Konso(e, L) menghasilkan sebuah list dari e dan L dengan e sebagai elemen pertama dari L.}
 # Realisasi:
def Konso(E, L):
    return [E] + L

 # Konsi: elemen, List -> List
 #  {Konsi(e, L) menghasilkan sebuah list dari e dan L dengan e sebagai elemen terakhir dari L.}
 # Realisasi:
def Konsi(L,E):
    return L + [E]

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

# DEFINISI DAN SPESIFIKASI PREDIKAT
 # isEmpty(L): List -> boolean
 #  {isEmpty(L) bernilai True jika List merupakan list kosong.}
 # Realisasi:
def isEmpty(L):
    return L==[]

# DEFINISI DAN SPESIFIKASI OPERASI LIST YANG DIPERLUKAN UNTUK SET
 # Rember: elemen, List -> List
 #  {Rember(x, L) menghapus sebuah elemen X dari list L. Jika x ada di list L, maka elemen L berkurang 1 Jika x tidak ada di list L maka L tetap. List kosong tetap menjadi list kosong.}
 # Realisasi:  
def Rember(x, L):
    if isEmpty(L): # Basis
        return []
    else: # Rekurens
        if FirstElmt(L) == x:
            return Tail(L)
        else:
            return Konso(FirstElmt(L), Rember(x, Tail(L)))
        
####### TUGAS #######

 # Rember2: elemen, List -> List
 #  {Rember2(x, L) menghapus sebuah elemen X dari list L. Jika x ada di list L, maka elemen L berkurang 1 Jika x tidak ada di list L maka L tetap. List kosong tetap menjadi list kosong.}
 # Realisasi:  
def Rember2(x, L):
    if isEmpty(L): # Basis
        return []
    else: # Rekurens
        if LastElmt(L) == x:
            return Head(L)
        else:
            return Konsi(Rember2(x, Head(L)), LastElmt(L))

# Aplikasi        
print(Rember2(2, [7, 2, 5, 2, 3])) # [7, 2, 5, 3]

 # MultiRember: elemen, List -> List
 #  {MultiRember(x, L) menghapus semua kemunculan elemen x dari list L. List baru yang dihasilkan tidak lagi memiliki elemen x. List kosong tetap menjadi list kosong.}
def MultiRember(x, L):
    if isEmpty(L): # Basis
        return []
    else:
        if FirstElmt(L) == x:
            return MultiRember(x, Tail(L))
        else:
            return Konso(FirstElmt(L), MultiRember(x, Tail(L)))

print(MultiRember(2, [7, 2, 5, 2, 3])) # [7, 5, 3]

 # IsMember: elemen, List -> bool
def IsMember(x, L):
    if isEmpty(L):
        return False
    else:
        if FirstElmt(L) == x:
            return True
        else:
            return IsMember(x, Tail(L))

# DEFINISI DAN SPESIKASI KONSTRUKTOR SET DARI LIST
 # MakeSet_V1: List -> Set
 #  {MakeSet_V1(L) membuat set dari list L dengan menghapus semua elemen yang muncul lebih dari satu, menyisakan elemen yang sama yang terakhir muncul.}
def MakeSet_V1(L):
    if isEmpty(L):
        return []
    else:
        if IsMember(FirstElmt(L), Tail(L)):
            return MakeSet_V1(Tail(L))
        else:
            return Konso(FirstElmt(L), MakeSet_V1(Tail(L)))

 # MakeSet_V2: List -> Set
 #  {MakeSet_V2(L) membuat set dari list L dengan menghapus semua elemen yang muncul lebih dari satu, menyisakan elemen yang sama yang pertama muncul.}
def MakeSet_V2(L):
    if isEmpty(L):
        return []
    else:
        return Konso(FirstElmt(L), MakeSet_V2(MultiRember(FirstElmt(L), Tail(L))))

# Aplikasi
print(MakeSet_V1([7, 2, 5, 2, 3])) #  [7, 5, 2, 3]
print(MakeSet_V2([7, 2, 5, 2, 3])) #  [7, 2, 5, 3]

 # DEFINISI DAN SPESIFIKASI PREDIKAT
 # IsSet: List -> boolean
 #  {IsSet(L) bernilai True apabila list L merupakan sebuah set.}
def IsSet(L):
    if isEmpty(L):
        return True
    else:
        if IsMember(FirstElmt(L), Tail(L)):
            return False
        else:
            return IsSet(Tail(L))

# Aplikasi
print(IsSet([7,5,2,3]))   # True
print(IsSet([7,2,5,2,3])) # False

 # IsSubSet: 2 Set -> boolean
 #  {IsSubset(H1, H2) bernilai True apabila H1 merupakan subset dari H2.}
def IsSubSet(H1, H2):
    if isEmpty(H1):
        return True
    else:
        if IsMember(FirstElmt(H1), H2):
            return IsSubSet(Tail(H1), H2)
        else:
            return False

# Verifikasi IsSubSet
print(IsSubSet([2,5], [7,2,5,3]))  # True
print(IsSubSet([2,6], [7,2,5,3]))  # False
print(IsSubSet([], [1,2,3]))       # True




