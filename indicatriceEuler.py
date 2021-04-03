import matplotlib.pyplot as plt

def indicatriceEuler(N):
    phi = list(range(N+1)) # LIste contenant les valeurs de phi
    for i in range(2,N+1):
        if phi[i] == i: #Si le nombre est premier
            for multiple in range(i, N+1, i): # Pour tous ces multiples
                phi[multiple] = phi[multiple]-phi[multiple]//i # On transforme phi[i]
    return phi

def plotIndicatriceEuler(n):
    X = list(range(n+1))
    Y = indicatriceEuler(n)
    plt.scatter(X, Y)
    plt.show()

def computePhi(n):
    return indicatriceEuler(n)[n]
# print(indicatriceEuler(100))
# plotIndicatriceEuler(100)


def diviseurs(n):
	listeDiviseurs = []
	for i in range(1,n+1):
		if n%i == 0:
			listeDiviseurs.append(i)
	return listeDiviseurs


S=0
phi = indicatriceEuler(2017)
for d in diviseurs(2016):
    print(d, phi[2016//d])
    S+=phi[2016//d]*d
print(f"Sum={S}")


