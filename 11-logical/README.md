# Chapter 11: Logical Operators


## 📺 Video Tutorial

[![Watch on YouTube](https://img.shields.io/badge/Watch-BroCode_Python_Master_Class-red?style=for-the-badge&logo=youtube)](https://youtu.be/TYyKQBC4bwE)


## 📺 Video Tutorial

[![Watch on YouTube](https://img.shields.io/badge/Watch-BroCode_Python_Master_Class-red?style=for-the-badge&logo=youtube)](https://youtu.be/TYyKQBC4bwE)

## 📚 What You'll Learn
Combine multiple conditions using logical operators to create powerful decision-making logic!

## 🎯 Learning Objectives
- Understand AND, OR, and NOT logical operators
- Combine multiple conditions in if statements
- Create complex decision-making logic
- Use truth tables to understand operator behavior

## 📖 Concept Explanation

### Logical Operators
Logical operators combine boolean expressions (conditions) to create more complex logic.

| Operator | Description | Example |
|----------|-------------|---------|
| `and` | Both conditions must be True | `age >= 18 and has_license` |
| `or` | At least one condition must be True | `is_weekend or is_holiday` |
| `not` | Reverses the boolean value | `not is_raining` |

### AND Operator
Returns True only if **both** conditions are True:
```python
if temp > 30 and is_sunny:
    print("Hot and sunny!")
```

Truth Table for AND:
| Condition 1 | Condition 2 | Result |
|-------------|-------------|--------|
| True | True | **True** |
| True | False | False |
| False | True | False |
| False | False | False |

### OR Operator
Returns True if **at least one** condition is True:
```python
if is_weekend or is_holiday:
    print("Day off!")
```

Truth Table for OR:
| Condition 1 | Condition 2 | Result |
|-------------|-------------|--------|
| True | True | **True** |
| True | False | **True** |
| False | True | **True** |
| False | False | False |

### NOT Operator
Reverses the boolean value:
```python
if not is_raining:
    print("No umbrella needed!")
```

Truth Table for NOT:
| Condition | Result |
|-----------|--------|
| True | False |
| False | True |

## 💡 Examples

### Example 1: Age and License Check
```python
age = 20
has_license = True

if age >= 18 and has_license:
    print("You can drive!")
else:
    print("You cannot drive yet.")
```

### Example 2: Weekend or Holiday
```python
is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("No work today!")
else:
    print("Time to work.")
```

### Example 3: Weather Advisory
```python
temp = 35
is_sunny = True
is_raining = False

if temp > 30 and is_sunny and not is_raining:
    print("Perfect beach weather!")
```

### Example 4: Login System
```python
username = "admin"
password = "secret123"
is_verified = True

if (username == "admin" and password == "secret123") and is_verified:
    print("Access granted!")
else:
    print("Access denied!")
```

## ✍️ Practice Exercises

1. **Voting Eligibility**: Check if person can vote (age >= 18 AND is_citizen)
2. **Discount Calculator**: Apply discount if purchase > $100 OR is_member
3. **Alarm System**: Sound alarm if is_night AND (motion_detected OR door_open)
4. **Grade Pass/Fail**: Pass if score >= 60 AND attendance >= 75%
5. **Weather Outfit**: Suggest outfit based on temp AND (is_raining OR is_snowing)
6. **Access Control**: Grant access if (is_admin OR is_manager) AND is_active

## 🔍 Common Mistakes

### Mistake 1: Confusing AND with OR
```python
# Wrong: This is too restrictive
if day == "Saturday" and day == "Sunday":  # day can't be both!
    print("Weekend")

# Correct:
if day == "Saturday" or day == "Sunday":
    print("Weekend")
```

### Mistake 2: Forgetting Parentheses
```python
# Ambiguous:
if age > 18 and is_student or has_id  # Unclear precedence

# Clear:
if (age > 18 and is_student) or has_id  # Much better!
```

### Mistake 3: Using = Instead of ==
```python
# Wrong:
if username = "admin":  # Assignment, not comparison!

# Correct:
if username == "admin":  # Comparison
```

## 📝 Operator Precedence
Python evaluates operators in this order:
1. Parentheses `()`
2. `not`
3. `and`
4. `or`

```python
# Without parentheses
result = True or False and False  # True (and evaluated first)

# With parentheses (recommended for clarity)
result = True or (False and False)  # True
result = (True or False) and False  # False
```

## 🎮 Real-World Examples

### Example: E-commerce Discount
```python
total = 150
is_member = True
has_coupon = False

# Member discount OR coupon discount
if (total >= 100 and is_member) or has_coupon:
    discount = total * 0.20
    final_price = total - discount
    print(f"Discount applied! Final price: ${final_price}")
else:
    print(f"Total: ${total}")
```

### Example: Security System
```python
is_armed = True
is_door_open = True
is_night = True
has_motion = False

if is_armed and (is_door_open or (is_night and has_motion)):
    print("🚨 ALERT! Intrusion detected!")
else:
    print("✓ System normal")
```

## 🚀 Challenge Projects

1. **Smart Thermostat**: Turn on AC if (temp > 75 and is_home) or override_on
2. **Library Fine Calculator**: Fine if overdue AND (not is_student OR days > 7)
3. **Flight Booking**: Available if (seats > 0) and (has_passport or is_domestic)
4. **Game Level Unlock**: Unlock if (score >= 1000 and level >= 5) or has_premium

## 🔗 Next Chapter
Continue to [Chapter 12: Conditional Expressions](../12-conditional/) to learn shorthand if-else statements!
