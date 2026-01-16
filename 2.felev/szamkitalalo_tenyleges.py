import random


def eltalalta(a,b):
    return a==b

def tippbekero():
    x=int(input("szam:"))
    return x

def main():
    kitalallando = random.randint(1,10)
    tipp = tippbekero()
    eltalalta(kitalallando,tipp)
    
main()