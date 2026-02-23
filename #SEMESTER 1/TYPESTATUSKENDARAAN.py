type Kendaraan = tuple[str, str, int, str]
type Pengemudi = tuple[str, int, bool, int]
type UjiEmisi = tuple[float, float, bool]
type UjiKeselamatan = tuple[bool, bool, bool]

# Konstruktor

def MakeKendaraan(NP: str, J: str, TP: int, BB: str) -> Kendaraan:
    return (NP, J, TP, BB)
def MakePengemudi(N: str, U: int, SIM: bool, PA: int) -> Pengemudi:
    return (N, U, SIM, PA)
def MakeUjiEmisi(CO: float, HC: float, L: bool) -> UjiEmisi:
    return (CO, HC, L)
def MakeUjiKeselamatan(R: bool, L: bool, B: bool) -> UjiKeselamatan:
    return (R, L, B)

# Selektor Kendaraan

def getNP(K: Kendaraan):
    return K[0]
def getJ(K: Kendaraan):
    return K[1]
def getTP(K: Kendaraan):
    return K[2]
def getBB(K: Kendaraan):
    return K[3]

# Selektor Pengemudi

def getN(P: Pengemudi):
    return P[0]
def getU(P: Pengemudi):
    return P[1]
def getSIM(P: Pengemudi):
    return P[2]
def getPA(P: Pengemudi):
    return P[3]

# Selektor UjiEmisi

def getCO(UE: UjiEmisi):
    return UE[0]
def getHC(UE: UjiEmisi):
    return UE[1]
def getL(UE: UjiEmisi):
    return UE[2]

# Selektor UjiKeselamatan

def getR(UK: UjiKeselamatan):
    return UK[0]
def getLa(UK: UjiKeselamatan):
    return UK[1]
def getB(UK: UjiKeselamatan):
    return UK[2]

# Predikat

def IsSIMTrue(P: Pengemudi):
    if P[2] == True:
        return "Layak Jalan"
    else:
        return "Tidak Layak"
    
# Operasi

def IsPA(P: Pengemudi):
    if P[3] >= 3:
        return "Tidak Layak"
    if 0 < P[3] < 3:
        return "Perlu Perbaikan"
    else:
        return "Layak Jalan"
def KonKend(K: Kendaraan):
    if K[2] < 2000:
        return "Tidak Layak"
    if K[3] == "Solar" and K[2] < 2010:
        return "Perlu Perbaikan"
    else:
        return "Layak Jalan" 
def UjiEm(UE: UjiEmisi):
    if UE[2] == False:
        if UE[0] > 2.5 or UE[1] > 800:
            return "Tidak Layak"
        if UE[0] <= 2.5 and UE[1] <= 800:
            return "Perlu Perbaikan"
    else:
        return "Layak Jalan"  
def UjiKes(UK: UjiKeselamatan):
    if UK[0] == False:
        return "Tidak Layak"
    if UK[1] == False or UK[2] == False:
        return "Perlu  Perbaikan"
    else:
        return "Layak Jalan"
    
# Operasi hasil

def StatusKendaraan(K: Kendaraan, P: Pengemudi, UE: UjiEmisi, UK: UjiKeselamatan):
    hasil_SIM = IsSIMTrue(P)
    hasil_PA = IsPA(P)
    hasil_KonKend = KonKend(K)
    hasil_UjiEm = UjiEm(UE)
    hasil_UjiKes = UjiKes(UK)

    hasil = [hasil_SIM, hasil_PA, hasil_KonKend, hasil_UjiEm, hasil_UjiKes]

    if all(h == "Layak Jalan" for h in hasil):
        status = "Layak Jalan"
    elif any(h == "Tidak Layak" for h in hasil):
        status = "Tidak Layak"
    else:
        status = "Perlu Perbaikan"

    return f"Nomor Polisi: {getNP(K)}\nNama Pengemudi: {getN(P)}\nStatus: {status}"

print(StatusKendaraan(MakeKendaraan("AB2314JK", "Mobil", 2013, "Bensin"),
                      MakePengemudi("Rafa Giovi", 29, True, 0), 
                      MakeUjiEmisi(1.0, 200, True), 
                      MakeUjiKeselamatan(True, True, True)))
print(StatusKendaraan(MakeKendaraan("AB2314JK", "Mobil", 1999, "Bensin"), 
                      MakePengemudi("Rafa Giovi", 29, True, 0), 
                      MakeUjiEmisi(1.0, 200, True), 
                      MakeUjiKeselamatan(True, True, True)))