#triangle numbers
#this method uses the Number of Divisors for the solution
#more info: http://mathschallenge.net/index.php?section=faq&ref=number/number_of_divisors

from math import sqrt
import time

def prime_factors(n):
    factors = []
    lastresult = n

    # 1 is a special case
    if n == 1:
        return [1]

    while 1:
        if lastresult == 1:
            break

        c = 2

        while 1:
            if lastresult % c == 0:
                break

            c += 1
            
        factors.append(c)
        lastresult /= c

    return factors

def d(facts):
    counts = []
    prod = 1
    f = set(facts)
    
    while len(f) > 0:
        counts.append(facts.count(f.pop()))
    for i in counts:
        prod *= (i + 1)
    return prod

def get_trinum(n):
    return (n * (n+1)) / 2

t1 = time.time()

num = 1
trinum = 0
trifactors = 0
biggest_factor = 0
while trifactors < 500:
    trinum = get_trinum(num)
    trifactors = d(prime_factors(trinum))
    if trifactors > biggest_factor:
        print "Tri num with most factors so far with n=%s is %s, with factors: %s" % (num, trinum, trifactors)
        biggest_factor = trifactors
    num += 1

t2 = time.time()
print 'Runtime: %0.3f sec' % float((t2 - t1))
