# Create an empty list called my_list
my_list = []

# Append the following elements to my_list: 9, 10, 19, 20
my_list.append(9)
my_list.append(10)
my_list.append(19)
my_list.append(20)

# Insert the value 15 at the second position in the list
my_list.insert(1, 15)

# Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])

# Remove the last element from my_list
my_list.pop()

# Sort my_list in ascending order
my_list.sort()

# Find and print the index of the value 19 in my_list
index_19 = my_list.index(19)
print("Index of value 19:", index_19)

# Print the modified list
print("Modified my_list:", my_list)
