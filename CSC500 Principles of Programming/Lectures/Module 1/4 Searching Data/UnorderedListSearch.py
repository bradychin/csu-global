# Search for an item in an unordered list
# sometimes called a linear search

# Declare list
items = [6, 2, 5, 1, 92, 19, 4, 10]

def find_item(item, itemList):
    for i in range(0, len(items)):
        if item == itemList[i]:
            return i
    return None

print(find_item(19, items))
print(find_item(23, items))