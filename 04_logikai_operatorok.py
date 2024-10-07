"""== egyenlő
!= nem
egyenlő
< kisebb
> nagyobb
<= kisebb
vagy
egyenlő
>= nagyobb
vagy
egyenlő"""
# Logikai
# operátorok
# and és
# or vagy
# not nem
#
# x = 5
# y = -3
#
# if x < 0 and y < 0:
#     print('mindkettő negatív')
#
# if x < 0 or y < 0:
#     print('van köztük negatív')
#
# if not x <= 0:
#     print('x pozitív')

"""1. Feladat
Készíts egy programot, amely a felhasználótól bekér egy egész számot,
majd megvizsgálja, hogy a megadott szám
- pozitív páros vagy
- negatív páratlan.
Az eredményről tájékoztatja a felhasználót."""

# numero = int(input("Adj meg egy számot! "))
# if numero % 2 == 0 and numero > 0:
#     print("A szám pozitív és páros.")
# elif numero % 2 != 0 and numero < 0:
#     print("A szám negatív és páratlan.")
# else:
#     print("Helytelen bevitel")


"""2. Feladat
Készíts egy programot, amely a felhasználótól két külön kérdésben megkérdezi,
hogy az ikrek (Henrik és Hanna) jönnek-e ma kosrazni! Például így:
Jön Henrik ma kosarazni? (igen/nem). A program írja ki, hogy melyik állítás igaz az
alábbiak közül:
- egyikük sem jön kosarazni,
- mind a ketten jönnek kosarazni,
- csak az egyikük jön kosarazni."""

# x = 'Henrik'
# y = 'Hanna'
# q = str(input(f"Jön {x} kosarazni? "))
# qq = str(input(f"Jön {y} kosarazni? "))
# if q == "igen" and qq == "igen":
#     print("Mind a ketten jönnek kosarazni.")
# elif q == "nem" and qq == "igen" or q == "igen" and qq == "nem":
#     print("Csak az egyikőjük jön kosarazni.")
# elif q == "nem" and qq == "nem":
#     print("Egyikőjük sem jön kosarazni.")


"""3. Feladat
Készíts egy programot, amely a felhasználó által megadott egész számról eldönti, hogy
- csak 3-mal osztható,
- csak 4-gyel osztható,
- 3-mal és 4-gyel is osztható,
- sem 3-mal, sem 4-gyel nem osztható!"""

kerdes = int(input("Adj meg egy számot! "))
if kerdes % 3 == 0 and kerdes % 4 == 0:
    print("A megadott szám hárommal és néggyel is osztható.")
elif kerdes % 3 != 0 and kerdes % 4 != 0:
    print("A megadott szám sem hárommal sem néggyel nem osztható.")
elif kerdes % 3 == 0:
    print("A megadott szám hárommal osztható.")
elif kerdes % 4 == 0:
    print("A megadott szám néggyel osztható.")