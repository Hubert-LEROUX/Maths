import random

nbPizzas = 9 # Nombre de pizzas à produire

print(nbPizzas) # Affiche le nbre de pizzas

for i in range(1,nbPizzas+1):
    #* Ligne pour générer d et p différents
    print(random.randint(1,10), random.randint(1,10)) 
    
    #* Ligne pour générer d et p égaux
    # d=p=random.randint(1,10)

    #* P=1 et d prend toutes les valeurs des 1 à nbPizzas
    # p = 1
    # d = i

    #* Question 3.b
    # d0 = 1
    # d = d0/(4**(nbPizzas-i))
    # p = 1/(4**i)

    # print(d,p) 

