from bellman_ford import bellman_ford

test_graphs = [
    [
        {
            'A': [('B', 10), ('F', 8)],
            'B': [('D',2)],
            'C': [('B', 1)],
            'D': [('C', -2)],
            'E': [('B', -4), ('D', -1)],
            'F': [('E', 1)]
        },
        'A',
        ''
    ],
    [
        {
            'A': [('B', 5)],
            'B': [('C', -2)],
            'C': [('D', 3)],
            'D': [('B', -2)]
        },
        'A',
        ''
    ],
    [
        {
            'A': [('B', 4), ('C', 2)],
            'B': [('C', -1), ('D', 5)],
            'C': [('D', 3), ('A', -2)],
            'D': []
        },
        'B',
        'D'
    ],
    [
        {
            'A': [('B', 1), ('C', 4)],
            'B': [('C', -2), ('D', 2)],
            'C': [('D', 3)],
            'D': []
        },
        'B',
        ''
    ]
]

test_case = 1
for graph, start, target in test_graphs:
    print(f'{"Test case " + str(test_case):-^40}')
    print(f'- Start: {start}')
    print(f'- Target: {'All nodes' if target=='' else target}\n')
    bellman_ford(graph, start, target)
    print('\n')
    test_case += 1