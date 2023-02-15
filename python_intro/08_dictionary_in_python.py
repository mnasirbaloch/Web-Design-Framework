# Creating a dictionary
my_dict = {"apple": 1, "banana": 2, "cherry": 3}

# Accessing values in a dictionary
print(my_dict["apple"])  # Output: 1
print(my_dict.get("banana"))  # Output: 2

# Adding a new key-value pair to a dictionary
my_dict["orange"] = 4

# Looping through a dictionary
for key in my_dict:
    print(key, my_dict[key])

# Removing a key-value pair from a dictionary
del my_dict["cherry"]

# Dictionary comprehension
my_squares = {x: x**2 for x in range(5)}
print(my_squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

