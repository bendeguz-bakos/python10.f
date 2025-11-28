x="a"
rovnev=[]
hosznev=[]
while x != "":
    x = input("írjbe egy szót:")
    if len(x)<=5:
        rovnev.append(x.lower())
    else:
        hosznev.append(x.lower())
        

print(f"a rövid szavak{rovnev} \na hosszú szavak {hosznev}")