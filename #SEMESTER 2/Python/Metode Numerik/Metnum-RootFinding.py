import matplotlib.pyplot as plt
import numpy as np

# Definisi fungsi objektif yang akan dicari nilai akarnya (titik potong terhadap sumbu x)
# Persamaan: f(x) = 3x - e^x
def f(x):
    return 3*x - np.exp(x)

# =====================================================================
# METODE TERTUTUP
# Metode yang membutuhkan dua tebakan awal yang harus mengurung akar.
# =====================================================================

# 1. Metode Biseksi
# Mencari akar dengan cara membagi dua interval tebakan awal secara berulang.
def input_biseksi():
    print("======METODE BISEKSI======")
    # Meminta pengguna memasukkan dua batas interval
    xb1 = float(input("Masukan tebakan akar 1:"))
    xb2 = float(input("Masukan tebakan akar 2:"))
    print(biseksi(xb1, xb2))

def biseksi(a, b, n = 0):
    e = 1e-6 # Toleransi error untuk kriteria berhenti (mendekati nol)
    c = (a+b)/2 # Menghitung titik tengah (nilai akar perkiraan)
    
    # Jika nilai fungsi pada c sudah lebih kecil dari toleransi (sudah sangat dekat dengan 0)
    if abs(f(c)) < e:
        return (f"Akar-akar: {c}\nIterasi: {n}")
    else:
        # Jika tanda f(a) dan f(b) sama, berarti interval tidak mengurung akar
        if f(a) * f(b) > 0: 
            print("input tidak valid")
            return input_biseksi() # Meminta input ulang
        
        # Mengecek di sub-interval mana akar berada
        if f(a) * f(c) < 0:
            # Akar berada di antara a dan c
            return biseksi(a,c, n + 1)
        else:
            # Akar berada di antara c dan b
            return biseksi(c,b, n + 1)
        
# 2. Metode Regula Falsi
# Mirip biseksi, namun titik potong baru dihitung menggunakan interpolasi linear (garis lurus) antara f(a) dan f(b).
def input_regulafalsi():
    print("======METODE REGULA FALSI======")
    xrf1 = float(input("Masukan tebakan akar 1:"))
    xrf2 = float(input("Masukan tebakan akar 2:"))
    print(regula_falsi(xrf1, xrf2))

def regula_falsi(a, b, n = 0):
    n_max = 100 # Batas maksimal iterasi untuk mencegah rekursi tak terbatas (infinite loop)
    if n > n_max:
        return f"Gagal konvergen setelah {n_max} iterasi."
    
    e = 1e-6 # Toleransi error
    # Menghitung titik c menggunakan rumus Regula Falsi
    c = b - ((f(b) *(b -a))/(f(b) - f(a)))
    
    # Kriteria berhenti
    if abs(f(c)) < e:
        return (f"Akar-akar: {c}\nIterasi: {n}")
    else:
        # Pengecekan apakah akar terkurung
        if f(a) * f(b) > 0: 
            print("input tidak valid")
            return input_regulafalsi()
            
        # Mempersempit interval
        if f(a) * f(c) < 0:
            return regula_falsi(a,c, n + 1)
        else:
            return regula_falsi(c,b, n + 1)

# =====================================================================
# METODE TERBUKA
# Metode yang bisa dimulai dari satu atau dua tebakan awal tanpa harus mengurung akar, 
# konvergensi lebih cepat tapi memiliki risiko divergen (tidak menemukan akar).
# =====================================================================

# 1. Newton Raphson
# Memanfaatkan nilai turunan pertama fungsi (gradien) untuk mencari titik potong sumbu x selanjutnya.
def input_newtonraphson():
    print("======METODE NEWTON RAPHSON======")
    # Hanya membutuhkan satu nilai tebakan awal
    xnr = float(input("Masukan tebakan akar 1:"))
    print(newton_raphson(xnr))

def newton_raphson(a, n=0):
    n_max = 100 # Batas maksimal iterasi untuk mencegah rekursi tak terbatas (infinite loop)
    if n > n_max:
        return f"Gagal konvergen setelah {n_max} iterasi."
    
    e = 1e-6 # Toleransi error
    h = 1e-8 # Nilai h untuk pendekatan numerik turunan pertama
    
    # Mencari nilai turunan f'(a)
    f_prime = (f(a+h) - f(a))/h
    
    # Mencari nilai x baru menggunakan rumus iterasi Newton-Raphson: x1 = x0 - (f(x0)/f'(x0))
    c = a - (f(a)/f_prime)
    
    # Kriteria berhenti
    if abs(f(c)) < e:
        return (f"Akar-akar: {c}\nIterasi: {n}")
    else:
        # Melanjutkan iterasi dengan tebakan akar yang baru (c)
        return newton_raphson(c, n+1)

# 2. Secant
# Modifikasi dari Newton Raphson, di mana turunan pertama didekati menggunakan garis potong (secant line) dari dua titik sebelumnya.
def input_secant():
    print("======METODE SECANT======")
    # Membutuhkan dua nilai tebakan awal (tidak harus mengurung akar)
    xs1 = float(input("Masukan tebakan akar 1:"))
    xs2 = float(input("Masukan tebakan akar 2:"))
    print(secant(xs1, xs2))

def secant(a, b, n = 0):
    n_max = 100 # Batas maksimal iterasi untuk mencegah rekursi tak terbatas (infinite loop)
    if n > n_max:
        return f"Gagal konvergen setelah {n_max} iterasi."
    
    e = 1e-6 # Toleransi error
    # Menghitung x baru menggunakan rumus Secant
    c = b - ((f(b) *(b -a))/(f(b) - f(a)))
    
    # Kriteria berhenti
    if abs(f(c)) < e:
        return (f"Akar-akar: {c}\nIterasi: {n}")
    else:
        # Melanjutkan iterasi dengan dua titik terakhir: b dan c
        return secant(b, c, n + 1)

# =====================================================================
# BLOK EKSEKUSI DAN PLOTTING GRAFIK
# =====================================================================

# Memanggil fungsi antarmuka (input) untuk setiap metode
input_biseksi()
input_regulafalsi()
input_newtonraphson()
input_secant()

# Membuat rentang data sumbu x untuk menampilkan grafik fungsi
x = np.linspace(-1, 2, 100) # Membuat array berisi 100 titik berjarak sama dari x = -1 hingga x = 2
y = f(x) # Menghitung nilai sumbu y untuk setiap titik x

# Menampilkan grafik menggunakan Matplotlib
plt.plot(x, y, label='f(x) = 3x - e^x') # Menggambar kurva persamaan
plt.axhline(0, color='red', linestyle='--') # Membuat garis referensi horizontal pada sumbu X (y=0) tempat akar berada
plt.grid(True) # Menampilkan garis kisi-kisi grafik
plt.legend() # Menampilkan legenda (keterangan label kurva)
plt.show() # Menampilkan jendela grafik ke layar