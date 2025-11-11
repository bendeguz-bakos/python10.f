paletta = ['kék', 'piros', 'fehér', 'fekete', 'zöld', 'sárga', 'barna', 'piros', 'fehér', 'szürke']
(valasztas := input('Adj meg egy színt!: '))
if valasztas in paletta:
    print(paletta.count(valasztas))
    paletta.append(valasztas)
else:
    print("ez nem szerepel a palettában, fel veszem")
    paletta.append(valasztas)
print(paletta)
   