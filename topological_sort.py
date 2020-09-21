from queue import Queue
from graph import *

def topological_sort(graph):
    queue = Queue();
    indegreeMap = {}

    for i in range(graph.numVertices):
        indegreeMap[i] = graph.get_indegree(i)

        if  ( indegreeMap[i] == 0):
            queue.put(i)
    sorted_list = []
    while not queue.empty():
        v = queue.get()
        sorted_list.append(v)

        for nv in graph.get_adjacent_vertices(v):
            indegreeMap[nv] = indegreeMap[nv] -1
            if indegreeMap[nv] == 0:
                queue.put(nv)

    if len(sorted_list) != graph.numVertices:
        raise ValueError("Not a DAG")
    return sorted_list

g = AdjacencySetGraph(9,True)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(2,7)
g.add_edge(2,4)
g.add_edge(2,3)
g.add_edge(1,5)
g.add_edge(5,6)
g.add_edge(3,6)
g.add_edge(3,4)
g.add_edge(6,8)

ts = topological_sort(g)
print (ts)

