filename = 'test.txt'
arr = []
with open(filename, 'r') as file:
    for line in file:
        arr.append(int(line.strip()))
    new_arr = tuple([arr[0], arr[1:]])

print(new_arr)



