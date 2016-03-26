'''
http://projecteuler.net/problem=83
Solution: N/A
Runtime: N/A
'''
import time
import os

from graph.graphs import Graph

p81 = __import__('Problem 081')

def build_graph(matrix):
    g = Graph(directed=False)
    g.add_node(0)
    row_jump = len(matrix[0])
    node_counter = 0
    
    for i, row in enumerate(matrix):
        for j, column in enumerate(row):
            if j != len(row) - 1:
                g.add_edge(node_counter, node_counter + 1, column)
            if i != len(matrix) - 1:
                g.add_edge(node_counter, node_counter + row_jump, row[j])
            node_counter += 1
    g.add_edge(24, 25, matrix[-1][-1])
    #g.add_edge(19, 25, matrix[-1][-1])
    return g

def main():
    m = p81.read_matrix_file(os.path.join('resources', 'p083_matrix.txt'))
    g = build_graph(m)
    #0 -> 6400
    d,p = p81.dijkstra(g, 0, 6400)
    bt = p81.backtrace(d, p, 6400)
    print bt
    
def small_matrix():
    m = p81.read_matrix_file(os.path.join('resources', 'p083_matrix5x5.txt'))
    g = build_graph(m)
    print g
    d,p = p81.dijkstra(g, 0, 25)
    bt = p81.backtrace(d, p, 25)
    print bt

if __name__ == "__main__":
    t1 = time.time()
    small_matrix()
    t2 = time.time()
    print 'Runtime: %0.3f sec' % float((t2 - t1))
