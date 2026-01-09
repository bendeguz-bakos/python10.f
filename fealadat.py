#Készíts egy programot, amely [1;10] intervallumon generál 5 darab véletlen egész számot és ezeket tárolja el egy listában! 
#A program számolja össze, és képernyőre írja ki a listában tárolt páros számok számát, valamint a lista elemeit!
import random
lsit=[]
for i in range(5):
    lsit.append(int(random.randint(1,10)))
    
parossak=[]
for x in lsit:
    if x%2==0:
        parossak.append(x)
        
print(parossak)
print(lsit)
