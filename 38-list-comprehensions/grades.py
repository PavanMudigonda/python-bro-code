# List Comprehensions = A concise way to create lists of python
#.                      Compact and easier to read than traditional loops
#                       [expression for value in iterable if condition ]


grades = ["80","95","67","58","77","63"]

# passing_grades = [ expression for value in iterable if condition]

passing_grades = [ grade for grade in grades if int(grade) >= 60 ]

print(passing_grades)