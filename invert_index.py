
import pwd

from numpy import number


print(pwd)
f0=open('file1.txt','w')
f1=open('file2.txt','w')
f2=open('file3.txt','w')
f0.write('he is a good person. whose name is Davide.')
f1.write('his phone number is 775-599-9201.')
f2.write('mostoften he is watching TV.')
f0=open('file1.txt','r')
f1=open('file2.txt','r')
f2=open('file3.txt','r')
text0=f0.read()
text1=f1.read()
text2=f2.read()
text=text0+text1+text2
print(text)
import re
from re import search
a=input('what do you want form David? (number-sexuality)')
if a=='number':
    match=re.search('\d{3}-\d{3}-\d{4}', text)
    print(match.group())
else:
    match=re.findall('he|his', text)
    print(match)

