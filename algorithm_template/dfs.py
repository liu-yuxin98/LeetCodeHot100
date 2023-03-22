
def dfs(graph, node):
    fringe = []
    fringe.append(node)
    visited = set()
    while fringe:
        node = fringe.pop()
        visited.append(node)
        neighbors = graph[node]
        for child in neighbors:
            if child not in visited:
                dfs(graph, child)
