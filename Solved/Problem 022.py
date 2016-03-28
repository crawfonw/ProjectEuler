'''
http://projecteuler.net/problem=022
Solution: 871198282
Runtime: 0.013 sec
With PyPy: N/A
'''
import os
import time

NAMES = os.path.join('euler', 'resources', 'p022_names.txt')

def main():
    with open(NAMES, 'rb') as f:
        names = sorted(f.read().replace('"', '').split(','))
        return sum((i+1) * sum((ord(x) - 96) for x in name.lower()) for i, name in enumerate(names))

if __name__ == "__main__":
    t1 = time.time()
    sol = main()
    t2 = time.time()
    print 'Solution: %s' % sol
    print 'Runtime: %0.3f sec' % float((t2 - t1))
