# Muhammad Rafa Giovi Pradana
# 24060125130114

# definisi dan spesifikasi
#  Fungsi B(a, b) adalah fungsi rekursif yang menghitung hasil B a / b dengan pengurangan berulang hingga a menjadi 0.

def B (a,b):
    if a == 0:
        return 0
    else:
        return 1 + (B (a-b,b))
    
print(B(80,10))