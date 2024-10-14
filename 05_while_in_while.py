# sor = 1
# while sor <= 3:
#     oszlop = 1
#     while oszlop <= 5:
#         print('O ', end='')
#         oszlop = oszlop + 1
#     print('')
#     sor = sor + 1

"""1. Feladat - Pocak
Készíts egy programot, amely a felhasználótól bekér egy páros számot, majd ennek megfelelően rajzol ki a
képernyőre egy pocak szerű alakzatot az alábbiak szerint"""

szam = int(input('Adj meg egy páros számot! '))

sor = 1
while sor <= szam // 2:
    print('O' * sor)
    sor += 1

sor = szam // 2
while sor > 0:
    print('O' * sor)
    sor -= 1

"""2. Feladat - \
Készíts egy programot, amely egymásba ágyazott ciklusok segítségével rajzolja ki egy 5 x 5-ös
mezőben az alábbi alakzatot!"""

