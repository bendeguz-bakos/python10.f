szavak = ["alma", "körte", "szilva", "barack", "cseresznye", "banán", "eper", "málna"]

for szo in szavak:
    print(szo,end=",")

print()

i=0
while i < len(szavak):
    print(szavak[i],end=",")
    i += 1

print()

for i,szo in enumerate(szavak):
    print(i,szo)