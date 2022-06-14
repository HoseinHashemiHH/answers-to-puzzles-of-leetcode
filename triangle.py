triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
#triangle=[[-10]]
def minm(tri):
    v=[]
    for t in range(len(tri)):
         v.append(min(tri[t]))
    return(sum(v))
x=minm(triangle)
print(x)
    