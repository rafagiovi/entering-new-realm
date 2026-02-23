from List import *

####### TIPE MHS #######

# Definisi Type Mhs
# Type Mhs berisi NIM dan Nama
type Mhs = tuple[int, str]

# Definisi dan Spesifikasi Konstruktor

# MakeMhs: string, string -> Mhs
#   {MakeMhs(NIM,Nama) membuat objek Mhs dengan NIM nim dan nama
# nama}
def MakeMhs(NIM: str, Nama: str) -> Mhs:
    return NIM, Nama

# Definisi dan Spesifikasi Selektor

# GetNama: Mhs -> string
#   {GetNama(M) mengambil nama dari mahasiswa M}
def GetNama(M: Mhs) -> str:
    return M[1]

# GetNIM: Mhs -> string
#   {GetNIM(M) mengambil NIM dari mahasiswa M}
def GetNIM(M: Mhs) -> str:
    return M[0]

####### TIPE MATKUL #######

# Definisi Type Matkul
# Matkul memiliki namamk, sks, dan list nilai (0-4) yang terurut naik. Nilai
# terakhir adalah nilai akhir.
type Matkul = tuple[str,int,list]

# Definisi dan Spesifikasi Konstruktor

# MakeMatkul: string, integer, list of real -> Matkul
#   {MakeMatkul(nama, sks, listNilai) membuat objek Matkul dengan nama
# mata kuliah nama, jumlah SKS sks, dan list nilai listNilai}
def MakeMatkul(nama: str, sks: int, listNilai: list[float]) -> Matkul:
    return nama, sks, listNilai

# Definisi dan Spesifikasi Selektor

# GetNamaMK: Matkul -> string
#   {GetNamaMK(MK) mengambil nama mata kuliah dari MK}
def GetNamaMK(MK: Matkul) -> str:
    return MK[0]

# GetSKS: Matkul -> integer
#   {GetSKS(MK) mengambil jumlah SKS dari MK}
def GetSKS(MK: Matkul) -> int:
    return MK[1]

# GetNilai: Matkul -> list of real
#   {GetNilai(MK) mengambil list nilai dari MK}
def GetNilai(MK: Matkul) -> list:
    return MK[2]

# Definisi dan Spesifikasi Operator

# NilaiSekarangMK: Matkul -> real
#   {NilaiSekarangMK(MK) mengambil nilai akhir dari MK.}
#   {Jika list kosong -> -1.0.}
#   {Jika tidak -> elemen terakhir}
def NilaiSekarangMK(MK: Matkul) -> float:
    if isEmpty(LastElmt(MK)):
        return -1.0
    else:
        return LastElmt(MK[2])

# SudahAmbilMK: Matkul -> boolean
#   {SudahAmbilMK(MK) mengembalikan True jika list nilai MK tidak kosong}
def SudahAmbilMK(MK: Matkul) -> bool:
    if isEmpty(GetNilai(MK)):
        return False
    else: return True

# MengulangMK: Matkul -> boolean
#   {MengulangMK(MK) mengembalikan True jika panjang list nilai MK > 1}
def MengulangMK(MK: Matkul) -> bool:
    if NbElmt(GetNilai(MK))>1:
        return True
    else:
        return False

# LulusMK: Matkul -> boolean
#   {LulusMK(MK) mengembalikan True jika nilai akhir MK >= 2.0}
def LulusMK(MK: Matkul) -> bool:
    if NilaiSekarangMK(MK) >= 2.0:
        return True
    else: return False

####### TIPE TRANSKRIP #######

# Definisi Type Transkrip
# Transkrip berisi data mahasiswa dan daftar mata kuliahnya.
type Transkrip = tuple[Mhs, Matkul]

# Definisi dan Spesifikasi Konstruktor

# MakeTranskrip: Mhs, list of Matkul → Transkrip
#   {MakeTranskrip(M, listMK) membuat objek Transkrip dengan data
# mahasiswa M dan list mata kuliah listMK}
def MakeTranskrip(M: Mhs, listMK: list) -> Transkrip:
    return M, listMK

# Definisi dan Spesifikasi Selektor

# GetMhs: Transkrip → Mhs
#   {GetMhs(T) mengambil data mahasiswa dari transkrip T}
def GetMhs(T: Transkrip) -> Mhs:
    return T[0]

# GetListMatkul: Transkrip → list of Matkul
#   {GetListMatkul(T) mengambil list mata kuliah dari transkrip T}
def GetListMatkul(T:Transkrip) -> Matkul:
    return T[1]

# Definisi dan Spesifikasi Operator

# CariMatkul: <Transkrip, string> → Matkul
#   {CariMatkul(T, namaMK) mencari dan mengambil Matkul dari
# transkrip T berdasarkan nama mata kuliah namaMK}
def CariMatkul(T: Transkrip, namaMK: str) -> Matkul:
    if isEmpty(GetListMatkul(T)):
        return []
    else: 
        if FirstElmt(FirstElmt(GetListMatkul(T))) == namaMK:
            return FirstElmt(GetListMatkul(T))
        else:
            return CariMatkul((GetMhs(T), Tail(GetListMatkul(T))), namaMK)

  
# TotalSKSLulus: Transkrip -> integer
#   {TotalSKSLulus(T) menjumlahkan seluruh SKS dari mata kuliah yang lulus
# (nilai ≥ 2.0) pada transkrip T}
def TotalSKSLulus(T: Transkrip) -> int:
    if isEmpty(GetListMatkul(T)):
        return 0
    else:
        if NilaiSekarangMK(FirstElmt(GetListMatkul(T))) >= 2.0:
            return GetSKS(FirstElmt(GetListMatkul(T))) + TotalSKSLulus(((GetMhs(T), Tail(GetListMatkul(T)))))
        else:
            return 0

# JumlahMatkulMengulang: Transkrip -> integer
# {JumlahMatkulMengulang(T) menghitung jumlah mata kuliah yang
# diulang (panjang list nilai > 1) pada transkrip T}
def JumlahMatkulMengulang(T:Transkrip) -> int:
    if isEmpty(GetListMatkul(T)):
        return 0
    else:
        if MengulangMK(FirstElmt(GetListMatkul(T))):
            return 1 + JumlahMatkulMengulang((GetMhs(T), Tail(GetListMatkul(T))))
        else:
            return 0

# IPKTranskrip: Transkrip -> real (SEMENTARA)
#   {IPKTranskrip(T) menghitung IPK dari transkrip T dengan rumus:
# (sigma(NilaiAkhir * SKS)/sigma SKS)}
def IPKTranskrip(T:Transkrip):
    # SigmaNS: Transkrip -> real
    #   {SigmaNS(T) menghitung sigma dari NilaiSekarangMK menggunakan
    # metode rekursif}
    def SigmaNS(T):
        if isEmpty(GetListMatkul(T)):
            return 0.0
        else:
            Matkul = NilaiSekarangMK(FirstElmt(GetListMatkul(T)))
            Sks = GetSKS(FirstElmt(GetListMatkul(T)))
            return (Matkul*Sks) + SigmaNS((GetMhs(T), Tail(GetListMatkul(T))))
        
    # SigmaS: Transkrip -> real
    #   {SigmaS(T) Menghitung sigma dari GetSKS menggunaka metode
    # rekursif}
    def SigmaS(T):
        if isEmpty(GetListMatkul(T)):
            return 0.0
        else:
            return GetSKS(FirstElmt(GetListMatkul(T))) + SigmaS((GetMhs(T), Tail(GetListMatkul(T))))
    return SigmaNS(T) / SigmaS(T)
        
####### SET TRANSKRIP #######

# Definisi Set Transkrip
# Set Transkrip adalah list berisi beberapa Transkrip mahasiswa
type SetTranskrip = tuple[list]

# Definisi dan Spesifikasi Konstruktor

# MakeSetTranskrip: -> SetTranskrip
#   {MakeSetTranskrip(ST) membuat SetTranskrip kosong (list kosong)}
def MakeSetTranskrip():
    return []

# Definisi dan Spesifikasi Predikat

# IsLulusSemua: list of Matkul -> boolean
#   {IsLulusSemua(ListMK) True jika semua MK di list lulus}

def IsLulusSemua(ListMK: list) -> bool:
    if isEmpty(ListMK):
        return True
    else:
        if LulusMK(FirstElmt(ListMK)):
            return IsLulusSemua(Tail(ListMK))
        else:
            return False

# Definisi dan Spesifikasi Fungsi bantu

# UpdateListMatkul: list of Matkul, string, real -> list of Matkul
#   {UpdateListMatkul(ListMK, namaMK, nilai) mengupdate nilai MK dalam list}

def UpdateListMatkul(ListMK: list, namaMK: str, nilai: float) -> list:
    if isEmpty(ListMK):
        return []
    else:
        if GetNamaMK(FirstElmt(ListMK)) == namaMK:
            return [MakeMatkul(GetNamaMK(FirstElmt(ListMK)), GetSKS(FirstElmt(ListMK)), GetNilai(FirstElmt(ListMK)) + [nilai])] + Tail(ListMK)
        else:
            return [FirstElmt(ListMK)] + UpdateListMatkul(Tail(ListMK), namaMK, nilai)
        
# ListMengulangMhs: list of Matkul -> list of string
#   {ListMengulangMhs(ListMK) mengembalikan list nama MK yang diulang}

def ListMengulangMhs(ListMK: list) -> list:
    if isEmpty(ListMK):
        return []
    else:
        if MengulangMK(FirstElmt(ListMK)):
            return [GetNamaMK(FirstElmt(ListMK))] + ListMengulangMhs(Tail(ListMK))
        else:
            return ListMengulangMhs(Tail(ListMK))
        
# ListSemuaMengulang: SetTranskrip -> list of string
#   {ListSemuaMengulang(S) menggabungkan semua nama MK yang diulang dari semua mhs}

def ListSemuaMengulang(S: SetTranskrip) -> list:
    if isEmpty(S):
        return []
    else:
        return ListMengulangMhs(GetListMatkul(FirstElmt(S))) + ListSemuaMengulang(Tail(S))
    
# CountElmt: list, string -> integer
#   {CountElmt(L, x) menghitung kemunculan elemen x dalam list L}

def CountElmt(L: list, x: str) -> int:
    if isEmpty(L):
        return 0
    else:
        if FirstElmt(L) == x:
            return 1 + CountElmt(Tail(L), x)
        else:
            return CountElmt(Tail(L), x)

# FindMaxFreq: list, list -> string
#   {FindMaxFreq(AllList, Candidates) mencari elemen dengan frekuensi tertinggi}

def FindMaxFreq(AllList: list, Candidates: list) -> str:
    if isEmpty(Candidates):
        return ""
    elif NbElmt(Candidates) == 1:
        return FirstElmt(Candidates)
    else:
        if CountElmt(AllList, FirstElmt(Candidates)) >= CountElmt(AllList, FindMaxFreq(AllList, Tail(Candidates))):
            return FirstElmt(Candidates)
        else:
            return FindMaxFreq(AllList, Tail(Candidates))

# Definisi dan Spesifikasi Operator

# AddTranskrip: SetTranskrip, Transkrip -> SetTranskrip
#   {AddTranskrip(S,T) menambahkan transkrip T ke akhir SetTranskrip S 
# jika NIM mahasiswa pada T belum ada di S. Jika sudah ada, tidak 
# ditambahkan}
def AddTranskrip(S: SetTranskrip, T:Transkrip) -> SetTranskrip:
    if isEmpty(S):
        return S + [T]
    else:
        if GetNIM(T) == GetNIM(FirstElmt(S)) and AddTranskrip(Tail(S), T):
            return S
        else:
            return S + [T]

# AddNilaiMatkul: SetTranskrip, string, string, real -> SetTranskrip
#   {AddNIlaiMatkul(S, nim, namaMK, nilai)menambahkan nilai baru nilai
# ke mata kuliah namaMK pada transkrip mahasiswa dengan NIM nim di
# SetTranskrip S}   

def AddNilaiMatkul(S: SetTranskrip, nim: str, namaMK: str, nilai: float) -> SetTranskrip:
    if isEmpty(S):
        return S
    else:
        if GetNIM(GetMhs(FirstElmt(S))) == nim:
            return [MakeTranskrip(GetMhs(FirstElmt(S)), UpdateListMatkul(GetListMatkul(FirstElmt(S)), namaMK, nilai))] + Tail(S)
        else:
            return [FirstElmt(S)] + AddNilaiMatkul(Tail(S), nim, namaMK, nilai)

# CariTranskripMhs: SetTranskrip, string -> Transkrip
#   {CariTranskripMhs(S, nim) mencari dan mengembalikan transkrip
# pertama dengan NIM nim dari SetTranskrip S}

def CariTranskripMhs(S: SetTranskrip, nim: str) -> Transkrip:
    if isEmpty(S):
        return ()
    else:
        if GetNIM(GetMhs(FirstElmt(S))) == nim:
            return FirstElmt(S)
        else:
            return CariTranskripMhs(Tail(S), nim)

# TopIPK: SetTranskrip -> Mhs
#   {TopIPK(S) menghasilkan mahasiswa dengan IPK tertinggi dari
# SetTranskrip S }

def TopIPK(S: SetTranskrip) -> Mhs:
    if isEmpty(S):
        return ()
    elif NbElmt(S) == 1:
        return GetMhs(FirstElmt(S))
    else:
        if IPKTranskrip(FirstElmt(S)) >= IPKTranskrip(CariTranskripMhs(Tail(S), GetNIM(TopIPK(Tail(S))))):
            return GetMhs(FirstElmt(S))
        else:
            return TopIPK(Tail(S))

# CountMhsPernahMengulang: SetTranskrip -> integer
#   {CountMhsPernahMengulang(S) menghitung jumlah mahasiswa yang
# pernah mengulang minimal 1 mata kuliah pada SetTranskrip S}

def CountMhsPernahMengulang(S: SetTranskrip) -> int:
    if isEmpty(S):
        return 0
    else:
        if JumlahMatkulMengulang(FirstElmt(S)) > 0:
            return 1 + CountMhsPernahMengulang(Tail(S))
        else:
            return CountMhsPernahMengulang(Tail(S))

# CountMhsLulusSemuaMatkul: SetTranskrip -> integer
#   {CountMhsLulusSemuaMatkul(S) menghitung jumlah mahasiswa yang
# lulus seluruh mata kuliah yang diambil pada SetTranskrip S}

def CountMhsLulusSemuaMatkul(S: SetTranskrip) -> int:
    if isEmpty(S):
        return 0
    else:
        if IsLulusSemua(GetListMatkul(FirstElmt(S))):
            return 1 + CountMhsLulusSemuaMatkul(Tail(S))
        else:
            return CountMhsLulusSemuaMatkul(Tail(S))

# MatkulPalingSeringDiulang: SetTranskrip -> string
#   {MatkulPalingSeringDiulang(S) menghasilkan nama mata kuliah yang
# paling sering diulang (frekuensi tertinggi) pada SetTranskrip S}

def MatkulPalingSeringDiulang(S: SetTranskrip) -> str:
    if isEmpty(S):
        return ""
    else:
        return FindMaxFreq(ListSemuaMengulang(S), ListSemuaMengulang(S))

# CountMhsDenganIPKRentang: <SetTranskrip, real, real> -> integer
#   {CountMhsDenganIPKRentang(S, a, b) menghitung jumlah mahasiswa
# dengan IPK dalam rentang [a, b] pada SetTranskrip S}

def CountMhsDenganIPKRentang(S: SetTranskrip, a: float, b: float) -> int:
    if isEmpty(S):
        return 0
    else:
        if a <= IPKTranskrip(FirstElmt(S)) <= b:
            return 1 + CountMhsDenganIPKRentang(Tail(S), a, b)
        else:
            return CountMhsDenganIPKRentang(Tail(S), a, b)
