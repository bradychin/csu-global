def main():
    # Take user input
    num1 = input('\nEnter the first number: ')
    num2 = input('Enter the second number: ')

    # Print results
    print(f"\n{num1} plus {num2} equals {float(num1) + float(num2)}")
    print(f"{num1} minus {num2} equals {float(num1) - float(num2)}\n")

if __name__ == "__main__":
    main()