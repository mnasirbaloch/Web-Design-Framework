# Declare and initialize a string variable
my_string = "Hello, World!"

# Convert string to all uppercase letters
uppercase_string = my_string.upper()
print("Uppercase string:", uppercase_string)

# Convert string to all lowercase letters
lowercase_string = my_string.lower()
print("Lowercase string:", lowercase_string)

# Get the length of the string
string_length = len(my_string)
print("String length:", string_length)

# Replace a specific character in the string
new_string = my_string.replace("o", "a")
print("New string:", new_string)

# Split the string into a list of substrings
split_string = my_string.split(",")
print("Split string:", split_string)

# Check if the string starts with a specific substring
starts_with_hello = my_string.startswith("Hello")
print("Starts with 'Hello':", starts_with_hello)

# Check if the string ends with a specific substring
ends_with_exclamation = my_string.endswith("!")
print("Ends with '!':", ends_with_exclamation)

# Find the index of a specific character in the string
index_of_o = my_string.index("o")
print("Index of 'o':", index_of_o)

# Check if all characters in the string are alphanumeric
is_alphanumeric = my_string.isalnum()
print("Is alphanumeric:", is_alphanumeric)

