import numpy as np
type intervalx = tuple[float, ...]

def f1(x):
    return np.exp(0.5*x)

def f2(x):
    return 1/(1+25*x)

def input1():
    # Input data
    x0 = 0
    x = 1
    interval = 5
    # Olahan input
    h = (x-x0)/interval
    t = (x-x0)/h
    a = tuple(round(0.0 + (h * i), 2) for i in range(interval + 1))

    return Forward(h, t, interval, a)

def tail(a):
    return a[1:]
def head(a):
    return a[:-1]

# 1. Polinom Newton Maju (Forward) – grid seragam, dekat ujung kiri

def fk(t,n):
    if n == 0:
        return 1
    else:
        tf = 1
        for a in range(n):
            tf *= (t - a)
        return tf
    
def delta(i, a, fx = f1):
    if i == 0:
        return fx(a[0])
    if i == 1:
        return fx(a[1]) - fx(a[0])
    else:
        return delta(i - 1, tail(a), fx) - delta(i - 1, head(a), fx)

def Forward(h, t, i, a:intervalx, fx = f1):
    r = 0
    f =(fk(t,i)/fk(i,i))*(delta(i, a, fx))
    if i == 0:
        return f
    else:
        return f + Forward(h, t, i-1 ,a , fx)

print(input1())

# 2. Polinom Newton Mundur (Backward) – grid seragam, dekat ujung kanan
# 3. Polinom Lagrange – grid umum (seragam/tidak seragam)
# 4. Metode Neville – evaluasi rekursif polinom interpolasi untuk satu titik (stabil)