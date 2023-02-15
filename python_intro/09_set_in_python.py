# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding elements to a set
my_set.add(6)
my_set.update([7, 8, 9])

# Removing elements from a set
my_set.discard(3)
my_set.remove(4)

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(set_a.union(set_b))      # Output: {1, 2, 3, 4, 5, 6}
print(set_a.intersection(set_b))  # Output: {3, 4}
print(set_a.difference(set_b))    # Output: {1, 2}
print(set_b.difference(set_a))    # Output: {5, 6}

# Looping through a set
for element in my_set:
    print(element)

