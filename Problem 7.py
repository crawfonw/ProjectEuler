import time

def is_prime(num):
    if num == 0 or num == 1:
        return False
    for i in range(num):
        if i == 0 or i == 1:
            pass
        elif num % i == 0:
            return False
    return True

def find_nth_prime(n):
    i = 0
    primes = 0
    while primes < n:
        if is_prime(i):
            primes += 1
        if primes == n:
            return i
        i += 1
    return "err" #debuggin'


t1 = time.time()
nth_prime = find_nth_prime(10001)
print nth_prime
t2 = time.time()
print 'Runtime: %0.3f sec' % float((t2 - t1))
