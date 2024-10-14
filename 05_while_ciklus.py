# szam = 1
# while szam <= 10:
#     print(szam)
#     # szam = szam + 1
#     szam+= 1
#
# folytatja = True
# while folytatja:
#     print('Vidd ki a szemetet!')
#     valasz = input('Mondjam még egyszer? (i/n) ')
#     if valasz == 'n':
#         folytatja = False
# print('>> Program vége! <<')


"""1. Feladat
Írj egy programot, amely kiírja a páros számokat 1 és 10 között!"""

# szam = 1
# while szam <= 10:
#     if szam % 2 == 0:
#         print(szam)
#     szam += 1

'''2. Feladat
Írj egy programot, amely csökkenő sorrendben írja ki a számokat 1 és 10 között!'''

# szam = 10
# while szam >= 1:
#     print(szam)
#     szam -= 1

"""3. Feladat
Írj egy programot, amely kiírja a páratlan számokat csökkenő sorrendben 1 és 10 között!"""

# numero = 9
# while numero >= 1:
#     print(numero)
#     numero -= 2

"""5. Feladat
Írj egy programot, amely a felhasználótól páros számot kér be. Amennyiben a megadott szám páratlan, újra és újra megtörténik az adatbekérés mindaddig,
amíg végül páros számot nem ad meg a felhasználó.
"""

# """felhasznaloi_input = int(input("Kérlek adj meg egy páros számot! "))"""
# folytat = False
#
# while folytat == False:
#     felhasznaloi_input = int(input("Kérlek adj meg egy páros számot! "))
#     if felhasznaloi_input % 2 == 0:
#         folytat = True
#         print("Köszönöm")

"""6. Feladat
Írj egy programot, amely [1;12] intervallumon állít elő 20 darab véletlenszámot!
A képernyőre kizárólag csak a 3-mal oszthatóakat írja ki, és a végén informálja
a felhasználót arról is, hány darab ilyen szám volt."""

import random

darab = 0

while darab < 20:
    veletlenszam = random.randint(1, 12)

    if veletlenszam % 3 == 0:
        print(veletlenszam)

    darab += 1

