from numpy import double, sqrt
import time

t1 = time.time()

def C(p,q,n):
    num = double((sqrt(p) + sqrt(q))**(2*n))
    frac = str(num).split('.')[1]

def N(p,q):
    pass

t2 = time.time()
print 'Runtime: %0.3f sec' % float((t2 - t1))
