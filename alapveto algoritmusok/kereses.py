szinek = ["piros", "sárga","zöld","kék","lila","fehér","fekete",]
keres_szin= "fehér"

i=0
indexe=0
talalat=False
while i < len(szinek):
    if szinek[i]==keres_szin:
        talalat=True
        indexe=i
    i+=1
    
if talalat:
    print(f"van {keres_szin} a listában a listában {indexe}-edik elem")