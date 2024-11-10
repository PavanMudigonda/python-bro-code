foods: list = []
prices: list = []
total = 0

while True:
    food = input("Enter a food item: ")
    if food == "q" or food == "quit" or food == "Q" or food == "quit":
        break
    price = float(input("Enter the price: $ "))
    foods.append(food)
    prices.append(price)

print("====Pavan's Food Emporium====")
for i in range(len(foods)):
    print(f"{i + 1} {foods[i]} ${prices[i]}")
    total += prices[i]

print(f"Total: ${total}")