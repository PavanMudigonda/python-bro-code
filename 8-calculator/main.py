operator = input("Enter operator: (+ or - or * or /): ")

number1 = float(input("Enter first number: "))

number2 = float(input("Enter second number: "))

if operator == "+":
    print(number1, "+", number2, "=", number1 + number2)
elif operator == "-":
    print(number1, "-", number2, "=", number1 - number2)
elif operator == "*":
    print(number1, "*", number2, "=", number1 * number2)
elif operator == "/":
    print(number1, "/", number2, "=", number1 / number2)
else:
    print(f'Invalid operator: {operator}')