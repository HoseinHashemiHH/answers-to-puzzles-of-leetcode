


#from turtle import shape


def sublist(list):
    sub=[]
    for i in range(len(list)+1):
        for j in range(i):
            sub.append(list[j:i])
    return sub

def substring(ar):
    s1=[[] for i in range(len(ar))]
    i=0
    while i<len(ar):
      for a in ar:    
          for s in a:
               s1[i].append(s)
          i+=1
    
    s2=[[] for i in range(len(ar))]
    for i in range(len(ar)):
       s2[i].extend(sublist(s1[i]))
    return s2

def long(ar):
    s3=substring(ar)
    s4=[]
    s5=[]
    for i in s3:
        for j in i:
            s4.append(j)
    for i in s4:
        if s4.count(i)>=3:
            s5.append(i)
    mx=0
    for x,s in enumerate(s5):
        if len(s5[x])>=mx:
            mx=len(s5[x])
            y=s5[x]
        else:
            continue
    return y,mx,s5

x,r,s5=long(['bravannadaspoloyiaharanghablamedamkoni', 'banafradaspoloyiavadamkoninnsghablameharan','baraghablamenrdamkonadaspoloyiiavannharan'])
print(x,r)



