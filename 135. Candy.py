# Example 1:

# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

# Example 2:

# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two conditions.

def candy_giving(childs_rate:list)->int:
    out=0
    # mx=max(childs_rate)
    for x,c_r in enumerate(childs_rate):
        out+=1
        rnum=c_r
        if len(childs_rate)>1 and x==0 and rnum>childs_rate[x+1]:
            out+=1
        if x==len(childs_rate)-1 and rnum>childs_rate[x-1]:
            out+=1
        if 1<=x<=len(childs_rate)-2:
            if (childs_rate[x-1]<rnum and rnum>=childs_rate[x+1]) or (childs_rate[x-1]<=rnum and rnum>childs_rate[x+1]):
                out+=1
    return out

def new_func(out):
    out+=1

def cmd_line():
    ratings = [1,2,3,8,6,9,3]
    c=candy_giving(ratings)
    print(c)
cmd_line()


