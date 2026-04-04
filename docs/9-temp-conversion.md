# Chapter 9: Temp Conversion

## 🚀 Open Notebook

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PavanMudigonda/python-bro-code/blob/main/9-temp-conversion/9-temp-conversion.ipynb) [![Open In Kaggle](https://img.shields.io/badge/Open%20in-Kaggle-20BEFF?style=flat&logo=kaggle)](https://kaggle.com/kernels/welcome?src=https://github.com/PavanMudigonda/python-bro-code/blob/main/9-temp-conversion/9-temp-conversion.ipynb)


[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PavanMudigondaTR/python-bro-code/blob/main/9-temp-conversion/9-temp-conversion.ipynb) [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://raw.githubusercontent.com/PavanMudigondaTR/python-bro-code/main/9-temp-conversion/9-temp-conversion.ipynb)

# Chapter 10: Temperature Converter Program

## 📺 Video Tutorial

**Python temperature conversion program 🌡️** (5:44)

[![Watch on YouTube](https://img.shields.io/badge/Watch-YouTube-red?style=for-the-badge&logo=youtube)](https://youtu.be/fy5QsDJmctQ)

## 📚 What You'll Learn
Convert temperatures between Fahrenheit and Celsius - essential for international travel and science!

## 🎯 Learning Objectives
- Understand temperature scales (Fahrenheit and Celsius)
- Apply mathematical conversion formulas
- Work with floating-point arithmetic
- Create conversion programs
- Format temperature output properly

## 📖 Concept Explanation

### Temperature Scales

#### Fahrenheit (°F)
- Used in the United States
- Water freezes at 32°F
- Water boils at 212°F
- Normal body temperature: 98.6°F

#### Celsius (°C)
- Used in most of the world
- Water freezes at 0°C
- Water boils at 100°C
- Normal body temperature: 37°C

### Conversion Formulas

#### Celsius to Fahrenheit
```
F = (C × 9/5) + 32
or
F = (C × 1.8) + 32
```

#### Fahrenheit to Celsius
```
C = (F - 32) × 5/9
or
C = (F - 32) / 1.8
```

## 💡 Examples

### Example 1: Freezing Point
```python
celsius = 0
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")  # 0°C = 32°F
```

### Example 2: Boiling Point
```python
celsius = 100
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")  # 100°C = 212°F
```

### Example 3: Body Temperature
```python
fahrenheit = 98.6
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit}°F = {celsius:.1f}°C")  # 98.6°F = 37.0°C
```

## ✍️ Practice Exercises

### Exercise 1: Add Kelvin Conversion
```python
# Kelvin to Celsius: K - 273.15 = C
# Celsius to Kelvin: C + 273.15 = K
```

### Exercise 2: Improve User Experience
```python
print("=== Temperature Converter ===")
print("F - Convert from Fahrenheit to Celsius")
print("C - Convert from Celsius to Fahrenheit")
```

### Exercise 3: Add Temperature Categories
```python
if temp_celsius < 0:
    print("Below freezing!")
elif temp_celsius < 10:
    print("Cold")
elif temp_celsius < 20:
    print("Cool")
elif temp_celsius < 30:
    print("Warm")
else:
    print("Hot!")
```

### Exercise 4: Batch Conversion
```python
# Convert multiple temperatures at once
temps = [0, 32, 68, 100]
for temp in temps:
    celsius = (temp - 32) * 5/9
    print(f"{temp}°F = {celsius:.1f}°C")
```

## 📝 Common Temperature Conversions

| Celsius (°C) | Fahrenheit (°F) | Description |
|--------------|-----------------|-------------|
| -40 | -40 | Same in both scales! |
| -18 | 0 | Very cold |
| 0 | 32 | Water freezes |
| 10 | 50 | Cool |
| 20 | 68 | Room temperature |
| 37 | 98.6 | Body temperature |
| 100 | 212 | Water boils |

## 🎮 Enhanced Temperature Converter

```python
def temperature_converter():
    """Convert between Fahrenheit and Celsius"""
    
    print("=" * 45)
    print("      TEMPERATURE CONVERTER")
    print("=" * 45)
    
    # Get input unit
    print("\nWhat unit is your temperature in?")
    print("F - Fahrenheit")
    print("C - Celsius")
    unit = input("Enter F or C: ").upper()
    
    # Get temperature value
    try:
        temp = float(input("Enter temperature: "))
    except ValueError:
        print("Error: Please enter a valid number!")
        return
    
    # Convert and display
    if unit == "F":
        celsius = (temp - 32) * 5/9
        print(f"\n{temp}°F = {celsius:.2f}°C")
        
        # Add category
        if celsius < 0:
            print("Status: Freezing!")
        elif celsius < 20:
            print("Status: Cold")
        elif celsius < 30:
            print("Status: Warm")
        else:
            print("Status: Hot!")
            
    elif unit == "C":
        fahrenheit = (temp * 9/5) + 32
        print(f"\n{temp}°C = {fahrenheit:.2f}°F")
        
        # Add category
        if temp < 0:
            print("Status: Freezing!")
        elif temp < 20:
            print("Status: Cold")
        elif temp < 30:
            print("Status: Warm")
        else:
            print("Status: Hot!")
    else:
        print("Error: Invalid unit! Please enter F or C")
    
    print("=" * 45)

# Run converter
temperature_converter()
```

## 🌡️ Real-World Applications

### Weather Reporting
```python
def weather_report(temp_c):
    """Display weather with temperature"""
    temp_f = (temp_c * 9/5) + 32
    
    print(f"\nToday's Temperature:")
    print(f"  {temp_c:.1f}°C / {temp_f:.1f}°F")
    
    if temp_c < 0:
        print("  🥶 Freezing! Bundle up!")
    elif temp_c < 15:
        print("  🧥 Chilly. Bring a jacket!")
    elif temp_c < 25:
        print("  😊 Pleasant weather!")
    else:
        print("  ☀️ Hot! Stay hydrated!")

weather_report(22)
```

### Cooking/Baking
```python
def oven_temp_converter(celsius):
    """Convert baking temperatures"""
    fahrenheit = (celsius * 9/5) + 32
    
    print(f"\nOven Temperature:")
    print(f"  {celsius}°C = {fahrenheit:.0f}°F")
    
    # Gas mark (UK)
    if 140 <= celsius <= 150:
        print("  Gas Mark: 1")
    elif 160 <= celsius <= 180:
        print("  Gas Mark: 4")
    elif 190 <= celsius <= 200:
        print("  Gas Mark: 6")
    elif 220 <= celsius <= 230:
        print("  Gas Mark: 8")

oven_temp_converter(180)
```

## 🚀 Challenge Projects

### Challenge 1: Triple Converter
Add Kelvin scale:
```python
# Celsius to Kelvin: K = C + 273.15
# Kelvin to Celsius: C = K - 273.15
# Absolute zero: 0 K = -273.15°C = -459.67°F
```

### Challenge 2: Temperature Range Converter
```python
# Convert a range of temperatures
low_f = 50
high_f = 80

low_c = (low_f - 32) * 5/9
high_c = (high_f - 32) * 5/9

print(f"Range: {low_f}-{high_f}°F = {low_c:.0f}-{high_c:.0f}°C")
```

### Challenge 3: Scientific Temperature Converter
```python
def convert_temperature(value, from_unit, to_unit):
    """Convert between C, F, and K"""
    # Convert to Celsius first
    if from_unit == 'F':
        celsius = (value - 32) * 5/9
    elif from_unit == 'K':
        celsius = value - 273.15
    else:
        celsius = value
    
    # Convert from Celsius to target unit
    if to_unit == 'F':
        return (celsius * 9/5) + 32
    elif to_unit == 'K':
        return celsius + 273.15
    else:
        return celsius

print(convert_temperature(100, 'C', 'F'))  # 212°F
print(convert_temperature(32, 'F', 'K'))   # 273.15 K
```

## 🔍 Understanding the Math

### Why 5/9 and 9/5?
- Celsius: 100 degrees between freezing and boiling
- Fahrenheit: 180 degrees between freezing and boiling
- Ratio: 180/100 = 9/5 or 100/180 = 5/9

### Why add/subtract 32?
- Water freezes at 0°C but 32°F
- This 32-degree offset must be adjusted

## 📊 Conversion Table Generator
```python
print("°C  | °F")
print("-" * 15)
for celsius in range(-10, 41, 5):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius:3d} | {fahrenheit:5.1f}")
```

Output:
```
°C  | °F
---------------
-10 |  14.0
 -5 |  23.0
  0 |  32.0
  5 |  41.0
 10 |  50.0
 15 |  59.0
 20 |  68.0
 25 |  77.0
 30 |  86.0
 35 |  95.0
 40 | 104.0
```

## 🎓 Key Takeaways from Video

1. Variables store data values that can be reused
2. Use if-elif-else for conditional logic
3. Follow along with the video for hands-on practice

> 💡 *These points cover the main concepts from the video tutorial to help reinforce your learning.*

## 🔗 Next Chapter
Continue to [Chapter 11: Logical Operators](11-logical.md) to learn about AND, OR, and NOT operations!

