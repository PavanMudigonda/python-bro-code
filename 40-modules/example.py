# Modules = a file containing code you want to include in your program
#           use 'import' to include a module (built-in or your own)
#.          useful to break up a large program reusable separate files

# import math as m

import math

# print(math.pi)

# print(math.pow(2,2))

# print(math.sqrt(9))

# a, b, c, d, e =1, 2, 3, 4, 5

# print(math.e ** a)


pi = math.pi

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def circumference(radius):
    return 2 * math.pi * radius

def area(radius):
    return math.pi * radius ** 2