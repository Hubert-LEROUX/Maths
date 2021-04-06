def pgcdEuclidean(a,b):
    """
    Compute the pgc of a and b
    """
    if a==0: # Si a vaut 0
        return b #On retourne l'autre
    elif b==0:
        return a # On retourne l'autre
    #sinon, on remplace le maximum M par M%m
    if a<=b: #b est plus grand
        return pgcdEuclidean(a, b%a)
    else: # a est plus grand
        return pgcdEuclidean(a%b, b)


def pgcdEuclideanExtended(a,b):
    """
    Compute the pgc of a and b
    """
    if a==0: # Si a vaut 0
        return b, 0, 1
    gcd, x1, y1 = pgcdEuclideanExtended(b%a, a)
    x = y1 -(b//a)*x1
    y = x1
    return gcd,x,y

print("PGCD(1274, 275)")
print(pgcdEuclideanExtended(1274, 275))


def inverseModulaireEfficace(m, modulo):
    gcd, x, y = pgcdEuclideanExtended(m, modulo)
    if gcd == 1:# Si l'inverse existe
        if x < 0:
            x += (-x//modulo)*modulo+modulo
        else:
            x%=modulo
        return x
    return None



def inverseModulaireNaive(m, modulo):
    """
    Calcule l'inverse u de m modulo modulo:
    u*m = 1 [modulo]
    """
    if pgcdEuclidean(m,modulo) == 1 :
        for i in range(1, modulo-1):
            if (m*i)%modulo == 1:
                return i

        