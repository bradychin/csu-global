import os
os.system('cls' if os.name == 'nt' else 'clear')

class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0, item_quantity=0, item_description='none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
    
    def total_item_price(self):
        return self.item_price * self.item_quantity
    
    def print_item_cost(self):
        return f'{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${self.total_item_price():.2f}'

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020", cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items
    
    def add_item(self, item_to_puchase):
        self.cart_items.append(item_to_puchase)

    def remove_item(self, item_name):
        for item in range(len(self.cart_items)):
            if self.cart_items[item].item_name == item_name:
                self.cart_items.remove(self.cart_items[item])
                break
        if all(self.cart_items[item].item_name != item_name for item in range(len(self.cart_items))):
            print('Item not found in cart. Nothing Removed')

    def modify_item(self, new_item_to_purchase, item_to_change):
        item_to_change.item_name = new_item_to_purchase.item_name
        item_to_change.item_price = new_item_to_purchase.item_price
        item_to_change.item_quantity = new_item_to_purchase.item_quantity
        item_to_change.item_description = new_item_to_purchase.item_description

    def get_num_items_in_cart(self):
        num_items = 0
        for item in range(len(self.cart_items)):
            num_items += self.cart_items[item].item_quantity
        return num_items

    def get_cost_of_cart(self):
        total_cost = 0
        for item in range(len(self.cart_items)):
            total_cost += self.cart_items[item].total_item_price()

        return total_cost

    def print_total(self):
        empty_output = 'SHOPPING CART IS EMPTY'

        total_output = []
        total_output.append(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
        total_output.append(f'Number of Items: {self.get_num_items_in_cart()}')
        for item in range(len(self.cart_items)):
            total_output.append(self.cart_items[item].print_item_cost())
        total_output.append(f'Total: ${self.get_cost_of_cart():.2f}')
        
        return '\n'.join(total_output) if self.cart_items else empty_output

    def print_descriptions(self):
        final_output = []
        final_output.append(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
        final_output.append(f'Item Descriptions')
        for item in range(len(self.cart_items)):
            final_output.append(f'{self.cart_items[item].item_name}: {self.cart_items[item].item_description}')
        return '\n'.join(final_output)

def print_menu(shopper):
    while True:
        print('\nMenu\n'
              'a - Add item to cart\n'
              'r - Remove item from cart\n'
              'c - Change item quantity\n'
              'i - Output items descriptions\n'
              'o - Output shopping cart\n'
              'q - Quit\n'
              )
        while True:
            try:
                choice = str(input('Chose an option: '))
                if choice == 'a' or choice == 'r' or choice == 'c' or choice == 'i' or choice == 'o' or choice == 'q':
                    break
                else:
                    print('Choose a valid menu item.')
            except ValueError:
                print('Please enter a menu item.')
        
        if choice == 'a':
            item_to_add = str(input(f'\nPlease enter the item: '))
            while True:
                try:
                    price = float(input(f'How much do(es) the {item_to_add} cost? $'))
                    if price <= 0:
                        print(f'{item_to_add} are not free!')
                    else:
                        break
                except ValueError:
                    print('Please enter a number')
            while True:
                try: 
                    quantity = int(input('How many do you want? '))
                    if quantity <= 0:
                        print(f'You need to have at least 1 {item_to_add}')
                    else:
                        break
                except ValueError:
                    print('Please enter a number')
            description = str(input('Enter item description: '))
            item_to_purchase = ItemToPurchase(item_to_add, price, quantity, description)
            shopper.add_item(item_to_purchase)
        elif choice == 'r':
            item_to_remove = input('What item do you want to remove? ')
            shopper.remove_item(item_to_remove)
        elif choice == 'c':
            item_to_modify = str(input('What item would you like to modify? '))
            for item in range(len(shopper.cart_items)):
                if item_to_modify == shopper.cart_items[item].item_name:
                    new_item_name = str(input('Enter the new item name: '))
                    new_price = float(input('Enter the new item price: '))
                    new_quantity = float(input('How many do you want? '))
                    new_description = str(input('Enter the new description: '))
                    new_item = ItemToPurchase(new_item_name, new_price, new_quantity, new_description)
                    shopper.modify_item(new_item, shopper.cart_items[item])
                    break
            if all(item_to_modify != shopper.cart_items[item].item_name for item in range(len(shopper.cart_items))):
                print('Item not found in cart. Nothing modified.')
        elif choice == 'i':
            print('\nOUTPUT ITEMS\' DESCRIPTION')
            print(shopper.print_descriptions())
        elif choice == 'o':
            print('\nOUTPUT SHOPPING CART')
            print(shopper.print_total())
        elif choice == 'q':
            print('\nThanks for shopping!\n')
            break


def main():
    shopper = ShoppingCart('Brady')
    print_menu(shopper)
    
if __name__ == '__main__':
    main()