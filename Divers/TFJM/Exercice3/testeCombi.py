"""
Ce fichier permet de tester différents arrangements de pizzas.
Il calcule tous les scores possibles 
!(Attention comme il s'agit de permutations, la complexité est O(n!))

Les pizzas arrivent en input de la forme
 - un entier sur une ligne: le nombre de pizzas
 - n lignes suivent avec pour chaque ligne deux entiers: p (le poids de la pizza) et d (la durée de fabrication)
# Soit vous les donnez manuellement.
# Soit vous vous servez de generate pizzas, qui les génèrent pour vous.
"""


import sys
import itertools




def arrangements(l, result=[]):
    """
    Retourne tous les arrangements possibles de la suite
    """

    if len(result)==len(l):
        yield result

    for element in l:
        if element not in result:
            result.append(element)
            arrangements(l, result)
            result.pop()



def factorial(n):
    if n <2:
        return 1
    return n*factorial(n-1)

def main():
    nbPizzas = int(input())
    pizzas = [tuple(map(int, input().split())) for _ in range(nbPizzas)] # Tuple d et p

    bestArrays = None
    bestScore = float("inf")

    def computeScoreAlternate(arr):
        """
        Arr contient des tuple (d, p) dans un certain ordre
        On calcule le score si l'on alterne gauche puis droite
        """
        score = 0
        n = len(arr)

        #* Pizzas pairs, on les met  à gauche
        distance = arr[0][0] # La taille de la première pizza
        for i in range(2,n, 2): # On compte à partir de la deuxième car la première finit en 0
            score += arr[i][1] * distance # Coût
            distance += arr[i][0] # On ajoute cette nouvelle distance
        #* Pizzas impairs, on les met à droit
        distance = 0
        for i in range(1,n, 2):
            distance += arr[i][0]
            score += arr[i][1] * distance

        return score
    def computeScoreAlign(pizz):
        """
        Arr contient des tuple (d, p) dans un certain ordre
        On calcule le score si on aligne toutes les pizza s à droite
        """
        score = 0
        n = len(pizz)

        # On met toutes les pizzas à droite
        distance = 0
        for d,p in pizz:
            distance+= d
            score+= p*distance

        return score


    fComputeScore = computeScoreAlternate
    
    # print(itertools.permutations(pizzas))
    for arr in itertools.permutations(pizzas):
        # print(list(arr))
        newScore = fComputeScore(list(arr))
        # print(newScore, "\t",list(arr))
        # print(score, array)
        if newScore < bestScore:
            bestScore = newScore
            bestArrays = [list(arr)]
        elif newScore == bestScore:
            bestArrays.append(list(arr))


    print("========================= MEILLEURS SCORES ======================")
    print(f"Nombre de permutations testées:{factorial(nbPizzas)}")
    print(f"Nombre de permutations meilleures:{len(bestArrays)}")
    print(f"\tBest score = {bestScore}")
    for arr in bestArrays:
        print(f"\t{arr}")


    print()
    print("=== Ordre des pizzas théorique ===")
    pizzas.sort(key = lambda x : x[1]/x[0], reverse=True)
    scoreTheo = fComputeScore(pizzas)
    print(f"Score = {scoreTheo} | Array = {pizzas}") #On trie par ordre décroissant du rapport p/d
    print(f"Is in the best solution: {scoreTheo == bestScore}")


if __name__ =="__main__":
    input = sys.stdin.readline 
    cout = sys.stdout.write
    main()