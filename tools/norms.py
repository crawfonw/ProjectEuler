def p_norm(p1, p2, p):
    if p == 'inf' or p == float('inf'):
        return max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))
    return pow(abs(p1[0] - p2[0])**p + abs(p1[1] - p2[1])**p, 1.0/p)

def euclidian(p1, p2):
    return p_norm(p1, p2, 2)

def manhattan(p1, p2):
    return p_norm(p1, p2, 1)

def chessboard(p1, p2): #chessboard/chebyshev distance; maximum/L-inf norm; what-have-you
    return p_norm(p1, p2, 'inf')
