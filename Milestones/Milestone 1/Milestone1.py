import os
os.system('cls' if os.name == 'nt' else 'clear')

class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
    
    def total_price(self):
        return self.item_price * self.item_quantity
    
    def print_item_cost(self):
        return f'{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = {self.total_price():.2f}'

def main():
    print('\nPlease enter two items.')

    item1_name = str(input('\nPlease enter the first item: '))
    item1_price = float(input('How much does the item cost? '))
    item1_quantity = int(input('How many do you want? '))
    item1 = ItemToPurchase(item1_name, item1_price, item1_quantity)

    item2_name = str(input('\nPlease enter the second item: '))
    item2_price = float(input('How much does the item cost? '))
    item2_quantity = int(input('How many do you want? '))
    item2 = ItemToPurchase(item2_name, item2_price, item2_quantity)

    print('\nTOTAL COST')
    print(item1.print_item_cost())
    print(item2.print_item_cost())
    print(f'Total: ${item1.total_price() + item2.total_price():.2f}\n')
    
if __name__ == '__main__':
    main()