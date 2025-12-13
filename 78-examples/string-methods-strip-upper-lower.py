# to remove space in string
animals= "  lions tigers and bears   "
animals1= "LIONS TIGERS AND BEARS"
number="1234"
print(animals.strip())  # strip on left and right
print(animals.lstrip()) # left strip
print(animals.rstrip()) # right strip


print(animals.upper())  # convert to upper
print(animals1.lower()) # convert to lower

print(animals.count("t")) # counts number of times a character/string appeared in variable given

print(animals1.endswith("BEAR"))

print(number.isnumeric())


print(" ".join(["What"+" a"+" wonderful"+" day"]))


# split 
print(("What a wonderful day").split())
