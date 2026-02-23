# Muhammad Rafa Giovi Pradana
# 24060125130114

# definisi dan spesifikasi

#   Fungsi P(a, b) adalah fungsi rekursif yang menghitung pangkat (a^n) dengan cara mengalikan a sebanyak b kali hingga b bernilai 0.

def P(a,b):
    if b == 0:
        return 1
    else:
        return a*(P(a,b-1))
    
print(P(5,6))
print(P(3,3))