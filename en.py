

import math
while True:
   try:
    i=int(input("your favourite float numbers of e is: "))
   except:
    print("please write a digit without percision: ")
    continue
   break
def perc_num(x):
    print('{} is e with {} percision number'.format(round(math.e,x), x))

perc_num(i)