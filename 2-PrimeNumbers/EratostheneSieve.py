import sys
import time

def sieve(N, tableau):
	for i in range(2, N//2):
		if tableau[i]:#Si on tombe sur un nombre premiers
			for multiple in range(2*i, N, i): #Alors tous ses mutlitples
				tableau[multiple] = False # Ne sont pas des nombres premiers

def affichage(N, tableau):
	for i in range(N):
		if tableau[i]:
			print(i, end = " | ")

if sys.argv[1]:
	print(sys.argv[1])
	N=int(sys.argv[1])
else:
	N=int(input("Calculons les nombres premiers jusquà N"))

tableau = [False]+[True]*(N-1)
start = time.time()
sieve(N, tableau)
print(f"Calcultated in {time.time()-start} seconds")
if input("Print ? (y/n)") == "y":
	affichage(N, tableau)

