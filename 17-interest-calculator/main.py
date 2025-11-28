principal = float(input("Enter the principal amount: "))

rate = float(input("Enter the rate of interest: "))

amortization = float(input("Enter the amortization period in years: "))

time = int(input("Enter the time in years: "))

while principal < 0 or rate < 0:
    print("Please enter a positive number")
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest: "))


while amortization < 0:
    print("Please enter a positive number")
    amortization = float(input("Enter the amortization period in years: "))

while time <= 0:
    time = int(input("enter time in years"))
    if time <= 0:
        print("time can't be less than or equal to zero")
        
print(f'Principal: {principal}')
print(f'Rate: {rate}')
print(f'Amortization: {amortization}')


total = principal * pow((1 + rate / 100),time)

print(f'Total with interest at end of amortization: $ {total:.2f}')