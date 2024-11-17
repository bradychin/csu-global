# Saves memory but does not decrease runtime O(N*M)

def longest_common_substring_optimized(string1, string2):
    matrix_row = [0] * len(string2)
    max_value = 0
    max_value_row = 0

    for row in range(len(string1)):
        up_left = 0
        for column in range(len(string2)):
            saved_current = matrix_row[column]
            if string1[row] == string2[column]:
                matrix_row[column] = up_left + 1
                if matrix_row[column] > max_value:
                    max_value = matrix_row[column]
                    max_value_row = row
            else:
                matrix_row[column] = 0
            up_left = saved_current
    start_index = max_value_row - max_value + 1
    return string1[start_index : max_value_row+1]

print(longest_common_substring_optimized('look','zybooks'))