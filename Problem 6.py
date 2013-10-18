import time

t1 = time.time()
suos = 0
sosu = 0
for i in range(1,101):
    suos += i*i
    sosu += i

sosu *= sosu
print sosu - suos
t2 = time.time()
print 'Runtime: %0.3f sec' % float((t2 - t1))
