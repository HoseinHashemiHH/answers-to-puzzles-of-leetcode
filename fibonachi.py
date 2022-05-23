
def get_n():

    while True:
        try:
         n=int(input('''please enter your number you need to end with the fibonachi serie: '''))
        except:
         print('please enter a round number: ')
         continue
        break
    return n
def fibo(a=1,b=1,n=100):
    fibon=[]
    fibon[0:1]=[1,1]
    for i in range(2,n):
        fibon.append(fibon[i-1]+fibon[i-2])
    print('your resulted fibonachi seri is:\n')
    for f in fibon:
        print(f)
n=get_n()
fibo(1,1,n)