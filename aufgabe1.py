nevek = []
i = 1
while (nev := input("adj meg egy nevet: ")) != "" and i <= 3:
    nevek.append(nev)
    i += 1
print("csak 3 név lehet!!:")
print(nevek)