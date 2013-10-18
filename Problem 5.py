import time

def lcm(one, two):
    """finds the lcm of two numbers"""
    lcm = (one*two)/gcd(one, two)
    return lcm

def gcd(one, two):
    """finds the gcd of two numbers"""
    while two:
        one, two = two, one % two
    return one

def lcm_list(ints):
    return reduce(lcm, ints)

l = [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]

t1 = time.time()
print lcm_list(l)
t2 = time.time()
print 'Runtime: %0.3f sec' % float((t2 - t1))
