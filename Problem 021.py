
from math import ceil
import time


t1 = time.time()
 
def d(n):
        f = 0
        for i in range (1, int(ceil(n / 2) + 1)):
                if n % i is 0:
                        f += i
        return f
 
_sum = 0
t1 = time.time()
for a in range(1, 10000):
        b = d(a)
        if a == d(b) and a != b:
                _sum += a

print _sum
t2 = time.time()
print 'Runtime: %0.3f sec' % float((t2 - t1))
