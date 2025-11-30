# Membership Operators = used to test whether a value or variable is found in sequence
#                       (string, list, tuple, set or dictionary)
#                       1. in
#.                      2. not in


email = "BroCode@gmail.com"

if '@' in email and '.' in email:
    print("valid email")
else:
    print("invalid email")