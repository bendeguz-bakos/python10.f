szamok =[43,2,41,32,435,1]
kerszam = int(input("írj egy számot : "))
i2=0
while i2<len(szamok):
    if kerszam == szamok[i2]:
        print("a keresett elem benne van ")
        break    
    i2+=1
    
print(f"a keresett szam indexe {i2}")
