


#Input: matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
#Output: [1,2,3,4,8,12,11,10,9,5,6,7]
import numpy as np
def spiral_order(matrix:list):
    #mat1=np.array(matrix)
    m=len(matrix)
    n=len(matrix[0])
    output=[]
    N,M,h,g=n,m,0,0
    while N>=0 and M>=0:
        for i in range(N):
           output.append(matrix[h][i])
        for j in range(1,M):
           output.append(matrix[j][-1-g])
        for k in range(N-2,-1,-1):
           output.append(matrix[-1-g][k])
        if m>3:
           for z in range(M-2,0,-1):
               output.append(matrix[z][h])
        if len(output)>=n*m:
            break   
        h+=1
        g+=1
        N-=1
        M-=1
    return output[:n*m]
def cmd_line():
    matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
    o=spiral_order(matrix)
    print(o)
cmd_line()

    

