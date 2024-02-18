a = 1.2
b = 1.1

Yn = a/b
Yn1 = 0
Xn = 0
h = 0.1

def f(x, y):
    return -2/a * x * y
print("Рунге -Кутта второй степени")
while Xn < 1:
    Yn1 = Yn + h * f(Xn, Yn)
    k1n1 = f(Xn + h, Yn1)
    k2n1 = f(Xn + h, Yn1 - h * k1n1)
    Yn1 = Yn + h/2 * (k1n1 + k2n1)
    print(Yn)
    
    Yn = Yn1
    Xn += h
    
    
Yn = a/b
Yn1 = 0
Xn = 0
print()
print('Рунге Кутта третьей степени')
while Xn < 1:
    k1n = f(Xn, Yn)
    k2n = f(Xn + h/2, Yn + h/2 * k1n)
    k3n = f(Xn + 3/4 * h, Yn + 3/4 * h * k2n)
    Yn1 = Yn + h/9 * (2 * k1n + 3 * k2n + 4 * k3n)
    
    print(Yn)
    Yn = Yn1
    Xn += h

Yn = a/b
Yn1 = 0
Xn = 0
print()
print('Рунге -Кутта четвертой степени ')
while Xn < 1:
    k1n = f(Xn, Yn)
    k2n = f(Xn + h/2, Yn + h/2 * k1n)
    k3n = f(Xn + h/2, Yn + h/2 * k2n)
    k4n=  f(Xn + h,Yn+k3n )
    Yn1 = Yn + h/6 * ( k1n + 2 * k2n + 2 * k3n + k4n)
    print(Yn)

    Yn = Yn1
    Xn += h    

Yn = a/b
Yn1 = 0
Xn = 0
print()
print('Рунге - Кутта третьей степени ')

while Xn < 1:
    k1n = f(Xn, Yn)
    k2n = f(Xn + h/3, Yn + h/3 * k1n)
    k3n = f(Xn + 2*h/3, Yn + 2*h/2 * k2n)
    Yn1 = Yn + h/4 * ( k1n +  3 * k3n )
    print(Yn)
    
    Yn = Yn1
    Xn += h    