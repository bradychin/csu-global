x = (1, 'two', 3.0, [4, 'four'], 5)
y = (1, 'two', 3.0, [4, 'four'], 5)
print(f'x is {x}')

print(type(x))
print(type(x[1]))

print(type(x))
print(type(y))
print(id(x))
print(id(y))

if x[0] is y[0]:
    print('yea')
else: 
    print('no')

if x is y:
    print('yea')
else: 
    print('no')

if isinstance(x, tuple):
    print('yea')
elif isinstance(x, list):
    print('list')
else: 
    print('no')