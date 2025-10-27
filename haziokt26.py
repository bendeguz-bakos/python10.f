import random
szamok = []
sorozat = []
debug =[]
i = 0
while i < 10:
    szamok = random.randint(0,50)
    debug.append(szamok)
    if szamok % 4 == 0:
        sorozat.append(szamok)
    i += 1
print(sorozat)
print(len(sorozat))
print(len(debug))