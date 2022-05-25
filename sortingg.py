
#Sorting - Implement two types of sorting algorithms:
# Merge sort and bubble sort.
#devide a list to m sublist
def dev(l,m):
    n=len(l)//m
    h=len(l)%m
    o=[]
    subl=[[0 for x in range(m)] for y in range(n)]
   # subl=[]
    #print(subl)
    for d in range(n):
        for k in range(m):
            subl[d][k]=l[k+d*m]
    
    o=l[-1:-(h+1):-1]
    
    subl_new=subl+[o]
    for i in subl_new:
        print(i)
    return subl_new
def sorting(full_arr):
    print(type(full_arr))
    f_a_s=[]
    for f_a in full_arr:
        f_a=sorted(f_a)
        f_a_s+=f_a

    return f_a_s
l=[-4,3,5,6,9,0,2,-3,8,4,7,2,19,-45,14]
full=dev(l,4)
print(sorting(full))

