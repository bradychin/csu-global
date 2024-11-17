def build_frequency_table(input_string):
    table = {}
    for char in input_string:
        if char in table:
            table[char] += 1
        else:
            table[char] = 1
    return table

def print_frequency_table(table):
    print('Letter | Frequency')
    for key, value in table.items():
        print(f'   {key}   |    {value}  ')