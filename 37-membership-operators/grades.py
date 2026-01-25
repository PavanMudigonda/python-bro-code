# Membership Operators = used to test whether a value or variable is found in sequence
#                       (string, list, tuple, set or dictionary)
#                       1. in
#.                      2. not in


grades = { "Sandy" : "A",
          "Mandy" : "B",
          "Teddy" : "C",
          "Maddy" : "D",
          "Randy" : "E",
          "Patty" : "F" }

student = input("Enter the name of the student to loop of grade: ")
    
if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f'{student} not found')