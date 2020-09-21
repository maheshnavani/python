from queue import Queue
from graph import *
from collections import deque

def build_distance_table(graph, start):
    distance_table = {}
    for vertex in range(graph.numVertices):
        distance_table[vertex] = (None, None)

    queue = Queue()
    queue.put(start)
    distance_table[start] = (0, start)

    while not queue.empty():
        vertex = queue.get()
        current_distance = distance_table[vertex][0]
        for neighbor in graph.get_adjacent_vertices(vertex):
            if ( distance_table[neighbor][0] == None):
                distance_table[neighbor] = ( 1+ current_distance ,vertex)
                queue.put(neighbor)

    return distance_table

def shortest_path(graph , start, end):
    distance_table = build_distance_table(graph, start)

    path = []
    next = end
    while(True):
        path.append(next)
        if distance_table[next][1] == None or distance_table[next][1] == start:
            break
        next = distance_table[next][1]

    if distance_table[next][1] == None:
        print ("No Path from %d to %d" % (start,end))
    else:
        path.append(start)
        path.reverse()
        print (path)

g = AdjacencySetGraph(8,True)
g.add_edge(0, 1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(1,4)
g.add_edge(3,5)
g.add_edge(5,4)
g.add_edge(3,6)
g.add_edge(6,7)
g.add_edge(0,7)

shortest_path(g, 0, 5)
shortest_path(g, 0, 6)
shortest_path(g, 7, 4)
