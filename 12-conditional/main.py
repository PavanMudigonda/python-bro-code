num = 5
a = 6
b = 7
age = 13
temperature = 22

user_role = 'admin'

print("positive" if num > 0 else "non-positive")
result = 'EVEN' if num % 2 == 0 else 'ODD'
print(result)

max_num = a if a > b else b
print(f'maximum number: {max_num}')
min_num = a if a < b else b
print(f'minimum number: {min_num}')

access_level = 'Full Access' if user_role == 'admin' else 'non-admin'