#Change Return Program - The user enters a cost and then the amount of money#
# given. The program will figure out the change and the number of quarters, dimes,#
# nickels, pennies needed for the change.#
def get_n():

    while True:
        try:
         c=int(input('''please enter your cost'''))
         g=int(input('''please enter your given money'''))
         
        except:
         print('please enter a round number: ')
         continue
        break
    return (c,g)
def ch_return(c=100,g=80):
    n_n,n_d,n_q=0,0,0
    r=c-g
    q=r%25
    n=r%5
    d=r%10
    p=r%5
    b=r-r%5
    if b%25==0:
        n_q=b/25
    elif b%10==0:
        n_d=b/10
    elif b%5==0:
        n_n=b/5
    else:
        pass
    return (n_n,n_d,n_q,p)
c1,g1=get_n()
nickle,dime,quarter,p=ch_return(c1,g1)
print(nickle,dime,quarter,p)

     

