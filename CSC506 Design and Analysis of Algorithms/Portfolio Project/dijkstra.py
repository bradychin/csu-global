# Run "dijkstra_test_input.py" to test this algorithm
import heapq

def dijkstra(graph, start, target=''):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    parent = {node: None for node in graph}
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip processing
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                parent[neighbor] = current_node
                heapq.heappush(priority_queue, (new_distance, neighbor))

    def reconstruct_path(end):
        path = []
        while end is not None:
            path.append(end)
            end = parent[end]
        return path[::-1]

    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        path = reconstruct_path(node)
        print(f'{start} -> {node}:')
        print(f'  Distance: {distances[node]}')
        print(f'  Path: {" -> ".join(path) if path else "No Path"}')

    return distances, parent