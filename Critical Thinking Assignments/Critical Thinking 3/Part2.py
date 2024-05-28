def main():
    time_now = input('\nEnter the current time (24hr): ')
    wait = input('Enter how many hours to wait for the alarm: ')
    alarm_time = calculate_alarm_time(int(time_now), int(wait))

    print(f'\nYour alarm will ring at {alarm_time}:00.\n')

def calculate_alarm_time(time, duration):
    while True:
        if duration >= 12:
            duration -= 12
            time += 12
            if time >= 24:
                time -= 24
        else:
            time += duration
            return time

if __name__ == '__main__':
    main()