unit = input("Enter the unit of temperature (F/C): ")

# In US temperate is measured in Fahrenheit F
# In Canada temperature is measured in Centigrade/Celsius C

temp = float(input("Enter the temperature: "))

if unit == "F":
    temp = (( temp - 32 ) * 5.0/9.0)
    print(f'The temperature in Fahrenheit is, {temp} C °')
elif unit == "C":
    temp = ( ( temp * 9.0/5.0 ) + 32 )    
    print(f'The temperature in Celsius is, {temp} F ')