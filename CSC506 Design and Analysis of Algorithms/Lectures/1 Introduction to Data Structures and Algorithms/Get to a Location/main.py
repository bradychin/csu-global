import math

# Point class
class Point:
    def __init__(self):
        self.x = 0
        self.y = 0


# Main program
# Define all points
# Read in x and y for Point P1
p = Point()
# p.x = int(input('Enter p.x: '))
# p.y = int(input('Enter p.y: '))
p.x = int(input())
p.y = int(input())

a = Point()
a.x = 0
a.y = 0

temp = Point()
temp.x = 0
temp.y = 0

# Read in num of steps to be taken in X and Y directions
# x_steps = int(input('Enter number of steps to be taken in x direction: '))
# y_steps = int(input('Enter number of steps to be taken in y direction: '))
x_steps = int(input())
y_steps = int(input())

# Read in num of steps to be taken (backwards) every 3 steps
# backwards_steps = int(input('Enter number of steps to be taken in the backwards directions: '))
backwards_steps = int(input())

# Write dynamic programming algorithm
iterations = 0
shortest_distance = float('inf')

while True:
    temp.x = a.x + x_steps
    temp.y = a.y + y_steps
    if (iterations+1) % 3 == 0:
        temp.x -= backwards_steps
        temp.y -= backwards_steps
    d = math.sqrt((p.x-temp.x)**2+(p.y-temp.y)**2)
    if d < shortest_distance:
        shortest_distance = d
        iterations += 1
        a.x = temp.x
        a.y = temp.y
        if d == 0:
            break
    elif d >= shortest_distance and temp.x > p.x and temp.y > p.y:
        break
    else:
        iterations += 1
        continue

# Output
print(f'\nPoint p: ({p.x},{p.y})')
print(f'Arrival point: ({a.x},{a.y})')
print(f'Distance between P and arrival: {shortest_distance:.6f}')
print(f'Number of iterations: {iterations}')












