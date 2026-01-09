import random as rnd
lsit = []
i=0
while i <=10:
    lsit.append(rnd.randint(-10,20))
    i+=1

y = 0
while y < len(lsit):
    if lsit[y] == 17:
        print("van benne ")
        break
    
    
    y+=1

    
#a 2.2 nem lehet megcsinálni tanár úr mert nem lehet 33 érték a listában
indexe = 0
x = 0
while x < len(lsit):
    if lsit[x] >10:
        print(x)
        indexe=x
        break
    i+=1
