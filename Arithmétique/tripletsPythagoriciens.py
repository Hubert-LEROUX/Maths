def pgcd(a,b):
    """
    Calcul du PGCD grâce à l'agorithme d'Euclide
    """
    if b == 0:
        return a 
    return pgcd(b, a%b)

def tripletsPythagoriciensPrimitifs(N):
    triplets = []
    for u in range(1,N):
        for v in range(u+1,N): 
            if pgcd(u, v) == 1:
                triplets.append((v**2-u**2, 2*u*v , u**2+v**2))
    return triplets

for triplet in tripletsPythagoriciensPrimitifs(10):
    print(triplet)