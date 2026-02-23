# Muhammad Rafa Giovi Pradana
# 24060125130114

# definisi dan spesifikasi

#   Fungsi P(A, B) adalah fungsi rekursif yang menghitung perkalian A × B menggunakan penjumlahan atau pengurangan berulang, tergantung tanda dari B.

def P(A,B):
    if B == 1:
        return A        
    elif B > 0:
        return A + (P(A,B-1))
    else:
        return -A + (P(A,B+1))
    
print(P(6,8))
print(P(2,9))