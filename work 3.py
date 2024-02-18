from math import cos
from sympy import *

def mol(a,b,n):
    s = 0
    h = round((b-a)/n,5)
    i = a
    while i <= b:
      
        if i == a or round(i,5) == b:
            s = s + f.subs(x,i)
        else:
            s = s + 2*f.subs(x,i)
        
        i+=h
    s = (h/2)*s
    return s       

a = 0.1
b = 0.6
n = 5
e = 0.00001
c=0

var('x')
var('f')
f = (4*x) - cos(x)
while abs(mol(a,b,n)-mol(a,b,2*n))>e:
    c=c+1
    n = 2*n
print(mol(a,b,n))
print( "количество итераций:",c,"раз" )

