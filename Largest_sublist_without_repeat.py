

def subs(l):
    ls = [[]]
    for i in range(len(l) + 1):
        for j in range(i):
            ls.append(l[j: i])
    return ls
l1 = [3,2,8,3,5,6,7,9,2,1,4,7]
l2=subs(l1)
s=[]
for l in l2:
        if len(set(l))==len(l):
            s.append(sum(l))
print(max(s))
