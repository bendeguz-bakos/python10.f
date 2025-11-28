#Készíts egy programot, amely [1;10] intervallumon generál 5 darab véletlen egész számot és ezeket tárolja el egy listában! A program számolja össze, és képernyőre írja ki a listában tárolt páros számok számát, valamint a lista elemeit!
import random as rnd
lista =[]
for i in range(0,5):
    lista.append(rnd.randint(1,10))
    
osszeg=0
for i in lista:
    osszeg+=i
    
print(osszeg)
parososszeg=0
for i in lista:
    if i % 2==0:  
        parososszeg+=i 
        
