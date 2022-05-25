

#'''Collatz Conjecture - Start with a number n > 1. Find the number of steps
#it takes to reach one using the following process: If n is even,
#divide it by 2. If n is odd, multiply it by 3 and add 1.

def get_n():

    while True:
        try:
         n=input('''please enter your number ''')
        except:
         print('please enter a round number: ')
         continue
        break
    print(type(n))
    return n

def even(n):
    if int(n)%2==0:
        return True
    else:
        return False
def alg_one(n):
        n=int(n)
        i=0
        while n>1:
         if even(n):
             n=n/2
             i+=1
         else:
             n=n*3+1
             i+=1
         if n==1:
             break
        return i
x=get_n()
p=alg_one(x)
print(p)
        
        
