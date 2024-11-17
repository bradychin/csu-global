def longest_common_substring(string1, string2):
    rows = len(string1)
    columns = len(string2)
    matrix = []
    for i in range(rows):
        matrix.append([0] * columns)

    max_value = float('-inf')
    max_row = 0
    max_column = 0

    print(f'   {'  '.join(string2)}')
    for row in range(rows):
        for column in range(columns):
            if string1[row] == string2[column]:
                up_left = 0
                if row >= 0 and column >= 0:
                    up_left = matrix[row-1][column-1]
                    matrix[row][column] = 1 + up_left
                    if matrix[row][column] > max_value:
                        max_value = matrix[row][column]
                        max_row = row
                        max_column = column
                else:
                    matrix[row][column] = 0
        print(f'{string1[row]} {matrix[row]}')

    substring_length = max_value
    print(f'\nsubstring length: {substring_length}')
    row_index = max_row
    print(f'max row index: {max_row}')
    start_index = row_index - substring_length + 1
    print(f'start row index: {start_index}')

    return print(f'Longest Common String: {string1[start_index : start_index + substring_length]}')

longest_common_substring('embrace', 'braille')
