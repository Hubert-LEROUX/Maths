"""
Ce fichier permet de déterminer qui gagne en fonction du nombre d'allumettes
"""
import sys

def BaptisteGagneTil(n, allumettes, coup=0):
    """
    Cette fonction permet de déterminer si c'est Baptiste ou Carole qui gagne
    @param: n est le nombre d'allumettes au départ
    @param: coup  est le coup auquel est joué ce coup:
        Si coup = 0 (mod 2). C'est Baptiste
        Sinon c'est Carole
    @param: allumettes liste des indices des allumettes restantes.
    @return: True si Baptiste gagne dans la configuration, False sinon
    """
    # print(allumettes, coup)
    if len(allumettes)==0: # Il ne reste plus d'allumettes
        # print((coup-1)%2==0)
        return (coup-1)%2==0 # Si Baptiste a joué au dernier tour, c'est lui qui a gagné

    def enleveLaIemeAllumette(allumettes, i):
        copie = allumettes[:]
        if i==0: #* On enlève la première
            if len(allumettes) > 1 and allumettes[i]+1 == allumettes[i+1]: # Si celle suivante est adjacente
                return copie[2:] # On enlève les deux premières
            return copie[1:]

        elif i==len(allumettes)-1: #* On enlève la dernière
            if len(allumettes) > 1 and allumettes[i-1]+1 == allumettes[i]: # Celle derrière est adjacente
                return copie[:-2] # On prend tout excepté les deux dernières
            return copie[:-1] # On prend tout excepté la dernière
        
        # Maintenant on sait que i est au milieu
        # On cherche la partie à éliminer
        iDeb = i
        if len(allumettes) > 1 and allumettes[i-1]+1 == allumettes[i]: # Celle derrière est adjacente
            iDeb -= 1
        iFin = i
        if len(allumettes) > 1 and allumettes[i]+1 == allumettes[i+1]: # Si celle suivante est adjacente
            iFin+=1

        if iFin < len(allumettes)-1:
            return copie[:iDeb] + copie[iFin+1:]
        return copie[:iDeb]


    # Maintenant on teste toutes les configurations
    result = BaptisteGagneTil(n, enleveLaIemeAllumette(allumettes, 0), coup+1)
    tourDeBaptiste = (coup%2==0)
    for i in range(1, len(allumettes)):
        if tourDeBaptiste:
            result = result or BaptisteGagneTil(n, enleveLaIemeAllumette(allumettes, i), coup+1)
            if result: # Pas la peine de continuer
                return result
        else:
            result = result and BaptisteGagneTil(n, enleveLaIemeAllumette(allumettes, i), coup+1)
            if not result: # On a un faux, pas la peine de continuer
                return result

    return result
        
        

if __name__ == '__main__':
    cout = sys.stdout.write
    input = sys.stdin.read 

    for n in range(32,40,2):
        gagne = BaptisteGagneTil(n, list(range(n)))
        # BaptisteGagneTil()
        
        cout(f"Pour n={n}: ")
        if gagne:
            print("Baptiste (joue en premier) gagne")
        else:
            print("Carole (joue en deuxième) gagne")

