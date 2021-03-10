# Get data from user and store it in a list, then
# display the most recent three entries nicely

# Setup empty list
all_calculations = []

# Get five items of Data
for item in range(0, 5):
    get_item = input("Enter an item: ")
    all_calculations.append(get_item)

# Show that everything made it to the list..
print()
print("*** The full list ***")
print(all_calculations)

print()

print("*** Most recent 3 ***")
# Print items starting at the END of the list
for item in range(0, 3):
    print(all_calculations[len(all_calculations) - item - 1])
