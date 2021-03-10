import re

# Data to be outputted
data = ['I', 'Love', 'Computers']

# Get filename, can't be blank / invalid
# Assume valid data for now

has_error = "yes"
while has_error == "yes":
    has_error = "no"
    filename = input("Enter a Filename (leave off the extension): ")

    valid_char = "[A-Za-z0-9_]"
    for letter in filename:
        if re.match(valid_char, letter):
            continue
        elif letter ==" ":
            problem = "No spaces allowed."
        else:
            problem = ("No {}'s allowed.".format(letter))
        has_error = "yes"

    if filename == "":
        problem = "Can't be blank"
        has_error = "yes"

    if has_error == "yes":
        print("Invalid filename - {}".format(problem))
        print()
    else:
        print("You entered a valid filename")

# Add .txt suffix
filename = filename + ".txt"

# Create file to hold data
f = open(filename, "w+")

# Add new line at the end of each item
for item in data:
    f.write(item + "\n")

f.close()
