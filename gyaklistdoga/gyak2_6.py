szamok = [4, 2, 9, 2, 7, 4, 2, 9, 4, 4, 2, 9, 9, 9,]
szamoksokszor = []
for x in szamok:
    if x not in szamoksokszor:
        szamoksokszor.append(x)
    
for szam in szamoksokszor:
    print(szam,">",szamok.count(szam))
    
    
legzobb=szamok[0]
leggyakoribb=0
for sazm in szamok:
    if szamok.count(sazm)>legzobb:
        legzobb = sazm
        
print(legzobb)
print(f"{szamok.count(legzobb)}alakalomma")