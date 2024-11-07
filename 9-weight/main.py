weight = float(input("Enter your weight: "))

unit = input("(L)bs or (K)g: ")

if unit.upper() == "L":
    weight_kg = weight * 0.45
    print(f"You are {weight_kg} kilos")
elif unit.upper() == "K":
    weight_lbs = weight / 0.45
    print(f"You are {weight_lbs} pounds")
else:
    print(f'Invalid unit: {unit}')

