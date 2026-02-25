import numpy as np
import matplotlib.pyplot as plt
import time
import pandas as pd

# =========================================================
# DEFINISI FUNGSI
# =========================================================
def f(x):
    return 3*x - np.exp(x)

# =========================================================
# VISUALISASI FUNGSI
# =========================================================
x = np.linspace(0, 1, 400)
plt.figure()
plt.plot(x, f(x))
plt.axhline(0)
plt.title("Grafik f(x) = 3x - e^x")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()

# =========================================================
# METODE BISEKSI
# =========================================================
def biseksi(a, b, tol=1e-6, max_iter=100):
    start = time.time()

    data = []
    eval_count = 0

    if f(a)*f(b) >= 0:
        print("Interval tidak valid!")
        return None

    for i in range(max_iter):
        c = (a+b)/2
        fc = f(c)
        eval_count += 1

        error = abs(fc)
        data.append([i+1, a, b, c, fc, error])

        if error < tol:
            break

        if f(a)*fc < 0:
            b = c
        else:
            a = c

    runtime = time.time() - start

    df = pd.DataFrame(data, columns=[
        "Iterasi", "a", "b", "c", "f(c)", "Error"
    ])

    print("\n========== HASIL METODE BISEKSI ==========")
    print(df)
    print("\nRingkasan:")
    print("Akar              =", c)
    print("Jumlah Iterasi    =", len(df))
    print("Evaluasi Fungsi   =", eval_count)
    print("Waktu Komputasi   =", runtime, "detik")

    return df, eval_count, runtime