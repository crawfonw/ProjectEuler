from math import sqrt
import time

def factor(n, noduplicates = False):
    intn = int(n)
    factors = []
    lastfactor = n
    i = 0

    # 1 is a special case
    if n == 1:
        return {1: 1}

    while 1:
        i += 1

        # avoid duplicates like {1: 3, 3: 1}
        if noduplicates and lastfactor <= i:
            break

        # stop when i is bigger than n
        if i > n:
            break

        if n % i == 0:
            factors.append(n / i)
            lastfactor = n / i

    return factors

def is_abundant(n):
    facts = list(factor(n))[1:]
    _sum = 0
    for i in facts:
        _sum += i
    return _sum > n

#find all abundant numbers up to 28123
#find all pos ints that cannot be written

#print is_abundant(12)
#print is_abundant(28)

abundants = []
_sum = 0

t1 = time.time()

for i in range(1, 28):
    if is_abundant(int(i)):
        abundants.append(i)

for i in range(1, 28):
    for abundant in abundants:
        if abs(i - abundant) not in abundants:
            _sum += i

print _sum
t2 = time.time()
print 'Runtime: %0.3f sec' % float((t2 - t1))
