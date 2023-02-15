# Declare a variable
x = 10

# If statement
if x > 5:
    print("x is greater than 5")

# If-else statement
if x < 5:
    print("x is less than 5")
else:
    print("x is greater than or equal to 5")

# If-elif-else statement
if x < 5:
    print("x is less than 5")
elif x > 10:
    print("x is greater than 10")
else:
    print("x is between 5 and 10")

# Nested if statements
if x > 5:
    print("x is greater than 5")
    if x < 15:
        print("x is less than 15")

# Ternary operator
y = "even" if x % 2 == 0 else "odd"
print("x is", y)

