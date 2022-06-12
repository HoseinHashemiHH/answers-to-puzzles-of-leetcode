


def x20(ar,x):
    rx=x
    ar_new=[]
    i=0
    while rx!=0 and len(ar)>=1:
      print(ar)
      if ar[-1]<=rx and ar[0]<=rx:
          mx=max(ar[-1],ar[0])
          indx=ar.index(mx)
          rx=rx-mx
          ar.pop(indx)
          i+=1
      elif ar[-1]<=rx and ar[0]>=rx:
          rx=rx-ar[-1]
          ar.pop(ar[-1])
          i+=1
      elif ar[-1]>=rx and ar[0]<=rx:
          rx=rx-ar[0]
          ar.pop(0)
          i+=1
      else:
        return -1,rx
    return i,rx
s=x20([3,2,20,1,1,3],10)
print(s)
    