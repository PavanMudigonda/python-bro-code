principal = float(input("Enter the principal amount: "))

rate = float(input("Enter the rate of interest: "))

amortization = float(input("Enter the amortization period in years: "))

while principal < 0 or rate < 0:
    print("Please enter a positive number")
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest: "))


while amortization < 0:
    print("Please enter a positive number")
    amortization = float(input("Enter the amortization period in years: "))
    
print(f'Principal: {principal}')
print(f'Rate: {rate}')
print(f'Amortization: {amortization}')


total = principal * (1 + rate * amortization)
print(f'Total with interest at end of amortization: $ {total:.2f}')