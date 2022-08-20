
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

# find connnectivity
marked = set()
def dfs_connected(s,t,graph):
    marked.add(s)
    if s == t:
        return True
    neighobrs = graph[s]
    for neighbor in neighobrs:
        if neighbor not in marked:
            value = dfs_connected(neighbor,t,graph)
            if value:
                return True
    return False
# for i in range(9):
#     for j in range(9):
#         marked = set()
#         print(str(i),str(j),dfs_connected(str(i),str(j),graph))


# find path between to node using dfs
edgeTo = dict()
marked = set()
# search the space start from s
def dfs(s,graph):
    marked.add(s)
    neighbors = graph[s]
    for neighbor in neighbors:
        if neighbor not in marked:
            edgeTo[neighbor] = s
            dfs(neighbor,graph)

dfs('0',graph)
print(edgeTo)

