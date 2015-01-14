import time

t1 = time.time()

p = None
l = []

for a in range(2, 101):
    for b in range(2, 101):
        p = a**b
        if p not in l:
            l.append(p)

print len(l)

t2 = time.time()
print 'Runtime: %0.3f sec' % float((t2 - t1))

