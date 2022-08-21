# CS61B https://www.youtube.com/watch?v=qho01LjqOIg&list=PL8FaHk7qbOD4tIQrwqsx16fNq6uXNhauw&index=4
graph = {
  '0' : ['1'],
  '1' : ['0','2', '4'],
  '2' : ['1','5'],
  '3' : ['4'],
  '4' : ['1','3','5'],
  '5' : ['2','4','6','8'],
  '6' : ['5','7'],
  '7' : ['6'],
  '8' : ['5'],
}
from collections import deque
# bfs_shortest
edgeTo = dict()
distTo = dict()
queue = deque()
marked = set()
# bfs start from s
def bfs_shortest(s,graph):
    distTo[s] = 0
    marked.add(s)
    queue.append(s)
    while queue:
        next_s = queue.popleft()
        print(next_s)
        neighbors = graph[next_s]
        for n in neighbors:
            if n not in marked:
                marked.add(n)
                queue.append(n)
                edgeTo[n] = next_s
                distTo[n] = distTo[next_s] + 1

# bfs_shortest('0',graph)
# print(distTo)
# print(edgeTo)


# cs61b https://www.youtube.com/watch?v=iMoFtG1md3w
graph = {
  0 : {1:2,2:1},
  1 : {2:5,3:11,4:3},
  2 : {5:15},
  3 : {4:2},
  4 : {2:1,5:4,6:5},
  5 : {},
  6 : {3:1,5:1},
}


from queue import PriorityQueue
import sys

fringe = PriorityQueue()
distTo = dict()
edgeTo = dict()
already_best = set()

# initial fringe
# initial disTo
for node in graph:
  fringe.put((sys.maxsize,node))
  distTo[node] = sys.maxsize

# O( (E+V)*log(V))
def dijikstra(s):
  distTo[s] = 0
  edgeTo[s] = s
  fringe.put((0,s))
  while len(already_best) < len(graph):
    cur_best = fringe.get()[1]
    print(cur_best)
    already_best.add(cur_best)
    neighbors = graph[cur_best]
    for neighbor in neighbors:
      if neighbor not in already_best:
        # relax cur_best
        if distTo[neighbor] > distTo[cur_best] + graph[cur_best][neighbor]:
          distTo[neighbor] = distTo[cur_best] + graph[cur_best][neighbor]
          edgeTo[neighbor] = cur_best
          fringe.put((distTo[neighbor],neighbor))

# print('-----------------dijikstra-----------')
# dijikstra(0)


# A_star
# instead using only distTo[s]+ lenghth(v,s) we now add a hypothesis towards goal
# the hypothesis h(v,goal) is the hytpothesis distance from v to goal node. 
# to simplify we use the smallest edge go out from node v as its h(v,goal)

from queue import PriorityQueue
import sys
fringe = PriorityQueue()
distTo = dict()
edgeTo = dict()
already_best = set()
# initial fringe
# initial disTo
for node in graph:
  fringe.put((sys.maxsize,node))
  distTo[node] = sys.maxsize
# inital hypothesis
hypothesis = dict()
for v in graph:
  if graph[v] != {}:
    hypothesis[v] = min( list(graph[v].values()) )
  else:
    hypothesis[v] = sys.maxsize # there is no outgoing edges from v so we set it to infinity

def A_star(s):
  distTo[s] = 0
  edgeTo[s] = s
  fringe.put((0,s))
  while len(already_best) < len(graph):
    cur_best = fringe.get()[1]
    print(cur_best)
    already_best.add(cur_best)
    neighbors = graph[cur_best]
    for neighbor in neighbors:
      if neighbor not in already_best:
        # relax cur_best
        if distTo[neighbor] > distTo[cur_best] + graph[cur_best][neighbor]:
          distTo[neighbor] = distTo[cur_best] + graph[cur_best][neighbor]
          edgeTo[neighbor] = cur_best
          fringe.put((distTo[neighbor]+hypothesis[neighbor],neighbor))

print('-----------------A*-----------')
A_star(0)
print(distTo)
print(edgeTo)

# change hypothesis and then rerun A_star.
# inital hypothesis
print('---------better hypothesis-------')
fringe = PriorityQueue()
distTo = dict()
edgeTo = dict()
already_best = set()
# initial fringe
# initial disTo
for node in graph:
  fringe.put((sys.maxsize,node))
  distTo[node] = sys.maxsize
hypothesis = {0:0,1:2,2:1,3:11,4:5,5:9,6:10}
A_star(0)
print(distTo)
print(edgeTo)
