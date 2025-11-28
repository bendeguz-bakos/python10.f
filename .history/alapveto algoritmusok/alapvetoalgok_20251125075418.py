while jegy != 0:
    jegy= int(input("adj meg egy jegye 1és 5 között "))
osszeg=0

for jegy in jegyek:
    osszeg+=jegy
    
print(osszeg)
print(f"a jegyek átlaga {osszeg/len(jegyek)}")