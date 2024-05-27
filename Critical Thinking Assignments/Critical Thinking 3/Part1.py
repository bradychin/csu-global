from decimal import *

def main():
    charge = input('\nEnter the cost of the food: $')
    tip = Decimal('0.18')
    sales_tax = Decimal('0.07')
    
    amount_with_tip = Decimal(charge) * tip
    amount_with_tax = Decimal(charge) * sales_tax

    print(f'\n18% tip: ${amount_with_tip}')
    print(f'7% sales tax: ${amount_with_tax}')
    print(f'Total price: ${Decimal(charge) + amount_with_tip + amount_with_tax}\n')

if __name__ == '__main__':
    main()