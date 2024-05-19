def main():
    # Take user input
    num1 = input('\nEnter the first number: ')
    num2 = input('Enter the second number: ')

    # Print results
    # Part 1
    print(f"\n{num1} plus {num2} equals {float(num1) + float(num2)}")
    print(f"{num1} minus {num2} equals {float(num1) - float(num2)}")

    # Part 2
    print(f"{num1} times {num2} equals {float(num1) * float(num2)}")
    print(f"{num1} divided by {num2} equals {round(float(num1) / float(num2), 2)}\n")

if __name__ == "__main__":
    main()