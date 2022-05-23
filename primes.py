from statistics import mode


def get_n():

    while True:
        try:
         n=int(input('''please enter your number you need to end with the primes: '''))
        except:
         print('please enter a round number: ')
         continue
        break
    return n

def primes(n):
    primes=[2,3,5,7,11]
    
    for i in range(13,n):
        for p in primes:
            if i%p==0:
                break
            elif p==primes[-1]:
                primes.append(i)
                break
            else:
                continue
    print('primes are:\n')
    for p in primes:
        print(p)
n=get_n()
primes(n)
            


