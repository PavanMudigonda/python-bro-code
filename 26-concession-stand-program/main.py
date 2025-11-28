# concession stand program

# use dictionary  {key:value}

menu = {"pizza": "3.0",
        "nachos": "4.5",
        "popcorn": "6.0",
        "fries": "2.50",
        "chips": "1.00",
        "pretzel": "3.00",
        "soda": "3.00",
        "lemonade": "4.25",                                
        }

cart = []
total = 0
print("----------MENU-------------")
for key,value in menu.items():
    print(f'{key:10}: ${float(value):.2f}')
print("---------------------------")

while True:
    food = input("Select an item to buy (q to quit):  ".lower())
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print(cart)

for food in cart:
    total += float(menu.get(food))
    print(food, end=" ")

print()
print(f'total: {total}')