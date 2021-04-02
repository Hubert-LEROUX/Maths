import sys

input = sys.stdin.readline          
cout = sys.stdout.write     


def bezout(a,b):
    if b==0: 
        return (1,0)
    else:
        u,v = bezout(b, a%b)
        return (v, u - (a//b)*v)

def inv(a,p):
    return bezout(a,p)[0]%p
    
def product_array(array):
    prod = array[0]
    for i in range(1,len(array)):
        prod*=array[i]
    return prod
#     if i==j:
#         return array[i]
#     else:
#         middle = (i+j)//2
#         return product_array(array, i, middle) * product_array(array, middle+1,j)

def gcd(a, b) :
    return a if b == 0 else gcd(b, a%b)

def ppcm_array(array):
    ppcm = array[0]
    for i in array[1:] :
        ppcm *= i//gcd(ppcm, i)
    return ppcm


def solve():
    n = int(input())
    coefficients = [0]*n
    restes = [0]*n
    modulos = [0]*n 
    for i in range(n):
        coefficients[i], restes[i], modulos[i] = map(int, input().split())
    
    #* Chaque équation est de la forme ax = r (mod n)
    #* On passe ici à x = a^(-1)r (mod n)
    for i in range(n):
        restes[i] *= inv(coefficients[i], modulos[i])
        # print(restes[i])

   
    ppcm = ppcm_array(modulos)
    solution = 0
    for i in range(n):
        k = (ppcm//modulos[i])
        solution += (restes[i] * k * inv(k,modulos[i])) 
        solution %= ppcm

    print(f"SOLUTION {solution}")
    print(f"MOD {ppcm}")
    

if __name__ == '__main__':
    # print(product_array([1,2,3,4,5,6,7],0,6))
    solve()
    # print(inv(77,17))