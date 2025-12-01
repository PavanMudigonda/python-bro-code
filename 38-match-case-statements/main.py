# Match-Case Statements (switch): An alternate to using many 'elif' statements
#                                Execute some code if a value matches a 'case'
#.                             Benefits: cleaner and syntax is more readable


# def day_of_week(day):
#     if day == 1:
#         return "Its a monday"
#     elif day == 2:
#         return "Its a tuesday"
#     elif day == 3:
#         return "Its a wednesday"
#     elif day == 4:
#         return "Its a thursday"
#     elif day == 5:
#         return "its a friday"
#     elif day == 6:
#         return "its a saturday"
#     elif day == 7:
#         return "its a sunday"
#     else:
#         return "Not a valid day"
    
# print(day_of_week(1))  


# def day_of_week(day):
#     match day:
#         case 1:
#             return "Its a monday"
#         case 2:
#             return "Its a tuesday"
#         case 3:
#             return "Its a wednesday"
#         case 4:
#             return "Its a thursday"
#         case 5:
#             return "its a friday"
#         case 6:
#             return "its a saturday"
#         case 7:
#             return "its a sunday"
#         case 8:
#             return "Not a valid day"
    
# print(day_of_week(1))  


def day_of_week(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False
    
print(day_of_week("Monday"))  