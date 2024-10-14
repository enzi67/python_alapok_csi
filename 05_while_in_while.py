""" 1. pelda """

# sor = 1
# while sor <= 3:
#     oszlop = 1
#     while oszlop <= 5:
#         print('O ', end='')
#         oszlop = oszlop + 1
#     print('')
#     sor = sor + 1


""" 2. pelda """

# darab_karakter = 1
# sor = 1
# while sor <= 7:
#     oszlop = 1
#     while oszlop <= darab_karakter:
#         print('O ', end='')
#         oszlop = oszlop + 1
#     print('')
#     darab_karakter = darab_karakter + 1
#     sor = sor + 1

"""1. Feladat - Pocak
Készíts egy programot, amely a felhasználótól bekér egy páros számot, majd ennek megfelelően rajzol ki a
képernyőre egy pocak szerű alakzatot az alábbiak szerint"""

# szam = int(input('Adj meg egy páros számot! '))
#
# sor = 1
# while sor <= szam // 2:
#     print('O' * sor)
#     sor += 1
#
# sor = szam // 2
# while sor > 0:
#     print('O' * sor)
#     sor -= 1

"""2. Feladat - \
Készíts egy programot, amely egymásba ágyazott ciklusok segítségével rajzolja ki egy 5 x 5-ös
mezőben az alábbi alakzatot!"""

# sor = 0
# while sor < 5:
#     oszlop = 0
#     while oszlop < 5:
#         print('O' if sor == oszlop else '.', end='')
#         oszlop += 1
#     print()
#     sor += 1

"""3. Feladat - X
Készíts egy programot, amely egymásba ágyazott ciklusok segítségével rajzolja ki egy 7 x 7-es
mezőben az alábbi alakzatot!"""

sor = 0
while sor < 7:
    oszlop = 0
    while oszlop < 7:
        print('O' if sor == oszlop or sor == 6 - oszlop else '.', end='')
        oszlop += 1
    print()
    sor += 1
