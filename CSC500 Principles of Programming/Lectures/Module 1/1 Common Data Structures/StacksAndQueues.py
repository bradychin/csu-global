# Try out python stack functions

# TODO: create new empty stack
stack = []

# TODO: push items onto stack
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

# TODO: print stack
print(stack)

# TODO: pop an item off the stack
x = stack.pop()
print(x)
print(stack)

# Try out pythonqueus functions
from collections import deque

# TODO: create a new empty deque object that will function as a queue
queue = deque()

# TODO: add some items to queue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

# TODO: print queue 
print(queue)

# TODO: pop 
y = queue.popleft()
print(y)
print(queue)