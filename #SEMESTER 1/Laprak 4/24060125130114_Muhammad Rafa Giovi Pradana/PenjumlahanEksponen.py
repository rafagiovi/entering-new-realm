# Muhammad Rafa Giovi Pradana
# 24060125130114

# definisi dan spesifikasi

#   Fungsi PE(x) adalah fungsi rekursif yang menghitung jumlah kuadrat dari 1^2 sampai x^2.


def PE(x):
    if x==1:
        return 1
    else:
        return x*x + PE(x-1)
    
print(PE(14))
print(PE(3))