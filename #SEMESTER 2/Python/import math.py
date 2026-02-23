import math

# 1. Fungsi bantuan untuk menghitung suku Binomium
def hitung_suku_binomium(x, n):
    # Rumus: (-1)^n * (2x)^n
    # n=0 -> 1, n=1 -> -2x, n=2 -> 4x^2, dst.
    return ((-1)**n) * ((2 * x)**n)

# --- BAGIAN INPUT ---
print("=== PROGRAM ANALISIS GALAT BINOMIUM f(x)=1/(1+2x) ===")
x_input = float(input("masukan nilai x (range: -0.5 < x < 0.5) : "))
n_input = int(input("pemotongan suku ke-n (n)                : "))

# --- PROSES PERHITUNGAN ---
# Nilai eksak menggunakan rumus asli pembagian
nilai_eksak = 1 / (1 + 2 * x_input)
total_hampiran = 0

print("\n--- Proses Perhitungan Suku ---")
for i in range(n_input):
    suku = hitung_suku_binomium(x_input, i)
    total_hampiran += suku
    print(f"Suku ke-{i+1:<2} : {suku:+.15f}")

#Menghitung Galat Truncation (Akibat berhenti di suku ke-n)
galat_truncation = abs(nilai_eksak - total_hampiran)

#Menghitung Galat Round-off (Estimasi gangguan memori komputer)
#Menggunakan Machine Epsilon standar (sekitar 1e-16)
galat_round_off = abs(total_hampiran * 1e-16)

# --- OUTPUT HASIL ---
print("-" * 55)
print(f"Nilai Eksak (1/(1+2x))   : {nilai_eksak:.18f}")
print(f"Total Hampiran Deret     : {total_hampiran:.18f}")
print("-" * 55) #untuk pembatas ajah
print(f"GALAT TRUNCATION         : {galat_truncation:.10e}")
print(f"GALAT ROUND-OFF          : {galat_round_off:.10e}")
print("-" * 55)