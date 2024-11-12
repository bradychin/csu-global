# Ordered search list

items = [2, 5, 10, 12, 26, 64, 69, 89, 102]

def binarysearch(item, itemlist):
    # Get the list size
    listsize = len(itemlist) - 1
    # Start at the two ends of the list
    lowerIdx = 0
    upperIdx = listsize

    while lowerIdx <= upperIdx:
        # TODO: calculate midpoint
        midpoint = (lowerIdx + upperIdx) // 2

        # TODO: if item is found, return index
        if itemlist[midpoint] == item:
            return midpoint
        # TODO: otherwise get next midpoint
        else: 
            if item > itemlist[midpoint]:
                lowerIdx = midpoint + 1
            else: 
                upperIdx = midpoint - 1
    
    if lowerIdx > upperIdx:
        return None
    
print(binarysearch(10, items))
print(binarysearch(89, items))
print(binarysearch(1923, items))