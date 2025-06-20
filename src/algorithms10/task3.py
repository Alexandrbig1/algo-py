import heapq


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


graph = {
    'A': {'B': 3, 'C': 12, 'D': 8},
    'B': {'A': 2, 'C': 1, 'D': 3},
    'C': {'A': 2, 'B': 1, 'D': 10, 'E': 8},
    'D': {'B': 3, 'C': 7, 'D': 10},
    'E': {'C': 8, 'D': 3, 'E': 7},
}

start_vertex = 'A'
shortest_paths = dijkstra(graph, start_vertex)
print("The shortest routes from", start_vertex, ":", shortest_paths)