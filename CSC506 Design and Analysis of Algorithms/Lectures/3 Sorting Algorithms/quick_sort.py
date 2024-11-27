import math

from qiskit.pulse.library.samplers import midpoint

counter_partitions = 0
counter_comparisons = 0

def partition(numbers, low_index, high_index):
    global counter_partitions, counter_comparisons
    counter_partitions += 1
    print(f'Counter Partitions: {counter_partitions}')
    midpoint = int(low_index + (high_index-low_index) / 2)
    pivot = numbers[midpoint]

    done = False

    while not done:
        while numbers[low_index] < pivot:
            counter_comparisons += 1
            low_index += 1

        while numbers[high_index] > pivot:
            counter_comparisons += 1
            high_index -= 1

        counter_comparisons += 1
        if low_index >= high_index:
            done = True
        else:
            temp = numbers[low_index]
            numbers[low_index] = numbers[high_index]
            numbers[high_index] = temp

            low_index += 1
            high_index -= 1

    return high_index

def quick_sort(numbers, low_index, high_index):
    if low_index >= high_index:
        return
    low_end_index = partition(numbers, low_index, high_index)
    print(numbers)
    quick_sort(numbers, low_index, low_end_index)
    quick_sort(numbers, low_end_index + 1, high_index)
    return numbers

def main():
    global counter_partitions, counter_comparisons
    numbers = [8, 2, 7, 6, 1, 4, 3, 5]
    low_index = 0
    high_index = len(numbers)-1

    mid = int(low_index + (high_index-low_index) / 2)
    pivot = numbers[mid]
    print(f'Midpoint: {mid}')
    print(f'Pivot: {pivot}')

    counter_partitions = 0
    counter_comparisons = 0

    sorted_numbers = quick_sort(numbers, low_index, high_index)

    print(f'\nSorted numbers: {sorted_numbers}')
    print(f'Total partitions: {counter_partitions}')
    print(f'Total comparisons: {counter_comparisons}')


    list_size = 1024
    print(f'\nFor {list_size} elements.')
    print(f'Best case part: {math.log2(list_size)}')
    print(f'Best case comparisons: {math.log2(list_size)*list_size}')
    print(f'Worst case part: {list_size - 1}')
    print(f'Worst case comparisons: {1+2*(list_size-1)}')

if __name__ == '__main__':
    main()