item = input("what would you like to buy? ")
price = float(input("what is the price of the item? "))
quantity = int(input("how many would you like to buy? "))
total = price * quantity
print(f'The total cost is ${total:.2f}.')