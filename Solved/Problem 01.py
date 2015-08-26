import time

t1 = time.time()
total = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        print i
        total += i

print total
t2 = time.time()
print 'Runtime: %0.3f sec' % float((t2 - t1))
