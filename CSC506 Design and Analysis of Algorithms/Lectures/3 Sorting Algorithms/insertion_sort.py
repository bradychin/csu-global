def insertion_sort(numbers):
    swaps = 0
    comparisons = 0

    for i in range(1, len(numbers)):
        print(f'\nIteration: i = {i}')
        j = i
        while j > 0 and numbers[j] < numbers[j-1]:
            comparisons += 1
            print(f'{numbers[j]} < {numbers[j-1]}: {numbers[j] < numbers[j-1]}')
            temp = numbers[j]
            numbers[j] = numbers[j-1]
            numbers[j-1] = temp
            j -= 1
            swaps += 1
            print(f'Swaps: {swaps}')

        if j > 0:
            comparisons += 1

        print(f'Comparisons: {comparisons}')
        print(f'{numbers}\n')

    return swaps, comparisons

def main():
    numbers = [10, 31, 53, 24, 60, 91, 59, 87, 88]

    swaps, comparisons = insertion_sort(numbers)

    print(f'Total swaps: {swaps}')
    print(f'Total comparisons: {comparisons}')

if __name__ == '__main__':
    main()