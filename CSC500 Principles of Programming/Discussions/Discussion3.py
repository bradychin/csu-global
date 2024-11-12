bill = [
    {'food': 'Hamburger', 'price': 5},
    {'food': 'Fries', 'price': 2},
    {'food': 'Drink', 'price': 1}
]
total_price = 0

for item in bill:
    total_price += item['price']
    print(f'{item['food']}: ${item['price']}')

print(f'Total: ${total_price}')
