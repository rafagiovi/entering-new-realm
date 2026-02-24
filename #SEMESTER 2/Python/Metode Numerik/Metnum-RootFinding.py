import matplotlib.pyplot as plt
import numpy as np

# Definisi fungsi
def f(x):
    return 3*x - np.exp(x)

# METODE TERUTUTUP
# 1. Metode Biseksi
def input_biseksi():
    print("======METODE BISEKSI======")
    xb1 = float(input("Masukan tebakan akar 1:"))
    xb2 = float(input("Masukan tebakan akar 2:"))
    print(biseksi(xb1, xb2))

def biseksi(a, b, n = 0):
    e = 1e-6
    c = (a+b)/2
    if abs(f(c)) < e:
        return (f"Akar-akar: {c}\nIterasi: {n}")
    else:
        if f(a) * f(b) > 0: 
            print("input tidak valid")
            return input_biseksi()
        if f(a) * f(c) < 0:
            return biseksi(a,c, n + 1)
        else:
            return biseksi(c,b, n + 1)
        
# 2. Metode Regula Falsi
def input_regulafalsi():
    print("======METODE REGULA FALSI======")
    xrf1 = float(input("Masukan tebakan akar 1:"))
    xrf2 = float(input("Masukan tebakan akar 2:"))
    print(regula_falsi(xrf1, xrf2))

def regula_falsi(a, b, n = 0):
    n_max = 100
    if n > n_max:
        return f"Gagal konvergen setelah {n_max} iterasi."
    e = 1e-6
    c = b - ((f(b) *(b -a))/(f(b) - f(a)))
    if abs(f(c)) < e:
        return (f"Akar-akar: {c}\nIterasi: {n}")
    else:
        if f(a) * f(b) > 0: 
            print("input tidak valid")
            return input_regulafalsi()
        if f(a) * f(c) < 0:
            return regula_falsi(a,c, n + 1)
        else:
            return regula_falsi(c,b, n + 1)

# METODE TERBUKA
# 1. Newton Raphson
def input_newtonraphson():
    print("======METODE NEWTON RAPHSON======")
    xnr = float(input("Masukan tebakan akar 1:"))
    print(newton_raphson(xnr))

def newton_raphson(a, n=0):
    e = 1e-6
    h = 1e-8
    f_prime = (f(a+h) - f(a))/h
    c = a - (f(a)/f_prime)
    if abs(f(c)) < e:
        return (f"Akar-akar: {c}\nIterasi: {n}")
    else:
        return newton_raphson(c, n+1)

# 2. Secant
def input_secant():
    print("======METODE SECANT======")
    xs1 = float(input("Masukan tebakan akar 1:"))
    xs2 = float(input("Masukan tebakan akar 2:"))
    print(secant(xs1, xs2))

def secant(a, b, n = 0):
    e = 1e-6
    c = b - ((f(b) *(b -a))/(f(b) - f(a)))
    if abs(f(c)) < e:
        return (f"Akar-akar: {c}\nIterasi: {n}")
    else:
        return secant(b, c, n + 1)


input_biseksi()
input_regulafalsi()
input_newtonraphson()
input_secant()

# Membuat data grafik
x = np.linspace(-1, 2, 100) # Membuat 100 titik dari -1 sampai 2
y = f(x)

# Plotting
plt.plot(x, y, label='f(x) = 3x - e^x')
plt.axhline(0, color='red', linestyle='--') # Garis sumbu X (y=0)
plt.grid(True)
plt.legend()
plt.show()


