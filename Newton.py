import math
import cmath

def function(x):
        return x*math.log10(x) -(1/2) 
xn1 = 0.1
xn =  2
эпсилон = 0.000001
x = xn1
if(function(xn1) * function(xn) < 0):
  i=0
  while(abs(function(x)) > эпсилон):
    i=i+1
    print("X: ", x, " f(x): ", function(x))
    x = xn - ((function(xn) * (xn - xn1)) / (function(xn) - function(xn1)))
    xn1 = xn
    xn = x
  print( "количество итераций:",i,"раз" ) 
