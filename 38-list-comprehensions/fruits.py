# List Comprehensions = A concise way to create lists of python
#.                      Compact and easier to read than traditional loops
#                       [expression for value in iterable if condition ]


fruits = ["apple","orange","banana","coconut"]

fruit_chars = [ fruit[0] for fruit in fruits ]

print(fruit_chars)

