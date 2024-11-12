import os
os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        try: 
            number_of_books_purchased = int(input('Enter the number of books purchased this month: '))
            if number_of_books_purchased < 0:
                print('Please enter a valid number of books.')
            else: 
                break
        except ValueError:
                print('Please enter a number.')
    points = 0

    if number_of_books_purchased >= 2 and number_of_books_purchased < 4:
        points += 5
    elif number_of_books_purchased >= 4 and number_of_books_purchased < 5:
        points += 15
    elif number_of_books_purchased >= 5 and number_of_books_purchased < 8:
        points += 30
    elif number_of_books_purchased >= 8:
        points += 60

    print(f'Points awarded: {points}\n')

if __name__ == '__main__':
    main()

