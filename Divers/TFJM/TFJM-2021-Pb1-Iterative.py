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
    """
    Convertie une liste de chiffres d'une base base en base 10
    @param: chiffres chiffres en base quelconque3
    @param: base de depart
    """
    number = 0
    for i, chiffre in enumerate(chiffres[::-1]):
        number+= base ** i * chiffre
    return number

# base, nbChiffres = map(int, input().strip().split())
# chiffres = list(map(int, input().strip().split()))
# print(baseQuelconque2dec(chiffres, base))


def dec2baseQuelcoque(number, base=2):
    """
    @param: number nombre en base 10
    @param: base base dans laquelle il faut convertir le nombre
    """
    if number==0: # Si le nombre est nul
        return [0] # On renvoie 0
    res = [] # On initialise une liste pour conserver les restes
    while number > 0 : # Tant que le nombre n'est pas negatif
        res.append(number%base) # On recupere son reste dans la division euclidienne de la base
        number //= base # On divise le nombre par la base
    return res[::-1]# On affiche le resultat en collant les restes dans l'ordre inverse

# number, base = map(int, input().strip().split())
# nbChiffres, chiffres = dec2baseQuelcoque(number, base)
# print(nbChiffres)
# print(chiffres)

def baseQuelconque2baseQuelcoque(baseA, baseB, chiffres):
    number = baseQuelconque2dec(chiffres, baseA)
    return dec2baseQuelcoque(number, baseB)




class Graph():  
    def __init__(self, nbNodes, graph, d=0, base=2, r=2):  
        # self.weight = weight # Adjency matrix
        self.graph = graph # LIste of adjency
        self.E = nbNodes  # Number of nodes
        self.maxTSP = 0
        self.d = d
        self.bestPath = []
        self.base = base
        self.r = r
        self.CCs = self.composantesConnexes()
        self.MAXIMUM = len(self.CCs[0]) # Le maximum de noeuds atteignables est majoré par la taille de la première composante connexe

  
    def hamCycle(self):  

        path = [-1] * self.E # Chemin
        marqued = [False]*self.E # Noeuds marqués
        dateDerniereUtilisationRoulette = [None] * len(self.graph[0]) # Récupère la date de la dernière utilisation de chaque roulette
        path[0] = 0 # On commence à la combinaison initiale
        marqued[0] = True
        pos = 1

  
        
        afaire = [(pos, path, marqued, dateDerniereUtilisationRoulette)]

        while afaire:
            pos, path, marqued, dateDerniereUtilisationRoulette = afaire.pop()

            if pos > self.maxTSP: # Nouveau record
                self.maxTSP = pos
                self.bestPath = path[:] #On fait une copie du chemin
                # print(f"Longueur = {pos} | {'-'.join([''.join(map(str,dec2baseQuelcoque(x, self.base))).zfill(self.r) for  x in self.bestPath[:pos]])}")
                # print(f"Longueur = {pos} | Rapport: {round((pos/self.E) * 100, 3)} %")

            if pos >= self.MAXIMUM:  # ON a fini
                return True, path


            for roulette, neighbor in enumerate(self.graph[path[pos-1]]): # Pour chaque combi accessible
                if not marqued[neighbor] and (dateDerniereUtilisationRoulette[roulette] is None or (abs(pos-dateDerniereUtilisationRoulette[roulette]) > self.d)):
                    # Si on est jamais allé dessus et que d nous permet de faire ce mouvemement
                    path[pos] = neighbor
                    ancinneDate = dateDerniereUtilisationRoulette[roulette]
                    dateDerniereUtilisationRoulette[roulette] = pos
                    marqued[neighbor] = True

                    afaire.append((pos+1, path[:], marqued[:], dateDerniereUtilisationRoulette[:]))

                    path[pos] = -1
                    dateDerniereUtilisationRoulette[roulette] = ancinneDate
                    marqued[neighbor] = False



        # On renvoie el meilleur chemin possible
        return False, self.bestPath


  
        
        return (True, path)

    def composantesConnexes(self):
        marqued = [False] * self.E
        CCs = [] 

        for source in range(self.E):
            if not marqued[source]: # Si le noeud n'est pas marque
                CC = []
                afaire = [source]
                while afaire:
                    node = afaire.pop()
                    if not marqued[node]:
                        marqued[node] = True
                        CC.append(node)
                        # On regarde chacun des voisins, s'il n'on pas ete faits, on les ajoute
                        for neighbor in self.graph[node]:
                            if not marqued[neighbor]:
                                afaire.append(neighbor)
                CCs.append(CC)
        return CCs





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
    # print(modifs)

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
    g = Graph(nbNodes, graph, d, nbChiffres, nbRoulettes)

    # CCs = g.composantesConnexes()
    print(f"COMPOSANTES CONNEXES : {len(g.CCs)}")
    for CC in g.CCs:
        print(f"TAILLE:{len(CC)} | {'-'.join([''.join(map(str,dec2baseQuelcoque(node, nbChiffres))).zfill(nbRoulettes) for node in CC])}")
        # print(f"TAILLE:{len(CC)}")


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
        # if possible:
        #     sys.stdout.write("0|"*(nbRoulettes-1)+"0\n")
        print("NB NOEUDS ATTEIGNABLES =", g.maxTSP)
        print("NB NOEUDS =", nbNodes)
    print(f"RAPPORT NB NOEUDS ATTEIGNABLES/NB NOEUDS = {(round((g.maxTSP/nbNodes) * 100))}%\n")

    return round(g.maxTSP/nbNodes,3) #On retourne le pourcentage de combinaisons qu'on a pu faire

def countNumberOfMultiples(array, m):
    assert m!=0
    nb = 0
    for element in array:
        if element % m == 0:
            nb+=1
    return nb

def main():
    # print("Bienvenue dans ce petit script pour tester des cas de l'exercice 1:")
    # print("Donnez-moi : r n d k [1 si l'ordre est important pour k, 0 sinon]")
    nbRoulettes, nbChiffres, d, k, boolOrdreImpt = map(int, input().split())
    print(f"r = {nbRoulettes} | n = {nbChiffres} | d = {d} | k = {k} | ordre important = {bool(boolOrdreImpt)}")
    test(nbChiffres, nbRoulettes, d, k, False, boolOrdreImpt)
    

if __name__ == '__main__':
    main()


