def numbers_to_words(num):
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
               'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty','sixty', 'seventy', 'eighty', 'ninty']

    if num < 20:
        return numbers[num]
    elif num < 100:
        return f'{tens[num // 10]} {"" if num % 10 == 0 else numbers[num % 10]}'
    elif num < 1000:
        return f'{numbers[num // 100]} hundred {"" if num % 100 == 0 else numbers_to_words(num % 100)}'
    elif num < 1000000:
        return f'{numbers_to_words(num // 1000)} thousand {"" if num % 1000 == 0 else numbers_to_words(num % 1000)}'
    else:
        return f'{numbers_to_words(num // 1000000)} million {"" if num % 1000000 == 0 else numbers_to_words(num % 1000000)}'

def check_writer(amount):
    # Parse dollars and cents
    dollars, cents = divmod(amount, 1)

    # Convert dollars to words
    dollar_words = f'{numbers_to_words(int(dollars))}{" dollars" if int(dollars) > 1 else " dollar"}'

    # Format cents. Convert to words
    formatted_cents = int(round(cents, 2) * 100)
    cent_words = '' if formatted_cents == 0 else numbers_to_words(formatted_cents) + (' cents' if formatted_cents > 1 else ' cent')

    return f'\nAmount in words: {dollar_words} {cent_words}'

if __name__ == '__main__':
    while True:
        try:
            number_input = float(input('Enter amount: '))
            if number_input < 0:
                print('Enter a number larger than 0.')
            elif number_input > 1000000000:
                print('Enter a number less than 1,000,000,000')
            else:
                break
        except ValueError:
            print('Enter a number between 0 and 999,999,999')
    print(check_writer(number_input))