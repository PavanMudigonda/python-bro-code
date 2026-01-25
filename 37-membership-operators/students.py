# Membership Operators = used to test whether a value or variable is found in sequence
#                       (string, list, tuple, set or dictionary)
#                       1. in
#.                      2. not in

students = ["John", "Mary", "Bob", "Mosh", "Sarah"]

student = input("Enter the name of a student: ")

if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} is not a student")
    
    
if student not in students:
    print(f"{student} not a student")
else:
    print(f"{student} is a student")