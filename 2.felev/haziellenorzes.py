lista=[]
def listafeltoltes():
    lista=[]
   #ide írd a kódod
    szam=0
    while True:
        szam=int(input("írj be egy számot (negatíval tovább mész): "))
        if(szam <0):
            break
        lista.append(szam)
    return lista

def harommal_oszthatok(lista):
    db = 0
    for szam in lista:
        if szam % 3 == 0:
            db+=1
    return db

lista = listafeltoltes()
print(harommal_oszthatok(lista))