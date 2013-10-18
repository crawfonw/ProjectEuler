from itertools import permutations
import time

t1 = time.time()

print '1,000,000th  lexicographic permutation:', list(permutations([0,1,2,3,4,5,6,7,8,9]))[999999]

t2 = time.time()
print 'Runtime: %0.3f sec' % float((t2 - t1))
