while jegy 
osszeg=0

for jegy in jegyek:
    osszeg+=jegy
    
print(osszeg)
print(f"a jegyek átlaga {osszeg/len(jegyek)}")