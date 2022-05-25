




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

def sumsr(x):

    x1=[int(a) for a in x]
    
    t=0
    for i in x1:
        t+=i**2
    return t

def happy(y):
        z = []
        z.append(sumsr(y))

        for i in range(1,10):
            z.append(sumsr(str(z[i-1])))
        if 1 not in z:
            print('{y} is happy number')
        else:
            print('{y} is not a happy number')
        print(z)



print(sumsr('62'))
x=get_n()
print(type(x))
print(happy(x))


    
