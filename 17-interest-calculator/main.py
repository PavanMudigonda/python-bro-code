# ============================================
# Chapter 17: Compound Interest Calculator
# ============================================
# This program calculates compound interest using the formula:
# A = P(1 + r/100)^t
# Where:
#   A = Final amount
#   P = Principal (initial amount)
#   r = Annual interest rate (as percentage)
#   t = Time (in years)

# ============================================
# Step 1: Get input values from user
# ============================================
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
amortization = float(input("Enter the amortization period in years: "))
time = int(input("Enter the time in years: "))

# ============================================
# Step 2: Validate principal and rate (must be positive)
# ============================================
while principal < 0 or rate < 0:
    print("Please enter a positive number")
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest: "))

# ============================================
# Step 3: Validate amortization period (must be positive)
# ============================================
while amortization < 0:
    print("Please enter a positive number")
    amortization = float(input("Enter the amortization period in years: "))

# ============================================
# Step 4: Validate time (must be greater than 0)
# ============================================
while time <= 0:
    time = int(input("Enter time in years: "))
    if time <= 0:
        print("Time can't be less than or equal to zero")

# ============================================
# Step 5: Display input summary
# ============================================        
print(f'Principal: ${principal:.2f}')
print(f'Rate: {rate}%')
print(f'Time: {time} years')
print(f'Amortization Period: {amortization} years')

# ============================================
# Step 6: Calculate compound interest
# ============================================
# Formula: A = P(1 + r/100)^t
# pow(base, exponent) raises base to the power of exponent
total = principal * pow((1 + rate / 100), time)

# ============================================
# Step 7: Display the result
# ============================================
print(f'\nTotal with interest after {time} years: ${total:.2f}')
print(f'Interest earned: ${total - principal:.2f}')