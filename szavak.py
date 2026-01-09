import random

szavak = ["alma", "auto", "macska", "asztal", "tukor", "robot", "iskola", "erdei", "villam", "cseresznye"]

titok = random.choice(szavak)
probkak = 0
hazsnalt = []

print("Szókitaláló játék — adj meg betűket! Max 10 próbálkozás.")

while probkak < 10:
    betu = input("Adj meg egy betűt: ").lower().strip()

    if len(betu) != 1 or not betu.isalpha():
        print("Csak egy betűt írj!")
        continue

    if betu in hazsnalt:
        print("Ezt már mondtad!")
        continue

    hazsnalt.append(betu)
    probkak += 1

    if betu in titok:
        print("Benne van!")
    else:
        print("Nincs benne!")

print("Elfogytak a próbálkozások!")
talalas = input("Melyik szóra gondolt a gép? ").strip().lower()

if talalas == titok:
    print("Eltaláltad!")
else:
    print(f"Nem talált. A szó ez volt: {titok}")