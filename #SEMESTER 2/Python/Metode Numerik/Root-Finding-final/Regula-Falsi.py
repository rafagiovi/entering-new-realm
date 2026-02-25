import matplotlib.pyplot as plt
import numpy as np

# Definisi fungsi objektif yang akan dicari nilai akarnya (titik potong terhadap sumbu x)
# Persamaan: f(x) = 3x - e^x
def f(x):
    return 3*x - np.exp(x)
# Persamaan: f(x) = e^x - x^2 + 3*x - 2
def g(x):
    return np.exp(x) - x**2 + 3*x - 2


# Visualisasi grafik fungsi dan grafik konvergen

def visualisasi(history, akar_akhir, fg):
    # Membuat figure dengan 2 subplot (grafik fungsi dan grafik konvergensi)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # --- Grafik 1: Visualisasi Fungsi f(x) ---
    # Menentukan rentang x untuk grafik (di sekitar akar yang ditemukan)
    x_range = np.linspace(akar_akhir - 2, akar_akhir + 2, 400)
    y_range = fg(x_range)
    
    ax1.plot(x_range, y_range, label='Fungsi yang Diuji', color='blue')
    ax1.axhline(0, color='black', linestyle='--', linewidth=1) 
    ax1.axvline(0, color='black', linestyle='--', linewidth=1)
    ax1.scatter(akar_akhir, fg(akar_akhir), color='red', zorder=5, label=f'Akar: {akar_akhir:.4f}')
    ax1.set_ylim(-2, 1) 
    ax1.set_title('Grafik Fungsi')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.grid(True, linestyle=':', alpha=0.6)
    ax1.legend()

    # --- Grafik 2: Visualisasi Konvergensi ---
    ax2.plot(range(len(history)), history, marker='o', linestyle='-', color='green')
    ax2.axhline(akar_akhir, color='red', linestyle='--', alpha=0.5, label='Nilai Konvergen')
    ax2.set_title('Grafik Konvergensi (Metode Biseksi)')
    ax2.set_xlabel('Iterasi ke-')
    ax2.set_ylabel('Estimasi Akar (c)')
    ax2.grid(True, linestyle=':', alpha=0.6)
    ax2.legend()

    plt.tight_layout()
    plt.show()

# =====================================================================
# KODE 
# =====================================================================

# 2. Metode Regula Falsi
# Mirip biseksi, namun titik potong baru dihitung menggunakan interpolasi linear (garis lurus) antara f(a) dan f(b).

def input_regulafalsi():
    print("======METODE REGULA FALSI======")
    print("Pilih Fungsi yang akan diujikan:")
    print("1. f(x) = 3x - e^x")
    print("2. f(x) = e^x - x^2 + 3*x - 2")
    fg = int(input(">>> "))
    # Meminta pengguna memasukkan dua batas interval
    print("Tebakan akar antara 0 ≤ x ≤ 1 (Berdasarkan tugas)")
    xrf1 = float(input("Masukan tebakan akar 1: "))
    xrf2 = float(input("Masukan tebakan akar 2: "))
    print("=========== LOG ITERASI ==========")
    if fg == 1:
        fg = f
    else:
        fg = g

    regula_falsi(xrf1, xrf2, fg)

def regula_falsi(a, b, fg, n = 0, history = None):
    if history is None:
        history = [] # Inisialisasi list history pada iterasi awal

    n_max = 100 # Batas maksimal iterasi untuk mencegah rekursi tak terbatas (infinite loop)
    if n > n_max:
        return f"Gagal konvergen setelah {n_max} iterasi."
    
    e = 1e-6 # Toleransi error
    # Menghitung titik c menggunakan rumus Regula Falsi
    c = b - ((fg(b) *(b -a))/(fg(b) - fg(a)))

    history.append(c)
    
    # Kriteria berhenti
    if abs(fg(c)) < e:
        print(f"Akar-akar: {c}\nIterasi: {n}")
        return visualisasi(history, c, fg)
    else:
        # Pengecekan apakah akar terkurung
        if fg(a) * fg(b) > 0: 
            print("input tidak valid")
            return input_regulafalsi()
            
        # Mempersempit interval
        if fg(a) * fg(c) < 0:
            print(f"Iterasi ke-{n}: {c}")
            return regula_falsi(a,c,fg, n + 1, history)
        else:
            print(f"Iterasi ke-{n}: {c}")
            return regula_falsi(c,b,fg, n + 1, history)
        

input_regulafalsi()