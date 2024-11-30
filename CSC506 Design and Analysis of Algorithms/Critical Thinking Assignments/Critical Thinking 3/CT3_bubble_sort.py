def bubble_sort(records):
    # Change as necessary
    sort_key = 'PatientID'

    for i in range(len(records) - 1, 0, -1):
        for j in range(i):
            if records[j][sort_key] > records[j + 1][sort_key]:
                temp = records[j]
                records[j] = records[j + 1]
                records[j + 1] = temp

def main():
    patient_records = [
        {"PatientID": 101, "Name": "Bob", "Age": 30, "Condition": "Diabetes"},
        {"PatientID": 105, "Name": "Charlie", "Age": 35, "Condition": "High Blood Pressure"},
        {"PatientID": 102, "Name": "Diana", "Age": 28, "Condition": "Asthma"},
        {"PatientID": 103, "Name": "Alice", "Age": 25, "Condition": "Flu"},
        {"PatientID": 104, "Name": "Eve", "Age": 40, "Condition": "Arthritis"},
    ]

    bubble_sort(patient_records)

    print('Sorted list of patient records:')
    for record in patient_records:
        print(record)

if __name__ == '__main__':
    main()