A = [2, 4, 6, 8, 10]
B = [1, 2, 3, 4, 5]

C = A +B
print(C)
#1.
for x in A :
    if x in B:
        print(x)
#2.

for x in A:
    if x not in B:
        print(x)
for x in B:
    if x not in A:
        print(x)
#3.