list = []
x=1
while x!=0:
    x = int(input("irj egy számot: "))
    list.append(x)
    
    
atlag=0
for i in list:
    atlag+=i
    
atlag = atlag/len(list)
print(f"az átlag:{atlag}")
legnagy=max(list)
legkis=min(list)
print(f"a legnagyobb szám a {legnagy} a legkisseb pedig a {legkis}")