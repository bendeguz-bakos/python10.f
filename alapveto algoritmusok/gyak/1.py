import random as rnd
lsit = []
i=0
while i <=10:
    lsit.append(rnd.randint(-10,20))
    i+=1


lsito = sum(lsit)
print(lsito)
lsitoparos = 0
lsitparos=[]
y = 0
while y < len(lsit):
    
    if lsit[y] % 2 == 0:
        lsitparos.append(lsit[y])
    y+=1
lsitoparos = sum(lsitparos)
print(lsitoparos)
print(lsit)