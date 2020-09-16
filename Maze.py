#Dungen Maze problem
from collections import deque 
#1. Ingest input Maze
input = ["S..#...",".#...#.",".#.....","..##...","#.#E.#." ]
maze = []
for row in input:
  cols = list(row);
  maze.append(cols)

dr= [-1,1,0,0]
dc= [0,0,-1,1]
R = len(maze)
C = len(maze[0])
rq = deque()
cq = deque()



class point:
  def __init__(self,row,col):
    self.row = row
    self.col = col
  def __eq__(self, another):
    return  self.row == another.row and self.col == another.col
  def __hash__(self):
    return hash(self.row) + hash(self.col)
  def __str__(self):
    return  "row={}|col={}".format(self.row ,self.col)

 
prev = {}



def explore_neighbours(r,c):
  for i in range(4):
    row = r + dr[i]
    col = c + dc[i]

    if ( row < 0 or col < 0 ):
       continue
    if ( row >= R or col >= C ):
       continue

    if (visited[row][col]):
       continue;
    if (maze[row][col] == "#"):
       continue;

    visited[row][col] = True
    rq.append(row)
    cq.append(col)
    prev[point(row,col)] =  point(r,c)


#2. Find the Start
sc =-1
sr =-1
for row in range(len(maze)):
  for col in range(len(maze[0])):
    if ( maze[row][col] == "S"):
      sr = row
      sc = col

print ("sr=%s|sc=%s",sr,sc)


visited = [[False for i in range(C)] for j in range(R)]

rq.append(sr)
cq.append(sc)
visited[sr][sc] = True;

found = False
end_point = None
while (rq):
  r = rq.pop();
  c = cq.pop();

  if (maze[r][c] == "E"):
    end_point = point(r,c)
    found = True
    break
  explore_neighbours(r,c);


next= prev[end_point]
solved = maze
while (next):
  if ( solved[next.row][next.col] == "S"):
    break
  solved[next.row][next.col] = "*"
  print ("row={}|col={}".format(next.row,next.col))
  next = prev.get(next,None)

for row in range(len(solved)):
  for col in range(len(solved[0])):
    print (solved[row][col],end=" ")
  print()
  
  
