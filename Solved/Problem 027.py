import time

BASE_EQ = '(%s)**2 + (a)*(%s) + (b)' #n^2 + an + b

def is_prime(num):
    if num < 0:
        return False
    if num == 0 or num == 1:
        return False
    for i in range(num):
        if i == 0 or i == 1:
            pass
        elif num % i == 0:
            return False
    return True

def generate_equations():
    eqs = []
    for a in range(1, 1000):
        for b in range(1, 1000):
            if is_prime(b):
                eqs.append(BASE_EQ.replace('a', str(a)).replace('b', str(b)))
                eqs.append(BASE_EQ.replace('a', str(-a)).replace('b', str(b)))
    return eqs

t1 = time.time()

print 'Generating equations...'
eqs = generate_equations()
print '%s equations generated.' % len(eqs)
print 'Testing equations...'
best = (None, None)
for i, e in enumerate(eqs):
    if i % 10000 == 0:
        print 'Tested %s equations so far...' % i
    n = 0
    while is_prime(eval(e % (n, n))):
        n += 1
    if best[1] < n:
        print 'New best formula!'
        print '%s produced %s sequential primes!' % ((e % ('n', 'n')), n)
        best = (e, n)
print 'Best: %s with a sequence of %s primes.' % ((e % ('n', 'n')), n)

print 'Done.'
        

t2 = time.time()
print 'Runtime: %0.3f sec' % float((t2 - t1))
