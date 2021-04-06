"""
Ce code a pour but de calculer l'image de x par les fonctions cos, sin et tan
"""
from math import sin, cos, tan, pi # On les importent pour la comparaison
import time

ZERO = 1e-15

def compare(f1, f2, f1Name, f2Name, X):
    for f, name in [(f1, f1Name), (f2, f2Name)]:
        start = time.time()
        print(f"Testing {name} with {X}")
        print(f"\tResult:\t{f(X)}")
        print(f"\tTime:\t{time.time()-start}")



#* https://fr.wikipedia.org/wiki/S%C3%A9rie_de_Taylor

def my_cos1(x, precision=50):
    """
    Retourne le cos d'un nombre
    """
    x = x % (2*pi)
    rep = 0
    inv_coef = 1    
    X = 1
    x2 = x**2
    for i in range(0, precision+1):
        rep += X/inv_coef
        inv_coef *= -(2*i+1)*(2*i+2)
        X*=x2
    if abs(rep)<ZERO:
        return 0
    return rep

def my_cos2(x, precision=100):
    x = x % (2*pi)
    rep = 0
    coef = 1    
    X = 1
    x2 = x**2
    for i in range(0, precision+1):
        rep += coef * X
        coef /= -(2*i+1)*(2*i+2)
        X*=x2
    if abs(rep)<ZERO:
        return 0
    return rep

def factIterative(n):
    if n<2:
        return 1
    rep = 1
    for i in range(2, n+1):
        rep*=i 
    return rep

def fastExpo(a,b):
    assert a >=0 and b>=0
    p=0
    p2 = 1  # 2^p
    ap2 = a # a ^ (2 ^ p)
    result = 1
    while b > 0:
        if p2 & b > 0:
            b-=p2
            result = (result*ap2)
        p+=1
        p2*=2
        ap2 = ap2 * ap2
    return result


def my_cos3(x, precision=50):
    x = x % (2*pi)
    rep = 0
    for i in range(0, precision+1):
        if i%2 == 0:
            rep+=fastExpo(x,2*i)/factIterative(2*i)
        else:
            rep-=fastExpo(x,2*i)/factIterative(2*i)
    if abs(rep)<ZERO:
        return 0
    return rep

def my_sin1(x, precision=20):
    """
    Retourne le cos d'un nombre
    20 suffit largement
    """
    x = x % (2*pi)
    rep = 0
    inv_coef = 1    
    X = x
    x2 = x**2
    for i in range(0, precision+1):
        rep += X/inv_coef
        inv_coef *= -(2*i+2)*(2*i+3)
        X*=x2
    if abs(rep)<ZERO:
        return 0
    return rep


def my_tan(x, precision=20):
    """
    Retourne le cos d'un nombre
    20 suffit largement
    """
    x = x % (2*pi)
    s = my_sin1(x)
    c = my_cos1(x)
    if c==0:
        return float("inf")
    rep = s/c
    if abs(rep)<ZERO:
        return 0
    return rep


if __name__ == "__main__":
    # print(pi/2)
    # print(my_cos1())
    for X in [pi/4, pi/6, pi/2, pi/3]:
        compare(sin, my_sin1, "SIN DE PYTHON", "MON SIN", X)
        print()
    for X in [pi/4, pi/6, pi/2, pi/3]:
        compare(tan, my_tan, "TAN DE PYTHON", "MON TAN", X)
        print()