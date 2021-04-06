import sys
from math import log

def calculeAire(a,b,function, n=1000):
    """
    Renvoie l'aire sous la courbe function
    n est la découpe
    l'approximation est d'amplitude 1/n
    """
    # Calculons u_n
    somme = 0
    delta = abs(b-a)
    for k in range(1,n+1):
        somme += function(a+(delta*(k/n)))
    u_n = somme/n * delta

    print(f"L'aire D sous la courbe est comprise entre : {u_n} <= A(D) <= {u_n+(1/n)}")

if __name__ == '__main__':
    calculeAire(0,17,lambda x: (x**1.5), 1000000)
    # print(log(6))