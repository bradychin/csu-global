def search_database(database, search_item):
    for index in range(len(database)):
        if database[index] == search_item:
            return f'\nItem found at index: {index}'
    else:
        return '\nWe do not have that item.'

def main():
    # Define database
    database = ['eggs', 'milk', 'bacon', 'chicken', 'yogurt', 'brocolli', 'chips']

    # Prompt user for item
    item = input('Enter the item that you are searching for: ')

    # Search database and return index of item
    item_index = search_database(database, item)

    # Print index of the requested item
    print(item_index)

if __name__ == '__main__':
    main()