import time

t1 = time.time()

s = 0
f1 = 1
f2 = 2
fNext = 0
while True:
    #print f1, f2
    if f2 % 2 == 0:
        if f2 > 4000000:
            break
        s += f2
    fNext = f1 + f2
    f1 = f2
    f2 = fNext

print s
t2 = time.time()
print 'Runtime: %0.3f sec' % float((t2 - t1))
