import random as rnd
szamok=[]
for x in range(15):
    szamok.append(rnd.randint(-10,10))
print(szamok)
    
pozitivak=0
for x in szamok:
    if x>0:
        pozitivak+=1
print(f"{pozitivak} db pozitiv van")
    
negativak=0
for x in szamok:
    if x<0:
        negativak+=1
print(f"{negativak} db negativ van")

nulla=0
for x in szamok:
    if x==0:
        nulla+=1
print(f"{nulla} db nulla van")