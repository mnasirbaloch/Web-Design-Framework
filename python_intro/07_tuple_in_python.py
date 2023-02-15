# Creating a tuple
my_tuple = (1, 2, 3, "four", 5.0)

# Accessing elements of a tuple
print(my_tuple[0])  # Output: 1
print(my_tuple[3])  # Output: "four"

# Slicing a tuple
print(my_tuple[1:3])  # Output: (2, 3)

# Looping through a tuple
for element in my_tuple:
    print(element)

# Unpacking a tuple
a, b, c, d, e = my_tuple
print(a)  # Output: 1
print(b)  # Output: 2

# Tuple comparison
tuple_1 = (1, 2, 3)
tuple_2 = (2, 3, 4)
tuple_3 = (1, 2, 3)
print(tuple_1 == tuple_2)  # Output: False
print(tuple_1 == tuple_3)  # Output: True

# Immutable nature of tuples
my_tuple[0] = 10  # Raises a TypeError: 'tuple' object does not support item assignment

