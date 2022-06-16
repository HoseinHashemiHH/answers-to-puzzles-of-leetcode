#17. Letter Combinations of a Phone Number




import itertools


def str2alphabet(phone):
    dic_ph={'2':'abc','3':'def','4':'ghi','5':'klm', '6':'nop','7':'qrs','8':'tuv','9':'wxyz'}
    list=[]
    for ph in phone:
        list.append(dic_ph[ph])
    list1=[]
    str=''
    if len(phone)>1:
      for i in range(0,3):
        str=list[0][i]
        k=0
        while k<3: 
            for x,l in enumerate(list):
               if x!=0: 
                  str+=l[k]
                  list1.append(str)
                  str=list[0][i]
            k+=1

      return list1
    else:
        return [x for x in dic_ph[phone]]
            

list_r=str2alphabet('2')
print(list_r)




    

    