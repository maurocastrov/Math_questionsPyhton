import math
import cmath

def function(x):
        return x*math.log10(x) -(1/2) 
xn1 = 1
xn =  3
precision = 0.0000001
x = xn1
if(function(xn1) * function(xn) < 0):
  while(abs(function(x)) > precision):
    print("X: ", x, " f(x): ", function(x))
    x = xn - ((function(xn) * (xn - xn1)) / (function(xn) - function(xn1)))
    xn1 = xn
    xn = x