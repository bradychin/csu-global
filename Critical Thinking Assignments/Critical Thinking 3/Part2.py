def main():
    time_now = input('\nEnter the current time (24hr): ')
    wait = input('Enter how many hours to wait for the alarm: ')
    alarm_time = calculate_time(time_now, wait)

    print(f'\nYour alarm will ring at {alarm_time}:00.\n')

def calculate_time(current_time, duration):
    parse = divmod(int(duration), 12)
    return int(current_time) + parse[1]

if __name__ == '__main__':
    main()