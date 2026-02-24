import matplotlib.pyplot as plt
import numpy as np

# Definisi fungsi
def f(x):
    return 3*x - np.exp(x)

# Metode Biseksi
def input_biseksi():
    xb1 = int(input("Masukan tebakan akar 1 (negatif):"))
    xb2 = int(input("Masukan tebakan akar 2 (positif):"))
    # n = int(input("Masukan Truncation:"))
    print(biseksi(xb1, xb2))

def biseksi(xb1, xb2, n = 0):
    e = 1e-6
    xr = (xb1+xb2)/2
    if abs(f(xr)) < e:
        return (f"Akar-akar: {xr}\nIterasi: {n}")
    else:
        if f(xb1) * f(xb2) > 0: 
            print("input tidak valid")
            return input_biseksi()
        if f(xb1) * f(xr) < 0:
            return biseksi(xb1,xr, n + 1)
        else:
            return biseksi(xr,xb2, n + 1)

input_biseksi()



# Membuat data grafik
x = np.linspace(-1, 2, 100) # Membuat 100 titik dari -1 sampai 2
y = f(x)

# Plotting
plt.plot(x, y, label='f(x) = 3x - e^x')
plt.axhline(0, color='red', linestyle='--') # Garis sumbu X (y=0)
plt.grid(True)
plt.legend()
plt.show()


