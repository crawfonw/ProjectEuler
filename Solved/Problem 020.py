'''
http://projecteuler.net/problem=020
Solution: 648
Runtime: 0.000 sec
With PyPy: N/A
'''
import time

# using std lib
# from math import factorial

# using memoized
def factorial(n, saved={0: 1, 1: 1}):
    return saved.setdefault(n, saved.get(n) or n * factorial(n-1))

# using strings
def main():
    return sum(int(x) for x in str(factorial(100)))

# only integers (faster)
def main():
    x = factorial(100)
    total = 0
    while x:
        total += x % 10
        x = x / 10
    return total

if __name__ == "__main__":
    t1 = time.time()
    sol = main()
    t2 = time.time()
    print 'Solution: %s' % sol
    print 'Runtime: %0.3f sec' % float((t2 - t1))
