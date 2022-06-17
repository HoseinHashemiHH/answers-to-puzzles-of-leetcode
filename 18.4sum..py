

import itertools


def pick4(ar):
    a=list(itertools.combinations(ar,4))
    return a

# def sum4(ar,tg):
#     p=pick4(ar,4)
def sum4(ar,tg):
    u=[]
    for tupl in pick4(ar):
        if sum(tupl)==tg:
            u.append(tupl)
    return u
nums = [1,0,-1,0,-2,2]; target = 0
print(sum4(nums,target))
