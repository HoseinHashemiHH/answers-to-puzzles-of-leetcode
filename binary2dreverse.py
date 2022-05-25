



# binary to decimal, decimal to binary
from decimal import Decimal
from encodings import utf_8
from unicodedata import decimal
from numpy import unicode_

from pyparsing import Char


def get_n():

    while True:
        try:
         n=int(input('''please enter your number: '''))
        except:
         print('please enter a round number: ')
         continue
        break
    return n
import sys
def binary(h):
    return bin(h)
def decimall(h):
    total=0
    h1=h.replace('0b','')
    h2=[int(s) for s in h1]
    h2.reverse()
    for i in range(len(h2)):
        total+=2**i*h2[i]
    return int(total)

n=get_n()
f=binary(n)
print(f)
print(decimall(f))
