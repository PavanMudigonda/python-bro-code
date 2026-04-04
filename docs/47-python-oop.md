# 🏗️ Python OOP (Object-Oriented Programming)

## 🚀 Open Notebook

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PavanMudigonda/python-bro-code/blob/main/47-python-oop/47-python-oop.ipynb) [![Open In Kaggle](https://img.shields.io/badge/Open%20in-Kaggle-20BEFF?style=flat&logo=kaggle)](https://kaggle.com/kernels/welcome?src=https://github.com/PavanMudigonda/python-bro-code/blob/main/47-python-oop/47-python-oop.ipynb)


## 📺 Video Tutorial

**Learn Python Object Oriented Programming! 🚗** (15:31)

## What You'll Learn

In this chapter, you'll be introduced to Object-Oriented Programming (OOP) in Python - one of the most important programming paradigms. You'll learn how to create classes as blueprints for objects, define attributes and methods, use the `__init__` constructor, understand the `self` parameter, and create multiple instances from a single class. This is your gateway to writing more organized, reusable, and scalable code.

## Learning Objectives

- Understand what objects and classes are in programming
- Create classes as blueprints for objects
- Define instance attributes using the `__init__` constructor method
- Implement methods (functions inside classes)
- Use the `self` parameter to access instance data
- Create and work with multiple object instances from a single class

## Concept Explanation

### What is Object-Oriented Programming?

**Object** = A bundle of related attributes (data) and methods (functions)  
**Class** = A blueprint for creating objects

**Real-world analogy:**
```
Blueprint (Class) → Houses (Objects)
-----------------------------------
Car Blueprint     → My car, Your car, Her car
Cookie Cutter     → Cookie 1, Cookie 2, Cookie 3
Student Form      → Alice, Bob, Charlie
```

### Classes and Objects

```python
# Class = Blueprint
class Car:
    pass

# Objects = Instances created from blueprint
car1 = Car()  # First car object
car2 = Car()  # Second car object
car3 = Car()  # Third car object
```

Each object is independent:
```python
car1.color = "red"
car2.color = "blue"

print(car1.color)  # red
print(car2.color)  # blue
```

### The `__init__` Constructor

The `__init__` method is automatically called when creating an object:

```python
class Car:
    def __init__(self, make, model):
        self.make = make      # Instance attribute
        self.model = model    # Instance attribute

# When you create an object:
my_car = Car("Toyota", "Camry")
# Python automatically calls: __init__(my_car, "Toyota", "Camry")
```

**Dunder Methods:** `__init__` has double underscores (dunderscore/dunder = **d**ouble **under**score). These are special methods Python recognizes.

### The `self` Parameter

`self` refers to the instance being created or modified:

```python
class Dog:
    def __init__(self, name):
        self.name = name  # self = the specific dog being created
    
    def bark(self):
        print(f"{self.name} says Woof!")  # self = the dog calling this method

# Create two dogs
dog1 = Dog("Rex")
dog2 = Dog("Buddy")

dog1.bark()  # self = dog1 → "Rex says Woof!"
dog2.bark()  # self = dog2 → "Buddy says Woof!"
```

**Why `self`?**
- Tells Python which object's data to use
- Required as first parameter in all instance methods
- Automatically passed (don't include it when calling methods)

```python
# Definition (with self):
def bark(self):
    print(f"{self.name} barks")

# Calling (without self - Python adds it automatically):
dog1.bark()  # Python calls: bark(dog1)
```

### Attributes vs Methods

**Attributes** = Variables that belong to an object (data)  
**Methods** = Functions that belong to an object (behavior)

```python
class Person:
    def __init__(self, name, age):
        # Attributes (data)
        self.name = name
        self.age = age
    
    # Method (behavior)
    def greet(self):
        print(f"Hello, I'm {self.name}")
    
    # Method (behavior)
    def have_birthday(self):
        self.age += 1

person = Person("Alice", 25)

# Access attribute
print(person.name)  # Alice

# Call method
person.greet()      # Hello, I'm Alice
person.have_birthday()
print(person.age)   # 26
```

### Class Anatomy

```python
class ClassName:                    # Class definition
    def __init__(self, param1):     # Constructor
        self.attribute = param1     # Instance attribute
    
    def method_name(self):          # Instance method
        return self.attribute       # Access attribute

# Create instance
object_name = ClassName("value")    # Calls __init__

# Use object
object_name.method_name()           # Call method
print(object_name.attribute)        # Access attribute
```

## Examples

### Example 1: Simple Car Class

```python
class Car:
    """A simple Car class."""
    
    def __init__(self, make, model, year):
        """Initialize car attributes."""
        self.make = make
        self.model = model
        self.year = year
    
    def describe(self):
        """Return formatted description."""
        return f"{self.year} {self.make} {self.model}"
    
    def honk(self):
        """Make the car honk."""
        print("Beep beep!")

# Create cars
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2019)

# Use cars
print(car1.describe())  # 2020 Toyota Camry
car1.honk()            # Beep beep!

print(car2.describe())  # 2019 Honda Civic
car2.honk()            # Beep beep!
```

### Example 2: Bank Account Class

```python
class BankAccount:
    """Represents a bank account."""
    
    def __init__(self, owner, balance=0):
        """Initialize account with owner and optional balance."""
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        """Add money to account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive")
    
    def withdraw(self, amount):
        """Remove money from account."""
        if amount > self.balance:
            print("Insufficient funds")
        elif amount <= 0:
            print("Withdrawal amount must be positive")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
    
    def get_balance(self):
        """Return current balance."""
        return self.balance

# Create accounts
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob")  # Uses default balance = 0

# Use accounts
account1.deposit(500)     # Deposited $500. New balance: $1500
account1.withdraw(200)    # Withdrew $200. New balance: $1300
print(account1.get_balance())  # 1300

account2.deposit(100)     # Deposited $100. New balance: $100
```

### Example 3: Student Class with Methods

```python
class Student:
    """Represents a student."""
    
    def __init__(self, name, grade=0):
        """Initialize student."""
        self.name = name
        self.grade = grade
        self.courses = []
    
    def enroll(self, course):
        """Enroll in a course."""
        self.courses.append(course)
        print(f"{self.name} enrolled in {course}")
    
    def set_grade(self, grade):
        """Set student's grade."""
        self.grade = grade
        print(f"{self.name}'s grade set to {grade}")
    
    def get_info(self):
        """Return student information."""
        courses_str = ", ".join(self.courses) if self.courses else "None"
        return f"Student: {self.name}\nGrade: {self.grade}\nCourses: {courses_str}"

# Create students
student1 = Student("Alice")
student2 = Student("Bob", 85)

# Use methods
student1.enroll("Math")
student1.enroll("Science")
student1.set_grade(92)

print(student1.get_info())
# Output:
# Student: Alice
# Grade: 92
# Courses: Math, Science
```

### Example 4: Rectangle Class with Calculations

```python
class Rectangle:
    """Represents a rectangle."""
    
    def __init__(self, width, height):
        """Initialize rectangle dimensions."""
        self.width = width
        self.height = height
    
    def area(self):
        """Calculate and return area."""
        return self.width * self.height
    
    def perimeter(self):
        """Calculate and return perimeter."""
        return 2 * (self.width + self.height)
    
    def is_square(self):
        """Check if rectangle is a square."""
        return self.width == self.height
    
    def scale(self, factor):
        """Scale rectangle by a factor."""
        self.width *= factor
        self.height *= factor

# Create rectangles
rect1 = Rectangle(10, 5)
rect2 = Rectangle(7, 7)

# Use methods
print(f"Area: {rect1.area()}")           # Area: 50
print(f"Perimeter: {rect1.perimeter()}") # Perimeter: 30
print(f"Is square: {rect1.is_square()}") # Is square: False

rect1.scale(2)  # Double the size
print(f"New area: {rect1.area()}")       # New area: 200

print(f"Is square: {rect2.is_square()}") # Is square: True
```

### Example 5: Dog Class with Multiple Instances

```python
class Dog:
    """Represents a dog."""
    
    def __init__(self, name, breed, age):
        """Initialize dog attributes."""
        self.name = name
        self.breed = breed
        self.age = age
        self.tricks = []
    
    def bark(self):
        """Make dog bark."""
        print(f"{self.name}: Woof woof!")
    
    def learn_trick(self, trick):
        """Teach dog a new trick."""
        self.tricks.append(trick)
        print(f"{self.name} learned {trick}!")
    
    def perform_tricks(self):
        """Show all tricks."""
        if self.tricks:
            print(f"{self.name}'s tricks:")
            for trick in self.tricks:
                print(f"  - {trick}")
        else:
            print(f"{self.name} doesn't know any tricks yet")
    
    def get_age_human_years(self):
        """Convert dog years to human years."""
        return self.age * 7

# Create dogs
dog1 = Dog("Rex", "German Shepherd", 3)
dog2 = Dog("Buddy", "Golden Retriever", 5)

# Each dog is independent
dog1.bark()                    # Rex: Woof woof!
dog1.learn_trick("Sit")        # Rex learned Sit!
dog1.learn_trick("Roll over")  # Rex learned Roll over!
dog1.perform_tricks()

dog2.bark()                    # Buddy: Woof woof!
dog2.learn_trick("Fetch")      # Buddy learned Fetch!
dog2.perform_tricks()

print(f"{dog1.name} is {dog1.get_age_human_years()} in human years")
```

### Example 6: Book Class

```python
class Book:
    """Represents a book."""
    
    def __init__(self, title, author, pages):
        """Initialize book."""
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 0
        self.is_finished = False
    
    def read(self, pages_read):
        """Read a certain number of pages."""
        if self.is_finished:
            print("Already finished this book!")
            return
        
        self.current_page += pages_read
        
        if self.current_page >= self.pages:
            self.current_page = self.pages
            self.is_finished = True
            print(f"Finished reading {self.title}!")
        else:
            progress = (self.current_page / self.pages) * 100
            print(f"Read {pages_read} pages. Progress: {progress:.1f}%")
    
    def get_info(self):
        """Return book information."""
        status = "Finished" if self.is_finished else f"Page {self.current_page}/{self.pages}"
        return f"'{self.title}' by {self.author} - {status}"

# Create books
book1 = Book("Python Programming", "John Doe", 300)
book2 = Book("Data Science", "Jane Smith", 450)

# Read books
book1.read(50)   # Read 50 pages. Progress: 16.7%
book1.read(100)  # Read 100 pages. Progress: 50.0%
book1.read(200)  # Finished reading Python Programming!

print(book1.get_info())  # 'Python Programming' by John Doe - Finished
print(book2.get_info())  # 'Data Science' by Jane Smith - Page 0/450
```

### Example 7: Complete Game Character Class

```python
class Character:
    """Represents a game character."""
    
    def __init__(self, name, health=100, strength=10):
        """Initialize character."""
        self.name = name
        self.max_health = health
        self.health = health
        self.strength = strength
        self.inventory = []
    
    def attack(self, target):
        """Attack another character."""
        damage = self.strength
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        target.take_damage(damage)
    
    def take_damage(self, amount):
        """Receive damage."""
        self.health -= amount
        if self.health < 0:
            self.health = 0
        
        print(f"{self.name} takes {amount} damage! Health: {self.health}/{self.max_health}")
        
        if self.health == 0:
            print(f"{self.name} has been defeated!")
    
    def heal(self, amount):
        """Restore health."""
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} healed {amount} HP! Health: {self.health}/{self.max_health}")
    
    def add_item(self, item):
        """Add item to inventory."""
        self.inventory.append(item)
        print(f"{self.name} picked up {item}")
    
    def show_status(self):
        """Display character status."""
        print(f"\n{self.name}'s Status:")
        print(f"  Health: {self.health}/{self.max_health}")
        print(f"  Strength: {self.strength}")
        print(f"  Inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}")

# Create characters
hero = Character("Hero", 100, 15)
enemy = Character("Goblin", 50, 8)

# Battle simulation
hero.show_status()
enemy.show_status()

hero.attack(enemy)
enemy.attack(hero)
hero.heal(10)
hero.add_item("Sword")
hero.add_item("Shield")

hero.show_status()
```

## Practice Exercises

### Beginner Exercises

1. **Person Class**
   - Attributes: name, age, city
   - Methods: introduce(), have_birthday(), move_to(city)
   - Create 3 different people

2. **Product Class**
   - Attributes: name, price, quantity
   - Methods: apply_discount(percent), restock(amount), sell(amount)
   - Test with different products

3. **Circle Class**
   - Attributes: radius
   - Methods: area(), circumference(), diameter()
   - Create circles of different sizes

4. **Counter Class**
   - Attributes: count (starts at 0)
   - Methods: increment(), decrement(), reset(), get_count()
   - Create multiple independent counters

5. **Temperature Class**
   - Attributes: celsius
   - Methods: to_fahrenheit(), to_kelvin(), set_temp()
   - Test conversions

### Intermediate Exercises

1. **Complete Bank Account System**
   - Add transaction history
   - Implement interest calculations
   - Add account types (checking, savings)
   - Create monthly statements

2. **Library Book System**
   - Book class with checkout/return
   - Track due dates
   - Calculate late fees
   - Show availability status

3. **Shopping Cart**
   - Add/remove items
   - Calculate total with tax
   - Apply discount codes
   - Show itemized receipt

4. **Game Inventory System**
   - Item class with properties
   - Add/remove/use items
   - Check weight limits
   - Sort by value/weight

5. **Employee Management**
   - Employee with salary, department
   - Calculate bonus, raise
   - Track work hours
   - Generate pay stubs

### Advanced Exercises

1. **RPG Character System**
   - Multiple character types
   - Skill systems
   - Equipment management
   - Level progression
   - Combat mechanics

2. **Social Media Post**
   - Post with content, author, timestamp
   - Like/comment functionality
   - Edit/delete posts
   - Share feature
   - Trending calculation

3. **Restaurant Order System**
   - MenuItem and Order classes
   - Table management
   - Bill calculation
   - Kitchen queue
   - Waiter assignment

4. **Hotel Reservation**
   - Room types and pricing
   - Booking system
   - Check-in/out
   - Guest management
   - Billing

5. **Task Management System**
   - Task with priority, deadline
   - Categories and tags
   - Dependencies
   - Progress tracking
   - Notifications

## Common Mistakes to Avoid

### Mistake 1: Forgetting `self`

❌ **Wrong:**
```python
class Dog:
    def __init__(name, age):  # Missing self!
        self.name = name
```

✅ **Correct:**
```python
class Dog:
    def __init__(self, name, age):  # self is first parameter
        self.name = name
        self.age = age
```

### Mistake 2: Not Using `self` to Access Attributes

❌ **Wrong:**
```python
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(f"{name} barks")  # Error: name not defined
```

✅ **Correct:**
```python
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(f"{self.name} barks")  # Use self.name
```

### Mistake 3: Passing `self` When Calling Methods

❌ **Wrong:**
```python
dog = Dog("Rex")
dog.bark(dog)  # Don't pass self manually!
```

✅ **Correct:**
```python
dog = Dog("Rex")
dog.bark()  # Python passes self automatically
```

### Mistake 4: Confusing Class and Instance

❌ **Wrong:**
```python
class Car:
    color = "red"  # Class attribute (shared by all)

car1 = Car()
car2 = Car()
Car.color = "blue"  # Changes for all instances!
```

✅ **Correct:**
```python
class Car:
    def __init__(self, color):
        self.color = color  # Instance attribute (unique to each)

car1 = Car("red")
car2 = Car("blue")  # Independent colors
```

## Real-World Applications

### 1. **Software Development**
- GUI applications (buttons, windows, forms)
- Game development (characters, items, levels)
- Web frameworks (requests, responses, models)
- Database ORMs (table representations)

### 2. **Data Science**
- DataFrame objects (pandas)
- Model objects (scikit-learn)
- Neural networks (TensorFlow, PyTorch)
- Data pipelines

### 3. **Business Applications**
- Customer management systems
- Inventory tracking
- Employee databases
- Financial modeling

### 4. **APIs and Services**
- REST API clients
- Service integrations
- Cloud resource management
- Authentication systems

## Challenge Projects

### 1. **Complete RPG Game**
- Character, Enemy, Item classes
- Battle system
- Inventory management
- Quest system
- Save/load game

### 2. **E-Commerce System**
- Product, Cart, Order classes
- User accounts
- Payment processing simulation
- Review system
- Recommendation engine

### 3. **School Management System**
- Student, Teacher, Course classes
- Enrollment system
- Grade tracking
- Attendance
- Report generation

### 4. **Social Network Simulation**
- User, Post, Comment classes
- Friend system
- News feed
- Notifications
- Privacy settings

### 5. **Fleet Management**
- Vehicle, Driver, Route classes
- Scheduling system
- Maintenance tracking
- Fuel management
- Performance analytics

---

## Navigation

← [Previous: 45 - Hangman Game](45-hangman-game.md) | [Next: 47 - Class Variables](47-class-variables.md) →

[↑ Back to Main README](../README.md)

## 🎓 Key Takeaways from Video

1. Variables store data values that can be reused
2. Define functions using the def keyword
3. Import modules to use external code

> 💡 *These points cover the main concepts from the video tutorial to help reinforce your learning.*