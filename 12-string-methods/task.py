# validate user input exercise

# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

user_name = input("enter a username: ")
if len(user_name) > 12:
    print("username can not be more than 12 characters")
elif not user_name.find(" ") == -1:
    print("username can not contain a space")
elif not user_name.isalpha():
    print("user name can not contain numerics")
else:
    print(f"welcome {user_name}")