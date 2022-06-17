

def newarray(ar,n):
    ar.pop(-n)
    new=ar
    return new
head = [1,2,3,4,5]; n = 2
x=newarray(head,n)
print(x)
