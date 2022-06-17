l={'[':1, ']':-1,'(':2,')':-2,'{':3,'}':-3}
def strtrue(str):
    n=len(str)
    for i in range(n-1,0,-2):
        print(i)
        if l[str[i]]!=-l[str[i-1]]:
            return False
    return True
