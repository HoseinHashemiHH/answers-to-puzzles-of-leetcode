


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]


from ctypes import sizeof
from ctypes.wintypes import SIZE
import math
def find_order_tree(root:list):
    n=len(root)
    k=int(math.log2(n+1))
    result=[]
    j=0
    i=0
    while i<len(root) and j<=k:
               result.append(root[i:i+ 2**j])
               i=2**j
               j+=1
    res=[[] for j in range(len(result))]
    for i in range(len(result)):
        for j in result[i]:
            if j!='null':
                res[i].append(j)
    return result ,res
def cmd_line():
    root = [3,9,20,'null','null',15,7,'null','null','null','null','null','null','null','null',1,2,3,4,1,2,3,4]
    r,res=find_order_tree(root)
    print(r,res)
cmd_line()