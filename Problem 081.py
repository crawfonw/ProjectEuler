'''
http://projecteuler.net/problem=81
Solution: 427337
Runtime: 1.737 sec
With PyPy: N/A

Used my Graph module to solve:
https://github.com/crawfonw/GraphUtils
'''
import time
import os

from graph.graphs import Digraph
from graph.datastructs import PriorityQueue

INF = float('inf')

def read_matrix_file(f):
    f = open(f, 'r')
    lines = f.readlines()
    f.close()
    
    converted_lines = []
    for line in lines:
        converted_lines.append(map(int, line.strip('\n').split(',')))
    return converted_lines

def build_graph(matrix):
    dg = Digraph()
    dg.add_node(0)
    row_jump = len(matrix[0])
    node_counter = 0
    
    for i, row in enumerate(matrix):
        for j, column in enumerate(row):
            dg.add_edge(node_counter, node_counter + 1, column)
            if i != len(matrix) - 1:
                dg.add_edge(node_counter, node_counter + row_jump, row[j])
            node_counter += 1
    return dg

def dijkstra(g, s, t):
    dist = {s: 0}
    prev = {s:None}
    q = PriorityQueue([])
    
    for v in g:
        if v != s:
            dist[v] = INF
            prev[v] = None
        q.enqueue(v, INF)
    
    while not q.is_empty():
        u = q.dequeue()
        if u == t:
            break
        else:
            for neighbor in g.neighbors.get(u):
                alt = dist[u] + g.get_edge_weight(u, neighbor)
                if alt < dist[neighbor]:
                    dist[neighbor] = alt
                    prev[neighbor] = u
    return dist, prev
    
def backtrace(dist, prev, target):
    S = []
    u = target
    while prev[u] is not None:
        S.insert(0,(u, dist[u]))
        u = prev[u]
    return S

def main():
    m = read_matrix_file(os.path.join('resources', 'p081_matrix.txt'))
    g = build_graph(m)
    #0 -> 6400
    d,p = dijkstra(g, 0, 6400)
    bt = backtrace(d, p, 6400)
    print bt

def main():
    m = read_matrix_file(os.path.join('resources', 'p081_matrix5x5.txt'))
    g = build_graph(m)
    d,p = dijkstra(g, 0, 25)
    bt = backtrace(d, p, 25)
    print bt

if __name__ == "__main__":
    t1 = time.time()
    main()
    t2 = time.time()
    print 'Runtime: %0.3f sec' % float((t2 - t1))
