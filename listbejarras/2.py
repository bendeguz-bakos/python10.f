szavak = ['ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python']
tsszavak = []
for szo in szavak:
    if szo.startswith(('T','t')):
        tsszavak.append(szo)
print(tsszavak)