class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.fraction = 1.0

class Knapsack:
    def __init__(self, max_weight, items):
        self.max_weight = max_weight
        self.items = items

def value_to_weight_ratio(item):
    return item.value / item.weight

def knapsack_fractional(knapsack, item_list):
    # Sort items by value
    item_list.sort(key = value_to_weight_ratio, reverse=True)

    # Add items to knapsack
    remaining_weight = knapsack.max_weight
    for item in item_list:
        if item.weight < remaining_weight:
            knapsack.items.append(item)
            remaining_weight -= item.weight
        elif item.weight >= remaining_weight:
            item.fraction = remaining_weight / item.weight
            knapsack.items.append(item)
            break

def main():
    item_1 = Item(6, 25)
    item_2 = Item(8, 42)
    item_3 = Item(12, 60)
    item_4 = Item(18, 95)
    item_list = [item_1, item_2, item_3, item_4]
    initial_knapsack_list = []

    max_weight = 38

    knapsack = Knapsack(max_weight, initial_knapsack_list)
    knapsack_fractional(knapsack,item_list)

    i = 1
    sum_weight = 0
    sum_value = 0

    for item in knapsack.items:
        sum_weight += item.weight * item.fraction
        sum_value += item.value * item.fraction
        print(f'{i}: Weight {item.weight*item.fraction}, Value ${item.value*item.fraction}')
        i += 1
    print(f'Total Weight: {sum_weight}')
    print(f'Total Value: {sum_value}')

if __name__ == '__main__':
    main()











