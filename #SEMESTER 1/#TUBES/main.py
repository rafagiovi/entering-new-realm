from TUBES import *

# print("===== Tipe Mahasiswa =====")
# Tipe Mahasiswa
M = MakeMhs("A11.2020.01234", "Reno")  # -> Membuat objek Mhs
# print(GetNIM(M))  # -> ”A11.2020.01234”
# print(GetNama(M))  # -> ”Reno”

# print("===== Tipe Matkul =====")
# Tipe Matkul
MK1 = MakeMatkul("Daspro", 3, [2.0, 3.0]) # Membuat objek Matkul
MK2 = MakeMatkul("Matdis", 2, []) # Membuat objek Matkul
# print(GetNamaMK(MK1)) # -> ”Daspro”
# print(GetSKS(MK1)) # -> 3
# print(GetNilai(MK1)) # -> [2.0, 3.0]
# print(NilaiSekarangMK(MK1)) # -> 3.0
# print(NilaiSekarangMK(MK2)) # -> -1.0
# print(SudahAmbilMK(MK2)) # -> false
# print(MengulangMK(MK1)) # -> true
# print(LulusMK(MK1)) # -> true

print("===== Tipe Transkrip =====")
# Tipe Transkrip
M = MakeMhs("A11.2020.01234", "Reno") # Membuat objek Mhs
MK1 = MakeMatkul("Daspro", 3, [2.0, 3.0]) # Membuat objek Matkul
MK2 = MakeMatkul("Matdis", 2, [3.0, 4.0])  # Membuat objek Matkul
MK3 = MakeMatkul("Alin", 4, [1.0, 2.0]) # Membuat objek Matkul
T = MakeTranskrip(M, [MK1, MK2]) # Membuat objek Transkrip
# print(GetMhs(T)) # -> M (objek Mahasiswa)
# print(GetListMatkul(T)) # -> [MK1, MK2, MK3]
# print(CariMatkul(T, "Daspro")) # -> MK1 (objek Matkul)
# print(TotalSKSLulus(T)) # -> 5
print(JumlahMatkulMengulang(T)) # -> 2
print(IPKTranskrip(T)) # -> 3.4

# print("===== Set Transkrip =====")
# # Set Transkrip
# S1 = MakeSetTranskrip() # SetTranskrip kosong []
# M1 = MakeMhs("A11.01", "Reno") # Objek Mhs
# MK1 = MakeMatkul("Daspro", 3, [2.0]) # Objek Matkul
# MK2 = MakeMatkul("Matdis", 2, [3.0]) # Objek Matkul
# T1 = MakeTranskrip(M1, [MK1, MK2]) # Objek Transkrip
# S2 = AddTranskrip(S1, T1) # SetTranskrip berisi 1 transkrip
# S3 = AddTranskrip(S2, T1) # SetTranskrip tetap berisi 1 transkrip
# M2 = MakeMhs("A11.02", "Andi") # Objek Mhs
# MK3 = MakeMatkul("Daspro", 3, [3.0]) # Objek Matkul
# MK4 = MakeMatkul("Matdis", 2, [4.0]) # Objek Matkul
# T2 = MakeTranskrip(M2, [MK3, MK4]) # Objek Transkrip
# S4 = AddTranskrip(S3, T2) # SetTranskrip berisi 2 transkrip
# M3 = MakeMhs("A11.03", "Budi") # Objek Mhs
# MK5 = MakeMatkul("Daspro", 3, [1.0, 2.0]) #Objek Matkul
# MK6 = MakeMatkul("Kalkulus", 4, [3.0]) # Objek Matkul
# T3 = MakeTranskrip(M3, [MK5, MK6]) #Objek Transkrip
# S5 = AddTranskrip(S4, T3) # SetTranskrip berisi 3 transkrip
# S6 = AddNilaiMatkul(S5, "A11.01", "Daspro", 3.0) # Nilai Daspro Reno: [2.0, 3.0]
# S7 = AddNilaiMatkul(S6, "A11.02", "Daspro", 4.0) # Nilai Daspro Andi: [3.0, 4.0]
# print(CariTranskripMhs(S7, "A11.01")) # Transkrip Reno
# print(CariTranskripMhs(S7, "A11.03 ")) # Transkrip Budi
# print(TopIPK(S7)) # M2 (Andi, IPK = 3.6)
# print(CountMhsPernahMengulang(S7)) # 3 (semua mengulang Daspro)
# print(CountMhsLulusSemuaMatkul(S7)) # 3 (semua lulus)
# print(MatkulPalingSeringDiulang(S7)) # ”Daspro” (diulang 3 mahasiswa)
# print(CountMhsDenganIPKRentang(S7, 2.0, 3.0)) # 2 (Reno dan Budi)


# print("===== TEST =====")
# print(T)