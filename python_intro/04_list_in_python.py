# Create a list
my_list = [1, 2, 3, 4, 5]

# Access an element by index
print("First element:", my_list[0])

# Change the value of an element
my_list[2] = 6
print("Modified list:", my_list)

# Append an element to the end of the list
my_list.append(7)
print("Appended list:", my_list)

# Insert an element at a specific index
my_list.insert(3, 8)
print("Inserted list:", my_list)

# Remove an element by value
my_list.remove(4)
print("List with element removed:", my_list)

# Remove an element by index
del my_list[0]
print("List with element deleted:", my_list)

# Get the length of the list
list_length = len(my_list)
print("List length:", list_length)

# Sort the list in ascending order
my_list.sort()
print("Sorted list:", my_list)

# Reverse the order of the list
my_list.reverse()
print("Reversed list:", my_list)

# Get the index of the first occurrence of a value
index_of_3 = my_list.index(3)
print("Index of 3:", index_of_3)

# Count the number of occurrences of a value
count_of_2 = my_list.count(2)
print("Count of 2:", count_of_2)

