from priority_dict import *
from graph import *


def build_distance_table (graph , source):
    distance_table = {}

    for v in range (graph.numVertices):
        distance_table[v] = (None,None)
    distance_table[source] = (0,source)

    priority_queue = priority_dict()
    priority_queue[source] = 0

    while len(priority_queue.keys()) > 0:
        current_vertex = priority_queue.pop_smallest()
        current_distance = distance_table[current_vertex][0]

        for neighbor in graph.get_adjacent_vertices(current_vertex):
            distance = current_distance + graph.get_edge_weight(current_vertex,neighbor)
            neighbor_distance = distance_table[neighbor][0]
            if (neighbor_distance == None or neighbor_distance > distance):
                distance_table[neighbor] = (distance,current_vertex)
                priority_queue[neighbor]  = distance

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

g = AdjacencyMatrixGraph(8,True)
g.add_edge(0, 1,1)
g.add_edge(1,2,2)
g.add_edge(1,3,6)
g.add_edge(2,3,2)
g.add_edge(1,4,3)
g.add_edge(3,5,1)
g.add_edge(5,4,5)
g.add_edge(3,6,1)
g.add_edge(6,7,1)
g.add_edge(0,7,8)

shortest_path(g,0,6)
shortest_path(g,4,7)
shortest_path(g,7,0)

