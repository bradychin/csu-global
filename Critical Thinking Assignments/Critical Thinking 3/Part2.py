import os
os.system('cls' if os.name == 'nt' else 'clear')

def get_current_time():
    while True:
        try:
            time_now = int(input('\nEnter the current time (00 - 23): '))
            if time_now > 23 or time_now < 0:
                print('The time must be between the hours 00 and 23.')
            else:
                return time_now
        except ValueError:
            print('Please enter a number.')

def get_wait_time():
    while True:
        try: 
            wait = int(input('\nEnter how many hours to wait for the alarm: '))
            if wait < 0:
                print('You cannot set an alarm in the past.')
            else:
                return wait
        except ValueError: 
            print('Please enter a number.')


def calculate_alarm_time(time, duration):
    while True:
        if duration >= 12:
            duration -= 12
            time += 12
            if time >= 24:
                time -= 24
        else:
            time += duration
            if time >= 24:
                time -= 24
            elif time == 24:
                time == 0
            return time

def main():
    current_time = get_current_time()
    wait_time = get_wait_time()
    alarm_time = calculate_alarm_time(current_time, wait_time)

    print(f'\nCurrent time: {current_time}:00')
    print(f'Alarm set {wait_time} hour(s) from now.')
    print(f'Your alarm will ring at {alarm_time}:00.\n')

if __name__ == '__main__':
    main()