def hozzaad(lsit):
    x=input("mit adjak hozzá?: ")
    lsit.append(x)
    return lsit
    
def kiir(lsit):
    return ", ".join(lsit)

def main():
    szamok = []
    for  i in range(3):
        szamok=hozzaad(szamok)
    print(kiir(szamok))
    
main()
