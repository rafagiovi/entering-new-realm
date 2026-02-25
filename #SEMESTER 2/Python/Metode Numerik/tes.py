import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

# Definisi fungsi objektif yang akan dicari nilai akarnya (titik potong terhadap sumbu x)
# Persamaan: f(x) = 3x - e^x
def f(x):
    return 3*x - np.exp(x)
# Persamaan: g(x) = e^x - x^2 + 3*x - 2
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

# 1. Metode Biseksi
# Mencari akar dengan cara membagi dua interval tebakan awal secara berulang.
def input_biseksi():
    print("========= METODE BISEKSI =========")
    # Meminta pengguna memasukkan dua batas interval
    print("Tebakan akar antara 0 ≤ x ≤ 1 (Berdasarkan tugas)")
    a = float(input("Masukan tebakan akar 1: "))
    b = float(input("Masukan tebakan akar 2: "))
    print()
    print("========= f(x) = 3x - e^x ========")
    print("=========== LOG ITERASI ==========")
    print(f"{'Iterasi':<8} | {'a':<10} | {'b':<10} | {'c':<10} | {'f(a)':<10} | {'f(b)':<10} | {'f(c)':<10}")
    print("-" * 86)
    biseksi(a, b, f)
    print()
    print("=== f(x) = e^x - x^2 + 3*x - 2 ===")
    print("=========== LOG ITERASI ==========")
    print(f"{'Iterasi':<8} | {'a':<10} | {'b':<10} | {'c':<10} | {'f(a)':<10} | {'f(b)':<10} | {'f(c)':<10}")
    print("-" * 86)
    biseksi(a, b, g)

# Menambahkan parameter eval_count dengan nilai default 0
def biseksi(a, b, fg, n = 0, history=None, eval_count=0):
    if history is None:
        history = [] # Inisialisasi list history pada iterasi awal

    e = 1e-6 # Toleransi error untuk kriteria berhenti (mendekati nol)
    c = (a+b)/2 # Menghitung titik tengah (nilai akar perkiraan)
    fc = fg(c)
    eval_count += 1 # Menghitung 1 evaluasi fungsi untuk fg(c)

    history.append(c)

    # Jika nilai fungsi pada c sudah lebih kecil dari toleransi (sudah sangat dekat dengan 0)
    if abs(fc) < e:
        akar_asli = fsolve(fg, a)[0]
        # 1. Menghitung Galat Sebenarnya
        galat = abs(akar_asli - c)

        # 2. Menghitung Galat Persentase
        galat_persentase = (galat / abs(akar_asli)) * 100

        print(f"{n:<8} | {a:<10.6f} | {b:<10.6f} | {c:<10.6f} | {fg(a):<10.6f} | {fg(b):<10.6f} | {fc:<10.6f}")
        print(f"========== HASIL AKHIR ==========")
        print(f"Akar-akar          : {c}")
        print(f"Akar Asli          : {akar_asli}")
        print(f"Galat Absolut      : {galat:.10f}")
        print(f"Galat Persentase   : {galat_persentase:.10f}%")
        print(f"Iterasi            : {n}")
        print(f"Evaluasi Fungsi    : {eval_count}") # Menampilkan total evaluasi fungsi

        return visualisasi(history, c, fg)
    else:
        eval_count += 2 # Menghitung 2 evaluasi fungsi untuk fg(a) dan fg(b) pada baris di bawah
        # Jika tanda f(a) dan f(b) sama, berarti interval tidak mengurung akar
        if fg(a) * fg(b) > 0:
            print("input tidak valid")
            return input_biseksi() # Meminta input ulang

        eval_count += 1 # Menghitung 1 evaluasi fungsi untuk fg(a) pada baris di bawah
        # Mengecek di sub-interval mana akar berada
        if fg(a) * fc < 0:
            # Akar berada di antara a dan c
            print(f"{n:<8} | {a:<10.6f} | {b:<10.6f} | {c:<10.6f} | {fg(a):<10.6f} | {fg(b):<10.6f} | {fc:<10.6f}")
            return biseksi(a,c, fg, n + 1, history, eval_count)
        else:
            # Akar berada di antara c dan b
            print(f"{n:<8} | {a:<10.6f} | {b:<10.6f} | {c:<10.6f} | {fg(a):<10.6f} | {fg(b):<10.6f} | {fc:<10.6f}")
            return biseksi(c,b, fg, n + 1, history, eval_count)

input_biseksi()