# List Comprehensions = A concise way to create lists of python
#.                      Compact and easier to read than traditional loops
#                       [expression for value in iterable if condition ]


numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]

positive_nums = [num for num in numbers if num >= 0 ]
negative_nums = [num for num in numbers if num <= 0 ]
even_nums = [ num for num in numbers if num % 2 == 0]
odd_nums = [ num for num in numbers if ((num >= 0) and (num % 2 != 0))]
print(f"positive number: {positive_nums}")
print(f"negative number: {negative_nums}")
print(f"even number: {even_nums}")
print(f"odd number: {odd_nums}")