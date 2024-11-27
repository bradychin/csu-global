def fibonacci_number_recursion(term_index):
    if term_index == 0:
        return 0
    elif term_index == 1:
        return 1
    else:
        return fibonacci_number_recursion(term_index - 1) + fibonacci_number_recursion(term_index - 2)


def fibonacci_number_dynamic(term_index):
    if term_index == 0:
        return 0
    previous = 0
    current = 1
    i = 1
    while i < term_index:
        next = previous + current
        previous = current
        current = next
        i += 1
    return current

print(fibonacci_number_recursion(3))
print(fibonacci_number_dynamic(4))