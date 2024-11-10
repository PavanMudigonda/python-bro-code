fruits =     ["apple", "banana", "cherry"]
vegetables = ["carrot", "lettuce", "onion"]
meats =      ["beef", "chicken", "pork"]

# Create a 2D list

food = [fruits, vegetables, meats]

# Access the 2D list
print(food[0][1]) # banana
print(food[1][0]) # carrot
print(food[2][2]) # pork
print(food[1][1]) # lettuce

# Modify the 2D list

food[0][1] = "blueberry"

print(food[0]) # ['apple', 'blueberry', 'cherry']