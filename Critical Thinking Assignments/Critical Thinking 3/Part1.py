import os
os.system('cls' if os.name == 'nt' else 'clear')
from decimal import *

def main():
    while True:
        try:
            charge = Decimal(input('\nEnter the cost of the food: $'))
            if charge <= 0:
                print('Food isn\'t free!')
            else:
                break
        except Exception:
            print('Please enter a number.')

    tip = Decimal('0.18')
    sales_tax = Decimal('0.07')
    
    amount_with_tip = charge * tip
    amount_with_tax = charge * sales_tax

    print(f'\n18% tip: ${amount_with_tip}')
    print(f'7% sales tax: ${amount_with_tax}')
    print(f'Total price: ${charge + amount_with_tip + amount_with_tax}\n')

if __name__ == '__main__':
    main()