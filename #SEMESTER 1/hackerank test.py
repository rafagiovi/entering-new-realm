# Bilangan

def Bilangan(a,b):
    if a % 2 == 0:
        genap = int(a / 2)
        if b <= genap:
            return (b * 2) - 1
        else:
            return (b - genap) * 2
    else:
        ganjil = int(a / 2) + 1
        if b <= ganjil:
            return (b * 2) - 1
        else:
            return (b - ganjil) * 2

print(Bilangan(7,5)) # 1, 3, 5, 7, 2, 4, 6

# Fungsi sederhana

def Deret(N):
    if N % 2 == 0:
        return N - int(N/2)
    else:
        return -(int(N/2) + 1)
    
print(Deret(7))

# Bus Rapid Transit

def isEmpty(L):
    return L==[]

def Konso(E, L):
   return [E] + L

def Konsi(L, E):
   return L + [E]

def FirstElmt(L):
   return L[0]

def LastElmt(L):
   return L[-1]

def Tail(L):
   return L[1:]

def Head(L):
   return L[:-1]

def isAtom(L):
   return type(L) != list

def isList(L):
   return type(L) == list

def getItemIndex(L, I): # Mengambil elemen indeks ke-I (basis-0)
   if L == []:
      return []
   elif I == 0:
      return FirstElmt(L)
   else:
      return getItemIndex(Tail(L), I-1)
   

def BRT(S):
   if isEmpty(S):
      return 0
   else:
        if isAtom(FirstElmt(S)):
            if isAtom(FirstElmt(S)):
                return FirstElmt(S) + BRT(Tail(S))
        else:
            return BRT(FirstElmt(S)) + BRT(Tail(S))

   

# print(BRT([[7,8,9,1],[1,2,5,2]]))
print(BRT([[7, 35, ['Port Clyris', 33], 36, 16, 10, ['Melbryn', 3], 36, 47, 23, ['Ho Melora', 5], 16, 9, 44, ['Londara', 34], 59, 18, 24, 12, 16], [33, 8, ['Kivara', 21], 4, 8, ['Londara', 8], 19, 28, ['Kudor', 43], 36, 6, ['Kalayra', 10], 15, 50, 11], [42, 40, 43, ['Lymara', 12], 50, 4, ['Tokara', 25], 18, 5, ['Atvene', 36], 15, 9, 40, ['Cairos', 15], 53, 57, 27, 60]]))