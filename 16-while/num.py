
num = input("Enter a number between 1 and 10: ")

while int(num) < 1 or int(num) > 10:
    print("You must enter a number between 1 and 10")
    num = input("Enter a number between 1 and 10: ")

print("You entered", num)