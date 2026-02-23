import math # Mengimpor modul matematika bawaan Python
# y = ln(x)

def ln(): # Fungsi untuk mencari galat dari ln(x) dengan Deret Taylor dan Maclaurin
    
    # --- INPUT VARIABEL ---
    x = 0.2 # float(input("Masukan input x :"))             # Meminta input nilai x yang akan dicari logaritmanya (batas konvergensi 0 < x <= 2)
    n = 5 # int(input("Masukan Pemotongan suku ke-n:"))     # Meminta jumlah iterasi pemotongan (truncation) suku ke-n
    a = math.log(x)                                         # a: Menyimpan nilai eksak (sebenarnya) dari ln(x) menggunakan fungsi bawaan Python
    
    print("\n==================================================")
    print("URAIAN OPERASI DERET TAYLOR")
    print("==================================================")
    a_hat = 0 # a_hat: Variabel untuk menyimpan nilai total perkiraan Deret Taylor
    
    # --- PROSES DERET TAYLOR ---
    for i in range(n): # Looping sebanyak n kali 
        p = i+1 # p: Penunjuk orde/suku ke- 
        s = ((-(x-1))**p)/-p  # s: Rumus per suku Taylor
        a_hat += s # Menambahkan nilai suku saat ini (s) ke total sementara (a_hat)
        
        print(f"Suku ke-{p}: ((-({x}-1))^{p}) / -{p} = {s:.6f} | Total Sementara: {a_hat:.6f}") # Mencetak proses tiap suku
        
    print("\n==================================================")
    print("URAIAN OPERASI DERET MACLAURIN")
    print("==================================================")
    
    # --- PROSES DERET MACLAURIN ---
    y = x-1 # y: Substitusi x-1 untuk menyesuaikan Deret Maclaurin ln(1+x) agar ekuivalen mencari ln(x)
    a2_hat = 0 # a2_hat: Variabel untuk menyimpan nilai total perkiraan Deret Maclaurin
    
    for o in range(n): # Looping sebanyak n kali
        pp = o+1 # pp: Penunjuk orde/suku ke- 
        sd = ((-y)**pp)/(-pp) # sd: Rumus per suku Maclaurin. Menggunakan variabel substitusi y
        a2_hat += sd # Menambahkan nilai suku saat ini (sd) ke total sementara (a2_hat)
        
        print(f"Suku ke-{pp}: ((-{y})^{pp}) / -{pp} = {sd:.6f} | Total Sementara: {a2_hat:.6f}") # Mencetak proses tiap suku

    print("\n==================================================")
    print("HASIL AKHIR & ANALISIS GALAT - DERET TAYLOR")
    print("==================================================")
    
    # --- ANALISIS GALAT TAYLOR ---
    G_Absolut = abs(a - a_hat) # G_Absolut: Menghitung selisih positif antara nilai eksak (a) dan perkiraan (a_hat)
    G_Relatif = G_Absolut/a # G_Relatif: Menghitung rasio galat absolut terhadap nilai eksak
    G_Persentase = G_Relatif * 100 # G_Persentase: Mengubah galat relatif menjadi bentuk persen
    
    print("Nilai Eksak           :", a) # Menampilkan nilai bawaan math.log
    print("Nilai Perkiraan       :", round(a_hat,n+1)) # Menampilkan hasil aproksimasi, dibulatkan n+1 desimal
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
    G_Relatif2 = G_Absolut2/a # G_Relatif2: Menghitung rasio galat absolut terhadap nilai eksak
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
ln()