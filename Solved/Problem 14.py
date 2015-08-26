
import time

def even_chain(n):
    return n / 2

def odd_chain(n):
    return 3*n + 1

def construct_chain(n):
    chain = []
    while n != 1:
        chain.append(n)
        if n % 2 == 0:
            n = even_chain(n)
        else:
            n = odd_chain(n)
    chain.append(1)
    return chain

def find_chain(n):
    seqs = []
    for i in range(1, n):
        seqs.append(len(construct_chain(i)))
    return seqs.index(max(seqs)) + 1

t1 = time.time()
print find_chain(1000000)
t2 = time.time()
print 'Runtime: %0.3f sec' % float((t2 - t1))
