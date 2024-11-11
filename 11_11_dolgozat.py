"""A csoport:
Készítsünk programot, amely dinnyék csomagolásához végez számításokat. A
dinnyéket szalaggal kell átkötni úgy, hogy kétszer körbe érje őket, és a masni
készítéséhez számolunk még 60 cm-t. A program kérje be a dinnye átmérőjét, a
dinnyék számát, és a rendelkezésre álló szalag hosszát! Számítsa ki, és írja a
képernyőre, hogy a bekért számú dinnye csomagolásához hány méter szalagra van
szükség, valamint állapítsa meg, hogy elegendő szalagunk van-e a művelet
elvégzéséhez, és ezt is közölje a felhasználóval!"""
def doga():

    import math

    atmero = float(input("Add meg a dinnye átmérőjét (cm): "))
    dinnye_szama = int(input("Add meg a dinnyék számát: "))
    szalag_hossz = float(input("Add meg a szalag hosszát (m): "))

    kor_kerulet = math.pi * atmero
    szalag_dinnyenkent = 2 * kor_kerulet + 60  # masnihoz kell még 60 cm !!!

    osszes_szalag_hossz_centimeter = szalag_dinnyenkent * dinnye_szama
    osszes_szalag_hossz_meter = osszes_szalag_hossz_centimeter / 100

    print(f"A dinnye csomagolásához {osszes_szalag_hossz_meter:.1f} méter szalag kell.")

    if szalag_hossz >= osszes_szalag_hossz_meter:
        print("Van elegendő szalag a csomagoláshoz.")
    else:
        print("Nincs elegendő szalag a csomagoláshoz. Rendelj még!")


doga()
