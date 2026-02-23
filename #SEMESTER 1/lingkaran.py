
def Posisi(a, b, r, x, y):
    if ((x - a) ** 2) + ((y-b) ** 2) < r ** 2:
        return "Dalam Lingkaran"
    if ((x - a) ** 2) + ((y-b) ** 2) == r ** 2:
        return "Pada Lingkaran"
    if ((x - a) ** 2) + ((y-b) ** 2) > r ** 2:
        return "Luar Lingkaran"
    
print(Posisi(2 ,3, 4, 2, 1))