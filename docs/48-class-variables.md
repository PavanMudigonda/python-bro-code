---
jupytext:
  text_representation:
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# 📊 Class Variables

## 🚀 Open Notebook

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PavanMudigonda/python-bro-code/blob/main/48-class-variables/48-class-variables.ipynb) [![Open In Kaggle](https://img.shields.io/badge/Open%20in-Kaggle-20BEFF?style=flat&logo=kaggle)](https://kaggle.com/kernels/welcome?src=https://github.com/PavanMudigonda/python-bro-code/blob/main/48-class-variables/48-class-variables.ipynb)


## 📺 Video Tutorial

[![Watch on YouTube](https://img.shields.io/badge/Watch-YouTube-red?style=for-the-badge&logo=youtube)](https://youtu.be/bytvWg4fPB0)

**Learn class variables in 8 minutes! 🎓** (8:47)

## What You'll Learn

In this chapter, you'll master the distinction between class variables and instance variables - a fundamental concept in OOP. You'll learn how class variables are shared among all instances of a class, how to define and access them properly, when to use them versus instance variables, and common use cases like counters, constants, and default values.

## Learning Objectives

- Distinguish between class variables and instance variables
- Define class variables in the class body (outside methods)
- Access class variables using `ClassName.variable` syntax
- Understand when class variables are shared vs instance variables are unique
- Implement counters and shared data using class variables
- Avoid common pitfalls when mixing class and instance variables

## Concept Explanation

### Class Variables vs Instance Variables

**Instance Variables** = Unique to each object (uses `self`)  
**Class Variables** = Shared by ALL objects (defined in class body)

```{code-cell} python
class Student:
    # CLASS VARIABLE (shared by all)
    school_name = "Python High School"
    
    def __init__(self, name):
        # INSTANCE VARIABLE (unique to each)
        self.name = name

# All students share the same school_name
student1 = Student("Alice")
student2 = Student("Bob")

print(student1.school_name)  # Python High School
print(student2.school_name)  # Python High School (same for both!)

# But each has their own name
print(student1.name)  # Alice
print(student2.name)  # Bob (different!)
```

### Where to Define Each Type

```{code-cell} python
class MyClass:
    # CLASS VARIABLES - defined in class body
    class_var = "shared"
    counter = 0
    
    def __init__(self, value):
        # INSTANCE VARIABLES - defined with self
        self.instance_var = value
```

### Accessing Class Variables

**Three ways to access class variables:**

```{code-cell} python
class Dog:
    species = "Canis familiaris"  # Class variable

dog1 = Dog()

# 1. Through class name (BEST PRACTICE)
print(Dog.species)

# 2. Through instance (works but not recommended)
print(dog1.species)

# 3. Inside methods using ClassName
class Dog:
    species = "Canis familiaris"
    
    def show_species(self):
        print(Dog.species)  # Access via class name
```

### Modifying Class Variables

**Important:** Modify using `ClassName.variable`:

```{code-cell} python
class Counter:
    count = 0  # Class variable
    
    def __init__(self):
        Counter.count += 1  # Modify using ClassName

c1 = Counter()  # count = 1
c2 = Counter()  # count = 2
c3 = Counter()  # count = 3

print(Counter.count)  # 3
```

**What NOT to do:**
```{code-cell} python
class Counter:
    count = 0
    
    def __init__(self):
        self.count += 1  # WRONG! Creates instance variable

c1 = Counter()
c2 = Counter()

print(Counter.count)  # Still 0! Didn't modify class variable
print(c1.count)       # 1 (instance variable)
print(c2.count)       # 1 (different instance variable)
```

### Common Use Cases

**1. Counters:**
```{code-cell} python
class Customer:
    total_customers = 0
    
    def __init__(self, name):
        self.name = name
        Customer.total_customers += 1
```

**2. Constants:**
```{code-cell} python
class Circle:
    PI = 3.14159  # Constant shared by all circles
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return Circle.PI * self.radius ** 2
```

**3. Default Values:**
```{code-cell} python
class Product:
    tax_rate = 0.08  # 8% tax for all products
    
    def __init__(self, price):
        self.price = price
    
    def total_price(self):
        return self.price * (1 + Product.tax_rate)
```

**4. Shared Configuration:**
```{code-cell} python
class DatabaseConnection:
    host = "localhost"
    port = 5432
    max_connections = 100
```

## Examples

### Example 1: Student Counter

```{code-cell} python
class Student:
    """Student class with counter."""
    
    # Class variables (shared by all)
    school_name = "Python Academy"
    total_students = 0
    
    def __init__(self, name, grade):
        # Instance variables (unique to each)
        self.name = name
        self.grade = grade
        
        # Increment class variable
        Student.total_students += 1
    
    def info(self):
        """Show student info."""
        return f"{self.name} - Grade {self.grade} - {Student.school_name}"

# Create students
s1 = Student("Alice", 10)
s2 = Student("Bob", 11)
s3 = Student("Charlie", 10)

# Each student has unique name and grade
print(s1.info())  # Alice - Grade 10 - Python Academy
print(s2.info())  # Bob - Grade 11 - Python Academy

# All share the same school_name and total_students
print(f"Total students: {Student.total_students}")  # 3
```

### Example 2: Bank Account with Interest Rate

```{code-cell} python
class BankAccount:
    """Bank account with shared interest rate."""
    
    # Class variable - same interest rate for all accounts
    interest_rate = 0.03  # 3%
    
    def __init__(self, owner, balance):
        # Instance variables - unique to each account
        self.owner = owner
        self.balance = balance
    
    def apply_interest(self):
        """Add interest to balance."""
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest
        print(f"{self.owner}: +${interest:.2f} interest")
    
    @classmethod
    def set_interest_rate(cls, rate):
        """Change interest rate for all accounts."""
        cls.interest_rate = rate
        print(f"Interest rate changed to {rate*100}%")

# Create accounts
acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob", 2000)

# Apply interest (3%)
acc1.apply_interest()  # Alice: +$30.00 interest
acc2.apply_interest()  # Bob: +$60.00 interest

# Change interest rate for ALL accounts
BankAccount.set_interest_rate(0.05)  # 5%

# Apply new rate
acc1.apply_interest()  # Alice: +$51.50 interest
acc2.apply_interest()  # Bob: +$103.00 interest
```

### Example 3: Product Catalog

```{code-cell} python
class Product:
    """Product with shared tax rate."""
    
    # Class variables
    tax_rate = 0.08  # 8% sales tax
    product_count = 0
    
    def __init__(self, name, price):
        # Instance variables
        self.name = name
        self.price = price
        self.id = Product.product_count
        
        # Increment product counter
        Product.product_count += 1
    
    def total_price(self):
        """Calculate price with tax."""
        return self.price * (1 + Product.tax_rate)
    
    def info(self):
        """Product information."""
        return f"#{self.id}: {self.name} - ${self.price:.2f} (${self.total_price():.2f} with tax)"

# Create products
p1 = Product("Laptop", 999.99)
p2 = Product("Mouse", 29.99)
p3 = Product("Keyboard", 79.99)

# Each has unique ID, name, price
print(p1.info())  # #0: Laptop - $999.99 ($1079.99 with tax)
print(p2.info())  # #1: Mouse - $29.99 ($32.39 with tax)
print(p3.info())  # #2: Keyboard - $79.99 ($86.39 with tax)

# All share same tax_rate
print(f"Tax rate: {Product.tax_rate * 100}%")
print(f"Total products: {Product.product_count}")
```

### Example 4: Game Character Types

```{code-cell} python
class Warrior:
    """Warrior character class."""
    
    # Class variables (same for all warriors)
    character_type = "Warrior"
    base_health = 120
    base_strength = 15
    total_warriors = 0
    
    def __init__(self, name):
        # Instance variables (unique to each warrior)
        self.name = name
        self.health = Warrior.base_health
        self.strength = Warrior.base_strength
        self.level = 1
        
        # Increment counter
        Warrior.total_warriors += 1
    
    def show_stats(self):
        """Display character stats."""
        print(f"\n{self.name} ({Warrior.character_type})")
        print(f"  Level: {self.level}")
        print(f"  Health: {self.health}")
        print(f"  Strength: {self.strength}")
    
    def level_up(self):
        """Increase level and stats."""
        self.level += 1
        self.health += 20
        self.strength += 5
        print(f"{self.name} leveled up to {self.level}!")

# Create warriors
w1 = Warrior("Conan")
w2 = Warrior("Xena")

# Each warrior is independent
w1.level_up()
w1.show_stats()

w2.show_stats()

# All share character_type and base stats
print(f"\nTotal Warriors: {Warrior.total_warriors}")
```

### Example 5: Circle with Shared PI

```{code-cell} python
class Circle:
    """Circle class with shared PI constant."""
    
    # Class variable - mathematical constant
    PI = 3.14159
    circles_created = 0
    
    def __init__(self, radius):
        # Instance variable
        self.radius = radius
        Circle.circles_created += 1
    
    def area(self):
        """Calculate area."""
        return Circle.PI * self.radius ** 2
    
    def circumference(self):
        """Calculate circumference."""
        return 2 * Circle.PI * self.radius
    
    def info(self):
        """Show circle information."""
        return f"Circle(r={self.radius}): Area={self.area():.2f}, Circumference={self.circumference():.2f}"

# Create circles
c1 = Circle(5)
c2 = Circle(10)
c3 = Circle(3)

# Each has different radius, but all use same PI
print(c1.info())  # Circle(r=5): Area=78.54, Circumference=31.42
print(c2.info())  # Circle(r=10): Area=314.16, Circumference=62.83
print(c3.info())  # Circle(r=3): Area=28.27, Circumference=18.85

print(f"\nTotal circles created: {Circle.circles_created}")
print(f"PI value used: {Circle.PI}")
```

### Example 6: Employee with Company Name

```{code-cell} python
class Employee:
    """Employee class with shared company info."""
    
    # Class variables (shared by all employees)
    company_name = "Tech Corp"
    company_address = "123 Tech Street"
    employee_count = 0
    total_salary = 0
    
    def __init__(self, name, position, salary):
        # Instance variables (unique to each employee)
        self.name = name
        self.position = position
        self.salary = salary
        self.employee_id = Employee.employee_count
        
        # Update class variables
        Employee.employee_count += 1
        Employee.total_salary += salary
    
    def give_raise(self, amount):
        """Increase salary."""
        self.salary += amount
        Employee.total_salary += amount
        print(f"{self.name} received ${amount} raise")
    
    def info(self):
        """Employee information."""
        return f"ID: {self.employee_id} | {self.name} - {self.position} | ${self.salary:,}"
    
    @staticmethod
    def company_info():
        """Display company information."""
        print(f"\n{Employee.company_name}")
        print(f"Location: {Employee.company_address}")
        print(f"Employees: {Employee.employee_count}")
        print(f"Total Payroll: ${Employee.total_salary:,}")

# Create employees
emp1 = Employee("Alice", "Developer", 80000)
emp2 = Employee("Bob", "Designer", 70000)
emp3 = Employee("Charlie", "Manager", 95000)

# Each employee is unique
print(emp1.info())
print(emp2.info())
print(emp3.info())

# Give raises
emp1.give_raise(5000)

# Show company info
Employee.company_info()
```

### Example 7: Game Settings

```{code-cell} python
class Game:
    """Game class with shared settings."""
    
    # Class variables (game settings)
    difficulty = "Normal"
    sound_volume = 0.7
    music_volume = 0.5
    max_players = 4
    games_played = 0
    
    def __init__(self, player_name):
        # Instance variables
        self.player_name = player_name
        self.score = 0
        self.level = 1
        
        Game.games_played += 1
    
    def play(self):
        """Simulate playing."""
        print(f"\n{self.player_name} is playing on {Game.difficulty} difficulty")
        print(f"Sound: {Game.sound_volume*100}% | Music: {Game.music_volume*100}%")
        self.score += 100
        print(f"Score: {self.score}")
    
    @classmethod
    def change_difficulty(cls, new_difficulty):
        """Change difficulty for all games."""
        cls.difficulty = new_difficulty
        print(f"Difficulty changed to {new_difficulty}")
    
    @classmethod
    def adjust_volumes(cls, sound, music):
        """Adjust volume settings."""
        cls.sound_volume = sound
        cls.music_volume = music
        print(f"Volumes updated: Sound={sound*100}%, Music={music*100}%")

# Create game sessions
game1 = Game("Player1")
game2 = Game("Player2")

# Play with default settings
game1.play()

# Change settings (affects all games)
Game.change_difficulty("Hard")
Game.adjust_volumes(0.9, 0.3)

# Play with new settings
game2.play()

print(f"\nTotal games played: {Game.games_played}")
```

## Practice Exercises

### Beginner Exercises

1. **Book Library**
   - Track total books with class variable
   - Each book has unique title and author
   - Show library statistics

2. **Car Dealership**
   - Shared dealership name
   - Count total cars sold
   - Each car has unique make/model/price

3. **Student Grade Tracker**
   - Shared school name and year
   - Count total students
   - Each student has unique grades

4. **Product Inventory**
   - Shared warehouse location
   - Count total products
   - Each product has unique stock level

5. **Temperature Monitor**
   - Shared unit system (C or F)
   - Each reading has unique value and time
   - Track total readings

### Intermediate Exercises

1. **Online Course Platform**
   - Shared platform name and fee structure
   - Track total enrollments
   - Each student has unique progress
   - Calculate total revenue

2. **Restaurant Order System**
   - Shared menu and prices
   - Count total orders
   - Each order has unique items
   - Track daily revenue

3. **Social Media Posts**
   - Shared platform rules
   - Count total posts
   - Each post has unique content and likes
   - Track trending topics

4. **Parking Lot Management**
   - Fixed number of spaces (class variable)
   - Track available spaces
   - Each car has unique entry time
   - Calculate fees

5. **Game High Score System**
   - Track global high score
   - Count total games
   - Each game has unique player score
   - Update high score when beaten

### Advanced Exercises

1. **Multi-Currency Bank**
   - Shared exchange rates (class variable)
   - Each account in different currency
   - Update rates affects all accounts
   - Currency conversion methods

2. **Dynamic Pricing System**
   - Shared base prices
   - Surge pricing affects all items
   - Each purchase has unique timestamp
   - Historical price tracking

3. **Network Monitoring**
   - Shared threshold limits
   - Each connection has unique metrics
   - Trigger alerts when threshold exceeded
   - Network-wide statistics

4. **Subscription Service**
   - Shared tier pricing
   - Count subscribers per tier
   - Each user has unique features access
   - Revenue calculations

5. **Factory Production**
   - Shared quality standards
   - Count total units
   - Each batch has unique quality score
   - Defect rate tracking

## Common Mistakes to Avoid

### Mistake 1: Using `self` Instead of `ClassName`

❌ **Wrong:**
```{code-cell} python
class Counter:
    count = 0
    
    def __init__(self):
        self.count += 1  # Creates instance variable!

c1 = Counter()
c2 = Counter()
print(Counter.count)  # Still 0!
```

✅ **Correct:**
```{code-cell} python
class Counter:
    count = 0
    
    def __init__(self):
        Counter.count += 1  # Modifies class variable

c1 = Counter()
c2 = Counter()
print(Counter.count)  # 2
```

### Mistake 2: Mutable Class Variables

❌ **Wrong:**
```{code-cell} python
class Team:
    members = []  # Shared list - BAD!
    
    def __init__(self, name):
        self.name = name
        Team.members.append(name)

t1 = Team("Alice")
t2 = Team("Bob")
# Both teams share the same members list!
```

✅ **Correct:**
```{code-cell} python
class Team:
    def __init__(self, name):
        self.members = []  # Each team has own list
        self.members.append(name)
```

### Mistake 3: Confusing Access Syntax

❌ **Wrong:**
```{code-cell} python
class Dog:
    species = "Canis"
    
    def show(self):
        print(self.species)  # Works but not clear

# Later someone does:
dog = Dog()
dog.species = "Felis"  # Creates instance variable!
print(Dog.species)  # Still "Canis"
```

✅ **Correct:**
```{code-cell} python
class Dog:
    species = "Canis"
    
    def show(self):
        print(Dog.species)  # Clear it's class variable

# If you need to modify:
Dog.species = "Felis"  # Modifies for all
```

### Mistake 4: Not Using Class Variables When Appropriate

❌ **Wrong:**
```{code-cell} python
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14159  # Why store in each circle?
    
    def area(self):
        return self.pi * self.radius ** 2
```

✅ **Correct:**
```{code-cell} python
class Circle:
    PI = 3.14159  # Share constant
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return Circle.PI * self.radius ** 2
```

## Real-World Applications

### 1. **Configuration Management**
- Database connection pools (max connections)
- API rate limits (requests per minute)
- Application settings (debug mode, version)
- Feature flags (enabled/disabled)

### 2. **Resource Tracking**
- License limits (max users)
- Memory pools (available resources)
- Connection pools (database connections)
- Thread pools (worker threads)

### 3. **Statistics and Counters**
- Total users registered
- Total transactions processed
- Error counts
- Performance metrics

### 4. **Shared Constants**
- Mathematical constants (PI, E)
- Physical constants
- Conversion factors
- Standard values

## Challenge Projects

### 1. **License Management System**
- Track total licenses
- Different license tiers
- Expiration management
- Usage analytics

### 2. **Rate Limiting System**
- Shared rate limits
- Per-user tracking
- Cooldown periods
- Burst allowances

### 3. **Resource Pool Manager**
- Fixed pool size
- Check out/in resources
- Waiting queue
- Usage statistics

### 4. **Multi-Tenant Application**
- Shared configuration
- Per-tenant customization
- Resource allocation
- Billing system

### 5. **Game Server**
- Server capacity limits
- Active player count
- Global events
- Leaderboards

---

## Navigation

← [Previous: 46 - Python OOP](46-python-oop.md) | [Next: 48 - Inheritance](48-inheritance.md) →

[↑ Back to Main README](../README.md)

## 🎓 Key Takeaways from Video

1. Variables store data values that can be reused
2. Follow along with the video for hands-on practice
3. Experiment with the code examples to deepen understanding

> 💡 *These points cover the main concepts from the video tutorial to help reinforce your learning.*