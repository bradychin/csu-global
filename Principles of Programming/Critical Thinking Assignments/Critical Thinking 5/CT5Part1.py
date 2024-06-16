import os
os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        try: 
            number_of_years = int(input('Enter the number of years: '))
            if number_of_years <= 0:
                print('Please enter a valid number of years.')
            else: 
                break
        except ValueError:
                print('Please enter a number.')

    months = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    number_of_months = 0
    rainfall = []

    for year in range(number_of_years):
        print(f'\nYear {year+1}')
        
        for month in months:
            while True:
                try:
                    monthly_rainfall = float(input(f'Enter the inches of rainfall in {month}: '))
                    if monthly_rainfall < 0:
                        print('Please enter a valid amount of rainfall.')
                    else:
                        break
                except ValueError:
                    print('Please enter a number.')
            number_of_months += 1
            rainfall.append(monthly_rainfall)
    
    total_rainfall = sum(rainfall)
    average_rainfall = total_rainfall/number_of_months

    print(f'\nNumber of months: {number_of_months}')
    print(f'Total rainfall: {total_rainfall} inches')
    print(f'Average rainfall over {number_of_months} months: {average_rainfall:.2f} inches/month\n')

if __name__ == '__main__':
    main()