szamok = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
index = 0
for index in range(len(szamok)):
    if szamok[index] % 2 == 0:
        szamok[index] = 0

print(szamok)