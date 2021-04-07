import time
import math

from eulerMethod import taylorSerieMethod

# e = taylorSerieMethod(1)
e = math.exp(1)
# print(e)

def compare(f1, f2, f1Name, f2Name, X):
    """
    Permet de comparer deux fonctions
    param f1: Première fonciton
    param f2: Deuxième fonciton
    param f1Name: Le nom de la première fonction
    param f2Name: Le nom de la seconde fonction
    param X: la valeur à calculer
    """
    for f, name in [(f1, f1Name), (f2, f2Name)]:
        start = time.time()
        print(f"Testing {name} with {X}")
        print(f"\tResult:\t{f(X)}")
        print(f"\tTime:\t{time.time()-start}")

def fastExpo(base, nb):
    """
    Retourn a^b
    """
    if nb <0:
        return 1/fastExpo(base, -nb)
    assert base>=0
    p=0
    p2 = 1  # 2^p
    ap2 = base # a ^ (2 ^ p)
    result = 1
    while nb > 0:
        if p2 & nb > 0:
            nb-=p2
            result = (result*ap2)
        p+=1
        p2*=2
        ap2 = ap2 * ap2
    return result


def dichotomicLog1(x,base=e, precision = 0.00001):
    """
    Retourne y tq base^y = x
    """
    assert base > 0 and x > 0, "Erreur dans les valeurs données en input"
    inf = -1
    sup = +1
    # On trouve la bonn borne pour inf
    while fastExpo(base, inf) > x:
        inf *= 2

    while fastExpo(base, sup) < x :
        sup *= 2

    #Maintenant que l'on a nos bornes, on peut travailler
    while sup-inf > precision:
        # On continue
        middle = (sup+inf) / 2
        # Maintenant, on distingue deux cas
        #* base < 1  alors la fonciton f:x -> base^x est décroissante !
        if base < 1:
            if fastExpo(base, middle) < x : # i.e. y<middle
                inf = middle
            else :
                sup = middle
            
        #* base > 1  alors la fonciton f:x -> base^x est croissante !
        else:
            if fastExpo(base, middle) > x :
                sup = middle
            else :
                inf = middle
    return (sup+inf)/2


def dichotomicLog2(x,base=e, precision = 0.00001):
    """
    Retourne y tq base^y = x
    """
    assert base > 0 and x > 0, "Erreur dans les valeurs données en input"
    if x==1:
        return 0
    inf = -1
    sup = +1
    # On trouve la bonn borne pour inf
    while math.pow(base, inf) > x:
        inf *= 2

    while math.pow(base, sup) < x :
        sup *= 2
    # print(inf, sup)
    #Maintenant que l'on a nos bornes, on peut travailler
    while sup-inf > precision:
        # On continue
        middle = (sup+inf) / 2
        # Maintenant, on distingue deux cas
        #* base < 1  alors la fonciton f:x -> base^x est décroissante !
        if base < 1:
            if math.pow(base, middle) < x : # i.e. y<middle
                sup = middle
            else :
                inf = middle
            
        #* base > 1  alors la fonciton f:x -> base^x est croissante !
        else:
            if math.pow(base, middle) > x :# i.e. y>middle
                sup = middle
            else :
                inf = middle
    return (sup+inf)/2

    

def my_ln_with_taylor_serie(x, precision=1000000):
    """
    Calculer le logarithme népérien d'un nombre à l'aide de la série de taylor 
    https://fr.wikipedia.org/wiki/S%C3%A9rie_de_Taylor
    (fonctionne seulement pour -1 < x <= 1, donc si x>1, on calculer -ln(1/x) = ln(x))
    """
    assert x>0
    if x == 1:
        return 0
    if x > 1: # car la formule fonctionne seulement pour -1 < x <= 1
        return -my_ln_with_taylor_serie(1/x)

    x -= 1 # PUisqu'on va calculer ln(1+x)
    X = x 
    rep = 0

    for n in range(1, precision+1):
        coef = 1/n
        if n%2 == 0:
            rep -= coef*X
        else:
            rep += coef*X
        X *= x  
    return rep



if __name__ == '__main__':
    # print(fastExpo(2,-5))
    # for X in [0.1,0.5,1,100,math.exp(5), math.exp(10)]:
    #     compare(math.log, my_ln_with_taylor_serie, "ln de la librairie", "mon ln", X)
    #     print()
    for X in [0.1,0.5,1,100,math.exp(5), math.exp(10)]:
        compare(math.log, dichotomicLog2, "ln de la librairie", "ln dichotomique", X)
        print()