'''
http://projecteuler.net/problem=34
Solution: 40730
Runtime: 0.128 sec (with PyPy)
'''

import time
from tools import fact

'''
Good enough upper bound for the solution.
Though I think 9*6! might be more precise (even less than that, actually).
'''
BOUND = fact(9)

FACTS = {}
for i in range(10):
    FACTS[str(i)] = fact(i)

def find_largest_digit(n, largest='0'):
    if type(n) != str:
        n = str(n)
    if n[0] > largest:
        return find_largest_digit(n[1:], n[0])
    else:
        return find_largest_digit(n[1:], largest)
        
def sum_fact_of_digits(n):
    return sum([FACTS[e] for e in str(n)])
    
def is_candidate(n):
    for e in str(n):
        if FACTS[e] > n:
            return False
    return True

def main():
    total = 0
    for i in range(3, BOUND+1):
        if is_candidate(i):
            if sum_fact_of_digits(i) == i:
                total += i
    print total

if __name__ == "__main__":
    t1 = time.time()
    main()
    t2 = time.time()
    print 'Runtime: %0.3f sec' % float((t2 - t1))