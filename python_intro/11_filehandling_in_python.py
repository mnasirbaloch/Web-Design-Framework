# Writing to a file
with open("intro.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("This is an intro file.\n")
    file.write("We can write multiple lines.\n")

# Reading from a file
with open("intro.txt", "r") as file:
    contents = file.read()
    print(contents)

# Reading line by line
with open("intro.txt", "r") as file:
    line = file.readline()
    while line:
        print(line.strip())  # strip() removes the newline character
        line = file.readline()

# Appending to a file
with open("intro.txt", "a") as file:
    file.write("This line is appended to the end.\n")

# Reading and writing binary data
with open("img.png", "rb") as binary_file:
    binary_data = binary_file.read()

with open("copy.png", "wb") as copy_file:
    copy_file.write(binary_data)

