# weight = float(input("Enter your weight: "))

# unit = input("(L)bs or (K)g: ")

# if unit.upper() == "L":
#     weight_kg = weight * 0.45
#     print(f"You are {weight_kg} kilos")
# elif unit.upper() == "K":
#     weight_lbs = weight / 0.45
#     print(f"You are {weight_lbs} pounds")
# else:
#     print(f'Invalid unit: {unit}')


weight = float(input("Enter your weight : "))

unit = str(input("Enter L for Lbs and K for Kgs: "))

# 1 kg = 1000 grams
# 1 lb = 453.6 grams

kg_to_lb_factor = 1000 / 453.6

print(f"kg_to_lb_factor, {kg_to_lb_factor}")


if unit.upper() == "L":
    weight = float(weight / kg_to_lb_factor)
    unit = "Lbs"
    print(f"your weight in Kgs {weight}")
elif unit.upper() == "K":
    weight = float(weight * kg_to_lb_factor)
    unit = "Kgs"
    print(f"your weight in Lbs {weight}")    
else:
    print("you have entered invalid unit for weight")