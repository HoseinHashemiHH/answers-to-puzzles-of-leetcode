

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

#     I can be placed before V (5) and X (10) to make 4 and 9. 
#     X can be placed before L (50) and C (100) to make 40 and 90. 
#     C can be placed before D (500) and M (1000) to make 400 and 900.

# Given an integer, convert it to a roman numeral.
def int2rmn(num):
    st=''
    if num//1000!=0:
        st+='M'*(num//1000)
        num-=(num//1000)*1000
    if num//900!=0 and num//900<100:
        st+='CM'
        num-=900
    if num//500!=0:
        st+='D'*(num//500)
        num-=(num//500)*500
    if num//400!=0 and num//400<1000:
        st+='CD'
        num-=400
    
    if num//100!=0:
        st+='C'*(num//100)
        num-=(num//100)*100
    if num//90!=0 and num//90<10:
        st+='XC'
        num-=90              
    if num//50!=0:
        st+='L'*(num//50)
        num-=(num//50)*50
    if num//40!=0 and num//40<10:
        st+='XL'
        num-=40   
    if num//10!=0:
        st+='X'*(num//10)
        num-=(num//10)*10
    if num//9!=0:
        st+='IX'
        num-=9 
    if num//5!=0:
        st+='V'*(num//5)
        num-=(num//5)*5
    if num//4!=0:
        st+='IV'
        num-=4
    if num//1!=0:
        st+='I'*(num//1)
    return st
# Input: num = 1994
# Output: "MCMXCIV"
x=int2rmn(1994)
print(x)
