# import random
#
# random_szam = random.randint(1, 10)
# print(random_szam)

"""1. Feladat
Készíts egy rövid programot, amely 1 és 3 között generál véletlenszámot,
majd összehasonlítja ezt a felhasználó által megadott, szintén ebbe a tartományba eső számmal!
Az összehasonlítás eredményéről tájékoztassa a felhasználót!"""


# user = int(input("Adj meg egy számot 1 és 3 között! "))
#
# import random
# random_szam = random.randint(1, 3)
# print(f"A gép száma: {random_szam}")
#
# if user == random_szam:
#     print("A számod megegyezik a random számmal!")
# elif user < random_szam:
#     print("A számod kisebb, mint a random szám!")
# elif user > random_szam:
#     print("A számod nagyobb, mint a random szám!")

"""2. Feladat
A program a pénzfeldobást modellezi.
Kérdezze meg a felhasználótól a választását (fej vagy írás), majd adjon tájékoztatást,
hogy eltalálta-e!"""

import random
penzerme = ["fej", "írás"]
dobas = random.choice(penzerme)

kerdes = str(input("Fej vagy írás? "))
print(f"A gép erre gondolt: {dobas}")
if kerdes == dobas:
    print("Eltaláltad!")
else:
    print("Nem talált!")