jegyek = []
while mjegyek != 0:
    mjegyek= int(input("adj meg egy jegyet 1 és 5 között (nullával kilépsz): "))
    if 0>mjegyek or 5<mjegyek:
        print("error")
        break
    else:
        jegyek.append(mjegyek)
        
if len(jegyek)==0:
    print
    
osszeg=0

for jegy in jegyek:
    osszeg+=jegy
    
print(osszeg)
print(f"a jegyek átlaga {osszeg/len(jegyek)}")