# ============================================
# CHAPTER 38: MATCH-CASE STATEMENTS
# ============================================
# Match-Case Statements (Python 3.10+) = An alternative to using many 'elif' statements
#                                        Execute code if a value matches a 'case'
#                                        Similar to 'switch' statements in other languages
#
# Benefits:
# - Cleaner syntax than multiple elif statements
# - More readable for complex conditionals
# - Pattern matching capabilities
# - Can use | (OR operator) to combine cases
# - _ (underscore) acts as default case (matches anything)
#
# Syntax:
# match variable:
#     case value1:
#         # code
#     case value2:
#         # code
#     case _:
#         # default code

# =============================================
# OLD WAY: MULTIPLE IF-ELIF STATEMENTS (Verbose)
# =============================================
# This works but becomes hard to read with many conditions
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

# =============================================
# BETTER WAY: MATCH-CASE WITH NUMBERS
# =============================================
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
#         case _:  # Default case (like 'else')
#             return "Not a valid day"
# print(day_of_week(1))  

# =============================================
# ADVANCED: MATCH-CASE WITH PATTERN MATCHING
# =============================================
# Using | (OR operator) to group multiple cases
# This is much cleaner than multiple elif statements!
def day_of_week(day):
    """
    Check if a day is a weekend or weekday.
    
    Parameters:
        day (str): Name of the day
    
    Returns:
        bool: True if weekend, False if weekday
    """
    match day:
        # Weekend case - combine multiple values with |
        case "Saturday" | "Sunday":
            return True
        
        # Weekday case - all weekdays in one line
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        
        # Default case - matches anything not covered above
        case _:
            return False

# =============================================
# TEST THE FUNCTION
# =============================================
print(day_of_week("Monday"))  # Output: False (weekday)
# print(day_of_week("Saturday"))  # Output: True (weekend)
# print(day_of_week("InvalidDay"))  # Output: False (default)  