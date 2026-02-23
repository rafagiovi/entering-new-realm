# y = 1/(1-x)

def f(): # Fungsi untuk mencari galat dari 1/(1-x) dengan Deret Taylor dan Maclaurin
    
    # --- INPUT VARIABEL ---
    x = 0.2 # float(input("Masukan input x :"))             # Batas konvergensi deret ini adalah -1 < x < 1
    n = 5 # int(input("Masukan Pemotongan suku ke-n:"))     # Jumlah iterasi pemotongan suku ke-n
    a = 1 / (1 - x)                                         # a: Menyimpan nilai eksak dari 1/(1-x)
    
    print("\n==================================================")
    print("URAIAN OPERASI DERET TAYLOR (Pusat a=0)")
    print("==================================================")
    a_hat = 0 # a_hat: Variabel untuk menyimpan nilai total perkiraan Deret Taylor
    
    # --- PROSES DERET TAYLOR ---
    for i in range(n): # Looping sebanyak n kali 
        p = i # p: Pangkat dimulai dari 0 
        s = x**p  # s: Rumus per suku Taylor sangat sederhana, hanya x pangkat p
        a_hat += s # Menambahkan nilai suku saat ini (s) ke total sementara (a_hat)
        
        print(f"Suku ke-{p}: {x}^{p} = {s:.6f} | Total Sementara: {a_hat:.6f}") # Mencetak proses tiap suku
        
    print("\n==================================================")
    print("URAIAN OPERASI DERET MACLAURIN")
    print("==================================================")
    
    # --- PROSES DERET MACLAURIN ---
    # Untuk fungsi 1/(1-x), Deret Maclaurin sama persis dengan Deret Taylor di pusat a=0
    a2_hat = 0 # a2_hat: Variabel untuk menyimpan nilai total perkiraan Deret Maclaurin
    
    for o in range(n): # Looping sebanyak n kali
        pp = o # pp: Pangkat dimulai dari 0
        sd = x**pp # sd: Rumus per suku Maclaurin
        a2_hat += sd # Menambahkan nilai suku saat ini (sd) ke total sementara (a2_hat)
        
        print(f"Suku ke-{pp}: {x}^{pp} = {sd:.6f} | Total Sementara: {a2_hat:.6f}") # Mencetak proses tiap suku

    print("\n==================================================")
    print("HASIL AKHIR & ANALISIS GALAT - DERET TAYLOR")
    print("==================================================")
    
    # --- ANALISIS GALAT TAYLOR ---
    G_Absolut = abs(a - a_hat) # G_Absolut: Menghitung selisih positif antara nilai eksak (a) dan perkiraan (a_hat)
    G_Relatif = G_Absolut/abs(a) # G_Relatif: Menghitung rasio galat absolut terhadap nilai eksak
    G_Persentase = G_Relatif * 100 # G_Persentase: Mengubah galat relatif menjadi bentuk persen
    
    print("Nilai Eksak           :", a) 
    print("Nilai Perkiraan       :", round(a_hat,n+1)) 
    print()
    print("ANALISIS GALAT")
    print("Galat Absolut         :", G_Absolut)
    print("Galat Relatif         :", G_Relatif)
    print(f"Galat Persentase      : {G_Persentase}%")
    print()

    print("==================================================")
    print("HASIL AKHIR & ANALISIS GALAT - DERET MACLAURIN")
    print("==================================================")
    
    # --- ANALISIS GALAT MACLAURIN ---
    G_Absolut2 = abs(a - a2_hat) # G_Absolut2: Menghitung selisih positif nilai eksak (a) dan perkiraan Maclaurin (a2_hat)
    G_Relatif2 = G_Absolut2/abs(a) # G_Relatif2: Menghitung rasio galat absolut terhadap nilai eksak
    G_Persentase2 = G_Relatif2 * 100 # G_Persentase2: Mengubah galat relatif menjadi bentuk persen
    
    print("Nilai Eksak           :", a)
    print("Nilai Perkiraan       :", round(a2_hat,n+1))
    print()
    print("ANALISIS GALAT")
    print("Galat Absolut         :", G_Absolut2)
    print("Galat Relatif         :", G_Relatif2)
    print(f"Galat Persentase      : {G_Persentase2}%")
    print()

# Menjalankan fungsi utama
f()