import matplotlib.pyplot as plt
import numpy as np

# --- Grafik Visualisasi Konvergensi Gabungan (Skala Logaritmik Error) ---
def visualisasi(hist_biseksi, hist_regula, hist_newton, hist_secant, judul_fungsi, fg):
    plt.figure(figsize=(10, 6))
    
    # Fungsi pembantu untuk mengubah nilai akar (c) menjadi nilai error absolut |f(c)|
    def hitung_error(history):
        return [abs(fg(c)) for c in history]

    # Plotting error dengan skala logaritmik
    if hist_biseksi:
        err_biseksi = hitung_error(hist_biseksi)
        plt.plot(range(len(err_biseksi)), err_biseksi, marker='o', linestyle='-', label='Biseksi', color='blue', alpha=0.6)
        plt.scatter(len(err_biseksi)-1, err_biseksi[-1], color='blue', s=200, marker='*', zorder=5)
        
    if hist_regula:
        err_regula = hitung_error(hist_regula)
        plt.plot(range(len(err_regula)), err_regula, marker='s', linestyle='--', label='Regula Falsi', color='orange', alpha=0.8)
        plt.scatter(len(err_regula)-1, err_regula[-1], color='orange', s=200, marker='*', zorder=5)

    if hist_newton:
        err_newton = hitung_error(hist_newton)
        plt.plot(range(len(err_newton)), err_newton, marker='^', linestyle='-.', label='Newton-Raphson', color='green', alpha=0.9)
        plt.scatter(len(err_newton)-1, err_newton[-1], color='green', s=200, marker='*', zorder=5)

    if hist_secant:
        err_secant = hitung_error(hist_secant)
        plt.plot(range(len(err_secant)), err_secant, marker='d', linestyle=':', label='Secant', color='red', alpha=0.9)
        plt.scatter(len(err_secant)-1, err_secant[-1], color='red', s=200, marker='*', zorder=5)
        
    plt.scatter([], [], color='black', s=150, marker='*', label='Titik Berhenti (Memenuhi Toleransi)')
        
    plt.title(f'Grafik Laju Konvergensi Error\n({judul_fungsi})')
    plt.xlabel('Iterasi ke-')
    plt.ylabel('Error Absolut |f(c)|')
    
    # MENGUBAH SUMBU Y MENJADI SKALA LOGARITMIK (10^-1, 10^-2, dst)
    plt.yscale('log') 
    
    # Menambahkan garis batas toleransi error (1e-6)
    plt.axhline(1e-6, color='black', linestyle='-', alpha=0.3, label='Batas Toleransi (10^-6)')
    
    plt.grid(True, which="both", linestyle=':', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Definisi fungsi objektif yang akan dicari nilai akarnya (titik potong terhadap sumbu x)
def f(x):
    return 3*x - np.exp(x)

def g(x):
    return np.exp(x) - x**2 + 3*x - 2

def biseksi(a, b, fg, n=0, history=None):
    if history is None:
        history = []
        
    e = 1e-6 
    c = (a+b)/2 
    history.append(c) 
    
    if abs(fg(c)) < e:
        return (f"Akar-akar: {c}\nIterasi: {n}")
    else:
        if fg(a) * fg(b) > 0: 
            return "Input Tidak Valid" 
        
        if fg(a) * fg(c) < 0:
            return biseksi(a, c, fg, n + 1, history)
        else:
            return biseksi(c, b, fg, n + 1, history)
        
def regula_falsi(a, b, fg, n=0, history=None):
    if history is None:
        history = []
        
    n_max = 100 
    if n > n_max:
        return f"Gagal konvergen setelah {n_max} iterasi."
    
    e = 1e-6 
    c = b - ((fg(b) * (b - a)) / (fg(b) - fg(a)))
    history.append(c)
    
    if abs(fg(c)) < e:
        return (f"Akar-akar: {c}\nIterasi: {n}")
    else:
        if fg(a) * fg(b) > 0: 
            return "Input Tidak Valid"
            
        if fg(a) * fg(c) < 0:
            return regula_falsi(a, c, fg, n + 1, history)
        else:
            return regula_falsi(c, b, fg, n + 1, history)
        
def newton_raphson(a, fg, n=0, history=None):
    if history is None:
        history = []
        
    n_max = 100 
    if n > n_max:
        return f"Gagal konvergen setelah {n_max} iterasi."
    
    e = 1e-6 
    h = 1e-8 
    
    f_prime = (fg(a+h) - fg(a))/h
    
    c = a - (fg(a)/f_prime)
    history.append(c)
    
    if abs(fg(c)) < e:
        return (f"Akar-akar: {c}\nIterasi: {n}")
    else:
        return newton_raphson(c, fg, n+1, history)

def secant(a, b, fg, n=0, history=None):
    if history is None:
        history = []
        
    n_max = 100 
    if n > n_max:
        return f"Gagal konvergen setelah {n_max} iterasi."
    
    e = 1e-6 
    c = b - ((fg(b) * (b - a)) / (fg(b) - fg(a)))
    history.append(c)
    
    if abs(fg(c)) < e:
        return (f"Akar-akar: {c}\nIterasi: {n}")
    else:
        return secant(b, c, fg, n + 1, history)
    
def eksekusi_program():
    a = 0
    b = 1
    
    # --- Analisis dan visualisasi untuk fungsi f(x) ---
    hist_bis_f, hist_reg_f, hist_new_f, hist_sec_f = [], [], [], []
    
    print("=== Hasil untuk f(x) ===")
    print("Biseksi:\n", biseksi(a, b, f, 0, hist_bis_f))
    print("\nRegula Falsi:\n", regula_falsi(a, b, f, 0, hist_reg_f))
    print("\nNewton-Raphson:\n", newton_raphson(b, f, 0, hist_new_f)) 
    print("\nSecant:\n", secant(a, b, f, 0, hist_sec_f))
    
    # Menambahkan argumen fungsi f agar bisa dihitung error-nya di visualisasi
    visualisasi(hist_bis_f, hist_reg_f, hist_new_f, hist_sec_f, "f(x) = 3x - e^x", f)

    # --- Analisis dan visualisasi untuk fungsi g(x) ---
    hist_bis_g, hist_reg_g, hist_new_g, hist_sec_g = [], [], [], []
    
    print("\n=== Hasil untuk g(x) ===")
    print("Biseksi:\n", biseksi(a, b, g, 0, hist_bis_g))
    print("\nRegula Falsi:\n", regula_falsi(a, b, g, 0, hist_reg_g))
    print("\nNewton-Raphson:\n", newton_raphson(b, g, 0, hist_new_g))
    print("\nSecant:\n", secant(a, b, g, 0, hist_sec_g))
    
    # Menambahkan argumen fungsi g agar bisa dihitung error-nya di visualisasi
    visualisasi(hist_bis_g, hist_reg_g, hist_new_g, hist_sec_g, "g(x) = e^x - x^2 + 3x - 2", g)

# Jalankan kode
eksekusi_program()