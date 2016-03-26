'''
http://projecteuler.net/problem=001
Solution: 233168
Runtime: 0.000 sec
With PyPy: 0.000 sec
'''
import time

TARGET = 999

def sum_target_divisible_by(t, n):
    m = t / n
    return n * (m * (m+1)) / 2

def smart():
    return sum_target_divisible_by(TARGET, 3) + sum_target_divisible_by(TARGET, 5) \
            - sum_target_divisible_by(TARGET, 15)

def brute_force():
    total = 0
    for i in range(TARGET + 1):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

if __name__ == "__main__":
    t1 = time.time()
    sol = smart()
    t2 = time.time()
    print 'Solution: %s' % sol
    print 'Runtime: %0.3f sec' % float((t2 - t1))
