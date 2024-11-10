
fruits = ["apple", "banana", "cherry", "dragon fruit", "elderberry", "fig", "grape", "honeydew"]

# Print the list
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))

fruits.append("kiwi")
fruits[0] = "apricot"
fruits.insert(1, "blueberry")
fruits.remove("banana")
fruits = fruits.sort()
for fruit in fruits:
    print(fruit)


# Print the list in reverse order