nevek = ["Anna", "Béla", "Csaba", "dóra", "Erika", "Feri", "Elemér"]


x = input(f"írj be egy nevet:")
if x in nevek:
    print("benne van") 
else:
    print("nincs benne")
    
esnevek=[e for e in nevek if e.startswith("E")]
        


        
