import random

nbPizzas = 9
print(nbPizzas)
for i in range(1,nbPizzas+1):
    #* Ligne pour générer d et p différents
    # print(random.randint(1,10), random.randint(1,10)) 
    
    #* Ligne pour générer d et p différents
    # d=p=random.randint(1,10)

    #* P=1 et d prend toutes les valeurs des 1 à nbPizzas
    p = 1
    d = i
    print(d,p) 


