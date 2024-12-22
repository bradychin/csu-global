# Run "bellman_ford_test_input.py" to test this algorithm

def bellman_ford(graph, start, target=''):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    parent = {node: None for node in graph}

    for _ in range(len(graph)-1):
        for current in graph:
            for neighbour, weight in graph[current]:
                if distances[current] + weight < distances[neighbour]:
                    distances[neighbour] = distances[current]  + weight
                    parent[neighbour] = current

    # negative cycle check
    for current in graph:
        for neighbor, weight in graph[current]:
            if distances[current] + weight < distances[neighbor]:
                print("Negative weight cycle detected.")
                return None, None  # Negative cycle found

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