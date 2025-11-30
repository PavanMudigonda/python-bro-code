# default arguments = A default value for certain parameters
#                     default is used when that argument is omitted
#                     make your functions more flexible, reduce # of arguments
#                     1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary


# default arguments must be placed after positional arguments
# example: def func(pos1, pos2, default1=5, default2="hello")

def net_price(price, tax_rate=0.08, discount=0):
    """Calculate the net price of an item after tax and discount"""
    final_price = price + (price * tax_rate) - discount
    return final_price

# print(net_price(500))


print(net_price(500,0.1))