

str1=str(input('your text is:\n '))
def l_wo(str1):
    stp=''
    for st in str1:
        if st in stp:
            break
        else:
            stp+=st
    return len(stp)

l1=l_wo(str1)
print(l1)