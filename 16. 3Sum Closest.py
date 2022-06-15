# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

 

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0

def sum3closest(ar,tg):
    m=[100000000]
    c=10
   

    for i in range(0,(len(ar))//2-1):
        for j in range(len(ar)-1,-1,-1):
            k=0
            while k<len(ar):
                
                if i!=j and j!=k and i!=k:
                   print(i,j,k)
                   h=abs(ar[i]+ar[j]+ar[k]-tg)
                   if h<min(m):
                       c=ar[i]+ar[j]+ar[k]
                       m.append((h))
                   
                k+=1
    return c
            
nums = [-1,2,1,-4,6,7]; target = 1       
x=sum3closest(nums,target)     
print(x) 