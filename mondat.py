jelek = []
while (vmi := input("Kérek egy mondatot (vagy nyomdmeg az entert a kilépéshez): ")) != "":
    if vmi.endswith("."):
        jelek.append("kijelentő")
    elif vmi.endswith("?"):
        jelek.append("kérdő")
    elif vmi.endswith("!"):
        jelek.append("felkiáltó/óhajtó/felszólító")
    else:
        print(f"deleting invalid input , deleting... 'C//system32//'dasda deleted")
print(jelek)