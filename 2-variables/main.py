# string
first_name: str = "Pavan"
last_name: str = "Mudigonda"
food: str = "pizza"
print(first_name)
email: str = "bro123@fake.com"

# int
age: int = 20
quantity: int = 3
num_of_students: int = 100

# float
pi: float = 3.14

# bool

is_student: bool = True
for_sale = False
is_online = True

print(f'Hello {first_name} {last_name}')
print(f'I like {food} !')
print(f'I am {age} years old')
print(f'I am buying {quantity} pizzas')
print(f'There are {num_of_students} students in the class')
print(f'The value of pi is {pi}')

print(f'Is the person a student? {is_student}')

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