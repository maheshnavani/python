
# Breadth First Seach
from collections import deque

g = {
  0:[9,7,11],
  1:[10,8],
  2:[12,3],
  3:[2,4,7],
  4:[3],
  5:[6],
  6:[7,5],
  7:[3,0,11],
  8:[9,1,12],
  9:[0,10,8],
  10:[1,9],
  11:[0,7],
  12:[2,8]
}

nodes = len(g)

def solve(s):
  q = deque()
  visited = [False for i in  range(nodes)]
  prev = [None for i in range(nodes)]
  visited[s] = True
  q.append(s)
  while (q):
    node = q.pop()
    neighbours = g.get(node)
    for next in neighbours:
      if ( not visited[next]):
        visited[next] = True
        q.append(next)
        prev[next] = node
  return prev

def reconstructPath(s,e,prev):
  path = []
  node = e;
  while (node != None):
    path.append(node)
    node = prev[node]
  
  path.reverse();
  if ( path[0] == s):
    return path
  return []


prev = solve(0)
path  = reconstructPath(0,4,prev)
print (path)
