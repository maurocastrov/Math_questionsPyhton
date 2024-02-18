
import math
import cmath
def poli(x):
        return x*math.log10(x) -(1/2) 

def deri(x):
    return math.log10(x) + 1/math.log(10, math.e) 
print ("Método de Newton-Raphson")
x=3
erroru=0.0000001
raiz=[ ]
raiz.insert(0,0)
i=0
error=1
while abs(error) > erroru:
    x1=x-(poli(x)/deri(x))
    raiz.append(x1)
    i=i+1
    x=x1
    error=(raiz[i]-raiz[i-1])/raiz[i]
    print(x) 
    
