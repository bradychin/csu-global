def linear_search(database, search_item, show_data):
    counter = 0
    for index in range(len(database)):
        counter += 1
        if show_data:
            print(f'({counter}) Index {index}: {database[index]}')
        if database[index] == search_item:
            return index, counter
    else:
        return -1, counter

def given_dataset():
    data = [12, 75, 18, 22, 94, 16, 22]

    i = 0
    key = 0
    key_index = 0

    print('NUMBERS: ')
    for i in range(len(data)):
        print(f'Index {i}: {data[i]}')

    key = int(input('\nEnter a search value: '))

    key_index = linear_search(data, key, True)

    if key_index[0] == -1:
        return print(f'\nWe did not find {key},\nIterations: {key_index[1]}')
    else:
        return print(f'\nFound {key} at index {key_index[0]}.\nIterations: {key_index[1]}')

def placeholder_dataset():
    size = int(input('Enter dataset size: '))
    dataset = []
    for i in range(size):
        dataset.append(i)

    out_of_range = int(input('Search too low [0] or too high [1]: '))
    location = max(dataset)+1 if out_of_range == 1 else min(dataset)-1

    iterations = linear_search(dataset, location, False)

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