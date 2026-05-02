import numpy as np

# Input array from the user
array1 = np.array(list(map(int, input().split())))

# Searching
search_value = int(input("Value to search: "))
count_value = int(input("Value to count: "))
broadcast_value = int(input("Value to add: "))

# Find indices where value matches in array1
indices=np.where(array1==search_value)[0]
print(indices)
# Count occurrences in array1
count=(np.count_nonzero(array1==count_value))
print(count)
# Broadcasting addition
new_array=array1+broadcast_value
print(new_array)
# Sort the first array
sorted=np.sort(array1)
print(sorted)