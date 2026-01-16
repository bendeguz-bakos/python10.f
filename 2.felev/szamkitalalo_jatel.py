import random as rnd

kitalallando=rnd.randint(1,10)
def eltalalta(tipp,kitalallando):
    if(tipp==kitalallando):
        return True
    else:
        return False    
def tipp_bekero():    
    tipp = int(input("mondj egy szamot: "))
    return tipp
    
def main():
    state = False
    while state == False:
        tipp_bekero()
        state=eltalalta(tipp_bekero,kitalallando)
        
main()