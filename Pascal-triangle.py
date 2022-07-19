

def pascal_triangle(rownum:int):
  kandoo=[[]for i in range(rownum)]
  kandoo[0].append(1)
  kandoo[1].extend([1,1])
  for r in range(2,rownum):
    for i in range(r+1):
      if i==0 or i==r:
        kandoo[r].append(1)
      else:
        kandoo[r].append(kandoo[r-1][i-1]+kandoo[r-1][i])
        print(i,r)
  return kandoo

def cmdline():
  k=pascal_triangle(7)
  print(k)

cmdline()
