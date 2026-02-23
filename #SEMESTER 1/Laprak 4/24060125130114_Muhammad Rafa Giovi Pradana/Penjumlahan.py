# Muhammad Rafa Giovi Pradana
# 24060125130114

# definisi dan spesifikasi

#   Fungsi TS(x) adalah fungsi rekursif yang menghitung jumlah semua bilangan dari 1 sampai x (yakni deret aritmetika).

def TS(x):
    if x==0:
        return 0
    else:
        return x + (TS(x-1))

print(TS(10))
print(TS(100))