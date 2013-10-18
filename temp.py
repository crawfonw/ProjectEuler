import pickle
import time

from tools import prime_factors, gcd

p_factors = dict()

def do_it(limit):
    #limit is non-inclusive
    for k in range(1, limit):
        for j in range(1, limit):
            for i in range(1, limit):
                if i + j != k or i > j or not (gcd(i, j) == gcd(i, k) == gcd(j, k) == 1):
                    pass
                else:
                    p_factors[i*j*k] = prime_factors(i*j*k)

f = open('primefacts120000.pkl', 'wb')

t1 = time.time()

do_it(120000)

t2 = time.time()
print 'Runtime: %0.3f sec' % float((t2 - t1))

pickle.dump(p_factors)
f.close()
