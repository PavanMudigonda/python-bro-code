unit = input("Enter the unit of temperature (F/C): ")
temp = float(input("Enter the temperature: "))
if unit == "F":
    temp = round(((temp - 32) * 5) / 9)
    print(f'The temperature in Fahrenheit is, {temp} {unit}')
elif unit == "C":
    temp = round(((temp * 9 ) / 5) + 32)
    print(f'The temperature in Celsius is, {temp} {unit}')