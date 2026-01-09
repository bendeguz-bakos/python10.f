szavak1 = ['Elemér', 'Emma', 'ajtó', 'róka', 'egér']
szavak2 = ['alma', 'barack', 'Attila', 'kávé', 'szekrény', 'asztal']
bs=0
bbb=[]
for b in szavak2:
    if b.startswith("A") or b.startswith("a"):
        bs+=1
        bbb.append(b)
es=0
eee=[]
for e in szavak1:
    if "e" in e or "E" in e:
        es+=1
        eee.append(e)
        
print(bbb)
print(eee)