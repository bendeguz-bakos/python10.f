#Írj egy programot, amely a felhasználótól kér be egész számokat [-5;5] intervallumban. A bekérés akkor fejeződjön be, amikor a felhasználó intervallumon kívüli értéket ad meg! A program írja ki a megadott intervallumba eső számokat és az összegüket!
szamok=[]
bekertszam=0
while 5>bekertszam>-5:
        szamok.append(bekertszam)
        bekertszam=int(input("szamot kerek:"))
print(szamok)
osszeg=0
for szam in szamok:
    osszeg += szam
    
print(osszeg)