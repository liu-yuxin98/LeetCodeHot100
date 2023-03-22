

def bfs(graph, node):
    from collections import deque
    visited = set()
    fringe = deque([])
    fringe.append(node)
    while fringe:
        node = fringe.popleft()
        visited.add(node)
        neighbors = graph[node]
        for neighbor in neighbors:
            if neighbor not in visited:
                fringe.append(neighbor)
