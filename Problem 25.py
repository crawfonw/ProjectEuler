def fib(n):
    if n <= 1:
        return n

    a = 0
    b = 1
    c = 1
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
    return c

hasFound = False
n = 4500 #guess
while not hasFound:
    a = fib(n)
    la = len(str(a))
    if la == 1000:
        print 'The %s digit of the fibonacci sequence has 1000 digits.' % n
        hasFound = True
    else:
        print n, la
        n += 1
