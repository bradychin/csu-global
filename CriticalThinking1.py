# Part 1
def add(number1, number2):
    return float(number1) + float(number2)

def subtract(number1, number2):
    return float(number1) - float(number2)

# Part 2 
def multiply(number1, number2):
    return float(number1) * float(number2)

def divide(number1, number2):
    return float(number1) / float(number2)

# Take user input
num1 = input('\nEnter the first number: ')
num2 = input('Enter the second number: ')

# Print results
print(f"\n{num1} plus {num2} equals " + str(add(num1, num2)))
print(f"{num1} minus {num2} equals " + str(subtract(num1, num2)))
print(f"{num1} times {num2} equals " + str(multiply(num1, num2)))
print(f"{num1} divided by {num2} equals " + str(divide(num1, num2)) + "\n")