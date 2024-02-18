
import math
import cmath
def poli(x):
        return x*math.log10(x) -(1/2)  

print ("Эта программа находит рут, методом бисекции")
xi=0.1
xs=2
error=.01
xa=(xi+xs)/2
i=0
print('{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}'.format('i','xi','xs','xa','знак','изменение','эпсилон'))
while abs(poli(xa) ) > error:
	i=i+1
	xa = (xi+xs)/2.0
	if poli(xi)*poli(xa) < 0:
		xs=xa
		signo="negative"
		limite="выше"

	else:
		xi=xa
		signo="positive"
		limite="ниже"
	print('{:^10}{:^10.4f}{:^10.4f}{:^10.4f}{:10}{:^10}{:^10.4f}'.format(i,float(xi),float(xs),float(xa),signo,limite,float(poli(xa))))	
print("корень: ",xa)
