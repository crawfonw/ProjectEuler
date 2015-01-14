import time

def is_prime(num):
    if num == 0 or num == 1:
        return False
    for i in range(num):
        if i == 0 or i == 1:
            pass
        elif num % i == 0:
            return False
    return True

t1 = time.time()
total = 0
for i in range(2000001):
    if i % 10000 == 0:
        print i
    if is_prime(i):
        total += i

print total
t2 = time.time()
print 'Runtime: %0.3f sec' % float((t2 - t1))
