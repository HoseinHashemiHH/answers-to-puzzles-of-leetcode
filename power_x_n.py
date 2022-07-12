


def pow_x_n(x:int,n)->int:
    
    if n>0:
        y=1
        for i in range(n):
            y*=x
        return y
    elif n<0:
        y=1
        for i in range(-n):
            y=y*1/x    
        return y
    elif n==0:
        return 1
    else:
        pass

                   
def cmd_line():
    booli=pow_x_n(3,-2)
    print(booli)
cmd_line()
