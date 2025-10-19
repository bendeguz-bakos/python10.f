import math
x = int(input("ird be a pocak hosszusaganak merteket: "))
for i in range(math.floor(x/2)):
    print('*' * (i+1))
for j in range(math.ceil(x/2)):
    print('*' * (math.ceil(x/2)-j)) 