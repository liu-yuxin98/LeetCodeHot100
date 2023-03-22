

def dijkstra(graph, start):
    import heapq
    # Initialize the distance to the starting node to 0 and all other distances to infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Initialize a priority queue with the starting node and its distance
    pq = [(0, start)]

    # Process nodes in order of increasing distance from the starting node
    while pq:
        # Get the node with the smallest distance from the starting node
        distance, node = heapq.heappop(pq)

        # If we've already processed this node, skip it
        if distance > distances[node]:
            continue

        # Update the distances to this node's neighbors if we've found a shorter path
        for neighbor, weight in graph[node].items():
            new_distance = distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(pq, (new_distance, neighbor))

    return distances
