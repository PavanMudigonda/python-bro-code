fruits =     ["apple", "banana", "cherry"]
vegetables = ["carrot", "lettuce", "onion"]
meats =      ["beef", "chicken", "pork"]

# Create a 2D list

groceries = [fruits, vegetables, meats]

# equal to below
# food = [
#     ["apple", "banana", "cherry"],
#     ["carrot", "lettuce", "onion"],
#     ["beef", "chicken", "pork"]
# ]

# Access the 2D list
print(groceries[0][1]) # banana
print(groceries[1][0]) # carrot
print(groceries[2][2]) # pork
print(groceries[1][1]) # lettuce

# Modify the 2D list

groceries[0][1] = "blueberry"

print(groceries[0]) # ['apple', 'blueberry', 'cherry']

for collection in groceries:
    for food in collection:
        print(food,end="")
        print()
    print()