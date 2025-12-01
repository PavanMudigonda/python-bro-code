# List Comprehensions = A concise way to create lists of python
#.                      Compact and easier to read than traditional loops
#                       [expression for value in iterable if condition ]


# doubles = []

# for x in range(1,11):
#     doubles.append(x * 2)
    
# print(doubles)

# doubles = [ expression for value in iteratable if condition ]

doubles = [ x * 2 for x in range(1,11)]
triples = [ y * 3 for y in range(1,11)]
squares = [ z * 4 for z in range(1,11)]
pentas  = [ a * 5 for a in range(1,11)]
print(doubles)
print(triples)
print(squares)
print(pentas)