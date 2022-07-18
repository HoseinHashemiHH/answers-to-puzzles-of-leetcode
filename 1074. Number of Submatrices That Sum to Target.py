

# Given a matrix and a target, return the number of non-empty submatrices that sum to target.
def sub_to_get_target(matrix:list,target:int)->int:
    m=len(matrix)
    n=len(matrix[0])
    sub=[]
    l,k=m,n
    #for i in range(m):
        # while l<m:
        #     sub.append(matrix[i:i+l][:])
        #     l+=1
        #for j in range(n):
            # sub.append(matrix[i][j])
            # sub.append(matrix[i][:])
            # if i==0:
            #     k=0
            #     while k<n:
            #        sub.append(matrix[:][j:j+k])
            #        if j==0:
            #         sub.append(matrix)
            #         k+=1
    p11,p12=0,0
    while p11<m and p12<n: 
                for i in range(l):
                   for j in range(k):
                     sub.append(matrix[p11:i][p12:j])
                p11+=1
                p12+=1
                l-=1
                k-=1
    total=0
    t=0
    for babysub in sub:
        for i in range(len(babysub)):
            for j in range(len(babysub[0])):
                       total+=babysub[i][j]
        if total==target:
            t+=1
    return t

def cmd_line():
    # matrix = [[1,-1],[-1,1]]; target = 0
    matrix = [[0,1,0],[1,1,1],[0,1,0]]; target = 0
    number=sub_to_get_target(matrix,target)
    print(number)
cmd_line()



            





            
