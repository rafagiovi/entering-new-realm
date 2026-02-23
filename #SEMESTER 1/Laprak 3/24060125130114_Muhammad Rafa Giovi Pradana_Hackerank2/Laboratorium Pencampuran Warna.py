# Nama: 
# NIM/Lab: 
# Nama Program: Simulasi Pencampuran Warna RGB

type RGB = tuple[int, int, int]

# Konstruktor: MakeWarna(r, g, b)
def MakeWarna(r, g, b):
    return (r, g, b)

# Selektor
def Red(W):
    return W[0]

def Green(W):
    return W[1]

def Blue(W):
    return W[2]

# Operator
def Mix(W1, W2):
    r = (Red(W1) + Red(W2)) // 2
    g = (Green(W1) + Green(W2)) // 2
    b = (Blue(W1) + Blue(W2)) // 2
    return MakeWarna(r, g, b)

# Predikat
def IsGray(W):
    return Red(W) == Green(W) == Blue(W)

# Fungsi Analisis
def DominantChannel(W):
    r, g, b = Red(W), Green(W), Blue(W)
    if r >= g and r >= b:
        return "Dominan Merah"
    elif g >= r and g >= b:
        return "Dominan Hijau"
    else:
        return "Dominan Biru"

# Fungsi untuk memproses dan menampilkan hasil
def process(r1, g1, b1, r2, g2, b2):
    # Validasi input
    if not all(0 <= val <= 255 for val in [r1, g1, b1, r2, g2, b2]):
        print("Input tidak valid")
        return

    W1 = MakeWarna(r1, g1, b1)
    W2 = MakeWarna(r2, g2, b2)
    Wmix = Mix(W1, W2)

    print(f"{Red(Wmix)} {Green(Wmix)} {Blue(Wmix)}")
    if IsGray(Wmix):
        print("Abu-abu")
    else:
        print(DominantChannel(Wmix))

# JANGAN DIHAPUS
data = list(map(int, input().split()))
process(data[0], data[1], data[2], data[3], data[4], data[5])