import os
os.system('cls' if os.name == 'nt' else 'clear')

def get_course_information(request):
    course_information = [
        {'course': 'CSC101', 'Room Number': 3004, 'Instructor': 'Haynes', 'Meeting Time': '8:00am'},
        {'course': 'CSC102', 'Room Number': 4501, 'Instructor': 'Alvarado', 'Meeting Time': '9:00am'},
        {'course': 'CSC103', 'Room Number': 6755, 'Instructor': 'Rich', 'Meeting Time': '10:00am'},
        {'course': 'NET110', 'Room Number': 1244, 'Instructor': 'Burke', 'Meeting Time': '11:00am'},
        {'course': 'COM241', 'Room Number': 1411, 'Instructor': 'Lee', 'Meeting Time': '1:00pm'}
    ]
    for information in course_information:
        if request == information['course']:
            return (
                f'\nCourse {request} information:'
                f'\nRoom number: {information['Room Number']}'
                f'\nInstructor: {information['Instructor']}'
                f'\nMeeting time: {information['Meeting Time']}\n'
            )
                
def main():
    while True:
        request = input(f'\nPlease enter a course number: ')
        if get_course_information(request) == None:
            print('That is not a valid course code.')
        else:
            print(get_course_information(request))
            break


if __name__ == '__main__':
    main()