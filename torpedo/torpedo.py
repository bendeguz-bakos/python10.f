import random as rnd
oszlop = ['A','B','C']
sor =  [1,2,3]

ellenfel_oszlop =oszlop[rnd.randint(0,2)]
ellenfel_sor =sor[rnd.randint(0,2)]  

print(f"{ellenfel_oszlop}{ellenfel_sor}")
prob=0
while True:
    jatekos_oszlop = input("irj egy betut A,B,C")
    jatekos_sor = int(input("irj egy szamot1-3"))
    
    if jatekos_oszlop.upper() == ellenfel_oszlop and jatekos_sor == ellenfel_sor:
        print(f"talált az ")
        print(prob)
        
    elif jatekos_oszlop == '' or jatekos_sor== 0:
        break
    else:
        prob+=1