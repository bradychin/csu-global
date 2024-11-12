import os
os.system('cls' if os.name == 'nt' else 'clear')
from inspect import signature, Parameter

class ItemToPurchase:
    def __init__(self, item_name, item_price, item_quantity, item_description):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
    
    def total_item_price(self):
        return self.item_price * self.item_quantity
    
    def print_item_cost(self):
        return f'{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${self.total_item_price():.2f}'

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
    
    def add_item(self, item_to_puchase):
        self.cart_items.append(item_to_puchase)
        print(f'\n{item_to_puchase.item_name} added to cart.')

    def remove_item(self, item_name):
        for item in range(len(self.cart_items)):
            if self.cart_items[item].item_name == item_name:
                self.cart_items.remove(self.cart_items[item])
                print(f'\n{item_name} removed from cart.')
                break
        else: 
            print('\nItem not found in cart. Nothing Removed')

    def modify_item(self, new_item_to_purchase, item_to_change):
        original_item = item_to_change.item_name
        item_to_change.item_name = new_item_to_purchase.item_name
        item_to_change.item_price = new_item_to_purchase.item_price
        item_to_change.item_quantity = new_item_to_purchase.item_quantity
        item_to_change.item_description = new_item_to_purchase.item_description
        print(f'\nItem {original_item} changed to {new_item_to_purchase.item_name}')

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

def enter_item_name(modified=None):
    while True:
        try:
            item_to_add = str(input(f'\nPlease enter modified item: ' if modified else f'\nPlease enter the new item: '))
            if not item_to_add.strip():
                raise ValueError
            else: 
                break
        except ValueError:
            print('The item has to have a name!')
    return item_to_add

def enter_item_price(item_name):
    while True:
        try:
            price = float(input(f'How much do(es) the {item_name} cost? $'))
            if price <= 0:
                print(f'{item_name} are not free!\n')
            else:
                break
        except ValueError:
            print('Please enter a number.\n')
    return price

def enter_item_quantity(item_name):
    while True:
        try: 
            quantity = int(input('How many do you want? '))
            if quantity <= 0:
                print(f'You need to have at least 1 {item_name}.\n')
            else:
                break
        except ValueError:
            print('Please enter a number.\n')
    return quantity

def enter_item_description(item_name):
    while True: 
        try: 
            description = str(input(f'Enter the {item_name} description: '))
            if not description.strip():
                raise ValueError
            else:
                break
        except ValueError:
            print('The item needs to have a description.\n')
    return description

def has_default_parameters(a_class):
    if hasattr(a_class, '__init__'):
        sig = signature(a_class.__init__)
        if any(param.default != Parameter.empty for param in sig.parameters.values()):
            return True
    return False
    
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
            item_to_add = enter_item_name()
            price = enter_item_price(item_to_add)
            quantity = enter_item_quantity(item_to_add)
            description = enter_item_description(item_to_add)
            item_to_purchase = ItemToPurchase(item_to_add, price, quantity, description)
            shopper.add_item(item_to_purchase)
        elif choice == 'r':
            print('\nCart Items:')
            for item in range(len(shopper.cart_items)):
                print(f'{shopper.cart_items[item].item_name}')
            item_to_remove = input('\nWhat item do you want to remove? ')
            shopper.remove_item(item_to_remove)
        elif choice == 'c':
            print('\nCart Items:')
            for item in range(len(shopper.cart_items)):
                print(f'{shopper.cart_items[item].item_name}')
            item_to_modify = str(input('\nWhat item would you like to modify? '))
            for item in range(len(shopper.cart_items)):
                if item_to_modify == shopper.cart_items[item].item_name:
                    if not has_default_parameters(shopper.cart_items[item]):
                        new_item_name = enter_item_name('modify')
                        new_price = enter_item_price(new_item_name)
                        new_quantity = enter_item_quantity(new_item_name)
                        new_description = enter_item_description(new_item_name)
                        new_item = ItemToPurchase(new_item_name, new_price, new_quantity, new_description)
                        shopper.modify_item(new_item, shopper.cart_items[item])
                        break
                    print('\nItem already has price, quantity, and description')
                    break
            else:
                print('\nItem not found in cart. Nothing modified.')
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
    while True: 
        try: 
            shopper_name = str(input(f'Please enter your name: '))
            if not shopper_name.strip():
                raise ValueError
            else:
                break
        except ValueError:
            print('You need to enter a name.\n')

    shopper_date = str(input('What is the date? '))

    shopper = ShoppingCart(shopper_name, shopper_date)
    print_menu(shopper)
    
if __name__ == '__main__':
    main()