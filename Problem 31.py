import time

total = 200
types = [1, 2, 5, 10, 20, 50, 100, 200]

def denom(n, k):
    if n < 0 or k < 1:
        return 0
    if n == 0:
        return 1
    return denom(n, k - 1) + denom(n - types[k - 1], k)

t1 = time.time()

print denom(total, len(types))

t2 = time.time()
print 'Runtime: %0.3f sec' % float((t2 - t1))

