from math import exp
import time
# Codé par Hubert LEROUX & Léopold BERNARD ®

def eulerMethod(n,d = 100000):
    """
    Renvoie la valeur de exp(n)
    """
    if n < 0: # par définition : e^(-n) = 1/(e^n)
        # mouvement illégal : on utilise des propriétés de e^n avant de la définir :(
        return 1/(eulerMethod(-n, d))
    # ON commence en sachant que exp(0)=1
    x = 0
    y = 1
    while x < n:
        y=y*(1+1/d)
        x+=1/d
    # Ceci revient à faire (1+1/d)^(d*n) = ((1+1/d)^d)^n = e^n
    # On retrouve la formule lim (n->+inf) de (1+1/n)^n = e
    # Trop stylé !
    return y 

def artithmeticMethodWithExpoRapide(x, precision=50):
    """
    On implémente ici la limite vu en cours:
    exp(x) = lim(n->+inf) de (1+x/n)^n
    ici n = 2^precision
    """
    assert precision <= 50, "La précision doit être inférieure ou égale à 50, au delà les nombres sont trop grands"
    y = (1+x/(1<<precision))
    for _ in range(precision):
        y = y * y 
    return y

def fastExponetiation(x,n):
    pass


def taylorSerieMethod(x,precision=100):
    """
    https://www.youtube.com/watch?v=O85OWBJ2ayo
    e^x = x^0 + x^1 (1/2)*x^2 +(1/6)*x^3 ...
    e^x = (somme de i=0 à n) de (1/i!)^i
    """
    ans = 1 # On a déjà x^0
    n = 1   # Le factoriel devant
    powerOfX = 1 # x^0
    for i in range(1,precision+1):
        powerOfX *= x
        n *= i
        ans += powerOfX/n
    return ans
    

def timeComputation (method_name, method, N) :
    start = time.time()
    computedExp = method(N)
    print(f"{method_name} :\n\tANSWER : {computedExp}\n\tTIME: {time.time()-start} seconds\n")


if __name__ == '__main__':
    # Petit script pour calculer exp(X) avec les différentes méthodes
    X = 1
    timeComputation("Bibliothèque mathématique de l'ordinateur", exp, X)
    timeComputation("Méthode de la suite de taylor", taylorSerieMethod, X)
    timeComputation("Méthode d'Euler implémentée", eulerMethod, X)
    timeComputation("Méthode d'exponentiation rapide", artithmeticMethodWithExpoRapide, X)