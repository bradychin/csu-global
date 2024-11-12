# List
x = [1, 2, 3, 4, 5]
x[1] = 42
for i in x:
    print(f'i is {i}')

# Tuple
y = (1, 2, 3, 4, 5)
# y[1] = 23 # error
for i in y:
    print(f'i is {i}')

# Dict
x = {'one': 1, 'two': 2, 'three': 3}
x['three'] = 43
for key, value in x.items():
    print(f'key: {key}, value: {value}')

