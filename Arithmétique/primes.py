

def sieve(n):
    primes = [2] 
    flags = [True]*(n+1)

    for i in range(3,n+1,2):
        if flags[i]:
            primes.append(i)
            for mul in range(2*i, n+1, i):
                flags[mul]=False
    return primes

print(sieve(70))
    
