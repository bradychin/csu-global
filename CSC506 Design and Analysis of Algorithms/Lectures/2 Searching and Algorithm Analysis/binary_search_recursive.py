def binary_search_recursive(numbers, low, high, key):
    if low > high:
        return -1
    mid = int((high + low) / 2)
    if numbers[mid] < key:
        return binary_search_recursive(numbers, mid+1, high, key)
    elif numbers[mid] > key:
        return binary_search_recursive(numbers, low, mid-1, key)
    return mid

def main():
    numbers = [14, 26, 42, 59, 71, 88, 92]
    low = 0
    high = len(numbers)
    key = 42

    print(binary_search_recursive(numbers, low, high, key))

if __name__ == '__main__':
    main()