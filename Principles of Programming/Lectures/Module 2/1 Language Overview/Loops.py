# Fibonacci series
# The sum of two elements defines the next

a, b = 0, 1

while b < 1000:
    print(b, end = ' ')
    a, b = b, a + b

print()

words = ['apple', 'amazon', 'tesla']
for word in words:
    print(word)
