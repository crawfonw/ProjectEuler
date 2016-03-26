import fractions
import math

# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def esieve(n):
    '''
    Finds all prime numbers <= n
    Memory footprint can be trimmed
    '''
    is_prime = [True] * (n - 1) # 2 -> is_prime[0], 3 -> is_prime[1], 4 -> is_prime[2]
    for i in range(2, int(math.sqrt(n))+1):
        if is_prime[i-2]:
            for j in range(int(math.pow(i, 2)), n + 1, i):
                is_prime[j-2] = False
    
    return [x for x in range(2, n+1) if is_prime[x-2]]

sieve_of_eratosthenes = esieve

def esieve2(n):
    '''
    Finds all prime numbers <= n
    '''
    is_prime = range(2, n+1)
    for i in range(2, int(math.sqrt(n))+1):
        if is_prime[i-2]:
            for j in range(int(math.pow(i, 2)), n + 1, i):
                is_prime[j-2] = 0
    return [x for x in is_prime if x]

# https://en.wikipedia.org/wiki/Fermat%27s_factorization_method
def fermat_sieve(n):
    raise NotImplementedError

# https://en.wikipedia.org/wiki/Lenstra_elliptic_curve_factorization
def lenstra(n):
    raise NotImplementedError

# https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm
def pollard_rho(n):
    def g(x):
        return (int(math.pow(x, 2)) - 1) % n
    
    x,y,d = 2,2,1
    while d == 1:
        x = g(x)
        y = g(g(y))
        d = fractions.gcd(abs(x - y), n)
    if d == n:
        raise
    else:
        return d

# https://en.wikipedia.org/wiki/Quadratic_sieve
def quadratic_sieve(n):
    raise NotImplementedError

if __name__ == '__main__':
    n = 100
    print 'sieve1', esieve(n)
    print 'sieve2', esieve2(n)