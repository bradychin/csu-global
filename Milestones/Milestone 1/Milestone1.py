import os
os.system('cls' if os.name == 'nt' else 'clear')

class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
    
    def total_item_price(self):
        return self.item_price * self.item_quantity
    
    def print_item_cost(self):
        return f'{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = {self.total_item_price():.2f}'

def main():
    number_of_items = 2
    print(f'\nPlease enter {number_of_items} items.')

    items = []
    for i in range(number_of_items):
        name = str(input(f'\nPlease enter the item {i+1}: '))
        while True:
            try:
                price = float(input(f'How much do(es) the {name} cost? $'))
                if price <= 0:
                    print(f'{name} are not free!')
                else:
                    break
            except ValueError:
                print('Please enter a number')
        while True:
            try: 
                quantity = int(input('How many do you want? '))
                if quantity <= 0:
                    print(f'You need to have at least 1 {name}')
                else:
                    break
            except ValueError:
                print('Please enter a number')
        item = ItemToPurchase(name, price, quantity)
        items.append(item)

    print('\nTOTAL COST')
    total_cost = 0
    for item in range(len(items)):
        print(items[item].print_item_cost())
        total_cost += items[item].total_item_price()

    print(f'Total: ${total_cost:.2f}\n')
    
if __name__ == '__main__':
    main()