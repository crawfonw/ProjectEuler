'''
http://projecteuler.net/problem=002
Solution: 4613732
Runtime: 0.000 sec
With PyPy: N/A
'''
import time

# recursive
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1) + fib(n-2)
# print 'fib', sum([fib(i) for i in range(3,34,3)])

# memoized
def fib_memo(n, saved={0: 1, 1: 1, 2: 1}):
    return saved.setdefault(n, saved.get(n) or fib_memo(n-1) + fib_memo(n-2))
# print 'fib_memo', sum([fib_memo(i) for i in range(3,34,3)])

# tail recur
def fib_tail(n, a=0, b=1):
    if n > 0:
        return fib_tail(n-1, b, a+b)
    else:
        return a
# print 'fib_tail', sum([fib_tail(i) for i in range(3,34,3)])

# iterative
def fib_iter(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a
# print 'fib_iter', sum([fib_iter(i) for i in range(3,34,3)])

# closed form
# numbers are small enough to not need to worry about precision
# phi = (1 + 5 ** 0.5) / 2
# print 'fib closed', sum([int(((phi ** n) - (-phi)**(-n)) / 5 ** 0.5) for n in range(3,34,3)])

# no precompute
def fib_help(MAX=4000000):
    v,n = 0,0
    while v < MAX:
        if v % 2 == 0: yield v 
        n,v = n+1, fib(n+1)
# print 'fib+while', sum(fib_help())

# no precompute and shorter
def fib(n):
    if n==1 or n==2: return 1
    return fib(n-1) + fib(n-2)
# print 'fib+list comp', sum([fib(i) for i in range(1, 34) if fib(i) % 2 == 0 and fib(i) < 4000000])

# two liner
# f = lambda n: 1 if n == 1 or n == 2 else f(n-1)+f(n-2)
# print 'fib+list comp+lambda', sum([f(i) for i in range(1, 34) if f(i) % 2 == 0 and f(i) < 4000000])

# one liner
# print 'fib+list comp+chain lambda', sum(x for x in map(lambda n: (lambda f, *a: f(f, *a))(lambda lfib, n: 1 if n == 1 or n == 2 else lfib(lfib, n-1) + lfib(lfib, n-2), n), range(1, 34)) if x % 2 == 0 and x < 4000000)


def main():
    phi = (1 + 5 ** 0.5) / 2
    return sum([int(((phi ** n) - (-phi)**(-n)) / 5 ** 0.5) for n in range(3,34,3)])

if __name__ == "__main__":
    t1 = time.time()
    sol = main()
    t2 = time.time()
    print 'Solution: %s' % sol
    print 'Runtime: %0.3f sec' % float((t2 - t1))
