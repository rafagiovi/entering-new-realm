# Muhammad Rafa Giovi Pradana
# 24060125130114

# definisi dan spesifikasi

# Fungsi KD(x) adalah fungsi rekursif yang menghitung nilai 2 * KD(x-1). Fungsi ini bekerja dengan cara memanggil dirinya sendiri hingga mencapai nilai dasar (x == 1), lalu mengalikan hasilnya dengan 2 setiap kali kembali dari pemanggilan rekursif.


def KD(x):
    if x == 1:
        return 1 
    else:
        return 2 * KD(x-1)
    
print(KD(3))
print(KD(7))