"""
Coded by Hubert LEROUX
Date: janvier-fevrier 2021
Il s'agit de trouver un cycle hamiltonien dans un graphe
Algorithme: TSP Brute Force avec backtrakcing
"""
import sys
input = sys.stdin.readline


# Recursion limit
sys.setrecursionlimit(10**9) 


def baseQuelconque2dec(chiffres, base=2):
    number = 0
    for i, chiffre in enumerate(chiffres[::-1]):
        number+= base ** i * chiffre
    return number

# base, nbChiffres = map(int, input().strip().split())
# chiffres = list(map(int, input().strip().split()))
# print(baseQuelconque2dec(chiffres, base))


def dec2baseQuelcoque(number, base=2):
    if number==0: # Si le nombre est nul
        return [0] # On renvoie 0
    res = [] # On initialise une liste pour conserver les restes
    while number > 0 : # Tant que le nombre n'est pas négatif
        res.append(number%base) # On récupère son reste dans la division euclidienne de la base
        number //= base # On divise le nombre par la base
    return res[::-1]# On affiche le résultat en collant les restes dans l'ordre inverse

# number, base = map(int, input().strip().split())
# nbChiffres, chiffres = dec2baseQuelcoque(number, base)
# print(nbChiffres)
# print(chiffres)

def baseQuelconque2baseQuelcoque(baseA, baseB, chiffres):
    number = baseQuelconque2dec(chiffres, baseA)
    return dec2baseQuelcoque(number, baseB)




class Graph():  
    def __init__(self, nbNodes, graph, d=0):  
        # self.weight = weight # Adjency matrix
        self.graph = graph # LIste of adjency
        self.E = nbNodes  # Number of nodes
        self.maxTSP = 0
        self.d = d
        self.bestPath = []
  
    # A recursive utility function to solve  
    # hamiltonian cycle problem  
    def hamCycleUtil(self, path, roulettesBougees,  pos):  
        if pos>self.maxTSP: #On a atteint un nouveau maximum
            self.maxTSP = pos # On le sauvegarde
            self.bestPath = path[:] #On fait une copie du chemin
        
        if pos == self.E:  # ON a fini
            return True
  
        for roulette, neighbor in enumerate(self.graph[path[pos-1]]): # Pour chaque que nous avons
            if not neighbor in path and (roulette not in roulettesBougees[max(0,pos-self.d):pos]): # Si on ne retombe pas sur le path et qu'on a pas tourne cette roulette avant
                path[pos]=neighbor
                roulettesBougees[pos]=roulette
                
                if self.hamCycleUtil(path, roulettesBougees, pos+1) == True:
                    return True
            # C'est nul
            # Pas de solution
            path[pos]=-1
            roulettesBougees[pos]=-1

  
        return False # On a trouve aucune solution
  
    def hamCycle(self):  
        path = [-1] * self.E 
        roulettesBougees = [-1] * self.E # Indice de la roulette bougée
  
        ''' Let us put vertex 0 as the first vertex  
            in the path. If there is a Hamiltonian Cycle,  
            then the path can be started from any point  
            of the cycle as the graph is undirected '''
        path[0] = 0
  
        if self.hamCycleUtil(path,roulettesBougees, 1) == False:  
            return (False,self.bestPath)
        return (True, path)

def combiPossibles(k, nbRoulettes, ordreImportant=False):
    choix = [-1]*k
    combinaisons = []

    def choisirSansOrdre(premier,compte):
        if compte == 0:
            combinaisons.append([1 if i in choix else 0 for i in range(nbRoulettes)]) # On sauvegarde la combinaison 0 si la roulette ne bouge pas 1 si elle bouge
            return
        for cours in range(premier,nbRoulettes-compte+1):
            choix[k - compte] = cours
            choisirSansOrdre(cours + 1,compte - 1)

    def choisirAvecOrdre(compte):
        if compte == 0: # On a fini
            # print(choix)
            combinaisons.append([choix.index(i)+1 if i in choix else 0 for i in range(nbRoulettes)]) # On sauvegarde la combinaison 0 si la roue n'a pas ete choisi sinon la roue tourne autatn que sa place
            return
        for roul in range(nbRoulettes): # Sinon pour chaque roulette
            if roul not in choix:
                choix[k - compte] = roul
                choisirAvecOrdre(compte-1)
                choix[k - compte] = -1

    
    if ordreImportant:
        choisirAvecOrdre(k)
    else:
        choisirSansOrdre(0,k)
    return combinaisons


def test(nbChiffres, nbRoulettes, d=0, k=1, afficheSolution=False, ordre=False):

    
    modifs = combiPossibles(k, nbRoulettes, ordreImportant=ordre)
    print(modifs)

    nbNodes = nbChiffres**nbRoulettes #Nombre de points
    graph = [[] for _ in range(nbNodes)] # Liste d'adjacence


    #* Construction du graphe
    for node in range(nbNodes): # Pour chaque noeud
        # Il faut transformer le nombre node en base nbChiffres
        chiffres = dec2baseQuelcoque(node, base=nbChiffres)[::-1] # LIste de chiffres representant la combinaison
        combinaison = [chiffres[i]  if i<len(chiffres) else 0 for i in range(nbRoulettes)]
        combinaison = combinaison[::-1]
        # Cette combinaison peut atteindre:
        for modif in modifs: # Pour chaque modification possible
            newCombinaison = baseQuelconque2dec([(combinaison[i]+modif[i])%nbChiffres for i in range(nbRoulettes)], base=nbChiffres)
            graph[node].append(newCombinaison)
            # weight[node][nodeAtteignable] == 1
    g = Graph(nbNodes, graph, d)


    # *Trouve les solutions
    possible, bestPath = g.hamCycle() 

    #*Affichage SOLUTION
    if afficheSolution:
        if possible:
            print("======== SOLUTION COMPLETE ===========")
        else:
            print("======== SOLUTION PARTIELLE ===========")

        for node in bestPath:
            if node==-1:
                sys.stdout.write("IMPOSSIBLE D'ALLER PLUS LOIN\n")
                break;
            chiffres = dec2baseQuelcoque(node, base=nbChiffres)[::-1]
            combinaison = ":".join([str(chiffres[i])  if i<len(chiffres) else "0" for i in range(nbRoulettes)])
            sys.stdout.write(f"{combinaison} - ")
        print("\\newline\nRAPPORT NB NOEUDS ATTEIGNABLES/NB NOEUDS = %f\n" % round(g.maxTSP/nbNodes,3))
        # if possible:
        #     sys.stdout.write("0|"*(nbRoulettes-1)+"0\n")
        print("\nNB NOEUDS ATTEIGNABLES =", g.maxTSP)
        print("NB NOEUDS =", nbNodes)

    return round(g.maxTSP/nbNodes,3) #On retourne le pourcentage de combinaisons qu'on a pu faire

def countNumberOfMultiples(array, m):
    assert m!=0
    nb = 0
    for element in array:
        if element % m == 0:
            nb+=1
    return nb

def main():
    print("Bienvenue dans ce petit script pour tester des cas de l'exercice 1:")
    print("Donnez-moi : r n d k [1 si l'ordre est important pour k, 0 sinon]")
    nbRoulettes, nbChiffres, d, k, boolOrdreImpt = map(int, input().split())
    test(nbChiffres, nbRoulettes, d, k, True, boolOrdreImpt)
    

if __name__ == '__main__':
    main()


