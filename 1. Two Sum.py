
import random
a=[random.randint(1,100) for i in range(1,10)]
print(a)
b=[]
tg=int(input('please enter a number betw 1 and 100:  '))
for i,j in enumerate(a):
    for k,l in enumerate(a):
        if j+l==tg and j!=l and (k,i) not in b:
            b.append((i,k))
for bb in b:
    print(bb)