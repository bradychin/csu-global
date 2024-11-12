# Determine if list is sorted

items1 = [2, 4, 5, 7, 8, 9, 10]
items2 = [2, 5, 1, 64 ,7, 3, 23, 4]

def is_sorted(itemlist):
    # TODO: Use the brute force method
    # for i in range(0, len(itemlist)-1):
    #     if (itemlist[i] > itemlist[i+1]):
    #         return False
    # return True
    return all(itemlist[i] <= itemlist[i+1] for i in range(len(itemlist)-1))

print(is_sorted(items1))
print(is_sorted(items2))