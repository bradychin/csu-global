# Using a hashtable to count individual items

# Define a set of items that we want to count
items = ['apple', 'amazon', 'google', 'meta', 'tesla', 'netflix', 'microsoft', 'google', 'apple', 'tesla', 'netflix']

# TODO: create a hashtable object to hold the items and counts
counter = dict()

# TODO: iterate over each item and increment the count for each one
for item in items:
    if (item in counter.keys()):
        counter[item] += 1
    else: 
        counter[item] = 1

# Print results
print(counter)