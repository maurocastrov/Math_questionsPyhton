from math import sqrt
x = [90 , 102,87,114,114.8,90,116,107,93,176,96,92,176,74,106,88,74,74.7,115,92,110]
y = [24.5,27.3,41,31,35.6,46,35,42.7,27,75,38,23.5,65,23,45.5,34,23,26,37,30,43]
n = len(x)
e = 0.0001

x1 = 0 
fg = 0 
xfg = 0 
xx1 = 0 
sy = 0
sx = 0
r = 0
A = 0
for i in range(n):
   
    x1 += x[i]
    fg += y[i]
    xfg += x[i]*y[i]
    xx1 += x[i]*x[i]
x1 = x1 / n
fg = fg / n 
xfg = xfg / n 
xx1 = xx1 / n 
print(x1,fg,xfg,xx1)
a = (xfg - fg*x1) / (xx1 - x1*x1)
b = fg - a * x1
print('A=',a,'B=',b)
for i in range(n):
    sx = sx + (x[i] - x1)*(x[i] - x1)
    sy = sy + (y[i] - fg)*(y[i] - fg)
    A = A + abs((y[i] - (a*x[i]+b))/y[i])
sx = sqrt(sx/n)
sy = sqrt(sy/n)
A = 100/n*A
print('A =' ,A)
for i in range(n):
    r = r + (x[i]-x1)*(y[i]-fg)
r = r/(n*sy*sx)
print('R =',r)