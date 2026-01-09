''''
A program kérjen be egy szöveget!

Határozza meg és írja ki a képernyőre, hogy
- az adott szövegben volt-e,
- ha igen akkor hány darab,
- és hányadik helyen / helyeken (a legelső hely az egyes számú)
a, e, i , o vagy u magánhangzó!

Mindegyik magánhangzóra külön-külön adja meg az információkat!
'''
Adb = 0
Edb = 0
Idb = 0
Odb = 0
Udb = 0
szoveg = input("írj be egy szöveget:").lower().strip()
Aindex = []
Eindex = []
Iindex = []
Oindex = []
Uindex = []
szamolo =0
for i in szoveg:
    if i == 'a':
        Adb+=1
        Aindex.append(szamolo)
    if i == 'e':
        Edb+=1
        Eindex.append(szamolo)
    if i == 'i':
        Idb+=1
        Iindex.append(szamolo)
    if i == 'o':
        Odb+=1
        Oindex.append(szamolo)
    if i == 'u':
        Udb+=1
        Uindex.append(szamolo)
    szamolo+=1
        
        

Aindex = [i + 1 for i in Aindex]
Eindex = [i + 1 for i in Eindex]
Iindex = [i + 1 for i in Iindex]
Oindex = [i + 1 for i in Oindex]
Uindex = [i + 1 for i in Uindex]




if Adb !=0:
    print(f"van benne 'a' betű")
    print(f"a {Aindex} edik helyeken ")
    print(f"{Adb}db 'a' betű van a szóban")
               
if Edb !=0:
    print(f"van benne 'e' betű")
    print(f"a {Eindex} edik helyeken ")
    print(f"{Edb}db 'e' betű van a szóban")
        
        
        
if Idb !=0:
    print(f"van benne 'i' betű")
    print(f"a {Iindex} edik helyeken ")
    print(f"{Idb}db 'i' betű van a szóban")
        
        
        
if Odb !=0:
    print(f"van benne 'o' betű")
    print(f"a {Oindex} edik helyeken ")
    print(f"{Odb}db 'o' betű van a szóban")
        
        
        
if Udb !=0:
    print(f"van benne 'u' betű")
    print(f"a {Uindex} edik helyeken ")
    print(f"{Udb}db 'u' betű van a szóban")
 
        
    
        
       
    
        
        
    
        
        
    
        
        