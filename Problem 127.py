#problem 127

import time
import pickle

from tools import gcd

f = open('primefacts120000.pkl', 'rb')
prime_facs = pickle.load(f)
f.close()

def rad(f):
    r = 1
    for i in f:
        r *= i
    return r

def is_abc_hit(a, b, c, radf):
    return (gcd(a, b) == gcd(a, c) == gcd(b, c) == 1) \
           and (a < b) \
           and (a + b == c) \
           and radf < c

def check(a, b, c):
    #facts = prime_factors(a*b*c)
    facts = prime_facts[a*b*c]
    return is_abc_hit(a, b, c, rad(facts))

def do_it(limit):
    #limit is non-inclusive
    s = 0
    found = 0
    for k in range(1, limit):
        for j in range(1, limit):
            for i in range(1, limit):
                if i + j != k or i > j:
                    pass
                elif check(i,j,k):
                    s += k
                    found += 1
                    print 'Found %s so far. Latest: c=%s; (%s, %s, %s)' % (found, k, i, j, k)
    return s, found



t1 = time.time()
#print check(5,27,32)
print do_it(120000)
t2 = time.time()
print 'Runtime: %0.3f sec' % float((t2 - t1))
