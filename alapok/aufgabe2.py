szavak = []
while (szo := input("adj meg egy szót: ")) != "":
    if szo[0] == "a" or szo[0] == "A":
        szavak.append(szo)
print(szavak)   