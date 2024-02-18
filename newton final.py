import math
import cmath

def poli(x):
       logaritmo = math.log10(x)
       y=x*logaritmo -(1/2) 
       return (y)

def deri(x):
    d=logaritmo + 1/ln(10)
    return (d)

print ("Método de Newton-Raphson")
x=1 
erroru=float(input(.0001))
raiz=[ ]
raiz.insert()
i=4
error=1
while abs(error) > erroru:
    x1=x-(poli(x)/deri(x))
    raiz.append(x1)
    i=i+1
    x=x1
    error=(raiz[i]-raiz[i-1])/raiz[i]
print (x1)
