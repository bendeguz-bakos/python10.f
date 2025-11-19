string_list = ["apple","banana","cherry","date","elderberry","agartha"]

for szo in string_list:
    print(szo)
    
for karakter in 'apple':
    print(karakter)

for index, karakter in enumerate('banana', start=2):
    print(f'{index}: {karakter}')

for _ in range(1,5,2):
    print("alma")

for szo in string_list:
    if szo.startswith(('a')):
        print(szo)
        
i = 0
while i < len(string_list):
    print(string_list['a'])
    lista[i]="törlés"
    i += 1                   