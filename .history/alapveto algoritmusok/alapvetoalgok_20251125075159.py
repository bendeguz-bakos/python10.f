jegyek = [3,2,5,5,5,1,4,2,5,3,4,1,3,3,2,4,5,1,4]
osszeg=0

for jehy in jegyek:
    osszeg+=jehy
    
print(osszeg)
print(f"a jegyek átlaga {osszeg/len}")