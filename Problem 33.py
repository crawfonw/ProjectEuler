'''
http://projecteuler.net/problem=33
Solution: 100
Runtime: 0.045 sec (with PyPy)
'''
import time
from fractions import Fraction

def which_digits_cancel(n,m):
    ns = str(n)
    ms = str(m)
    if ns[0] == ns[1] or ms[0] == ms[1]:
        return (-1,-1)
    if len(ns) != len(ms):
        return (-1,-1)
    for i in range(len(ns)):
        for j in range(len(ms)):
            if ns[i] == ms[j]:
                return (i, j)
    return (-1,-1)

def main():
    f = Fraction(1)
    for n in range(10, 100):
        for m in range(10, 100):
            if n != m and n < m and n % 10 != 0 and m % 10 != 0:
                tup = which_digits_cancel(n,m)
                if tup != (-1,-1):
                    ns = str(n)[(tup[0] + 1) % 2]
                    ms = str(m)[(tup[1] + 1) % 2]
                    if not ms == '0':
                        if float(ns)/float(ms) == float(n)/m:
                            #print '%s/%s = %s/%s' % (n,m,ns,ms)
                            f *= Fraction(n,m)
    print f

if __name__ == "__main__":
    t1 = time.time()
    main()
    t2 = time.time()
    print 'Runtime: %0.3f sec' % float((t2 - t1))