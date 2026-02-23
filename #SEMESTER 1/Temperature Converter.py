def Temp_Cnvrt():
    print("==============================")
    print("     Temperature Converter    ")
    print("==============================")
    print("   1.Masuk         2.Keluar   ")
    try:
        strt = int(input("Pilih Opsi: "))
        if strt == 1:
            main1()
        elif strt == 2:
            exit
    except ValueError:
        print("⚠️  Harap masukkan angka")
        return Temp_Cnvrt()

def main1():
    try:
        Celcius = float(input("Suhu Celcius: "))
        if Celcius > -273.15:
            cnvrt(Celcius)
        else:
            print("Suhu minimal Celcius adalah 273.15, Harap masukkan suhu yang lebih tinggi6")
            main1()
    except ValueError:
        main1()
def cnvrt(Celcius):
    print("Convert ke derajat:\n1. Reamur\n2. Farrenheit\n3. Kelvin\n4. Keluar")
    try:
        opr = int(input("Pilih opsi: "))
        if opr == 1:
            opr1(Celcius)
        elif opr == 2:
            opr2(Celcius)
        elif opr == 3:
            opr3(Celcius)
        elif opr == 4:
            exit
    except ValueError:
        cnvrt()

def opr1(Celcius):
    print("Celcius -> Reamur")
    Reamur = Celcius * 4/5
    print("==============================")
    print("\033[1mHasil:\033[0m", Reamur)
    Temp_Cnvrt()


def opr2(Celcius):
    print("Celcius -> Fahrenheit")
    Fahrenheit = (Celcius * 9/5) + 32
    print("==============================")
    print("\033[1mHasil:\033[0m", Fahrenheit)
    Temp_Cnvrt()

def opr3(Celcius):
    print("Celcius -> Kelvin")
    print("==============================")
    Kelvin = Celcius + 273.15
    print("\033[1mHasil:\033[0m", Kelvin)
    Temp_Cnvrt()



Temp_Cnvrt()