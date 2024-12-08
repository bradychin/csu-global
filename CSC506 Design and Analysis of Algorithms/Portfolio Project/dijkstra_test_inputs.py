from dijkstra import dijkstra

test_graphs = [
    [
        {
            'A': [('B', 5), ('C', 3), ('E', 11)],
            'B': [('A', 5), ('C', 1), ('F', 2)],
            'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
            'D': [('C', 1), ('E', 9), ('F', 3)],
            'E': [('A', 11), ('C', 5), ('D', 9)],
            'F': [('B', 2), ('D', 3)]
        },
        'A',
        ''
    ],
    [
        {
            'A': [('B', 4), ('C', 2)],
            'B': [('C', 3), ('D', 2), ('E', 3)],
            'C': [('B', 1), ('D', 4), ('E', 5)],
            'D': [],
            'E': [('D', 1)]
        },
        'B',
        'E'
    ],
    [
        {
            'A': [('B', 2), ('C', 5)],
            'B': [('C', 1), ('D', 4)],
            'C': [('D', 2)],
            'D': []
        },
        'B',
        ''
    ],
    [
        {
            'A': [('B', 3), ('C', 6)],
            'B': [('C', 2), ('D', 1)],
            'C': [('D', 4)],
            'D': [('E', 5)],
            'E': []
        },
        'D',
        'C'
    ]
]

test_case = 1
for graph, start, target in test_graphs:
    print(f'{"Test case " + str(test_case):-^40}')
    print(f'- Start: {start}')
    print(f'- Target: {'All nodes' if target=='' else target}\n')
    dijkstra(graph, start, target)
    print('\n')
    test_case += 1