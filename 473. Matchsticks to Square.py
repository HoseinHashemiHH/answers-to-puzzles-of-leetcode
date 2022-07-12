



def matchstickstosquar(matchsticks:list):
    squardict={}
    for i in range(4):
        if i not in squardict:
            squardict[i]=0
    sum=0
    for m in (matchsticks):
        sum+=m
    if sum%4!=0:
        return False
    side=sum/4
    total=0
    for j in range(len(matchsticks)):
                   total+=matchsticks[j]
                   if total==side:
                      squardict[i]=1
                      i+=1
                   if i==3:
                       return True
    return False
                   
def cmd_line():
    booli=matchstickstosquar([-0.1,0.5,0.5,1.1,0.1,0.9,1,0,0,0])
    print(booli)
cmd_line()
    
                   
                   
                   
