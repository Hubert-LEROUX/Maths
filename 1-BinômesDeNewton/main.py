import sympy
import pprint
import time
import sys

sys.setrecursionlimit(10000)


# def factoriel(n):
#     if n <= 1:
#         return 1
#     return factoriel(n-1)*n

def fact (n, r=1) :
    if n <= 1 :
        return r
    else :
        return fact(n-1, r*n)

def combinaison(k, n):
    """
    Calcule k parmi n
    """
    return fact(n)/(fact(n-k)*fact(k))

def develop (n) :
    """
    Retourne une liste 1D des facteurs de (a+b)^n
    """
    return [combinaison(k, n) for k in range (n+1)]

def power(a, b, n) :
    """
    Retourne (a+b)^n
    """
    expr = f''
    coefs = develop(n)
    expr += f'{coefs[1]}*a**{n}+'
    for i in range (1, len(coefs)-1) :
        expr += f'{coefs[i]}*a**{n-i}*b**{i}+'
    expr += f'{coefs[-1]}*b**{n}'
    print(expr)


def powerPretty(a, b, n) :
    """
    Retourne (a+b)^n
    """
    x = sympy.Symbol(a)
    y = sympy.Symbol(b)
    expr = f''
    coefs = develop(n)
    expr += f'{coefs[0]}*{x}**{n}+'
    for i in range (1, len(coefs)-1) :
        expr += f'{coefs[i]}*{x}*{n-i}*{y}**{i}+'
    expr += f'{coefs[-1]}*{y}**{n}'
    equ = sympy.sympify(expr)
    sympy.pprint(equ)
    return None

powerPretty("a","b",2)

def powerB(a, b, n):
    """
    Retourne (a+b)^n
    """
    x = sympy.Symbol(a)
    y = sympy.Symbol(b)
    equ = sympy.sympify(f'({x}+{y})**{n}')
    equ = sympy.expand(equ)
    sympy.pprint(equ)
    return None
# powerB ('a', 'b', 5)

def trianglePascal(N):
    """
    Retourne une liste 2D du triangle de Pascal contenant N lignes
    """
    triangle = [[1]]
    for indice_ligne in range(1,N):
        previous_line = triangle[-1]
        new_line = []
        for indice in range(len(previous_line)+1) :
            if indice == 0 or indice==len(previous_line): # Si on est au début ou à la fin, on renvoie un 1
                number = 1
            elif 0< indice < len(previous_line): # Sinon on calcule
                number = previous_line[indice-1]+previous_line[indice]
            new_line.append(number)
        triangle.append(new_line)
    return triangle
    
def trianglePascalRecursif (n, s=[[1]]) :
    if n==0 :
        return s
    else :
        s.append([1] + [s[-1][i]+s[-1][i+1] for i in range (len(s[-1])-1)] + [1])
        return trianglePascalRecursif(n-1, s)

# comparaison des 2 méthodes de triangles de Pascal
# N=1000
# startNormal = time.time()
# _ = trianglePascal(N)
# print(f"Version normale: {N} lignes en {time.time()-startNormal}")
# startRecursif = time.time()
# _ = trianglePascalRecursif(N)
# print(f"Version Récursive: {N} lignes en {time.time()-startRecursif}")




# sympy.pprint(sympy.Integral(sympy.sqrt(1/x), x), use_unicode=True)
# equ = sympy.sympify('x**5+3*x**2')
# sympy.pprint(sympy.Integral(sympy.sqrt(1/x), x), use_unicode=True)
# sympy.pprint(equ)
# sympy.pprint(equ, use_unicode=True)
