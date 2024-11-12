import os
os.system('cls' if os.name == 'nt' else 'clear')

def check_if_vaild_course(request, dictionary):
    for key in dictionary:
        if request == key:
            return True
    return False

def main():
    room_number = {
        'CSC101': 3004,
        'CSC102': 4501,
        'CSC103': 6755,
        'NET100': 1244,
        'COM241': 1411
    }

    instructors = {
        'CSC101': 'Haynes',
        'CSC102': 'Alvarado',
        'CSC103': 'Rich',
        'NET100': 'Burke',
        'COM241': 'Lee'
    }

    meeting_times = {
        'CSC101': '8:00 am',
        'CSC102': '9:00 am',
        'CSC103': '10:00 am',
        'NET100': '11:00 am',
        'COM241': '1:00 pm'
    }

    print('''Available courses: 
    - CSC101
    - CSC102
    - CSC103
    - NET100
    - COM241
          ''')

    while True:
        try: 
            course_request = input('Please enter a course number: ').upper()
            if check_if_vaild_course(course_request, room_number) == False:
                raise KeyError('No room number found for this request.')
            elif check_if_vaild_course(course_request, instructors) == False:
                raise KeyError('No instructor found for this request.')
            elif check_if_vaild_course(course_request, meeting_times) == False:
                raise KeyError('No meeting time found for this request.')
            else: 
                break
        except KeyError as error:
            print(f'Error: {error}\n')

    print(f'\nInformation for course {course_request}')
    print(f'Room Number: {room_number[course_request]}')
    print(f'Instructor: {instructors[course_request]}')
    print(f'meeting_time: {meeting_times[course_request]}\n')

if __name__ == '__main__':
    main()