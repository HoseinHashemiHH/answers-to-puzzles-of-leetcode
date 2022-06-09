

import numpy as np
array1=[1,2,-2,3,2,9,-11,5,2.5,6,-5]
array2=[3,4,-5]
array1.sort()
array2.sort()
array1.extend(array2)
if len(array1)%2:
    med=array1[len(array1)//2]
else:
    med=(array1[len(array1)//2]+array1[len(array1)//2-1])/2
print(array1,'\n',len(array1),'\n',med)

