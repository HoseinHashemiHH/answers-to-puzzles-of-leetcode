



import itertools


def rotate_list_left(_list : list, rotation_value: int)-> list:

    result_list = _list

    for k in range(0, len(_list)):
        result_list[k-rotation_value] = _list[k]

    return result_list


def subl3(ar):
    v=[]
    # for i in range(len(ar)):
    #     for j in range(len(ar)):
    #         for k in range(len(ar)):
    #             if i!=j and j!=k and i!=k: 
    #                 v.append(([ar[i],ar[j],ar[k]]))
    v=itertools.combinations(ar,3)
    return v
            

def sum3(ar):
    u=[]
    s=subl3(ar)
    for ss in s:
        if sum(ss)==0:
            u.append(ss)
    # for uu in u:
    #     if rotate_list_left(uu,1) in u or rotate_list_left(uu,2) in u :
    #         u.remove(uu)
    return u

nums = [-1,0,1,2,-1,-4]
x=sum3(nums)
print(x)


