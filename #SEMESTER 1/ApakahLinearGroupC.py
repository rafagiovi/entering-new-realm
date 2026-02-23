# --------------------------------------
# INPUT USER UNTUK DIMENSI DAN FUNGSI YANG MAU DIUJI
# --------------------------------------
# INPUT VARIABEL YANG INGIN DIGUNAKAN SESUAI DIMENSI 
variabel = input("Masukkan variabel fungsi (misal: x, y, z,): ").replace(" ", "") # -> "x,y"
# INPUT EKSPRESI FUNGSI YANG INGIN DIUJI
ekspresi = input("Misal untuk 3D: 2*x + y , x - y , 3*y + 1 : ") # -> "2*x + y , x - y"
# SUSUN FUNGSI TRANSFORMASI BERDASARKAN INPUT USER
try: # COBA FUNGSI
    F = eval(f"lambda {variabel}: [{ekspresi}]") # -> "lambda x,y: [2*x + y , x - y]"
except Exception as f: # HANDLING ERRORNYA
    print(f"Terjadi ERROR saat membuat fungsi: {f}")
    print("Pastikan variabel dan ekspresi Anda sudah benar.")
    exit() 

# --------------------------------------
# MEMBUAT DOMAIN LIST DARI VARIABEL KEMUDIAN SIMPAN DI DIMENSI
# --------------------------------------
# MEMBUAT DOMAIN
domain = [i for i in variabel.split(",")]
# PANJANG DOMAIN / DIMENSI
dimensi = len(domain)

# --------------------------------------
# MEMBUAT FUNGSI PENJUMLAHAN VEKTOR DAN PERKALIAN VEKTOR BERULANG
# --------------------------------------
# FUNGSI PENJUMLAHAN VEKTOR  BERULANG
def penjumlahan_vektor(u, v):
    return [u[i] + v[i] for i in range(len(u))] # -> u + v = (u1 ​+ v1​, u2​ + v2​,..., un ​+ vn​)
# FUNGSI PERKALIAN SKALAR BERULANG
def perkalian_skalar(k, u):
    return [k * u[i] for i in range(len(u))] # -> k ⋅ u = (k ⋅ u1 ​,k ⋅ u2​,..., k ⋅ un​)

# --------------------------------------
# MEMBUAT FUNGSI UNTUK MEMERIKSA APAKAH KEDUA KOMPENEN SAMA / HAMPIR SAMA, DENGAN TOLERANSI TERTENTU
# --------------------------------------
# FUNGSI UNTUK MEMERIKSA KESAMAAN DUA KOMPONEN DENGAN TOLERANSI
def kesamaan(u, v, toleransi = 1e-9):
    return all(abs(u[i] - v[i]) < toleransi for i in range(len(u))) # Jaga2 0.1 + 0.2 = 0.30000000000000004

# --------------------------------------
# FUNGSI UTAMA UNTUK MEMERIKSA APAKAH FUNGSI TRANSFORMASI LINEAR ATAU TIDAK
# --------------------------------------
# FUNGSI APAKAH LINEAR 
def apakah_linear(F, dimensi):
    # MEMBUAT VEKTOR DASAR UNTUK PENGUJIAN KE FUNGSI
    vektor_penguji = [
        [0] * dimensi, # -> [0, 0, 0, ..., 0]
        [1] * dimensi, # -> [1, 1, 1, ..., 1]
    ]
    
    # MEMBUAT VEKTOR BASIS SATUAN UNTUK TAMBAHAN VEKTOR UJI
    for i in range(dimensi):
        vektor_basis = [0] * dimensi
        vektor_basis[i] = 1 # -> i = 0 → vektor_basis = [1, 0, 0, ...]. i = 1 → vektor_basis = [0, 1, 0, ...] 
        vektor_penguji.append(vektor_basis) 

    # FUNGSI UNTUK PEMBUKTIAN SUATU FUNGSI TRANSOFRMASI LINEAR ATAU TIDAK 1
    # F(u+v) = F(u) + F(v)
    uji_penjumlahan = True
    for i in range(len(vektor_penguji)):
        for x in range(len(vektor_penguji)):
            u = vektor_penguji[i]
            v = vektor_penguji[x]
            if not kesamaan(F(*penjumlahan_vektor(u, v)), penjumlahan_vektor(F(*u), F(*v))):
                uji_penjumlahan = False
                break
        if not uji_penjumlahan:
            break
    
    # FUNGSI UNTUK PEMBUKTIAN SUATU FUNGSI TRANSFORMASI LINEAR ATAU TIDAK 2
    # F(ku) = kF(u) 
    uji_perkalian = True
    uji_skalar = [0, 1, 2, 3, -1, -2, 0.2, 0.5] 
    for k in uji_skalar:
        for u in vektor_penguji:
            if not kesamaan(F(*perkalian_skalar(k, u)), perkalian_skalar(k, F(*u))):
                uji_perkalian = False
                break
        if not uji_perkalian:
            break   

    # PENENTU AKHIR
    if uji_penjumlahan and uji_perkalian:
        return "Merupakan Fungsi Transformasi Linear!"
    else:
        return "Bukan Merupakan Fungsi Transformasi Linear!"
    

# --------------------------------------
# UJI FUNGSI
# --------------------------------------
print(apakah_linear(F, dimensi))