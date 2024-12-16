# Run "bellman_ford_test_input.py" to test this algorithm

def bellman_ford(graph, start, target=''):
    distances = {node: 0 if node == start else float('inf') for node in graph}
    paths = {node: [] for node in graph}
    paths[start].append(start)

    for _ in range(len(graph)-1):
        for current in graph:
            for neighbour, distance in graph[current]:
                if distance + distances[current] < distances[neighbour]:
                    distances[neighbour] = distance + distances[current]
                    paths[neighbour] = paths[current][:] + [neighbour]

    # negative cycle check
    for current in graph:
        for neighbor, weight in graph[current]:
            if distances[current] + weight < distances[neighbor]:
                print("Negative weight cycle detected.")
                return None, None  # Negative cycle found

    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        print(f'{start} -> {node}:')
        print(f'  Distance: {distances[node]}')
        print(f'  Path: {" -> ".join(paths[node])}')

    return distances, paths