# Quick sort
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 52]

def quickSort(dataset, first, last):
    if first < last:
        # calculate split point
        pivotIdx = partition(dataset, first, last)

        # Sort the two partitions
        quickSort(dataset, first, pivotIdx-1)
        quickSort(dataset, pivotIdx+1, last)

def partition(datavalues, first, last):
    # Choose the first item as the pivot value
    pivotvalue = datavalues[first]
    
    # Establish upper and lower index
    lower = first + 1 
    upper = last

    # Start searching for crossing point
    done = False
    while not done:
        # TODO: advance the lower index
        while lower <= upper and datavalues[lower] <= pivotvalue:
            lower += 1
        
        # TODO: advance the upper index
        while datavalues[upper] >= pivotvalue and upper >= lower:
            upper-=1

        # TODO: if index crosses, we found the split point
        if upper < lower:
            done = True
        else:
            temp = datavalues[lower]
            datavalues[lower] = datavalues[upper]
            datavalues[upper] = temp
        
    # when the split is found, exchange the pivot value
    temp = datavalues[first]
    datavalues[first] = datavalues[upper]
    datavalues[upper] = temp

    # return the split point index
    return upper


print(items)
quickSort(items, 0, len(items)-1)
print(items)
