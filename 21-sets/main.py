
# collection = single "variable" used to store multiple values
# List  = [] ordered and changeable. Duplicate OK
# Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. duplicated OK. FASTER


fruits = {"apple", "banana", "cherry", "dragon fruit", "elderberry", "fig", "grape", "honeydew"}

# print(dir(fruits))

for fruit in fruits:
    print(fruit)

fruits.add("kiwi")

print(fruits)

fruits.remove("banana")

print(fruits)

