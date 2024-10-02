# use a recursive algorithm to find a maximum value

# declare a list of value to operate on
items = [6, 20 , 23, 12 , 1, 234, 34, 5]

def find_max(items):
    # TODO: breaking condition: last item in list? return it
    if len(items) == 1:
        return items[0]

    # TODO: other get the first item and call function again to operate 
    # on the rest of the list
    op1 = items[0]
    print('items[0]: ', op1)
    op2 = find_max(items[1:])
    print('findmax: ', op2)

    # TODO: perform the comparision when we're down to just two
    if op1 > op2:
        print('op1: ', op1)
        return op1
    else: 
        print('op2: ', op2)
        return op2

# Test the function
print(find_max(items))