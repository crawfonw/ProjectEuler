
'''
http://projecteuler.net/problem=504
Solution: N/A
Runtime: N/A
With PyPy: N/A

Use Pick's Theorem - https://en.wikipedia.org/wiki/Pick%27s_theorem
'''
import itertools
import time

from tools.combinatorics import number_permutations
from tools.misc import is_square

def picks(A, b):
    return A + 1 - b // 2

def area_of_quad(a,b,c,d):
    '''
    A(a, 0), B(0, b), C(-c, 0), D(0, -d)
    reduced "Shoelace formula" if you want to name it
    '''
    return int(0.5*(a*b + c*d + c*b + a*d))

def lattice_points_on_line(p1,p2):
    start, end = (p1[0], p2[0]) if p1[0] < p2[0] else (p2[0], p1[0])
    slope = (p2[1]-p1[1]) // (p2[0]-p1[0])
    return [(x, x*slope) for x in range(start, end+1) if int(x*slope) == x*slope]

def get_points(p1,p2):
    if p1[0] == p2[0]:
        if p1[1] < p2[1]:
            return [(p1[0],x) for x in range(p1[1],p2[1])]
        else:
            return [(p1[0],x) for x in range(p1[1],p2[1],-1)]
    if p2[1] == p2[1]:
        if p1[0] < p2[0]:
            return [(x,p1[1]) for x in range(p1[0],p2[0])]
        else:
            return [(x,p1[1]) for x in range(p1[0],p2[0],-1)]

def main():
    # need to reduce scope for larger m
    # any two lattices with same values in different positions are in the same partition
    # and can be skipped
    m = 4
    print 'For m = %s,' % m
    quads_with_square_num_lattice_points = 0
    perms = itertools.product(range(1, m+1), repeat=4)
    print 'There are %s number of permuatations.' % m**m
    for perm in perms:
        a,b,c,d = perm
        num_boundary_points = len(set(get_points((a,0),(0,b)) + get_points((0,-d), (a,0)) + get_points((0,b),(-c,0)) + get_points((-c,0),(0,-d))))
        A = area_of_quad(a,b,c,d)
        i = picks(A, num_boundary_points)
        if i != 1 and i != 0 and is_square(i):
            print (a,b,c,d), i
            quads_with_square_num_lattice_points += 1

    print '%s have a square number of lattice points.' % quads_with_square_num_lattice_points

if __name__ == "__main__":
    t1 = time.time()
    main()
    t2 = time.time()
    print 'Runtime: %0.3f sec' % float((t2 - t1))
