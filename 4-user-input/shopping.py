item = input("what item would you like to buy? ")
price = float(input("what is the price of the item? "))
quantity = int(input("how many would you like to buy? "))
total = price * quantity
print(f"you have bought {quantity} x {item}/s")
print(f'The total cost for buying {item}, ${total:.1f}.')