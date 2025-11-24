# execute some code WHILE some condition remains true
age = int(input("Enter your age: "))

while age < 18:
    print("You are a minor")
    age = int(input("Enter your age: "))