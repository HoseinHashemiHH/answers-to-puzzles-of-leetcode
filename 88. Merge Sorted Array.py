




import numpy as np


def array(n,m):
  nums1=[x for x in range(n+m)]
  nums2=[y for y in range(m)]
  nums1.sort(reverse=True)
  nums2.sort(reverse=True)
  for i in range(n,len(nums1)):
      nums1[i]=0
  for i in range(n,len(nums1)):
      nums1.remove(0)
  for i in nums2:
      nums1.append(i)
  nums1.sort(reverse=True)
  print(nums2,nums1)

if not __name__=="main":
      array(7,9)
      
  
      