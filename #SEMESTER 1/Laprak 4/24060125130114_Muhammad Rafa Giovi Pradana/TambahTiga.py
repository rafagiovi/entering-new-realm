# Muhammad Rafa Giovi Pradana
# 24060125130114

# definisi dan spesifikasi

#   Fungsi TG(n) adalah fungsi rekursif yang menghasilkan deret kelipatan tiga, yaitu menghitung 3 * n.

def TG(n):
    if n==0:
        return 0
    else:
        return 3 + TG(n-1)
    
print(TG(50))