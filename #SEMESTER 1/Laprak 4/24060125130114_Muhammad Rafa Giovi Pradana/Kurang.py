# Muhammad Rafa Giovi Pradana
# 24060125130114

# definisi dan spesifikasi
#   Fungsi K(a, b) adalah fungsi rekursif yang menghitung hasil pengurangan a - b dengan cara menambah atau mengurangi a dan b secara berulang hingga b menjadi 0.

def K(a,b):
    if b == 0:
        return a
    elif b > 0:
        return K(a-1,b-1)
    elif b < 0:
        return K(a+1,b+1)
print(K(12,-6))