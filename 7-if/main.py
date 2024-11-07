age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign up.")
elif age <= 0:
    print("You are not born yet.")
elif age == 17:
    print("You are 17 years old, you can sign up next year.")
elif age >= 18:
    print("You are now signed up")
else:
    print("You are a minor therefore not eligible to sign up.")

# Output: