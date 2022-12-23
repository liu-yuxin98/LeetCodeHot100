
def shortestPathLength(graph: list[list[int]]) -> int:

    from collections import deque
    fringe = deque()
    path = []
    # suppose start from node i 
    i = 0
    fringe.append(i)
    visited = []
    while fringe:
        if len(visited) == len(graph):
            return path
        node = fringe.popleft()
        if node not in visited:
            visited.append(node)
        
        path.append(node)

        neighbors = graph[node]
        visited_neighbors = [neighbor for neighbor in neighbors if neighbor in visited ]
        un_visited_neighbors = [neighbor for neighbor in neighbors if neighbor not in visited ]

        for neighbor in un_visited_neighbors:
            fringe.append(neighbor)
        for neighbor in visited_neighbors:
            fringe.append(neighbor)

    return False


graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]


print(shortestPathLength(graph))