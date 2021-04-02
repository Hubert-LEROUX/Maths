from math import sqrt, pi
import time

def approximatePiWithNewton(precision=20):
    """
    Il faut calculer l'intégrale entre 0 et 1/2 de (1-x^2)^(1/2)
    """
    n = 0.5

    integral = 0
    coef = 1

    # On intègre de 0 à 1/2
    x = 0.5
    X = -0.25
    powerOfX = 0.5

    for i in range(precision+1):
        #* Calcul
        integral += coef * (powerOfX/(2*i+1)) # On ajoute à la somme le terme coefficient * x^d/d où d est la puissance de x

        #$ Arrangement des futurs coefficients
        powerOfX *= X # Puissance siuvante de x2
        coef *= ((n-i)/(i+1))
        # print(coef)

    pi_estimation = 12 * (integral - (sqrt(3)/8))
    return pi_estimation


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

    return u_n

def piApproximationWithGeometry(n=10000):
    integral = calculeAire(0, 0.5, lambda x : sqrt(1-x**2),n)
    pi_estimation = 12 * (integral - (sqrt(3)/8))
    return pi_estimation

if __name__ == "__main__":
    t = time.time()
    estimation = piApproximationWithGeometry()
    print(f"PI_ARCHIMEDE = {estimation}\t TIME : {time.time()-t} seconds")
    t = time.time()
    estimation = approximatePiWithNewton()
    print(f"PI_NEWTON =    {estimation}\t TIME : {time.time()-t} seconds")