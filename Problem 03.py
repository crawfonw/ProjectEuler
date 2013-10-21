import time

def find_factors(num, nodups=False):
    factors = []
    lastfactor = num
    i = 0
    if num == 1:
        factors.append(Rational(1))
        return factors
    while True:
        i += 1
        if nodups and lastfactor < i:
            break
        if i > num:
            break
        if num % i == 0:  
            factors.append(num / i)
            lastfactor = num / i
    factors.append(1)
    return factors

def find_primes(num_list):
    primes = []
    for n in num_list:
        isPrime = True
        for i in range(n):
            if i == 0 or i == 1 or i == n:
                pass
            elif n % i == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(n)
    primes.sort(reverse=True)
    return primes

t1 = time.time()
factors = find_factors(600851475143)
primeFactors = find_primes(factors)
print primeFactors
t2 = time.time()
print 'Runtime: %0.3f sec' % float((t2 - t1))
