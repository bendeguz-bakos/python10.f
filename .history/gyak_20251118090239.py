import random
szamok =  [1, 2, 2, 3, 2, 4, 6, 4, 2, 6]
print(max(szamok),min(szamok))
szamok.reverse
print(szamok)

hosz=int(input("írjbe egy számot: "))
list=[]
for i in range(hosz):
    list.append(i*hosz)
    i=+1
print(list)

vszamk=int(input("irjegyszámot:"))
vszamk2=int(input("irjegyszámot:"))
if vszamk or vszamk2 in szamok:
    print("igen")
    
listnagys=int(input("irhbeegyszámot"))
listaatlag=[]

for i in range(listnagys):
    listaatlag.append(random.randint(1,10))
print(sum(listaatlag)/listnagys)
betuk=[]
szamok2=[]
x=0
for i in range(10):
    x=input("irj egy betut:")
    betuk.append(x)
for i in range(10):
    x=(input("irj egy szamot:"))
    betuk.append(x)    