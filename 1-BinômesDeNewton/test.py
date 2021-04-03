import pprint

def trianglePascal(N):
    """
    Retourne une liste 2D du triangle de Pascal contenant N lignes
    """
    triangle = [[1]]
    for indice_ligne in range(1,N):
        previous_line = triangle[-1]
        new_line = []
        for indice in range(len(previous_line)+1) :
            if indice == 0 or indice==len(previous_line): # Si on est au début ou à la fin, on renvoie un 1
                number = 1
            elif 0< indice < len(previous_line): # Sinon on calcule
                number = previous_line[indice-1]+previous_line[indice]
            new_line.append(number)
        triangle.append(new_line)
    return triangle

pprint.pprint(trianglePascal(20))
