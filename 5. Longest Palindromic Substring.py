


def parl(pp):

       for p in range(0,len(pp)):
           if pp[p]==pp[-1-p]:
             if p==len(pp)-1:
               #pps.append(ps)
               return True
             else:
                 continue
           else:
            break
       return False

str1=str(input('your text is:\n '))
l=0
ps=[]
pps=[]
pps=str1.split()
for pp in pps:
    if parl(pp):
        if len(pp)>2:
          ps.append(pp)



#pp=max([len(pp) for pp in pps])
print(ps, max([len(p) for p in ps]))
        

