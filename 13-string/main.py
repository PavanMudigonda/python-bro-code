name = input("Enter your name: ")

print("Hello, " + name + "!")

len = len(name)

print("Your name has " + str(len) + " characters.")

result = name.upper()

print("Your name in uppercase: " + result)

result = name.lower()

print("Your name in lowercase: " + result)

result = name.title()

print("Your name in titlecase: " + result)


find_p = name.find("P")

print("The position of the letter 'P': " + str(find_p))

#result = name.isdigit()

result = name.isnumeric()


print("Is your name a number? " + str(result))