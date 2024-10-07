"""1.1 Feladat
Készíts egy programot, amely megkérdezi a felhasználótól, hogy jó napja van-e!
A válasz kétféle lehet: igen vagy nem. A választól függően írjon ki üzenetet a gép!
"""
# nap = str(input("Jó napod van? "))
# nap_lowercase = nap.lower()
# if nap_lowercase == "igen" or nap == "Igen" or nap == "Aha":
#     print("Ennek örülök!")
# else:
#     print("womp womp")


"""1.2 Feladat
Fejleszd tovább az első feladat programját úgy,
hogy amennyiben a felhasználó nem a két lehetséges válasz (igen/nem)
közül ad meg egyet, a gép kiírja: "Sajnos nem értem a válaszodat!"""

# nap = str(input("Jó napod van? "))
# if nap == "igen" or nap == "Igen" or nap == "aha":
#     print("Ennek örülök!")
# elif nap == "nem" or nap == "Nem":
#     print("womp womp")
# else:
#     print("Sajnos nem értem a válaszodat!")


"""2. Feladat
Készíts egy programot, ami bekér egy számot a felhasználótól,
majd kiírja, hogy a megadott szám páros-e vagy páratlan!
[Tipp] A maradékos osztás segít! Mennyivel is kell elosztanod a számot maradékosan,
hogy kiderüljön páros-e? Ebben az esetben mennyi lesz a maradék?"""

#szam2 = int(input("Adj meg egy számot! "))
# print(szam2 % 2)
#if szam2 % 2 == 0:
#    print("A megadott szám páros.")
#else:
#    print("A megadott szám páratlan.")

"""3. Feladat
Készíts egy programot! A gép "gondol" egy számra 1 és 5 között,
vagyis egy változóban tárolj egy ilyen számot! Azután a program bekér egy számot
a felhasználótól, majd kiírja, hogy ez a szám egyenlő-e a gép által "gondolt" számmal,
vagy annál kisebb, illetve nagyobb."""

import random
random_number = random.randint(a=1, b=5)
number = input("Gondoltam egy számra! ")
print(f"Erre gondoltam: {random_number}")
if random_number == number:
    print("Eltaláltad!")
if random_number != number:
    print("Nem talált!")