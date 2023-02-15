# Division by zero example
numerator = 10
denominator = 0

try:
    result = numerator / denominator
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
else:
    print("Result is:", result)

# File not found example
try:
    with open("nonexistent_file.txt") as file:
        contents = file.read()
except FileNotFoundError:
    print("Error: File not found")
else:
    print(contents)

# Catching multiple exceptions
try:
    result = int("not_an_integer")
except (ValueError, TypeError):
    print("Error: Cannot convert to integer")

# Finally block
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
finally:
    print("This block always executes, regardless of whether an exception was raised")

