import os
os.system('cls' if os.name == 'nt' else 'clear')

def main():
    number_of_books_purchased = int(input('Enter the number of books purchased this month: '))
    points = 0

    if number_of_books_purchased >= 2 and number_of_books_purchased < 4:
        points += 5
    elif number_of_books_purchased >= 4 and number_of_books_purchased < 5:
        points += 15
    elif number_of_books_purchased >= 6 and number_of_books_purchased < 8:
        points += 30
    elif number_of_books_purchased >= 8:
        points += 60

    print(f'Points awarded: {points}')


if __name__ == '__main__':
    main()