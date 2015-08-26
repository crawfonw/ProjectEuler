import time

def recurring_cycle_length(n):
    cycleLen = 0
    #  remove powers of 2 and 5 in n
    while (n % 2 == 0):
        n /= 2
    while (n % 5 == 0):
        n /= 5
    if n > 1:
        a = 10 % n
        cycleLen = 1
        while a != 1:
            a *= 10
            a %= n
            cycleLen += 1
    return cycleLen

def max_len_recurring_cycle_in_range(n):
    # iterate from the max num down
    maxCycleLen = 0
    maxCycleLenGenerator = n
    for i in range(n, 1, -1):
        currLen = recurring_cycle_length(i)
        if(currLen > maxCycleLen):
            maxCycleLen = currLen
            maxCycleLenGenerator = i
        if(currLen == i-1):
            break
    return maxCycleLenGenerator, maxCycleLen


t1 = time.time()

n, l = max_len_recurring_cycle_in_range(1000)
print 'n: %s Cycle length: %s' % (n, l)

t2 = time.time()
print 'Runtime: %0.3f sec' % float((t2 - t1))
