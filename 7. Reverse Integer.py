


p=input('enter your digit round number with + or -?  ')
if int(p) not in range(-2**31,2**31-1):
    s=0
else:
  s=p[::-1]
  if s[-1]=='-':
    s1=s[-1]+s
    s=s1[:len(s1)-1]
  if s[-1]=='+':
    s1=s[-1]+s
    s=s1[:len(s1)-1]
print(s)  

    

# l1=[]
# l1=l.reverse()
# print(type(l1))
# a=l.pop(0)
# l1.append(a)
# rnum=''.join(l1)


