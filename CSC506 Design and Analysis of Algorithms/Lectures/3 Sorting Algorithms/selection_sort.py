def selection_sort(numbers):
    comparisons = 0
    for i in range(len(numbers)):
        index_smallest = i
        print(f'\ni {i}: Loop iteration {i+1}')

        for j in range(i + 1, len(numbers)):
            comparisons += 1
            print(f'j {j}: {numbers}')
            if numbers[j] < numbers[index_smallest]:
                index_smallest = j

        temp = numbers[i]
        numbers[i] = numbers[index_smallest]
        numbers[index_smallest] = temp
        print(f'End iteration: {numbers}')

    return comparisons

def main():
    numbers = [10, 2, 78, 4, 45, 32, 7, 11]

    # Display the contents of the list
    print('UNSORTED:', numbers)

    # Call the selection_sort() function
    comparisons = selection_sort(numbers)

    # Display the (sorted) contents of the list
    print('\nSORTED:', numbers)
    print(f'Total Comparisons: {comparisons}')

if __name__ == '__main__':
    main()