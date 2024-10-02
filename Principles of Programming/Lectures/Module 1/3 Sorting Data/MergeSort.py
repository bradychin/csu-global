# Merge sort

def mergeSort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]
        
        # TODO: recursively break down array
        mergeSort(leftarr)
        mergeSort(rightarr)

        # TODO: perform merging
        i=0 # left arr
        j=0 # right arr
        k=0 # merged arr

        #TODO: while both arrays have content
        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                dataset[k] = leftarr[i]
                i+=1
            else:
                dataset[k] = rightarr[j]
                j+=1
            k+=1

        # TODO: if left array still has values, add them
        while i < len(leftarr):
            dataset[k] = leftarr[i]
            i+=1
            k+=1

        # TODO: if right array still has values, add them
        while j < len(rightarr):
            dataset[k] = rightarr[j]
            j+=1
            k+=1

items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 52]
print(items)
mergeSort(items)
print(items)