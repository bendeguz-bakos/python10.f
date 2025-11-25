szamok = [10, 3, 45, 6, 23, 3, 99]
szamok.sort()
print(szamok)
szamok.reverse()
print(szamok)
#1.

uj=[]
for x in szamok:
    if x not in uj:
        uj.append(x)
print(uj)
#2.

