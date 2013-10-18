#triangle numbers
from math import sqrt
import time

def factor(n, noduplicates = False):
    intn = int(n)
    factors = []
    lastfactor = n
    i = 0

    # 1 is a special case
    if n == 1:
        return {1: 1}

    while 1:
        i += 1

        # avoid duplicates like {1: 3, 3: 1}
        if noduplicates and lastfactor <= i:
            break

        # stop when i is bigger than n
        if i > n:
            break

        if n % i == 0:
            factors.append(n / i)
            lastfactor = n / i

    return factors

def is_prime(num):
    if num == 0 or num == 1:
        return False
    for i in range(num):
        if i == 0 or i == 1:
            pass
        elif num % i == 0:
            return False
    return True

def get_trinum(n):
    return (n * (n+1)) / 2

t1 = time.time()
num = 1
trinum = 0
trifactors = 0
biggest_factor = 0
while trifactors < 500:

    if not is_prime(trinum):
        trifactors = len(factor(trinum))
        if trifactors > biggest_factor:
            print "Tri num with most factors so far with n=%s is %s, with factors: %s" % (num, trinum, trifactors)
            biggest_factor = trifactors
    num += 1
    trinum = get_trinum(num)
    
print trinum
t2 = time.time()
print 'Runtime: %0.3f sec' % float((t2 - t1))
