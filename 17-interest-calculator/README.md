# Chapter 17: Compound Interest Calculator

## 📚 What You'll Learn
Calculate compound interest using mathematical formulas in Python - a practical application of math and programming!

## 🎯 Learning Objectives
- Understand compound interest formula
- Use exponentiation operator (**)
- Format financial data for display
- Build a practical calculator program
- Apply math concepts in programming
- Validate user input for financial calculations

## 📖 Concept Explanation

### What is Compound Interest?
Compound interest is interest calculated on the initial principal AND on the accumulated interest from previous periods. It's the concept of "interest on interest."

### The Formula
```
A = P(1 + r/100)^t

Where:
A = Final amount
P = Principal (initial amount)
r = Annual interest rate (as percentage)
t = Time (in years)
```

### Why It Matters
- **Savings**: Understand how your money grows
- **Loans**: Calculate total amount you'll pay
- **Investments**: Plan for future financial goals
- **Real-world skill**: Essential for personal finance

### Mathematical Operations in Python
```python
# Exponentiation
result = base ** exponent

# Example
2 ** 3  # 2 × 2 × 2 = 8
```

## 💡 Examples

### Example 1: Basic Compound Interest
```python
principal = 1000
rate = 5
time = 3

# A = P(1 + r/100)^t
amount = principal * (1 + rate/100) ** time

print(f"Initial: ${principal}")
print(f"Rate: {rate}%")
print(f"Time: {time} years")
print(f"Final Amount: ${amount:.2f}")
print(f"Interest Earned: ${amount - principal:.2f}")
```

Output:
```
Initial: $1000
Rate: 5%
Time: 3 years
Final Amount: $1157.63
Interest Earned: $157.63
```

### Example 2: Interactive Calculator
```python
print("=== Compound Interest Calculator ===\n")

principal = float(input("Enter principal amount: $"))
rate = float(input("Enter annual interest rate (%): "))
time = float(input("Enter time (years): "))

# Calculate
amount = principal * (1 + rate/100) ** time
interest = amount - principal

# Display results
print(f"\n--- Results ---")
print(f"Principal: ${principal:,.2f}")
print(f"Interest Rate: {rate}%")
print(f"Time Period: {time} years")
print(f"Final Amount: ${amount:,.2f}")
print(f"Interest Earned: ${interest:,.2f}")
```

### Example 3: Multiple Scenarios Comparison
```python
principal = 5000
rate = 7

print(f"Principal: ${principal}")
print(f"Annual Rate: {rate}%\n")

for years in [1, 5, 10, 20, 30]:
    amount = principal * (1 + rate/100) ** years
    interest = amount - principal
    print(f"{years} years: ${amount:,.2f} (Earned: ${interest:,.2f})")
```

Output:
```
Principal: $5000
Annual Rate: 7%

1 years: $5,350.00 (Earned: $350.00)
5 years: $7,012.76 (Earned: $2,012.76)
10 years: $9,835.76 (Earned: $4,835.76)
20 years: $19,348.42 (Earned: $14,348.42)
30 years: $38,061.26 (Earned: $33,061.26)
```

### Example 4: Different Interest Rates
```python
principal = 10000
time = 10

print(f"Principal: ${principal}")
print(f"Time: {time} years\n")

for rate in [3, 5, 7, 10]:
    amount = principal * (1 + rate/100) ** time
    print(f"{rate}% rate: ${amount:,.2f}")
```

### Example 5: Monthly Compounding
```python
# For monthly compounding: A = P(1 + r/100/12)^(12*t)
principal = 1000
annual_rate = 6
years = 5

# Annual compounding
amount_yearly = principal * (1 + annual_rate/100) ** years

# Monthly compounding
amount_monthly = principal * (1 + annual_rate/100/12) ** (12 * years)

print(f"With annual compounding: ${amount_yearly:.2f}")
print(f"With monthly compounding: ${amount_monthly:.2f}")
print(f"Difference: ${amount_monthly - amount_yearly:.2f}")
```

## 🔍 Common Mistakes

### Mistake 1: Forgetting to Divide Rate by 100
```python
# Wrong
rate = 5
amount = 1000 * (1 + rate) ** 3  # Treats 5 as 500%!

# Correct
rate = 5
amount = 1000 * (1 + rate/100) ** 3  # Treats 5 as 5%
```

### Mistake 2: Using Wrong Operator for Exponentiation
```python
# Wrong
amount = 1000 * (1.05) ^ 3  # ^ is XOR, not exponent!

# Correct
amount = 1000 * (1.05) ** 3  # ** is exponentiation
```

### Mistake 3: Not Formatting Financial Output
```python
# Poor output
print(f"Amount: ${1234.5678}")  # $1234.5678

# Better output
print(f"Amount: ${1234.5678:.2f}")  # $1234.57
print(f"Amount: ${1234.5678:,.2f}")  # $1,234.57
```

### Mistake 4: Integer Division Issues
```python
# Potential issue
rate = 5
partial = 1 + rate/100  # Good: results in 1.05

# But watch out for this:
months = 12
monthly_rate = rate / 100 / months  # Make sure rate is float
```

## ✍️ Practice Exercises

### Easy
1. Calculate interest on $500 at 3% for 2 years
2. Find the final amount for $2000 at 4% for 5 years
3. Calculate interest earned on $1500 at 6% for 1 year

### Medium
4. Create a calculator that asks for all inputs
5. Show year-by-year growth for 5 years
6. Calculate how long to double money at different rates
7. Compare simple vs compound interest

### Hard
8. Build a retirement savings calculator
9. Create a loan payoff calculator
10. Calculate monthly compounding for savings account

## 🎮 Real-World Applications

### Application 1: Savings Goal Calculator
```python
print("=== Savings Goal Calculator ===\n")

goal = float(input("Savings goal: $"))
initial = float(input("Starting amount: $"))
rate = float(input("Annual interest rate (%): "))

# Calculate years needed
years = 0
current = initial

while current < goal:
    years += 1
    current = initial * (1 + rate/100) ** years

print(f"\nYou'll reach ${goal:,.2f} in {years} years!")
print(f"Final amount: ${current:,.2f}")
```

### Application 2: Investment Comparison
```python
print("=== Investment Comparison Tool ===\n")

investment = float(input("Investment amount: $"))
time = int(input("Investment period (years): "))

print("\nComparing different interest rates:\n")

rates = [4, 5, 6, 7, 8]

for rate in rates:
    amount = investment * (1 + rate/100) ** time
    interest = amount - investment
    
    print(f"{rate}%: Final = ${amount:,.2f}, Earned = ${interest:,.2f}")
```

### Application 3: Retirement Planner
```python
print("=== Retirement Planner ===\n")

current_age = int(input("Your current age: "))
retirement_age = int(input("Retirement age: "))
current_savings = float(input("Current savings: $"))
annual_contribution = float(input("Annual contribution: $"))
rate = float(input("Expected annual return (%): "))

years = retirement_age - current_age
total = current_savings

for year in range(1, years + 1):
    # Add annual contribution
    total += annual_contribution
    # Apply interest
    total = total * (1 + rate/100)

print(f"\nAt age {retirement_age}:")
print(f"Total savings: ${total:,.2f}")
print(f"Total contributed: ${current_savings + (annual_contribution * years):,.2f}")
print(f"Total interest: ${total - current_savings - (annual_contribution * years):,.2f}")
```

## 🚀 Challenge Projects

### Challenge 1: Full-Featured Calculator
Create a calculator with:
- Choice of annual/monthly/daily compounding
- Option to add regular contributions
- Graphical display of growth (text-based chart)
- Inflation adjustment option

### Challenge 2: Loan Calculator
Build a program that:
- Calculates total loan payment
- Shows monthly payment amount
- Displays amortization schedule
- Compares different loan terms

### Challenge 3: Investment Dashboard
Create a program with:
- Multiple investment accounts
- Different rates for each
- Total portfolio value
- Best/worst performing investments

### Challenge 4: Break-Even Calculator
Calculate:
- Time to double your money
- Rate needed to reach a goal in X years
- Principal needed to earn X amount

### Challenge 5: Financial Scenario Planner
Build a tool that:
- Compares multiple scenarios side-by-side
- Saves results to a file
- Shows best-case and worst-case outcomes
- Adjusts for taxes and fees

## 📊 Format Specifiers Reference

```python
value = 1234.56789

# Two decimal places
print(f"{value:.2f}")  # 1234.57

# With comma separator
print(f"{value:,.2f}")  # 1,234.57

# Fixed width
print(f"{value:10.2f}")  #    1234.57

# Percentage
print(f"{0.15:.1%}")  # 15.0%
```

## 🧮 Formula Variations

### Simple Interest (for comparison)
```python
# I = P × r × t / 100
simple_interest = principal * rate * time / 100
```

### Compound Interest (different frequencies)
```python
# Annual: A = P(1 + r/100)^t
# Monthly: A = P(1 + r/100/12)^(12t)
# Daily: A = P(1 + r/100/365)^(365t)
# Continuous: A = P × e^(rt/100)
```

## 💪 Try It Yourself

Modify `main.py` to:
1. Add input validation (positive numbers only)
2. Show growth year by year
3. Compare different rates side-by-side
4. Add option for monthly compounding
5. Calculate how long to reach a specific goal

## 🔗 Next Chapter
Continue to [Chapter 18: For Loops](../18-for/) to learn about iteration and the for loop!
