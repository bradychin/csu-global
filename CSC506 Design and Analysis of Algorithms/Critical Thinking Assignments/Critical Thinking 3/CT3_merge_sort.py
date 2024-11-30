def merge(records, i, j, k):

    # Change as necessary
    sort_key = 'Age'

    merged_size = k - i + 1
    merged_numbers = [None] * merged_size
    merge_pos = 0

    left_pos = i
    right_pos = j + 1

    while left_pos <= j and right_pos <= k:
        if records[left_pos][sort_key] <= records[right_pos][sort_key]:
            merged_numbers[merge_pos] = records[left_pos]
            left_pos += 1
        else:
            merged_numbers[merge_pos] = records[right_pos]
            right_pos += 1
        merge_pos += 1

    while left_pos <= j:
        merged_numbers[merge_pos] = records[left_pos]
        left_pos += 1
        merge_pos += 1

    while right_pos <= k:
        merged_numbers[merge_pos] = records[right_pos]
        right_pos += 1
        merge_pos += 1

    for merge_pos in range(merged_size):
        records[i + merge_pos] = merged_numbers[merge_pos]

def merge_sort(numbers, i, k):
    j = 0
    if i < k:
        j = (i+k) // 2
        merge_sort(numbers, i, j)
        merge_sort(numbers, j+1, k)
        merge(numbers, i, j, k)

def main():
    patient_records = [
        {"PatientID": 101, "Name": "Bob", "Age": 30, "Condition": "Diabetes"},
        {"PatientID": 105, "Name": "Charlie", "Age": 35, "Condition": "High Blood Pressure"},
        {"PatientID": 102, "Name": "Diana", "Age": 28, "Condition": "Asthma"},
        {"PatientID": 103, "Name": "Alice", "Age": 25, "Condition": "Flu"},
        {"PatientID": 104, "Name": "Eve", "Age": 40, "Condition": "Arthritis"},
    ]

    merge_sort(patient_records, 0, len(patient_records) - 1)

    print('Sorted list of patient records:')
    for record in patient_records:
        print(record)

if __name__ == '__main__':
    main()
