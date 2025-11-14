import random as rnd
list = []
for i in range(10):
    list.append(rnd.randint(1,3))
szam = int(input("Kérek egy számot 1 és 3 között: "))
if szam in list:
    list.remove(szam)
    print(f"A szám szerepelt a listában, eltávolítottam: {szam}")
print(list)