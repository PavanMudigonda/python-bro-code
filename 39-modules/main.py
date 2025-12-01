#.........................main.py...............................

# module = a file containing code you wnat to incldue in your program
#.        use 'import' to include a module (built in or your own)
#         useful to break up a large program reusable separate files

import example

result = example.pi
print(result)

square_value = example.square(3)

print(f"square value: {square_value}")

cube_value = example.cube(3)

print(f"cube value: {cube_value}")

circumference_value = example.circumference(3)

print(f"circumference value: {circumference_value}")

area_value = example.area(4)

print(f"area value: {area_value}")