def bubble_sort(numbers):
    for i in range(len(numbers) - 1, 0, -1):
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp
            print(numbers)

def main():
    numbers = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    bubble_sort(numbers)
    print(f'done: {numbers}')

if __name__ == '__main__':
    main()