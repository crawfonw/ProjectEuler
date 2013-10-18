'''
http://projecteuler.net/problem=370
http://www.jamestanton.com/wp-content/uploads/2010/07/triangles_general-essay1.pdf
http://www.jstor.org/stable/2690701?seq=2
http://mathworld.wolfram.com/IntegerTriangle.html
'''


from math import ceil, sqrt
import pp
import time

max_P = 10**3#10**6
m = max_P / 2
count = 0
ls = []

t1 = time.time()

for c in range(1, m):
    for b in range(1, c + 1):
        for a in range(1, b + 1):
            if b**2 == a*c and a + b + c <= max_P and a + b > c:
                count += 1

'''
for a in range(1, m):
    for b in range(1, m):
        if a <= b and a + b < max_P:
            for c in range(1, m):
                if b <=c and a + b > c and a + b + c <= max_P:
                    if b**2 == a*c:
                        count += 1
                        #ls.append((a,b,c))
'''

t2 = time.time()                   
print count
print 'Runtime: %0.3f sec' % float((t2 - t1))
#print ls

'''
def num_tri_for_seq(a, r):
    tests = [a*r**(n - 1) for n in range(1,4)] #test for a + b > c
    if sum(tests[:2]) <= tests[2]:
        return 0
    ss = []
    count = 0
    for n in range(1, 21):
        An = a*r**(n - 1)
        if An >= max_P / 2: #No side can be more than max_P / 2
            break
        if sum(ss[-2:]) + An > max_P:
            break
        ss.append(An)
    if len(ss) - 2 > 0:
        count += (len(ss) - 2)
    print ss
    return count

for a in range(1, max_P):
    if a % 100000 == 0: print a
    for r in range(2, max_P / a):
        count += num_tri_for_seq(a, r)

print count, count + m

#print num_tri_for_seq(125000, 2)
'''
