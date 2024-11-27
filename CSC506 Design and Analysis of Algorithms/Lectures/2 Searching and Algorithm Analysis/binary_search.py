def binary_search(dataset, key, show_data):
    mid = 0
    low = 0
    high = len(dataset) - 1
    counter = 0

    while high >= low:
        counter += 1
        mid = int((high + low) / 2)
        if dataset[mid] < key:
            low = mid + 1
        elif dataset[mid] > key:
            high = mid - 1
        else:
            return mid, counter

        if show_data:
            print(f'({counter}) Index {mid}: {dataset[mid]}')

    return -1, counter

def given_dataset():
    data = [12, 18, 22, 34, 41, 74, 88]

    i = 0
    key = 0
    key_index = 0

    print('NUMBERS: ')
    for i in range(len(data)):
        print(f'Index {i}: {data[i]}')

    key = int(input('\nEnter a search value: '))

    key_index = binary_search(data, key, True)

    if key_index[0] == -1:
        return print(f'\nWe did not find {key}.\nIterations: {key_index[1]}')
    else:
        return print(f'\nFound {key} at index {key_index[0]}.\nIterations: {key_index[1]}')

def placeholder_dataset():
    size = int(input('Enter dataset size: '))
    dataset = []
    for i in range(size):
        dataset.append(i)

    out_of_range = int(input('Search too low [0] or too high [1]: '))
    location = max(dataset)+1 if out_of_range == 1 else min(dataset)-1

    iterations = binary_search(dataset, location, False)

    return print(f'\nIterations: {iterations[1]}')

def main():
    decision = int(input('Use given dataset [0] or placeholder dataset [1]: '))
    if decision == 0:
        given_dataset()
    elif decision == 1:
        placeholder_dataset()
    else:
        print('Please rerun')

if __name__ == '__main__':
    main()