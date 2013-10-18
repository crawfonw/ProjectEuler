from math import sqrt
import time

def is_triplet(a,b,c):
    return a*a < b*b and b*b < c*c

def find_c(a,b):
    return sqrt(a*a + b*b)


t1 = time.time()
for i in range(1, 1001):
    for j in range(1, 1001):
        c = find_c(i, j)
        if is_triplet(i,j,c):
            if i + j + c == 1000:
                print [i,j,c]
                print i*j*c
t2 = time.time()
print 'Runtime: %0.3f sec' % float((t2 - t1))
