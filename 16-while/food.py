# execute some code WHILE some condition remains true
food = input("What is your favorite food? ")

while food != "q":
    print("You like", food, "?")
    food = input("What is your favorite food? ")

print("you are quitting the while loop!")