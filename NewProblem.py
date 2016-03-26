import os
import sys

doc = """'''
http://projecteuler.net/problem={}
Solution: N/A
Runtime: N/A
With PyPy: N/A
'''
import time



def main():
    pass

if __name__ == "__main__":
    t1 = time.time()
    sol = main()
    t2 = time.time()
    print 'Solution: %s' % sol
    print 'Runtime: %0.3f sec' % float((t2 - t1))
"""

def create_file(n):
    f = open('Problem %s.py' % n,'w')
    f.write(doc.format(n))
    f.close()

def main():
    if sys.argv < 2:
        sys.exit('Usage: %s problem-number' % sys.argv[0])
    else:
        if 'Problem %s.py' % sys.argv[1] in os.listdir(os.getcwd()):
            sys.exit('Problem %s.py already exists.' % sys.argv[1])
        create_file(sys.argv[1])

if __name__ == "__main__":
    main()
