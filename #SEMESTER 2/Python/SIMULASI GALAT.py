#  SIMULASI GALAT
##############################################
# Galat Absolut     :
#                       ϵ=|a - a_hat|
# Galat Relatif     :
#                       ϵr = (|a - a_hat|)/|a|
# Galat Presentase  :
#                       ϵp = ϵr * 100%
##############################################
# Realisasi
# a merupakan nilai eksak sedangan a_hat merupakan nilai perkiraan
# a = 5 ** 0.5
# a_hat = 2.24
# Alternatif command input


# print("==== MENCARI GALAT PADA OPERASI AKAR ====")
# print("Masukan nilai akar:")
# a = (float(input(">>> "))) ** 0.5
# a_hat = round(a,2)
# # G_Absolut merupakan galat absolut
# G_Absolut = abs(a - a_hat)
# # G_Relatif merupakan galat relatif
# G_Relatif = abs(a - a_hat)/abs(a)
# # G_Persentase merupakan galat persentase
# G_Persentase = G_Relatif * 100

# print("Nilai Eksak      :", a)
# print("Nilai Perkiraan  :", a_hat)
# print("Galat Absolute   :", G_Absolut)
# print("Galat Relatif    :", G_Relatif)
# print(f"Galat Persentase  : {G_Persentase}%")



######## STUDI KASUS: BINOMIUM NEWTON ########
# Analisis apa yang terjadi jika nilai x membuat deret tidak konvergen:
#       1/(1 + 2x) = (1 + 2x)**-1
# Deret Binomium Newton adalah pengembangan dari Binomial Newton untuk pangkat negatif atau pecahan
#       (1 + x)^n = 1 + nx + (n(n-1)/2!)x^2 + (n(n-1)(n-2)/3!)x^3 + ...
########## Definisi dan Spesifikasi ##########

# DEFINISI:
# Fungsi SK1BN() mempelajari konvergensi Deret Binomium Newton pada fungsi f(x) = 1/(1+2x)
# Deret Binomium: (1+2x)^-1 = 1 - 2x + 4x^2 - 8x^3 + 16x^4 - ...
#               atau: 1 + (-2x) + (-2x)^2 + (-2x)^3 + (-2x)^4 + ...
# 
# SPESIFIKASI:
# Input:
#   - x: nilai variabel (float)
#   - n_suku: jumlah suku deret yang digunakan untuk perkiraan (int)
# 
# Proses:
#   - Validasi input x: harus dalam range -0.5 < x < 0.5 untuk konvergen
#   - Hitung nilai eksak: a2 = (1 + 2x)^-1
#   - Hitung nilai perkiraan: a2_hat = Σ(-2x)^i untuk i=0 hingga n_suku
#   - Hitung galat absolut, relatif, dan persentase
# 
# Output:
#   - Nilai Eksak (exact value)
#   - Nilai Perkiraan (approximate value dengan warning jika divergen)
#   - Galat Absolut: |a2 - a2_hat|
#   - Galat Relatif: |a2 - a2_hat|/|a2|
#   - Galat Persentase: Galat Relatif × 100%

################# Realisasi ##################

def whatisy(x, bb = -10, ba = 10, nilai = 5):
        if bb < x < ba:
            return nilai
        else:
            return whatisy(x, bb*10, ba*10, nilai*10)
        
def whatisn(x, bb = -10, ba = 10, nilai = 1):
    if -0.5<x<0.5:
        return
    else:
        if bb < x < ba:
            return nilai
        else:
            return whatisn(x, bb*10, ba*10, nilai+1)
        
def SK1BN():
    print()
    print("======= STUDI KASUS: BINOMIUM NEWTON =======")
    print("Fungsi                : f(x) = 1/(1 + 2x)")
    x = float(input("Input x               : "))
    n_suku = int(input("Pemotongan suku ke-n  : "))

    if -0.5<x<0.5:
        m = ("")
        pass
    elif x == -0.5:
        print()
        print("Penyebut tidak bisa 0 😭😭😭😭😭😭")
        print()
        return SK1BN()
    else:   
        if 0.5<=x<1 or -1<x<=-0.5:
            y = whatisy(x)
            n = whatisn(x)
            z = abs(int(x*10)) 
            m = ("<====| Error |")
            pass
        else:
            y = whatisy(x)
            n = whatisn(x)
            z = abs(int(x))
            m = ("<====| Error |")
            pass
        print()
        print("============= ERROR =============")
        print(f"""Deret Binominum Newton memiliki batasan yang dinamakan batas
konvergen yaitu setiap langkah yang di ambil semakin pendek,
contoh deret binomium newton (1/(1+2x):
              
1 - {x/y} + {round(((abs(x)/y)**2),2+n)} - {round(((abs(x)/y)**3),3+n)} + {round(((abs(x)/y)**4),4+n)} - ... 
              
Pada perhitungan ini, batas konvergennya adalah -0.5 < x < 0.5. 
Jika nilai x berada diluar batas itu akan terjadi divergen, 
yaitu setiap langkah yang diambil semakin besar, contoh deret
binomium newton (1/(1+2x):
              
1 + {2*z} - {(2*z)**2} + {(2*z)**3} - {(2*z)**4} + ... 

akibatnya, hasil(Nilai Perkiraan) yang dikeluarkan menjadi tidak
akurat, bisa dilihat sebagai berikut:""")
        
    print()

    a2 = (1 + 2*x)**-1
    a2_hat = 0
    for i in range(n_suku + 1): 
        suku = (-2*x)**i
        a2_hat += suku

    # G_Absolut merupakan galat absolut
    G_Absolut2 = abs(a2 - a2_hat)
    # G_Relatif merupakan galat relatif
    G_Relatif2 = G_Absolut2/a2
    # G_Persentase merupakan galat persentase
    G_Persentase2 = G_Relatif2 * 100

    print("Nilai Eksak           :", a2)
    print("Nilai Perkiraan       :", round(a2_hat,n_suku+1), m)
    print()
    print("ANALISIS GALAT")
    print("Galat Absolut         :", G_Absolut2)
    print("Galat Relatif         :", G_Relatif2)
    print(f"Galat Persentase      : {G_Persentase2}%")
    print()

SK1BN()

