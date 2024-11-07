temp = float(input("What is the temperature outside? "))
is_sunny = True

if temp > 20 and is_sunny:
    print("Don't forget your sunscreen!")
elif temp <= 20 and is_sunny:
    print("Wear a hat!")
elif temp > 20 and not is_sunny:
    print("Take an umbrella!")
else:
    print("Stay home!")