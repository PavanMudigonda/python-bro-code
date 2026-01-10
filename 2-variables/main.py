# ============================================
# Chapter 2: Variables and Data Types
# ============================================
# Variables are containers for storing data values
# Python has several built-in data types: str, int, float, bool

# ============================================
# STRING VARIABLES (str)
# ============================================
# Strings hold text data and must be enclosed in quotes
first_name: str = "Pavan"  # str indicates this variable holds a string
last_name: str = "Mudigonda"
food: str = "pizza"
print(first_name)
email: str = "bro123@fake.com"

# ============================================
# INTEGER VARIABLES (int)
# ============================================
# Integers are whole numbers (no decimal points)
age: int = 20  # int indicates this variable holds an integer
quantity: int = 3
num_of_students: int = 100

# ============================================
# FLOAT VARIABLES (float)
# ============================================
# Floats are numbers with decimal points
pi: float = 3.14  # float indicates this variable holds a decimal number
price = 10.99  # Python can infer the type without explicit annotation
gpa = 3.2
distance = 5.5

# Printing float variables using f-strings
print(f"the value of pi is {pi}")
print(f"the price is {price}")
print(f"the GPA is {gpa}")
print(f"the distance is {distance}")

# ============================================
# BOOLEAN VARIABLES (bool)
# ============================================
# Booleans can only be True or False
is_student: bool = True  # bool indicates this variable holds a boolean value
for_sale = False
is_online = True

# ============================================
# Using Variables in F-Strings
# ============================================
# F-strings (formatted strings) allow you to embed variables inside strings
# Prefix the string with 'f' and put variables in {}
print(f'Hello {first_name} {last_name}')
print(f'I like {food} !')
print(f'I am {age} years old')
print(f'I am buying {quantity} pizzas')
print(f'There are {num_of_students} students in the class')
print(f'The value of pi is {pi}')

print(f'Is the person a student? {is_student}')

# ============================================
# Using Variables in Conditional Statements
# ============================================
# Variables can be used in if-else statements to make decisions
if is_student:
    print(f'{first_name} is a student')
else:
    print(f'{first_name} is not a student')
    
if for_sale:
    print('Item is for sale')
else:
    print('Item is not for sale')

if is_online:
    print('User is online')
else:
    print('User is offline')