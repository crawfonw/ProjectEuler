import time

from math import floor

def R(M, N):
    totals = [0]*N
    total = 0
    for x in range(M + 1, N + 1):
        for y in range(x, N + 1):
            if ((y**2)/(x**2)) % 2 == 1:
                #totals[x - 1] += 1
                total += 1
    return total

t1 = time.time()
t = R(0, 100)
t2 = time.time()
print 'Runtime: %0.3f sec' % float((t2 - t1))

print 'Totals: %s' % t
#print 'Total: %s' % sum(t)

'''
for i in range(0, 21):
    t = R(0, i)
    print 'R(0, %s)' % i
    print 'Totals: %s' % t
    print 'Total: %s' % sum(t)
'''
