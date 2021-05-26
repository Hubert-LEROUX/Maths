def getEulerCycleUndirected(graph, start=0):
    """
    @param: graph, liste d'adjacence du graphe
    @return: liste cycle eulérien, cycle passant par chaque arrête une seule fois
    """
    assert all(len(x)%2==0 for x in graph) # Condition nécessaire et suffisante sur l'existence d'un cycle
    P = [] # Chaîne principale
    Q = [start] # Chaîne mirroir prolongements
    R = [] # Prolongements

    nbNodes = len(graph)
    next = [0]*nbNodes # Conserve le prochain voisin à explorer
    seen = [set() for _ in range(nbNodes)]

    while Q:
        node = Q.pop() # On retire un noeud
        P.append(node)
        
        while next[node] < len(graph[node]): # Tant qu'il reste des voisins
            neighbor = graph[node][next[node]] # On récupère le voisin
            next[node]+=1 # On incrémente pour le prochain boisin
            if neighbor not in seen[node]:
                seen[neighbor].add(node)
                R.append(neighbor)
                node = neighbor

        Q+= R[::-1]
        R=[]
    return P

ALPHABET = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
graphA = [[ALPHABET.index(x) for x in list("BCDE")],
          [ALPHABET.index(x) for x in list("ACDE")],
          [ALPHABET.index(x) for x in list("ABDE")],
          [ALPHABET.index(x) for x in list("ABCE")],
          [ALPHABET.index(x) for x in list("ABCD")],]

print([ALPHABET[x] for x in getEulerCycleUndirected(graphA)])