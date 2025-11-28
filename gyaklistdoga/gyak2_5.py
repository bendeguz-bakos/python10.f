szavak = ["asztal", "ablak", "szék", "ceruza", "alma", "autó", "toll"]

akezd =[x for x in szavak if x.startswith("a")]
aveg =[x for x in szavak if x.endswith("a")]
print(akezd, aveg)