[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PavanMudigondaTR/python-bro-code/blob/main/8-weight-conversion/8-weight-conversion.ipynb) [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://raw.githubusercontent.com/PavanMudigondaTR/python-bro-code/main/8-weight-conversion/8-weight-conversion.ipynb)

# Chapter 9: Weight Converter Program

## 📺 Video Tutorial

**Python weight conversion exercise 🏋️** (5:47)

[![Watch on YouTube](https://img.shields.io/badge/Watch-YouTube-red?style=for-the-badge&logo=youtube)](https://youtu.be/80kjCBRjkmU)

## 📺 Video Tutorial

[![Watch on YouTube](https://img.shields.io/badge/Watch-BroCode_Python_Master_Class-red?style=for-the-badge&logo=youtube)](https://youtu.be/fy5QsDJmctQ)

## 📚 What You'll Learn
Create a practical unit converter that switches between pounds and kilograms!

## 🎯 Learning Objectives
- Work with unit conversions
- Use conversion factors in calculations
- Format decimal output
- Create practical, real-world programs
- Understand metric vs imperial measurements

## 📖 Concept Explanation

### Weight Units
- **Pounds (lbs)**: Imperial/US measurement system
- **Kilograms (kg)**: Metric measurement system (used in most of the world)

### Conversion Formula
```
1 kilogram = 2.20462 pounds
1 pound = 0.453592 kilograms

Or using grams:
1 kg = 1000 grams
1 lb = 453.6 grams
Therefore: 1 kg ≈ 2.2046 lbs
```

### How the Program Works
```
1. Ask for weight value
2. Ask for current unit (L or K)
3. Calculate conversion factor
4. Convert to opposite unit
5. Display result
```

## 💡 Examples

### Example 1: Pounds to Kilograms
```
Input: 150 pounds
Calculation: 150 / 2.20462 = 68.04 kg
Output: "Your weight in Kgs: 68.04"
```

### Example 2: Kilograms to Pounds
```
Input: 70 kilograms
Calculation: 70 * 2.20462 = 154.32 lbs
Output: "Your weight in Lbs: 154.32"
```

## ✍️ Practice Exercises

### Exercise 1: Add Rounding Options
```python
# Ask user how many decimal places they want
decimal_places = int(input("Decimal places: "))
print(f"Weight: {weight:.{decimal_places}f}")
```

### Exercise 2: Improve User Interface
```python
print("=== Weight Converter ===")
print("L - Convert from Pounds to Kilograms")
print("K - Convert from Kilograms to Pounds")
choice = input("Select option: ")
```

### Exercise 3: Add More Weight Units
Add conversions for:
- Ounces (oz): 1 lb = 16 oz
- Stones (st): 1 stone = 14 lbs (used in UK)
- Grams (g): 1 kg = 1000 g

### Exercise 4: Bidirectional Converter
```python
# Let user choose which direction:
# 1. lbs to kg
# 2. kg to lbs
```

## 🔍 Code Analysis

### Using .upper()
```python
unit = input("Enter L or K: ")
if unit.upper() == "L":  # Accepts both 'l' and 'L'
    # convert...
```
This makes the program more user-friendly!

### Formatting Output
```python
# Without formatting:
print(f"Weight: {weight}")  # 68.039215686274506

# With formatting (2 decimal places):
print(f"Weight: {weight:.2f}")  # 68.04
```

## 🎮 Enhanced Weight Converter

```python
def weight_converter():
    """Convert between pounds and kilograms"""
    
    print("=" * 40)
    print("     WEIGHT CONVERTER")
    print("=" * 40)
    
    # Get weight
    try:
        weight = float(input("\nEnter weight value: "))
        if weight <= 0:
            print("Error: Weight must be positive!")
            return
    except ValueError:
        print("Error: Please enter a valid number!")
        return
    
    # Get unit
    print("\nSelect unit:")
    print("L - Pounds (lbs)")
    print("K - Kilograms (kg)")
    unit = input("Your choice (L/K): ").upper()
    
    # Conversion factor
    LBS_TO_KG = 0.453592
    KG_TO_LBS = 2.20462
    
    # Convert and display
    if unit == "L":
        converted = weight * LBS_TO_KG
        print(f"\n{weight} lbs = {converted:.2f} kg")
    elif unit == "K":
        converted = weight * KG_TO_LBS
        print(f"\n{weight} kg = {converted:.2f} lbs")
    else:
        print("Error: Invalid unit!")
    
    print("=" * 40)

# Run converter
weight_converter()
```

## 📝 Common Weight Conversions

| Pounds (lbs) | Kilograms (kg) |
|--------------|----------------|
| 1 | 0.45 |
| 10 | 4.54 |
| 50 | 22.68 |
| 100 | 45.36 |
| 150 | 68.04 |
| 200 | 90.72 |

## 🌍 Real-World Applications

### Fitness & Health
```python
# BMI Calculator with weight conversion
height_m = float(input("Height in meters: "))
weight_kg = float(input("Weight in kg: "))
bmi = weight_kg / (height_m ** 2)
print(f"BMI: {bmi:.1f}")
```

### Travel
```python
# Luggage weight checker
weight_lbs = float(input("Luggage weight (lbs): "))
weight_kg = weight_lbs * 0.453592

if weight_kg > 23:  # Standard airline limit
    print(f"Overweight! {weight_kg:.1f} kg exceeds 23 kg limit")
else:
    print(f"Within limit: {weight_kg:.1f} kg")
```

## 🚀 Challenge Projects

### Challenge 1: Multi-Unit Converter
Create a converter for:
- Weight (lbs, kg, oz, stones)
- Length (miles, km, feet, meters)
- Temperature (C, F, K)
- Volume (gallons, liters)

### Challenge 2: Batch Converter
```python
# Convert multiple weights at once
weights = [120, 150, 180, 200]
for weight in weights:
    kg = weight * 0.453592
    print(f"{weight} lbs = {kg:.2f} kg")
```

### Challenge 3: Conversion Table Generator
```python
# Generate a conversion table
print("LBS | KG")
print("-" * 15)
for lbs in range(10, 210, 10):
    kg = lbs * 0.453592
    print(f"{lbs:3d} | {kg:6.2f}")
```

## 🎓 Key Takeaways from Video

1. Variables store data values that can be reused
2. Use if-elif-else for conditional logic
3. Follow along with the video for hands-on practice

> 💡 *These points cover the main concepts from the video tutorial to help reinforce your learning.*

## 🔗 Next Chapter
Continue to [Chapter 10: Temperature Converter](../10-temp/) to create another conversion program!

