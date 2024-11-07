import math

pi = math.pi

print(pi)

print(math.sqrt(16))

print(math.pow(2, 3))

print(math.floor(2.9))

print(math.ceil(2.1))

print(math.e)

# circle

radius = float(input("Enter the radius of the circle: "))

circumference = 2 * math.pi * radius

print(f"The circumference of the circle is {circumference}")

area = math.pi * math.pow(radius, 2)

print(f"The area of the circle is {area}")

# triangle

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))

c = a**2 + b**2
print(f"The length of side c is {math.sqrt(c)}")

