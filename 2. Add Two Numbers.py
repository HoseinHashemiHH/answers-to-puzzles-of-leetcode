
import random
n=3
a=[random.randint(0,9) for i in range(n)]
b=[random.randint(0,9) for i in range(n)]
num_a=0
for i,aa in enumerate(a):
    num_a+=aa*10**i
num_b=0
for i,bb in enumerate(b):
    num_b+=bb*10**i
print(a,b,num_a+num_b)