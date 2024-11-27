def shell_short(numbers, gap_values):
    for gap_value in gap_values:
        print(f'Gap value: {gap_value}')

        for i in range(gap_value):
            print('new loop')
            interleaved_list = insertion_sort_interleaved(numbers, i, gap_value)
            print(f'Interleaved List: {interleaved_list}')

        print(f'Sorted: {numbers}\n')

def insertion_sort_interleaved(numbers, start_index, gap):
    interleaved_list = []

    for i in range(start_index+gap, len(numbers), gap):
        j = i
        print(f'{numbers[j]} < {numbers[j-gap]}: {numbers[j] < numbers[j - gap]}')
        interleaved_list.append(numbers[j])
        interleaved_list.append(numbers[j-gap])

        while (j-gap >= start_index) and (numbers[j] < numbers[j - gap]):
            temp = numbers[j]
            numbers[j] = numbers[j - gap]
            numbers[j - gap] = temp
            j -= gap

    return list(set(interleaved_list))

def main():
    numbers = [23,65,35,89,98,84,94,68,54,67,83,46,91,72,39]
    gap_values = [5, 3, 1]

    shell_short(numbers, gap_values)
    print(f'\nFinal: {numbers}')

if __name__ == '__main__':
    main()