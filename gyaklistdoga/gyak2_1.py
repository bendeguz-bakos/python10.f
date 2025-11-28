szavak = ["alma", "banán", "ananász", "eper", "szilva"]
for i in szavak:
    if i.startswith("a"):
        print(i)
#1.
    
x=0
for o in szavak:
    if "n" in o:
        x+=1
print(x)
#2.

cserelt = [s.replace("a","@") for s in szavak]
print(cserelt)
#3.

for big in szavak:
    print(big.capitalize())
#4.