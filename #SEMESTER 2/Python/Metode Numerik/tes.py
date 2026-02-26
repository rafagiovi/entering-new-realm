import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time

# =========================================================
# DEFINISI FUNGSI DAN TURUNAN
# =========================================================
def f(x):
    return np.exp(x) - x**2 + 3*x - 2

def df(x):
    return np.exp(x) - 2*x + 3

# =========================================================
# VISUALISASI FUNGSI
# =========================================================
x_plot = np.linspace(0,1,400)
plt.figure()
plt.plot(x_plot, f(x_plot))
plt.axhline(0)
plt.title("Grafik f(x) = e^x - x^2 + 3x - 2")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()

# =========================================================
# METODE NEWTON-RAPHSON
# =========================================================
def newton_raphson(x0, tol=1e-6, max_iter=100):
    start = time.time()

    data = []
    eval_f = 0
    eval_df = 0
    x = x0

    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        eval_f += 1
        eval_df += 1

        if dfx == 0:
            print("Turunan nol! Metode gagal.")
            break

        error = abs(fx)
        data.append([i+1, x, fx, dfx, error])

        if error < tol:
            break

        x = x - fx/dfx

    end = time.time()
    runtime = end - start

    df_result = pd.DataFrame(data, columns=[
        "Iterasi", "x", "f(x)", "f'(x)", "Error"
    ])

    print("\n========== HASIL NEWTON-RAPHSON ==========")
    print(df_result)
    print("\nRingkasan:")
    print("Akar              =", x)
    print("Jumlah Iterasi    =", len(df_result))
    print("Evaluasi f(x)     =", eval_f)
    print("Evaluasi f'(x)    =", eval_df)
    print("Waktu Komputasi   =", runtime, "detik")

    return df_result, eval_f, eval_df, runtime


# =========================================================
# METODE SECANT
# =========================================================
def secant(x0, x1, tol=1e-6, max_iter=100):
    start = time.time()

    data = []
    eval_f = 0

    for i in range(max_iter):
        f0 = f(x0)
        f1 = f(x1)
        eval_f += 2

        if (f1 - f0) == 0:
            print("Pembagi nol! Metode gagal.")
            break

        error = abs(f1)
        data.append([i+1, x1, f1, error])

        if error < tol:
            break

        x2 = x1 - f1*(x1-x0)/(f1-f0)
        x0 = x1
        x1 = x2

    end = time.time()
    runtime = end - start

    df_result = pd.DataFrame(data, columns=[
        "Iterasi", "x", "f(x)", "Error"
    ])

    print("\n========== HASIL SECANT ==========")
    print(df_result)
    print("\nRingkasan:")
    print("Akar              =", x1)
    print("Jumlah Iterasi    =", len(df_result))
    print("Evaluasi f(x)     =", eval_f)
    print("Waktu Komputasi   =", runtime, "detik")

    return df_result, eval_f, runtime


# =========================================================
# JALANKAN METODE
# =========================================================
df_newton, eval_f_newton, eval_df_newton, time_newton = newton_raphson(0.5)
df_secant, eval_f_secant, time_secant = secant(0, 1)


# =========================================================
# GRAFIK PERBANDINGAN KONVERGENSI
# =========================================================
plt.figure()
plt.plot(df_newton["Iterasi"], df_newton["Error"], marker='o', label="Newton-Raphson")
plt.plot(df_secant["Iterasi"], df_secant["Error"], marker='s', label="Secant")
plt.yscale("log")
plt.title("Perbandingan Kurva Konvergensi")
plt.xlabel("Iterasi")
plt.ylabel("Error (log scale)")
plt.legend()
plt.grid()
plt.show()


# =========================================================
# PERBANDINGAN KINERJA METODE
# =========================================================
print("\n================ PERBANDINGAN METODE ================")
print("Metode            | Iterasi | Eval f(x) | Eval f'(x) | Waktu (detik)")
print("---------------------------------------------------------------------")
print(f"Newton-Raphson    | {len(df_newton):^7d} | {eval_f_newton:^9d} | {eval_df_newton:^10d} | {time_newton:.6f}")
print(f"Secant            | {len(df_secant):^7d} | {eval_f_secant:^9d} | {'-':^10} | {time_secant:.6f}")
print("=====================================================================")