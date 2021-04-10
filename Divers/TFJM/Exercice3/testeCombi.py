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


    fComputeScore = computeScoreAlign
    
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

    print(f"Best score = {bestScore}")
    for arr in bestArrays:
        print(arr)


    print("Ordre des pizzas théorique:")
    pizzas.sort(key = lambda x : x[1]/x[0], reverse=True)
    print(f"Score = {fComputeScore(pizzas)} | Array = {pizzas}") #On trie par ordre décroissant du rapport p/d






if __name__ =="__main__":
    input = sys.stdin.readline 
    cout = sys.stdout.write
    main()