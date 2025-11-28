elso = int(input("Kérem az első évszámot: "))
masodik = int(input("Kérem a második évszámot: "))
nagyobb = 0
kissebb = 0
evek = []
if elso == masodik:
    print("kell mééég alma lééé kell méég alma léé sooooos")
elif elso < masodik: 
    kissebb = elso
    nagyobb = masodik
else:
    kissebb = masodik
    nagyobb = elso
for ev in range(kissebb, nagyobb + 1):
    if ev % 4 == 0 and ev % 100 !=0:
        evek.append(ev)
    elif ev % 100 == 0 and ev % 400 == 0:
        evek.append(ev)
print(f"szökőévek: {evek}")

